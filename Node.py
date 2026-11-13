class Node:
    """Вузол однозв'язного списку для стека та черги."""

    def __init__(self, item):
        """
        Створює новий вузол.
        :param item: значення нового елемента
        """
        self.mItem = item
        self.mNext = None

class DequeNode:
    """Вузол двозв'язного списку для дека."""

    def __init__(self, item):
        """
        Створює новий вузол дека.
        :param item: значення нового елемента
        """
        self.mItem = item
        self.mNext = None
        self.mPrev = None
