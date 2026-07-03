import pytest

from inventory.api import search_items
from inventory.models import SAMPLE_ITEMS


def test_search_items_filters_and_returns_plain_dicts():
    results = search_items(
        {"category": "ELECTRONICS", "max_price": 39.99, "in_stock": True},
        items=SAMPLE_ITEMS,
    )

    assert results == [
        {
            "sku": "EL-001",
            "name": "USB-C Hub",
            "category": "Electronics",
            "price": 39.99,
            "in_stock": True,
        }
    ]


def test_search_items_ignores_unknown_query_keys():
    results = search_items({"ignored": "value", "min_price": 100}, items=SAMPLE_ITEMS)

    assert [item["sku"] for item in results] == ["EL-002"]


@pytest.mark.parametrize("key", ["min_price", "max_price"])
def test_search_items_rejects_non_numeric_price_bounds(key):
    with pytest.raises(ValueError, match=key):
        search_items({key: "not numeric"}, items=SAMPLE_ITEMS)
