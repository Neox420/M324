import datetime
import pytest
import helper


def test_sort():
    # Given: I have several to-dos with dates
    todos = [
        ("Universum debuggen", "2023-09-06"),
        ("Sinn des Lebens entdecken", "2023-09-01"),
        ("Superheld werden", "2023-10-25"),
        ("Netto null", "2050-01-01"),
    ]

    # When: I add the items
    for todo in todos:
        helper.add(todo[0], todo[1])

    # Then: They should be sorted by date
    for i in range(len(helper.items) - 1):
        assert helper.items[i].date < helper.items[i + 1].date


def test_add():
    # Given: I want to add a to-do with a date
    text = "Lorem ipsum"
    date = "2023-09-02"

    # When: I add the item
    helper.add(text, date)

    # Then: The most recently added to-do should have a date
    item = helper.items[-1]
    assert isinstance(item.date, datetime.date)


def test_category_assignment():
    # Given: I want to assign a category to a to-do
    text = "Debugging"
    date = "2023-09-06"
    category = "Software"

    # When: I add the item and assign a category
    helper.add(text, date)
    helper.assign_category(text, category)

    # Then: The item should have the assigned category
    item = helper.items[-1]  # Get the last added item
    assert isinstance(item.date, datetime.date)
    assert item.category == category
