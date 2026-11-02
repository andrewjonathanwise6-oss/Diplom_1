import pytest

from ingredient import Ingredient


class TestIngredient:
    @pytest.mark.parametrize(
        ("ingredient_type", "name", "price"),
        [
            ("SAUCE", "hot sauce", 100.0),
            ("FILLING", "cutlet", 250.5),
            ("SAUCE", "water", 0.0),
        ],
    )
    def test_get_type_returns_ingredient_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize(
        ("ingredient_type", "name", "price"),
        [
            ("SAUCE", "hot sauce", 100.0),
            ("FILLING", "cutlet", 250.5),
            ("SAUCE", "water", 0.0),
        ],
    )
    def test_get_name_returns_ingredient_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_name() == name

    @pytest.mark.parametrize(
        ("ingredient_type", "name", "price"),
        [
            ("SAUCE", "hot sauce", 100.0),
            ("FILLING", "cutlet", 250.5),
            ("SAUCE", "water", 0.0),
        ],
    )
    def test_get_price_returns_ingredient_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_price() == price
