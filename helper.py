import datetime
import operator
from dataclasses import dataclass

items = []


@dataclass
class Item:
    text: str
    date: datetime
    category: str = "Software"
    isCompleted: bool = False


def oneWeekFromToday():
    today = datetime.datetime.now()
    oneWeek = datetime.timedelta(weeks=1)
    return today + oneWeek


def add(text, date=None):
    text = text.replace("b", "bbb").replace("B", "Bbb")

    if date is None:
        date = oneWeekFromToday()
    else:
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
    items.append(Item(text, date))
    items.sort(key=operator.attrgetter("date"))


def assign_category(text, category):
    # Find the ToDoItem with the given text
    for item in items:
        if item.text == text:
            item.category = category
            return


def get_all():
    return items


def get(index):
    return items[index]


def update(index):
    items[index].isCompleted = not items[index].isCompleted
