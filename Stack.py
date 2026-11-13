from Node import Node


class Stack:
    """Клас для роботи зі стеком (LIFO)."""

    def __init__(self):
        """Створює порожній стек."""
        self.mTop = None

    def empty(self):
        """
        Перевіряє, чи стек є порожнім.
        :return: True, якщо стек порожній
        """
        return self.mTop is None

    def push(self, item):
        """
        Додає елемент на вершину стека.
        :param item: значення нового елемента
        """
        node = Node(item)
        node.mNext = self.mTop
        self.mTop = node

    def pop(self):
        """
        Видаляє та повертає елемент із вершини стека.
        :return: значення видаленого елемента або None
        """
        if self.empty():
            return None

        item = self.mTop.mItem
        self.mTop = self.mTop.mNext
        return item

    def size(self):
        """
        Визначає кількість елементів у стеку.
        :return: кількість елементів
        """
        count = 0
        current = self.mTop

        while current is not None:
            count += 1
            current = current.mNext

        return count

    def print_stack(self):
        """
        Виводить елементи стека від вершини до основи.
        """
        if self.empty():
            print("Стек порожній.")
            return

        current = self.mTop

        print("Вершина стека:", end=" ")

        while current is not None:
            print(current.mItem, end=" -> ")
            current = current.mNext

        print("None")
