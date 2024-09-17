# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# pylint: disable=bad-continuation, line-too-long, protected-access
"""Classes for working with vision models."""

import base64
import collections
import dataclasses
import hashlib
import io
import json
import pathlib
import typing
from typing import Any, Dict, List, Literal, Optional, Union

from google.protobuf import struct_pb2

from proto.marshal.collections import maps
from proto.marshal.collections import repeated


# pylint: disable=g-import-not-at-top
try:
    from IPython import display as IPython_display
except ImportError:
    IPython_display = None

try:
    from PIL import Image as PIL_Image
except ImportError:
    PIL_Image = None


def to_value(value) -> struct_pb2.Value:
    """Return a protobuf Value object representing this value."""
    if isinstance(value, struct_pb2.Value):
        return value
    if value is None:
        return struct_pb2.Value(null_value=0)
    if isinstance(value, bool):
        return struct_pb2.Value(bool_value=value)
    if isinstance(value, (int, float)):
        return struct_pb2.Value(number_value=float(value))
    if isinstance(value, str):
        return struct_pb2.Value(string_value=value)
    if isinstance(value, collections.abc.Sequence):
        return struct_pb2.Value(list_value=to_list_value(value))
    if isinstance(value, collections.abc.Mapping):
        return struct_pb2.Value(struct_value=to_mapping_value(value))
    raise ValueError("Unable to coerce value: %r" % value)

def to_list_value(value) -> struct_pb2.ListValue:
    # We got a proto, or else something we sent originally.
    # Preserve the instance we have.
    if isinstance(value, struct_pb2.ListValue):
        return value
    if isinstance(value, repeated.RepeatedComposite):
        return struct_pb2.ListValue(values=[v for v in value.pb])

    # We got a list (or something list-like); convert it.
    return struct_pb2.ListValue(
        values=[to_value(v) for v in value]
    )

def to_mapping_value(value) -> struct_pb2.Struct:
    # We got a proto, or else something we sent originally.
    # Preserve the instance we have.
    if isinstance(value, struct_pb2.Struct):
        return value
    if isinstance(value, maps.MapComposite):
        return struct_pb2.Struct(
            fields={k: v for k, v in value.pb.items()},
        )

    # We got a dict (or something dict-like); convert it.
    return struct_pb2.Struct(
        fields={
            k: to_value(v) for k, v in value.items()
        }
    )



_SUPPORTED_UPSCALING_SIZES = [2048, 4096]


class Image:
    """Image."""

    __module__ = "vertexai.vision_models"

    _loaded_bytes: Optional[bytes] = None
    _loaded_image: Optional["PIL_Image.Image"] = None

    def __init__(
        self,
        image_bytes: Optional[bytes],
    ):
        """Creates an `Image` object.

        Args:
            image_bytes: Image file bytes. Image can be in PNG or JPEG format.
        """
        self._image_bytes = image_bytes

    @staticmethod
    def load_from_file(location: str) -> "Image":
        """Loads image from local file or Google Cloud Storage.

        Args:
            location: Local path or Google Cloud Storage uri from where to load
                the image.

        Returns:
            Loaded image as an `Image` object.
        """
        # Load image from local path
        image_bytes = pathlib.Path(location).read_bytes()
        image = Image(image_bytes=image_bytes)
        return image


    @property
    def _image_bytes(self) -> bytes:
        return self._loaded_bytes

    @_image_bytes.setter
    def _image_bytes(self, value: bytes):
        self._loaded_bytes = value

    @property
    def _pil_image(self) -> "PIL_Image.Image":
        if self._loaded_image is None:
            if not PIL_Image:
                raise RuntimeError(
                    "The PIL module is not available. Please install the Pillow package."
                )
            self._loaded_image = PIL_Image.open(io.BytesIO(self._image_bytes))
        return self._loaded_image

    @property
    def _size(self):
        return self._pil_image.size

    @property
    def _mime_type(self) -> str:
        """Returns the MIME type of the image."""
        if PIL_Image:
            return PIL_Image.MIME.get(self._pil_image.format, "image/jpeg")
        # Fall back to jpeg
        return "image/jpeg"

    def show(self):
        """Shows the image.

        This method only works when in a notebook environment.
        """
        if PIL_Image and IPython_display:
            IPython_display.display(self._pil_image)

    def save(self, location: str):
        """Saves image to a file.

        Args:
            location: Local path where to save the image.
        """
        pathlib.Path(location).write_bytes(self._image_bytes)

    def _as_base64_string(self) -> str:
        """Encodes image using the base64 encoding.

        Returns:
            Base64 encoding of the image as a string.
        """
        # ! b64encode returns `bytes` object, not `str`.
        # We need to convert `bytes` to `str`, otherwise we get service error:
        # "received initial metadata size exceeds limit"
        return base64.b64encode(self._image_bytes).decode("ascii")


