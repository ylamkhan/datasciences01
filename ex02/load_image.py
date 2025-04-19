import numpy as np
from PIL import Image
import os


def ft_load(path: str) -> np.array:
    # (you can return to the desired format)
    """ loading image and return array 2D"""
    try:
        if path is None:
            raise AssertionError("the path is None")
        if not isinstance(path, str):
            raise AssertionError("the path not string")
        if not os.path.exists(path):
            raise AssertionError("File not found")
        extension = os.path.splitext(path)[1].lower()
        if extension not in ['.jpg', '.jpeg']:
            text = "Unsupported file format. Only JPG and JPEG are supported."
            raise AssertionError(text)
        with Image.open(path) as img:
            img_rgp = img.convert("RGB")
            pixels = np.array(img_rgp)
            print("The shape of image is: ", pixels.shape)
            return pixels
    except AssertionError as ve:
        print("\033[91mAssertionError\033[0m", ve)
        return None
