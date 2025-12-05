from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King class"""

    @property
    def eyes(self):
        """Property eyes"""
        return self.__dict__["eyes"]

    @eyes.setter
    def eyes(self, value: str):
        """Setter eyes"""
        self.__dict__["eyes"] = value

    @property
    def hairs(self):
        """Property hairs"""
        return self.__dict__["hairs"]

    @hairs.setter
    def hairs(self, value: str):
        """Setter hairs"""
        self.__dict__["hairs"] = value

    def get_eyes(self):
        """Getter eyes"""
        return self.eyes

    def set_eyes(self, eyes: str):
        """Setter eyes"""
        self.eyes = eyes

    def get_hairs(self):
        """Getter hairs"""
        return self.hairs

    def set_hairs(self, hairs: str):
        """Setter hairs"""
        self.hairs = hairs
