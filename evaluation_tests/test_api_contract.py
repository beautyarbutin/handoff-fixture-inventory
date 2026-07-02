from inventory.api import search_items
from inventory.models import SAMPLE_ITEMS


def test_search_items_reuses_catalog_filtering_semantics():
    results = search_items(
        {
            "category": "BOOKS",
            "min_price": 9.99,
            "max_price": 12.50,
            "in_stock": False,
        },
        items=SAMPLE_ITEMS,
    )

    assert results == [
        {
            "sku": "BK-002",
            "name": "Paperback Planner",
            "category": "books",
            "price": 9.99,
            "in_stock": False,
        }
    ]


def test_search_items_omits_unknown_query_keys():
    results = search_items({"unknown": "ignored", "in_stock": True}, items=SAMPLE_ITEMS)

    assert [item["sku"] for item in results] == ["BK-001", "EL-001", "KT-001"]


def test_search_items_rejects_invalid_price_values():
    try:
        search_items({"min_price": "cheap"}, items=SAMPLE_ITEMS)
    except ValueError as exc:
        assert "min_price" in str(exc)
    else:
        raise AssertionError("search_items should reject non-numeric min_price")

