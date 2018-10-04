from .address import Address

class User:

    def __init__(self, name: str, address: Address = None):
        self.name = name
        self.address = address