import pytest

from database import Database
from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.mark.parametrize(
    ("collection", "expected"),
    [
        (
            "buns",
            [
                ("black bun", 100),
                ("white bun", 200),
                ("red bun", 300),
            ],
        ),
        (
            "ingredients",
            [
                (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
                (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
                (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
                (INGREDIENT_TYPE_FILLING, "cutlet", 100),
                (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
                (INGREDIENT_TYPE_FILLING, "sausage", 300),
            ],
        ),
    ],
)
def test_database_initializes_available_items(collection, expected):
    database = Database()
    items = getattr(database, collection)

    if collection == "buns":
        actual = [(bun.get_name(), bun.get_price()) for bun in items]
    else:
        actual = [
            (ingredient.get_type(), ingredient.get_name(), ingredient.get_price())
            for ingredient in items
        ]

    assert actual == expected


def test_available_buns_returns_database_bun_list():
    database = Database()

    assert database.available_buns() is database.buns


def test_available_ingredients_returns_database_ingredient_list():
    database = Database()

    assert database.available_ingredients() is database.ingredients
