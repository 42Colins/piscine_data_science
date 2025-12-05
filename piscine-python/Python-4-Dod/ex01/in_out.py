def square(x: int | float) -> int | float:
    """Function to square a number"""
    return x * x


def pow(x: int | float) -> int | float:
    """Function to power a number"""
    return x ** x


def outer(x: int | float, function) -> object:
    """Function to outer a number"""
    count = x

    def inner() -> float:
        """Function to inner a number"""
        nonlocal count
        count = function(count)
        return count

    return inner
