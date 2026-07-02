from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    sku: str
    name: str
    category: str
    price: float
    in_stock: bool


SAMPLE_ITEMS = [
    Item("BK-001", "Hardcover Notebook", "Books", 12.50, True),
    Item("BK-002", "Paperback Planner", "books", 9.99, False),
    Item("EL-001", "USB-C Hub", "Electronics", 39.99, True),
    Item("EL-002", "Noise Canceling Headphones", "Electronics", 149.00, False),
    Item("KT-001", "Steel Water Bottle", "Kitchen", 22.00, True),
]

