class calculator:

    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Dot product method"""
        result = [x * y for x, y in zip(V1, V2)]
        print("Dot product:", sum(result))

    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add vector method"""
        result = [x + y for x, y in zip(V1, V2)]
        print("Added vector:", result)

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract vector method"""
        result = [x - y for x, y in zip(V1, V2)]
        print("Substracted vector:", result)
