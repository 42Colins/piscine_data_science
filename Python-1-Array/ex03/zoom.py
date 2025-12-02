import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_zoom(image: np.array, factor: int) -> np.array:
    """
    ft_zoom function that receives a 2D array (list of lists)
    and a zoom factor, and returns a zoomed 2D array
    """
    if not isinstance(image, np.ndarray):
        raise TypeError("image must be a numpy array")
    if not isinstance(factor, int):
        raise TypeError("factor must be an integer")
    if factor <= 0:
        raise ValueError("factor must be a positive integer")

    zoomed_image = image[100:500, 400:900]
    print("Zoomed shape:", zoomed_image.shape)
    return zoomed_image


def main():
    image = ft_load("Animal.jpeg")
    zoomed_image = ft_zoom(image, 2)
    plt.imshow(zoomed_image)
    plt.show()
    print(zoomed_image)


if __name__ == "__main__":
    try:
        main()
    except (TypeError, ValueError, FileNotFoundError) as err:
        print(f"{err.__class__.__name__}: {err}")
