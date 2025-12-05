def ft_filter(function, iterable):
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None, return the items
    that are true.
    """
    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))


def main():
    """Main function"""
    print(ft_filter.__doc__)

    def is_even(num):
        return num % 2 == 0

    numbers = [1, 2, 3, 4, 5, 6]
    filtered_numbers = list(ft_filter(is_even, numbers))
    print(filtered_numbers)
    mixed_values = [0, 1, "", "Hello", None, [], [1, 2], False, True]
    filtered_values = list(ft_filter(None, mixed_values))
    print(filtered_values)

    real_filtered_numbers = list(filter(is_even, numbers))
    print(real_filtered_numbers)
    mixed_values = [0, 1, "", "Hello", None, [], [1, 2], False, True]
    filtered_values = list(filter(None, mixed_values))
    print(filtered_values)


# Test usage
if __name__ == "__main__":
    main()
