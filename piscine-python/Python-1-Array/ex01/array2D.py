import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    slice_me function that receives a 2D array (list of lists),
    a start index and an end index, and returns a sliced 2D array
    securiser si un element n'est pas une liste
    """
    try:
        if not isinstance(family, list):
            raise TypeError("family must be a list of lists")
        for item in family:
            if not isinstance(item, list):
                raise TypeError("All elements of family must be lists")
    except TypeError as e:
        print(e)
        return []
    arr = np.array(family)
    array = arr[start:end]
    print("My shape is", arr.shape)
    print("My new shape is", array.shape)
    return array.tolist()