class ImageGenerationModel:
    """Generates images from text prompt.

    Examples::

        model = ImageGenerationModel.from_pretrained("imagegeneration@002")
        response = model.generate_images(
            prompt="Astronaut riding a horse",
            # Optional:
            number_of_images=1,
            seed=0,
        )
        response[0].show()
        response[0].save("image1.png")
    """

    __module__ = "vertexai.preview.vision_models"

    _INSTANCE_SCHEMA_URI = "gs://google-cloud-aiplatform/schema/predict/instance/vision_generative_model_1.0.0.yaml"

    def _generate_images(
        self,
        prompt: str,
        *,
        negative_prompt: Optional[str] = None,
        number_of_images: int = 1,
        width: Optional[int] = None,
        height: Optional[int] = None,
        aspect_ratio: Optional[Literal["1:1", "9:16", "16:9", "4:3", "3:4"]] = None,
        guidance_scale: Optional[float] = None,
        seed: Optional[int] = None,
        base_image: Optional["Image"] = None,
        mask: Optional["Image"] = None,
        edit_mode: Optional[
            Literal[
                "inpainting-insert",
                "inpainting-remove",
                "outpainting",
                "product-image",
            ]
        ] = None,
        mask_mode: Optional[Literal["background", "foreground", "semantic"]] = None,
        segmentation_classes: Optional[List[str]] = None,
        mask_dilation: Optional[float] = None,
        product_position: Optional[Literal["fixed", "reposition"]] = None,
        output_mime_type: Optional[Literal["image/png", "image/jpeg"]] = None,
        compression_quality: Optional[float] = None,
        language: Optional[str] = None,
        add_watermark: Optional[bool] = None,
        safety_filter_level: Optional[
            Literal["block_most", "block_some", "block_few", "block_fewest"]
        ] = None,
        person_generation: Optional[
            Literal["dont_allow", "allow_adult", "allow_all"]
        ] = None,
    ) -> "ImageGenerationResponse":
        """Generates images from text prompt.

        Args:
            prompt: Text prompt for the image.
            negative_prompt: A description of what you want to omit in the generated
              images.
            number_of_images: Number of images to generate. Range: 1..8.
            width: Width of the image. One of the sizes must be 256 or 1024.
            height: Height of the image. One of the sizes must be 256 or 1024.
            aspect_ratio: Aspect ratio for the image. Supported values are:
                * 1:1 - Square image
                * 9:16 - Portait image
                * 16:9 - Landscape image
                * 4:3 - Landscape, desktop ratio.
                * 3:4 - Portrait, desktop ratio
            guidance_scale: Controls the strength of the prompt. Suggested values
              are - * 0-9 (low strength) * 10-20 (medium strength) * 21+ (high
              strength)
            seed: Image generation random seed.
            base_image: Base image to use for the image generation.
            mask: Mask for the base image.
            edit_mode: Describes the editing mode for the request. Supported values
              are - * inpainting-insert: fills the mask area based on the text
              prompt (requires mask and text) * inpainting-remove: removes the
              object(s) in the mask area. (requires mask)
                * outpainting: extend the image based on the mask area. (Requires
                  mask) * product-image: Changes the background for the predominant
                  product or subject in the image
            mask_mode: Solicits generation of the mask (v/s providing mask as an
              input). Supported values are:
                * background: Automatically generates a mask for all regions except
                  the primary subject(s) of the image
                * foreground: Automatically generates a mask for the primary
                  subjects(s) of the image.
                * semantic: Segment one or more of the segmentation classes using
                  class ID
            segmentation_classes: List of class IDs for segmentation. Max of 5 IDs
            mask_dilation: Defines the dilation percentage of the mask provided.
              Float between 0 and 1. Defaults to 0.03
            product_position: Defines whether the product should stay fixed or be
              repositioned. Supported Values:
                * fixed: Fixed position
                * reposition: Can be moved (default)
            output_mime_type: Which image format should the output be saved as.
              Supported values: * image/png: Save as a PNG image * image/jpeg: Save
              as a JPEG image
            compression_quality: Level of compression if the output mime type is
              selected to be image/jpeg. Float between 0 to 100
            language: Language of the text prompt for the image. Default: None.
              Supported values are `"en"` for English, `"hi"` for Hindi, `"ja"` for
              Japanese, `"ko"` for Korean, and `"auto"` for automatic language
              detection.
            add_watermark: Add a watermark to the generated image
            safety_filter_level: Adds a filter level to Safety filtering. Supported
              values are: * "block_most" : Strongest filtering level, most strict
              blocking * "block_some" : Block some problematic prompts and responses
              * "block_few" : Block fewer problematic prompts and responses *
              "block_fewest" : Block very few problematic prompts and responses
            person_generation: Allow generation of people by the model Supported
              values are: * "dont_allow" : Block generation of people *
              "allow_adult" : Generate adults, but not children * "allow_all" :
              Generate adults and children

        Returns:
            An `ImageGenerationResponse` object.
        """
        # Note: Only a single prompt is supported by the service.
        instance = {"prompt": prompt}
        shared_generation_parameters = {
            "prompt": prompt,
            # b/295946075 The service stopped supporting image sizes.
            # "width": width,
            # "height": height,
            "number_of_images_in_batch": number_of_images,
        }

        if base_image:
            instance["image"] = {
                "bytesBase64Encoded": base_image._as_base64_string()  # pylint: disable=protected-access
            }
            shared_generation_parameters["base_image_hash"] = hashlib.sha1(
                base_image._image_bytes  # pylint: disable=protected-access
            ).hexdigest()

        if mask:
            instance["mask"] = {
                "image": {
                    "bytesBase64Encoded": mask._as_base64_string()  # pylint: disable=protected-access
                },
            }
            shared_generation_parameters["mask_hash"] = hashlib.sha1(
                mask._image_bytes  # pylint: disable=protected-access
            ).hexdigest()

        parameters = {}
        max_size = max(width or 0, height or 0) or None
        if aspect_ratio is not None:
            parameters["aspectRatio"] = aspect_ratio
        elif max_size:
            # Note: The size needs to be a string
            parameters["sampleImageSize"] = str(max_size)
            if height is not None and width is not None and height != width:
                parameters["aspectRatio"] = f"{width}:{height}"

        parameters["sampleCount"] = number_of_images
        if negative_prompt:
            parameters["negativePrompt"] = negative_prompt
            shared_generation_parameters["negative_prompt"] = negative_prompt

        if seed is not None:
            # Note: String seed and numerical seed give different results
            parameters["seed"] = seed
            shared_generation_parameters["seed"] = seed

        if guidance_scale is not None:
            parameters["guidanceScale"] = guidance_scale
            shared_generation_parameters["guidance_scale"] = guidance_scale

        if language is not None:
            parameters["language"] = language
            shared_generation_parameters["language"] = language

        parameters["editConfig"] = {}
        if edit_mode is not None:
            parameters["editConfig"]["editMode"] = edit_mode
            shared_generation_parameters["edit_mode"] = edit_mode

        if mask is None and edit_mode != "product-image":
            parameters["editConfig"]["maskMode"] = {}
            if mask_mode is not None:
                parameters["editConfig"]["maskMode"]["maskType"] = mask_mode
                shared_generation_parameters["mask_mode"] = mask_mode

            if segmentation_classes is not None:
                parameters["editConfig"]["maskMode"]["classes"] = segmentation_classes
                shared_generation_parameters["classes"] = segmentation_classes

        if mask_dilation is not None:
            parameters["editConfig"]["maskDilation"] = mask_dilation
            shared_generation_parameters["mask_dilation"] = mask_dilation

        if product_position is not None:
            parameters["editConfig"]["productPosition"] = product_position
            shared_generation_parameters["product_position"] = product_position

        parameters["outputOptions"] = {}
        if output_mime_type is not None:
            parameters["outputOptions"]["mimeType"] = output_mime_type
            shared_generation_parameters["mime_type"] = output_mime_type

        if compression_quality is not None:
            parameters["outputOptions"]["compressionQuality"] = compression_quality
            shared_generation_parameters["compression_quality"] = compression_quality

        if add_watermark is not None:
            parameters["addWatermark"] = add_watermark
            shared_generation_parameters["add_watermark"] = add_watermark

        if safety_filter_level is not None:
            parameters["safetySetting"] = safety_filter_level
            shared_generation_parameters["safety_filter_level"] = safety_filter_level

        if person_generation is not None:
            parameters["personGeneration"] = person_generation
            shared_generation_parameters["person_generation"] = person_generation

        response = self._endpoint.predict(
            instances=[to_value(instance)],
            parameters=parameters,
        )

        generated_images: List["GeneratedImage"] = []
        for idx, prediction in enumerate(response.predictions):
            generation_parameters = dict(shared_generation_parameters)
            generation_parameters["index_of_image_in_batch"] = idx
            encoded_bytes = prediction.get("bytesBase64Encoded")
            generated_image = GeneratedImage(
                image_bytes=base64.b64decode(encoded_bytes) if encoded_bytes else None,
                generation_parameters=generation_parameters,
            )
            generated_images.append(generated_image)

        return ImageGenerationResponse(images=generated_images)

    def generate_images(
        self,
        prompt: str,
        *,
        negative_prompt: Optional[str] = None,
        number_of_images: int = 1,
        aspect_ratio: Optional[Literal["1:1", "9:16", "16:9", "4:3", "3:4"]] = None,
        guidance_scale: Optional[float] = None,
        language: Optional[str] = None,
        seed: Optional[int] = None,
        add_watermark: Optional[bool] = True,
        safety_filter_level: Optional[
            Literal["block_most", "block_some", "block_few", "block_fewest"]
        ] = None,
        person_generation: Optional[
            Literal["dont_allow", "allow_adult", "allow_all"]
        ] = None,
    ) -> "ImageGenerationResponse":
        """Generates images from text prompt.

        Args:
            prompt: Text prompt for the image.
            negative_prompt: A description of what you want to omit in the generated
                images.
            number_of_images: Number of images to generate. Range: 1..8.
            aspect_ratio: Changes the aspect ratio of the generated image Supported
                values are:
                * "1:1" : 1:1 aspect ratio
                * "9:16" : 9:16 aspect ratio
                * "16:9" : 16:9 aspect ratio
                * "4:3" : 4:3 aspect ratio
                * "3:4" : 3:4 aspect_ratio
            guidance_scale: Controls the strength of the prompt. Suggested values are:
                * 0-9 (low strength)
                * 10-20 (medium strength)
                * 21+ (high strength)
            language: Language of the text prompt for the image. Default: None.
                Supported values are `"en"` for English, `"hi"` for Hindi, `"ja"`
                for Japanese, `"ko"` for Korean, and `"auto"` for automatic language
                detection.
            seed: Image generation random seed.
            add_watermark: Add a watermark to the generated image
            safety_filter_level: Adds a filter level to Safety filtering. Supported
                values are:
                * "block_most" : Strongest filtering level, most strict
                blocking
                * "block_some" : Block some problematic prompts and responses
                * "block_few" : Block fewer problematic prompts and responses
                * "block_fewest" : Block very few problematic prompts and responses
            person_generation: Allow generation of people by the model Supported
                values are:
                * "dont_allow" : Block generation of people
                * "allow_adult" : Generate adults, but not children
                * "allow_all" : Generate adults and children
        Returns:
            An `ImageGenerationResponse` object.
        """
        return self._generate_images(
            prompt=prompt,
            negative_prompt=negative_prompt,
            number_of_images=number_of_images,
            aspect_ratio=aspect_ratio,
            guidance_scale=guidance_scale,
            language=language,
            seed=seed,
            add_watermark=add_watermark,
            safety_filter_level=safety_filter_level,
            person_generation=person_generation,
        )

    def edit_image(
        self,
        *,
        prompt: str,
        base_image: "Image",
        mask: Optional["Image"] = None,
        negative_prompt: Optional[str] = None,
        number_of_images: int = 1,
        guidance_scale: Optional[float] = None,
        edit_mode: Optional[
            Literal[
                "inpainting-insert", "inpainting-remove", "outpainting", "product-image"
            ]
        ] = None,
        mask_mode: Optional[Literal["background", "foreground", "semantic"]] = None,
        segmentation_classes: Optional[List[str]] = None,
        mask_dilation: Optional[float] = None,
        product_position: Optional[Literal["fixed", "reposition"]] = None,
        output_mime_type: Optional[Literal["image/png", "image/jpeg"]] = None,
        compression_quality: Optional[float] = None,
        language: Optional[str] = None,
        seed: Optional[int] = None,
        safety_filter_level: Optional[
            Literal["block_most", "block_some", "block_few", "block_fewest"]
        ] = None,
        person_generation: Optional[
            Literal["dont_allow", "allow_adult", "allow_all"]
        ] = None,
    ) -> "ImageGenerationResponse":
        """Edits an existing image based on text prompt.

        Args:
            prompt: Text prompt for the image.
            base_image: Base image from which to generate the new image.
            mask: Mask for the base image.
            negative_prompt: A description of what you want to omit in
                the generated images.
            number_of_images: Number of images to generate. Range: 1..8.
            guidance_scale: Controls the strength of the prompt.
                Suggested values are:
                * 0-9 (low strength)
                * 10-20 (medium strength)
                * 21+ (high strength)
            edit_mode: Describes the editing mode for the request. Supported values are:
                * inpainting-insert: fills the mask area based on the text prompt
                (requires mask and text)
                * inpainting-remove: removes the object(s) in the mask area.
                (requires mask)
                * outpainting: extend the image based on the mask area.
                (Requires mask)
                * product-image: Changes the background for the predominant product
                or subject in the image
            mask_mode: Solicits generation of the mask (v/s providing mask as an
                input). Supported values are:
                * background: Automatically generates a mask for all regions except
                the primary subject(s) of the image
                * foreground: Automatically generates a mask for the primary
                subjects(s) of the image.
                * semantic: Segment one or more of the segmentation classes using
                class ID
            segmentation_classes: List of class IDs for segmentation. Max of 5 IDs
            mask_dilation: Defines the dilation percentage of the mask provided.
                Float between 0 and 1. Defaults to 0.03
            product_position: Defines whether the product should stay fixed or be
                repositioned. Supported Values:
                * fixed: Fixed position
                * reposition: Can be moved (default)
            output_mime_type: Which image format should the output be saved as.
                Supported values:
                * image/png: Save as a PNG image
                * image/jpeg: Save as a JPEG image
            compression_quality: Level of compression if the output mime type is
              selected to be image/jpeg. Float between 0 to 100
            language: Language of the text prompt for the image. Default: None.
                Supported values are `"en"` for English, `"hi"` for Hindi,
                `"ja"` for Japanese, `"ko"` for Korean, and `"auto"` for
                automatic language detection.
            seed: Image generation random seed.
            safety_filter_level: Adds a filter level to Safety filtering. Supported
                values are:
                * "block_most" : Strongest filtering level, most strict
                blocking
                * "block_some" : Block some problematic prompts and responses
                * "block_few" : Block fewer problematic prompts and responses
                * "block_fewest" : Block very few problematic prompts and responses
            person_generation: Allow generation of people by the model Supported
                values are:
                * "dont_allow" : Block generation of people
                * "allow_adult" : Generate adults, but not children
                * "allow_all" : Generate adults and children

        Returns:
            An `ImageGenerationResponse` object.
        """
        return self._generate_images(
            prompt=prompt,
            negative_prompt=negative_prompt,
            number_of_images=number_of_images,
            guidance_scale=guidance_scale,
            seed=seed,
            base_image=base_image,
            mask=mask,
            edit_mode=edit_mode,
            mask_mode=mask_mode,
            segmentation_classes=segmentation_classes,
            mask_dilation=mask_dilation,
            product_position=product_position,
            output_mime_type=output_mime_type,
            compression_quality=compression_quality,
            language=language,
            add_watermark=False,  # Not supported for editing yet
            safety_filter_level=safety_filter_level,
            person_generation=person_generation,
        )

    def upscale_image(
        self,
        image: Union["Image", "GeneratedImage"],
        new_size: Optional[int] = 2048,
        upscale_factor: Optional[Literal["x2", "x4"]] = None,
        output_mime_type: Optional[Literal["image/png", "image/jpeg"]] = "image/png",
        output_compression_quality: Optional[int] = None,
    ) -> "Image":
        """Upscales an image.

        This supports upscaling images generated through the `generate_images()`
        method, or upscaling a new image.

        Examples::

            # Upscale a generated image
            model = ImageGenerationModel.from_pretrained("imagegeneration@002")
            response = model.generate_images(
                prompt="Astronaut riding a horse",
            )
            model.upscale_image(image=response[0])

            # Upscale a new 1024x1024 image
            my_image = Image.load_from_file("my-image.png")
            model.upscale_image(image=my_image)

            # Upscale a new arbitrary sized image using a x2 or x4 upscaling factor
            my_image = Image.load_from_file("my-image.png")
            model.upscale_image(image=my_image, upscale_factor="x2")

            # Upscale an image and get the result in JPEG format
            my_image = Image.load_from_file("my-image.png")
            model.upscale_image(image=my_image, output_mime_type="image/jpeg",
            output_compression_quality=90)

        Args:
            image (Union[GeneratedImage, Image]): Required. The generated image
                to upscale.
            new_size (int): The size of the biggest dimension of the upscaled
                image.
                Only 2048 and 4096 are currently supported. Results in a
                2048x2048 or 4096x4096 image. Defaults to 2048 if not provided.
            upscale_factor: The upscaling factor. Supported values are "x2" and
                "x4". Defaults to None.
            output_mime_type: The mime type of the output image. Supported values
                are "image/png" and "image/jpeg". Defaults to "image/png".
            output_compression_quality: The compression quality of the output
                image
                as an int (0-100). Only applicable if the output mime type is
                "image/jpeg". Defaults to None.

        Returns:
            An `Image` object.
        """
        target_image_size = new_size if new_size else None
        longest_dim = max(image._size[0], image._size[1])

        if not new_size and not upscale_factor:
            raise ValueError("Either new_size or upscale_factor must be provided.")

        if not upscale_factor:
            x2_factor = 2.0
            x4_factor = 4.0
            epsilon = 0.1
            is_upscaling_x2_request = abs(new_size / longest_dim - x2_factor) < epsilon
            is_upscaling_x4_request = abs(new_size / longest_dim - x4_factor) < epsilon

            if not is_upscaling_x2_request and not is_upscaling_x4_request:
                raise ValueError(
                    "Only x2 and x4 upscaling are currently supported. Requested"
                    f" upscaling factor: {new_size / longest_dim}"
                )
        else:
            if upscale_factor == "x2":
                target_image_size = longest_dim * 2
            else:
                target_image_size = longest_dim * 4
        if new_size not in _SUPPORTED_UPSCALING_SIZES:
            raise ValueError(
                "Only the folowing square upscaling sizes are currently supported:"
                f" {_SUPPORTED_UPSCALING_SIZES}."
            )

        instance = {"prompt": ""}

        instance["image"] = {
            "bytesBase64Encoded": image._as_base64_string()  # pylint: disable=protected-access
        }

        parameters = {
            "sampleCount": 1,
            "mode": "upscale",
        }

        if upscale_factor:
            parameters["upscaleConfig"] = {"upscaleFactor": upscale_factor}

        else:
            parameters["sampleImageSize"] = str(new_size)

        parameters["outputOptions"] = {"mimeType": output_mime_type}
        if output_mime_type == "image/jpeg" and output_compression_quality is not None:
            parameters["outputOptions"][
                "compressionQuality"
            ] = output_compression_quality

        response = self._endpoint.predict(
            instances=[to_value(instance)],
            parameters=parameters,
        )

        upscaled_image = response.predictions[0]

        if isinstance(image, GeneratedImage):
            generation_parameters = image.generation_parameters

        else:
            generation_parameters = {}

        generation_parameters["upscaled_image_size"] = target_image_size

        encoded_bytes = upscaled_image.get("bytesBase64Encoded")
        return GeneratedImage(
            image_bytes=base64.b64decode(encoded_bytes) if encoded_bytes else None,
            generation_parameters=generation_parameters,
        )


