from typing import Any

from inventory.models import SAMPLE_ITEMS, Item


def search_items(query: dict[str, Any], items: list[Item] | None = None) -> list[dict[str, Any]]:
    """Search inventory items for API clients.

    T2 should implement this function by reusing inventory.catalog.filter_items.
    """
    _ = query
    _ = items or SAMPLE_ITEMS
    raise NotImplementedError("T2 should expose catalog filtering through this API")

