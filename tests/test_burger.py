from unittest.mock import Mock

import pytest

from bun import Bun
from burger import Burger
from ingredient import Ingredient


@pytest.fixture
def ingredients():
    return [
        Ingredient("FILLING", "onion", 10.0),
        Ingredient("SAUCE", "sauce", 20.0),
        Ingredient("FILLING", "tomato", 30.0),
    ]


def test_new_burger_starts_without_bun_or_ingredients():
    burger = Burger()

    assert burger.bun is None
    assert burger.ingredients == []


def test_set_buns_assigns_bun():
    burger = Burger()
    bun = Bun("sesame", 100.0)

    burger.set_buns(bun)

    assert burger.bun is bun


def test_add_ingredient_appends_ingredient(ingredients):
    burger = Burger()

    burger.add_ingredient(ingredients[0])

    assert burger.ingredients == [ingredients[0]]


@pytest.mark.parametrize(
    ("index", "expected_names"),
    [
        (0, ["sauce", "tomato"]),
        (1, ["onion", "tomato"]),
        (2, ["onion", "sauce"]),
    ],
)
def test_remove_ingredient_removes_requested_item(ingredients, index, expected_names):
    burger = Burger()
    burger.ingredients = ingredients.copy()

    burger.remove_ingredient(index)

    assert [ingredient.get_name() for ingredient in burger.ingredients] == expected_names


@pytest.mark.parametrize(
    ("index", "new_index", "expected_names"),
    [
        (0, 2, ["sauce", "tomato", "onion"]),
        (2, 0, ["tomato", "onion", "sauce"]),
        (1, 1, ["onion", "sauce", "tomato"]),
    ],
)
def test_move_ingredient_reorders_items(ingredients, index, new_index, expected_names):
    burger = Burger()
    burger.ingredients = ingredients.copy()

    burger.move_ingredient(index, new_index)

    assert [ingredient.get_name() for ingredient in burger.ingredients] == expected_names


def test_get_price_doubles_bun_price_and_adds_ingredient_prices():
    bun = Mock(spec=Bun)
    bun.get_price.return_value = 120.0
    first_ingredient = Mock(spec=Ingredient)
    first_ingredient.get_price.return_value = 35.0
    second_ingredient = Mock(spec=Ingredient)
    second_ingredient.get_price.return_value = 55.0
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(first_ingredient)
    burger.add_ingredient(second_ingredient)

    price = burger.get_price()

    assert (
        price == 330.0
        and bun.get_price.call_count == 1
        and first_ingredient.get_price.call_count == 1
        and second_ingredient.get_price.call_count == 1
    )


def test_get_receipt_formats_bun_ingredients_and_total_price():
    burger = Burger()
    burger.set_buns(Bun("Sesame", 120.0))
    burger.add_ingredient(Ingredient("SAUCE", "Mustard", 25.0))
    burger.add_ingredient(Ingredient("FILLING", "Patty", 125.0))

    receipt = burger.get_receipt()

    assert receipt == (
        "(==== Sesame ====)\n"
        "= sauce Mustard =\n"
        "= filling Patty =\n"
        "(==== Sesame ====)\n\n"
        "Price: 390.0"
    )