@dataclasses.dataclass
class ImageGenerationResponse:
    """Image generation response.

    Attributes:
        images: The list of generated images.
    """

    __module__ = "vertexai.preview.vision_models"

    images: List["GeneratedImage"]

    def __iter__(self) -> typing.Iterator["GeneratedImage"]:
        """Iterates through the generated images."""
        yield from self.images

    def __getitem__(self, idx: int) -> "GeneratedImage":
        """Gets the generated image by index."""
        return self.images[idx]


_EXIF_USER_COMMENT_TAG_IDX = 0x9286
_IMAGE_GENERATION_PARAMETERS_EXIF_KEY = (
    "google.cloud.vertexai.image_generation.image_generation_parameters"
)


class GeneratedImage(Image):
    """Generated image."""

    __module__ = "vertexai.preview.vision_models"

    def __init__(
        self,
        image_bytes: Optional[bytes],
        generation_parameters: Dict[str, Any],
    ):
        """Creates a `GeneratedImage` object.

        Args:
            image_bytes: Image file bytes. Image can be in PNG or JPEG format.
            generation_parameters: Image generation parameter values.
        """
        super().__init__(image_bytes=image_bytes)
        self._generation_parameters = generation_parameters

    @property
    def generation_parameters(self):
        """Image generation parameters as a dictionary."""
        return self._generation_parameters

    @staticmethod
    def load_from_file(location: str) -> "GeneratedImage":
        """Loads image from file.

        Args:
            location: Local path from where to load the image.

        Returns:
            Loaded image as a `GeneratedImage` object.
        """
        base_image = Image.load_from_file(location=location)
        exif = base_image._pil_image.getexif()  # pylint: disable=protected-access
        exif_comment_dict = json.loads(exif[_EXIF_USER_COMMENT_TAG_IDX])
        generation_parameters = exif_comment_dict[_IMAGE_GENERATION_PARAMETERS_EXIF_KEY]
        return GeneratedImage(
            image_bytes=base_image._image_bytes,  # pylint: disable=protected-access
            generation_parameters=generation_parameters,
        )

    def save(self, location: str, include_generation_parameters: bool = True):
        """Saves image to a file.

        Args:
            location: Local path where to save the image.
            include_generation_parameters: Whether to include the image
                generation parameters in the image's EXIF metadata.
        """
        if include_generation_parameters:
            if not self._generation_parameters:
                raise ValueError("Image does not have generation parameters.")
            if not PIL_Image:
                raise ValueError(
                    "The PIL module is required for saving generation parameters."
                )

            exif = self._pil_image.getexif()
            exif[_EXIF_USER_COMMENT_TAG_IDX] = json.dumps(
                {_IMAGE_GENERATION_PARAMETERS_EXIF_KEY: self._generation_parameters}
            )
            self._pil_image.save(location, exif=exif)
        else:
            super().save(location=location)

