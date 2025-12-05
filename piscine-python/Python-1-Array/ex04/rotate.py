import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_rotate(image: np.array) -> np.array:
    """
    rotate function that receives a 2D array (list of lists)
     and returns a rotated 2D array
    """
    if not isinstance(image, np.ndarray):
        raise TypeError("image must be a numpy array")
    new_shape = (image.shape[1], image.shape[0])
    rotated_image = np.zeros(new_shape)
    for i in range(image.shape[1]):
        for j in range(image.shape[0]):
            rotated_image[i][j] = image[j][i]
    print("Rotated shape):", rotated_image.shape)
    return rotated_image


def ft_zoom(image: np.array) -> np.array:
    """
    ft_zoom function that receives a 2D array (list of lists)
    and a zoom factor, and returns a zoomed 2D array
    """
    if not isinstance(image, np.ndarray):
        raise TypeError("image must be a numpy array")

    zoomed_image = image[100:500, 400:900]
    zoomed_image = (np.mean(zoomed_image, axis=2)).astype(np.uint8)
    print("Zoomed shape:", zoomed_image.shape)
    return zoomed_image


def main():
    image = ft_load("Animal.jpeg")
    zoomed_image = ft_zoom(image)
    rotated_image = ft_rotate(zoomed_image)
    plt.imshow(rotated_image, cmap="gray")
    plt.show()
    print(zoomed_image)


if __name__ == "__main__":
    try:
        main()
    except (TypeError, ValueError, FileNotFoundError) as err:
        print(f"{err.__class__.__name__}: {err}")
