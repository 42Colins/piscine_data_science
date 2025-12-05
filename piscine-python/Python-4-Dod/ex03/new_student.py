import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Class Student"""
    name: str
    surname: str
    active: bool = True
    id: str = field(init=False, default_factory=generate_id)
    login: str = field(init=False)

    def __post_init__(self):
        """Post init"""
        self.login = f"{self.name[0].lower()}{self.surname[:7].lower()}"
