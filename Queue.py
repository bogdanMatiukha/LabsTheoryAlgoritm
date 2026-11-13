from Node import Node


class Queue:
    """Клас для роботи з чергою (FIFO)."""

    def __init__(self):
        """Створює порожню чергу."""
        self.mFront = None
        self.mRear = None

    def empty(self):
        """
        Перевіряє, чи черга є порожньою.
        :return: True, якщо черга порожня
        """
        return self.mFront is None

    def enqueue(self, item):
        """
        Додає новий елемент у кінець черги.
        :param item: значення нового елемента
        """
        node = Node(item)

        if self.empty():
            self.mFront = node
            self.mRear = node
        else:
            self.mRear.mNext = node
            self.mRear = node

    def dequeue(self):
        """
        Видаляє та повертає перший елемент черги.
        :return: значення видаленого елемента або None
        """
        if self.empty():
            return None

        item = self.mFront.mItem
        self.mFront = self.mFront.mNext

        if self.mFront is None:
            self.mRear = None

        return item

    def size(self):
        """
        Визначає кількість елементів у черзі.
        :return: кількість елементів
        """
        count = 0
        current = self.mFront

        while current is not None:
            count += 1
            current = current.mNext

        return count

    def print_queue(self):
        """
        Виводить усі елементи черги від початку до кінця.
        """
        if self.empty():
            print("Черга порожня.")
            return

        current = self.mFront

        print("Початок черги:", end=" ")

        while current is not None:
            print(current.mItem, end=" -> ")
            current = current.mNext

        print("Кінець")
