def ft_mean(args: list[float]) -> float:
    """Function to calculate mean"""
    return sum(args) / len(args)


def ft_median(args: list[float]) -> float:
    """Function to calculate median"""
    return sorted(args)[len(args) // 2]


def ft_var(args: list[float]) -> float:
    """Function to calculate variance"""
    return sum((x - ft_mean(args)) ** 2 for x in args) / len(args)


def quartile(args: list[float], quartile: int) -> float:
    """Function to calculate quartile"""
    return sorted(args)[len(args) // 4 * quartile]


def ft_quartile(args: list[float]) -> list[float]:
    """Function to calculate quartiles"""
    return (quartile(args, 1), quartile(args, 3))


def ft_std(args: list[float]) -> float:
    """Function to calculate standard deviation"""
    return (ft_var(args))**0.5


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Function to calculate statistics"""
    if not args:
        print("ERROR")
        return
    for x in args:
        if not isinstance(x, (float, int)):
            print("ERROR : Arguments must be numbers")
            return
    for key, value in kwargs.items():
        match value:
            case "mean":
                print("Mean:", ft_mean(args))
            case "median":
                print("Median:", ft_median(args))
            case "var":
                print("Variance:", ft_var(args))
            case "quartile":
                print("Quartile:", ft_quartile(args))
            case "std":
                print("Standard deviation:", ft_std(args))
            case _:
                print("ERROR")
