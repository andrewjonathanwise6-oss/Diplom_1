import pytest

from ingredient import Ingredient


@pytest.mark.parametrize(
    ("ingredient_type", "name", "price"),
    [
        ("SAUCE", "hot sauce", 100.0),
        ("FILLING", "cutlet", 250.5),
        ("SAUCE", "water", 0.0),
    ],
)
def test_ingredient_returns_its_attributes(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)

    assert ingredient.get_type() == ingredient_type
    assert ingredient.get_name() == name
    assert ingredient.get_price() == price
