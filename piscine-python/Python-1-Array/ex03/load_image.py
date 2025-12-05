import numpy as np
import imageio.v2 as iio
import os


def ft_load(path: str) -> np.array:
    """
    ft_load function that loads an image from a given path
    and returns it as a 2D array (list of lists)
    """
    if not isinstance(path, str):
        raise TypeError("path must be a string")
    if not path:
        raise ValueError("path must not be empty")
    if not (path.endswith(".jpeg") or path.endswith(".png")
            or path.endswith(".jpg")):
        raise ValueError("path must be a valid image file (.jpeg, .png, .jpg)")
    if not os.path.isfile(path):
        raise FileNotFoundError(f"No such file: '{path}'")

    img = iio.imread(path)
    arr = np.array(img)
    print("The shape of image is :", arr.shape)
    return arr
