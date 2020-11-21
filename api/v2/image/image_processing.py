from io import BytesIO

import requests
from PIL import Image


def pil_image_resize(image: Image, new_width: int) -> Image:
    source_width, source_height = image.width, image.height
    new_height = (source_height * new_width) // source_width
    return image.resize((new_width, new_height))


def pil_image_by_link(link: str) -> Image:
    response = requests.get(link)
    return Image.open(BytesIO(response.content))


def pil_image_to_bytes(image: Image) -> bytes:
    img_byte_arr = BytesIO()
    image.save(img_byte_arr, format='png')
    return img_byte_arr.getvalue()


def compose_imageproxy_response(new_width: int, link: str) -> bytes:
    image = pil_image_by_link(link)
    resized_image = pil_image_resize(image, new_width)
    return pil_image_to_bytes(resized_image)
