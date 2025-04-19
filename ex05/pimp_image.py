import numpy as np


def ft_invert(array) -> np.ndarray:
    """
    Inverts the color of the image received.
    """
    return 255 - array


def ft_red(array) -> np.ndarray:
    """
    Keeps only the red channel.
    """
    result = array * [1, 0, 0]
    return result


def ft_green(array) -> np.ndarray:
    """
    Keeps only the green channel.
    """
    result = array.copy()
    result[:, :, 0] = result[:, :, 0] - result[:, :, 0]
    result[:, :, 2] = result[:, :, 2] - result[:, :, 2]
    return result


def ft_blue(array) -> np.ndarray:
    """
    Keeps only the blue channel.
    """
    result = np.zeros_like(array)
    result[:, :, 2] = array[:, :, 2]
    return result


def ft_grey(array) -> np.ndarray:
    """
    Converts the image to grayscale using the average method.
    """
    # Calculate the average across the RGB channels
    average = array[:, :, 0] / 3 + array[:, :, 1] / 3 + array[:, :, 2] / 3
    grey_values = average.astype(np.uint8)
    grey_image = np.stack((grey_values, grey_values, grey_values), axis=-1)
    return grey_image
