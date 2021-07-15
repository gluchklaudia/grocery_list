from dataclasses import dataclass

@dataclass
class Product:
    """The class that holds the grocery list."""
    name: str
    amount: str
    is_purchased: bool=False