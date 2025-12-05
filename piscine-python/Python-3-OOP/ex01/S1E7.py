from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor Baratheon"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"
        super().__init__(first_name, is_alive)

    def die(self):
        """Method die"""
        super().die()

    def __str__(self):
        """Method __str__"""
        return f"Vector : '{self.family_name}', '{self.eyes}', '{self.hairs}'"

    def __repr__(self):
        """Method __repr__"""
        return f"Vector : '{self.family_name}', '{self.eyes}', '{self.hairs}'"


class Lannister(Character):
    """Representing the Lannister family"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor Lannister"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"
        super().__init__(first_name, is_alive)

    def die(self):
        """Method die"""
        super().die()

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """Decorator create_lannister"""
        return cls(first_name, is_alive)

    def __str__(self):
        """Method __str__"""
        return f"Vector : '{self.family_name}', '{self.eyes}', '{self.hairs}'"

    def __repr__(self):
        """Method __repr__"""
        return f"Vector : '{self.family_name}', '{self.eyes}', '{self.hairs}'"
