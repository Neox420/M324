from dataclasses import dataclass

items = []


@dataclass
class Item:
    text: str
    isCompleted: bool = False
    date: str = ""


def add(text):
    text = text.replace('b', 'bbb').replace('B', 'Bbb')
    items.append(Item(text, date))
    items.sort(key=operator.attrgetter('date'))


def get_all():
    return items


def get(index):
    return items[index]


def update(index):
    items[index].isCompleted = not items[index].isCompleted
