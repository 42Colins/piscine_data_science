class calculator:
    def __init__(self, value: list[float]):
        """Init calculator"""
        self.value = value

    def __add__(self, object) -> None:
        """Add method"""
        self.value = [x + object for x in self.value]
        print(self.value)

    def __mul__(self, object) -> None:
        """Multiply method"""
        self.value = [x * object for x in self.value]
        print(self.value)

    def __sub__(self, object) -> None:
        """Subtract method"""
        self.value = [x - object for x in self.value]
        print(self.value)

    def __truediv__(self, object) -> None:
        """Divide method"""
        if object == 0:
            print("ERROR: Division by zero")
            return
        self.value = [x / object for x in self.value]
        print(self.value)
