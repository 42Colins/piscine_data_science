import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array: np.array) -> np.array:
    """
    Inverts the color of the image received.
    """
    inverted_array = 255 - array
    plt.imshow(inverted_array)
    plt.show()
    return inverted_array


def ft_red(array: np.array) -> np.array:
    """ft_red function that make a red filter on the image"""
    red_array = array.copy()
    red_array[..., 1] = red_array[..., 1] * 0
    red_array[..., 2] = red_array[..., 2] * 0
    plt.imshow(red_array)
    plt.show()
    return red_array


def ft_green(array: np.array) -> np.array:
    """ft_green function that make a green filter on the image"""
    green_array = array.copy()
    green_array[..., 0] = green_array[..., 0] - green_array[..., 0]
    green_array[..., 2] = green_array[..., 2] - green_array[..., 2]
    plt.imshow(green_array)
    plt.show()
    return green_array


def ft_blue(array: np.array) -> np.array:
    """ft_blue function that make a blue filter on the image"""
    blue_array = np.zeros_like(array)
    blue_array[..., 2] = array[..., 2]
    plt.imshow(blue_array)
    plt.show()
    return blue_array


def ft_grey(array: np.array) -> np.array:
    """ft_grey function that make a grey filter on the image"""
    grey_array = array.copy()
    mean = grey_array.mean(axis=2)
    grey_array[..., 0] = mean
    grey_array[..., 1] = mean
    grey_array[..., 2] = mean
    plt.imshow(grey_array)
    plt.show()
    return grey_array
