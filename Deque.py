from Node import DequeNode


class Deque:
    """Клас для роботи з деком."""

    def __init__(self):
        """Створює порожній дек."""
        self.mLeft = None
        self.mRight = None

    def empty(self):
        """
        Перевіряє, чи дек є порожнім.
        :return: True, якщо дек порожній
        """
        return self.mLeft is None

    def push_left(self, item):
        """
        Додає елемент з лівого боку дека.
        :param item: значення нового елемента
        """
        node = DequeNode(item)

        if self.empty():
            self.mLeft = node
            self.mRight = node
        else:
            node.mNext = self.mLeft
            self.mLeft.mPrev = node
            self.mLeft = node

    def push_right(self, item):
        """
        Додає елемент з правого боку дека.
        :param item: значення нового елемента
        """
        node = DequeNode(item)

        if self.empty():
            self.mLeft = node
            self.mRight = node
        else:
            node.mPrev = self.mRight
            self.mRight.mNext = node
            self.mRight = node

    def pop_left(self):
        """
        Видаляє та повертає елемент з лівого боку дека.
        :return: значення видаленого елемента або None
        """
        if self.empty():
            return None

        item = self.mLeft.mItem
        self.mLeft = self.mLeft.mNext

        if self.mLeft is None:
            self.mRight = None
        else:
            self.mLeft.mPrev = None

        return item

    def pop_right(self):
        """
        Видаляє та повертає елемент з правого боку дека.
        :return: значення видаленого елемента або None
        """
        if self.empty():
            return None

        item = self.mRight.mItem
        self.mRight = self.mRight.mPrev

        if self.mRight is None:
            self.mLeft = None
        else:
            self.mRight.mNext = None

        return item

    def size(self):
        """
        Визначає кількість елементів у деку.
        :return: кількість елементів
        """
        count = 0
        current = self.mLeft

        while current is not None:
            count += 1
            current = current.mNext

        return count

    def print_deque(self):
        """
        Виводить елементи дека зліва направо.
        """
        if self.empty():
            print("Дек порожній.")
            return

        current = self.mLeft

        print("Лівий кінець:", end=" ")

        while current is not None:
            print(current.mItem, end=" <-> ")
            current = current.mNext

        print("Правий кінець")
