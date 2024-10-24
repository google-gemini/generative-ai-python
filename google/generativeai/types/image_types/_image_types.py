import base64
import io
import json
import mimetypes
import os
import pathlib
import typing
from typing import Any, Dict, Optional, Union

from google.generativeai import protos
from google.generativeai import client

# pylint: disable=g-import-not-at-top
if typing.TYPE_CHECKING:
    import PIL.Image
    import PIL.ImageFile
    import IPython.display

    IMAGE_TYPES = (PIL.Image.Image, IPython.display.Image)
    ImageType = PIL.Image.Image | IPython.display.Image
else:
    IMAGE_TYPES = ()
    try:
        import PIL.Image
        import PIL.ImageFile

        IMAGE_TYPES = IMAGE_TYPES + (PIL.Image.Image,)
    except ImportError:
        PIL = None

    try:
        import IPython.display

        IMAGE_TYPES = IMAGE_TYPES + (IPython.display.Image,)
    except ImportError:
        IPython = None

    ImageType = Union["Image", "PIL.Image.Image", "IPython.display.Image"]
# pylint: enable=g-import-not-at-top

__all__ = ["Image", "GeneratedImage", "check_watermark", "CheckWatermarkResult", "ImageType"]


def _pil_to_blob(image: PIL.Image.Image) -> protos.Blob:
    # If the image is a local file, return a file-based blob without any modification.
    # Otherwise, return a lossless WebP blob (same quality with optimized size).
    def file_blob(image: PIL.Image.Image) -> protos.Blob | None:
        if not isinstance(image, PIL.ImageFile.ImageFile) or image.filename is None:
            return None
        filename = str(image.filename)
        if not pathlib.Path(filename).is_file():
            return None

        mime_type = image.get_format_mimetype()
        image_bytes = pathlib.Path(filename).read_bytes()

        return protos.Blob(mime_type=mime_type, data=image_bytes)

    def webp_blob(image: PIL.Image.Image) -> protos.Blob:
        # Reference: https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#webp
        image_io = io.BytesIO()
        image.save(image_io, format="webp", lossless=True)
        image_io.seek(0)

        mime_type = "image/webp"
        image_bytes = image_io.read()

        return protos.Blob(mime_type=mime_type, data=image_bytes)

    return file_blob(image) or webp_blob(image)


def image_to_blob(image: ImageType) -> protos.Blob:
    if PIL is not None:
        if isinstance(image, PIL.Image.Image):
            return _pil_to_blob(image)

    if IPython is not None:
        if isinstance(image, IPython.display.Image):
            name = image.filename
            if name is None:
                raise ValueError(
                    "Conversion failed. The `IPython.display.Image` can only be converted if "
                    "it is constructed from a local file. Please ensure you are using the format: Image(filename='...')."
                )
            mime_type, _ = mimetypes.guess_type(name)
            if mime_type is None:
                mime_type = "image/unknown"

            return protos.Blob(mime_type=mime_type, data=image.data)

    if isinstance(image, Image):
        return protos.Blob(mime_type=image._mime_type, data=image._image_bytes)

    raise TypeError(
        "Image conversion failed. The input was expected to be of type `Image` "
        "(either `PIL.Image.Image` or `IPython.display.Image`).\n"
        f"However, received an object of type: {type(image)}.\n"
        f"Object Value: {image}"
    )


class CheckWatermarkResult:
    def __init__(self, predictions):
        self._predictions = predictions

    @property
    def decision(self):
        return self._predictions[0]["decision"]

    def __str__(self):
        return f"CheckWatermarkResult([{{'decision': {self.decision!r}}}])"

    def __bool__(self):
        decision = self.decision
        if decision == "ACCEPT":
            return True
        elif decision == "REJECT":
            return False
        else:
            raise ValueError("Unrecognized result")


def check_watermark(
    img: pathlib.Path | ImageType, model_id: str = "models/image-verification-001"
) -> "CheckWatermarkResult":
    """Checks if an image has a Google-AI watermark.

    Args:
        img: can be a `pathlib.Path` or a `PIL.Image.Image`, `IPythin.display.Image`, or `google.generativeai.Image`.
        model_id: Which version of the image-verification model to send the image to.

    Returns:

    """
    if isinstance(img, Image):
        pass
    elif isinstance(img, pathlib.Path):
        img = Image.load_from_file(img)
    elif IPython.display is not None and isinstance(img, IPython.display.Image):
        img = Image(image_bytes=img.data)
    elif PIL.Image is not None and isinstance(img, PIL.Image.Image):
        blob = _pil_to_blob(img)
        img = Image(image_bytes=blob.data)
    elif isinstance(img, protos.Blob):
        img = Image(image_bytes=img.data)
    else:
        raise TypeError(
            f"Not implemented: Could not convert a {type(img)} into `Image`\n    {img=}"
        )

    prediction_client = client.get_default_prediction_client()
    if not model_id.startswith("models/"):
        model_id = f"models/{model_id}"

    instance = {"image": {"bytesBase64Encoded": base64.b64encode(img._loaded_bytes).decode()}}
    parameters = {"watermarkVerification": True}

    response = prediction_client.predict(
        model=model_id, instances=[instance], parameters=parameters
    )

    return CheckWatermarkResult(response.predictions)


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
    def load_from_file(location: os.PathLike) -> "Image":
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
    def _pil_image(self) -> "PIL_Image.Image":  # type: ignore
        if self._loaded_image is None:
            if not PIL:
                raise RuntimeError(
                    "The PIL module is not available. Please install the Pillow package."
                )
            self._loaded_image = PIL.Image.open(io.BytesIO(self._image_bytes))
        return self._loaded_image

    @property
    def _size(self):
        return self._pil_image.size

    @property
    def _mime_type(self) -> str:
        """Returns the MIME type of the image."""
        import PIL

        return PIL.Image.MIME.get(self._pil_image.format, "image/jpeg")

    def show(self):
        """Shows the image.

        This method only works when in a notebook environment.
        """
        if PIL and IPython:
            IPython.display.display(self._pil_image)

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

    def _repr_png_(self):
        return self._pil_image._repr_png_()  # type:ignore

    check_watermark = check_watermark


_EXIF_USER_COMMENT_TAG_IDX = 0x9286
_IMAGE_GENERATION_PARAMETERS_EXIF_KEY = (
    "google.cloud.vertexai.image_generation.image_generation_parameters"
)


class GeneratedImage(Image):
    """Generated image."""

    __module__ = "google.generativeai"

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
    def load_from_file(location: os.PathLike) -> "GeneratedImage":
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
            if not PIL:
                raise ValueError("The PIL module is required for saving generation parameters.")

            exif = self._pil_image.getexif()
            exif[_EXIF_USER_COMMENT_TAG_IDX] = json.dumps(
                {_IMAGE_GENERATION_PARAMETERS_EXIF_KEY: self._generation_parameters}
            )
            self._pil_image.save(location, exif=exif)
        else:
            super().save(location=location)
