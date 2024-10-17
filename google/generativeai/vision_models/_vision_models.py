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
import io
import json
import os
import pathlib
import typing
from typing import Any, Dict, List, Literal, Optional, Union

from google.generativeai import client
from google.generativeai.types import image_types
from google.generativeai import protos
from google.generativeai.types import content_types


# pylint: disable=g-import-not-at-top
if typing.TYPE_CHECKING:
    from IPython import display as IPython_display
else:
    try:
        from IPython import display as IPython_display
    except ImportError:
        IPython_display = None

if typing.TYPE_CHECKING:
    import PIL.Image as PIL_Image
else:
    try:
        from PIL import Image as PIL_Image
    except ImportError:
        PIL_Image = None


AspectRatio = Literal["1:1", "9:16", "16:9", "4:3", "3:4"]
ASPECT_RATIOS = AspectRatio.__args__  # type: ignore

OutputMimeType = Literal["image/png", "image/jpeg"]
OUTPUT_MIME_TYPES = OutputMimeType.__args__  # type: ignore

SafetyFilterLevel = Literal["block_low_and_above", "block_medium_and_above", "block_only_high"]
SAFETY_FILTER_LEVELS = SafetyFilterLevel.__args__  # type: ignore

PersonGeneration = Literal["dont_allow", "allow_adult"]
PERSON_GENERATIONS = PersonGeneration.__args__  # type: ignore


class ImageGenerationModel:
    """Generates images from text prompt.

    Examples::

        model = ImageGenerationModel.from_pretrained("imagegeneration@002")
        response = model.generate_images(
            prompt="Astronaut riding a horse",
            # Optional:
            number_of_images=1,
        )
        response[0].show()
        response[0].save("image1.png")
    """

    def __init__(self, model_id: str):
        if not model_id.startswith("models"):
            model_id = f"models/{model_id}"
        self.model_name = model_id
        self._client = None

    @classmethod
    def from_pretrained(cls, model_name: str):
        """For vertex compatibility"""
        return cls(model_name)

    def _generate_images(
        self,
        prompt: str,
        *,
        negative_prompt: Optional[str] = None,
        number_of_images: int = 1,
        width: Optional[int] = None,
        height: Optional[int] = None,
        aspect_ratio: Optional[AspectRatio] = None,
        guidance_scale: Optional[float] = None,
        output_mime_type: Optional[OutputMimeType] = None,
        compression_quality: Optional[float] = None,
        language: Optional[str] = None,
        safety_filter_level: Optional[SafetyFilterLevel] = None,
        person_generation: Optional[PersonGeneration] = None,
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
            output_mime_type: Which image format should the output be saved as.
              Supported values: * image/png: Save as a PNG image * image/jpeg: Save
              as a JPEG image
            compression_quality: Level of compression if the output mime type is
              selected to be image/jpeg. Float between 0 to 100
            language: Language of the text prompt for the image. Default: None.
              Supported values are `"en"` for English, `"hi"` for Hindi, `"ja"` for
              Japanese, `"ko"` for Korean, and `"auto"` for automatic language
              detection.
            safety_filter_level: Adds a filter level to Safety filtering. Supported
              values are:
              * "block_most" : Strongest filtering level, most strict blocking
              * "block_some" : Block some problematic prompts and responses
              * "block_few" : Block fewer problematic prompts and responses
            person_generation: Allow generation of people by the model Supported
              values are:
              * "dont_allow" : Block generation of people
              * "allow_adult" : Generate adults, but not children

        Returns:
            An `ImageGenerationResponse` object.
        """
        if self._client is None:
            self._client = client.get_default_prediction_client()
        # Note: Only a single prompt is supported by the service.
        instance = {"prompt": prompt}
        shared_generation_parameters = {
            "prompt": prompt,
            # b/295946075 The service stopped supporting image sizes.
            # "width": width,
            # "height": height,
            "number_of_images_in_batch": number_of_images,
        }

        parameters = {}
        max_size = max(width or 0, height or 0) or None
        if aspect_ratio is not None:
            if aspect_ratio not in ASPECT_RATIOS:
                raise ValueError(f"aspect_ratio not in {ASPECT_RATIOS}")
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

        if guidance_scale is not None:
            parameters["guidanceScale"] = guidance_scale
            shared_generation_parameters["guidance_scale"] = guidance_scale

        if language is not None:
            parameters["language"] = language
            shared_generation_parameters["language"] = language

        parameters["outputOptions"] = {}
        if output_mime_type is not None:
            if output_mime_type not in OUTPUT_MIME_TYPES:
                raise ValueError(f"output_mime_type not in {OUTPUT_MIME_TYPES}")
            parameters["outputOptions"]["mimeType"] = output_mime_type
            shared_generation_parameters["mime_type"] = output_mime_type

        if compression_quality is not None:
            parameters["outputOptions"]["compressionQuality"] = compression_quality
            shared_generation_parameters["compression_quality"] = compression_quality

        if safety_filter_level is not None:
            if safety_filter_level not in SAFETY_FILTER_LEVELS:
                raise ValueError(f"safety_filter_level not in {SAFETY_FILTER_LEVELS}")
            parameters["safetySetting"] = safety_filter_level
            shared_generation_parameters["safety_filter_level"] = safety_filter_level

        if person_generation is not None:
            parameters["personGeneration"] = person_generation
            shared_generation_parameters["person_generation"] = person_generation

        response = self._client.predict(
            model=self.model_name, instances=[instance], parameters=parameters
        )

        generated_images: List["GeneratedImage"] = []
        for idx, prediction in enumerate(response.predictions):
            generation_parameters = dict(shared_generation_parameters)
            generation_parameters["index_of_image_in_batch"] = idx
            encoded_bytes = prediction.get("bytesBase64Encoded")
            generated_image = image_types.GeneratedImage(
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
        aspect_ratio: Optional[AspectRatio] = None,
        guidance_scale: Optional[float] = None,
        language: Optional[str] = None,
        safety_filter_level: Optional[SafetyFilterLevel] = None,
        person_generation: Optional[PersonGeneration] = None,
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
            safety_filter_level: Adds a filter level to Safety filtering. Supported
                values are:
                * "block_most" : Strongest filtering level, most strict
                blocking
                * "block_some" : Block some problematic prompts and responses
                * "block_few" : Block fewer problematic prompts and responses
            person_generation: Allow generation of people by the model Supported
                values are:
                * "dont_allow" : Block generation of people
                * "allow_adult" : Generate adults, but not children
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
            safety_filter_level=safety_filter_level,
            person_generation=person_generation,
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

