import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    slice_me function that receives a 2D array (list of lists),
    a start index and an end index, and returns a sliced 2D array
    """
    arr = np.array(family)
    array = arr[start:end]
    print("My shape is", arr.shape)
    print("My new shape is", array.shape)
    return array.tolist()
