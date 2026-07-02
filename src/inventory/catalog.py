from collections.abc import Iterable

from inventory.models import Item


def filter_items(
    items: Iterable[Item],
    *,
    category: str | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
    in_stock: bool | None = None,
) -> list[Item]:
    """Filter inventory items.

    Category matching is case-insensitive. Price bounds are inclusive.
    """
    normalized_category = category.casefold() if category else None
    result: list[Item] = []

    for item in items:
        if normalized_category and item.category.casefold() != normalized_category:
            continue
        if min_price is not None and item.price < min_price:
            continue
        if max_price is not None and item.price > max_price:
            continue
        if in_stock is not None and item.in_stock is not in_stock:
            continue
        result.append(item)

    return result

