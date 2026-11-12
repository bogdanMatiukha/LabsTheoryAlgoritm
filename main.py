class Node:
    def __init__(self, item):
        """
        Створює новий вузол списку.
        :param item: значення нового елемента
        """
        self.mItem = item
        self.mNext = None


class LinkedList:
    """Клас для роботи з однозв'язним кільцевим списком."""

    def __init__(self):
        self.mFirst = None

    def empty(self):
        """
        Перевіряє, чи список є порожнім.
        :return: True, якщо список порожній, інакше False
        """
        return self.mFirst is None

    def appendToEndList(self, item):
        """
        Додає новий елемент у кінець списку.
        :param item: значення нового елемента
        """
        node = Node(item)

        if self.empty():
            self.mFirst = node
            node.mNext = node
        else:
            current = self.mFirst

            while current.mNext != self.mFirst:
                current = current.mNext

            current.mNext = node
            node.mNext = self.mFirst

    def print_list(self):
        """
        Виводить усі елементи списку на екран.
        """
        if self.empty():
            print("Список порожній.")
            return

        current = self.mFirst

        while True:
            print(current.mItem, end=" -> ")
            current = current.mNext

            if current == self.mFirst:
                break

        print("(початок списку)")

    def insert_after_middle(self, item):
        """
        Додає новий елемент після середнього елемента списку.
        :param item: значення нового елемента
        """
        if self.empty():
            print("Список порожній.")
            return

        size = self.get_size()
        middle = (size - 1) // 2

        current = self.mFirst

        for i in range(middle):
            current = current.mNext

        node = Node(item)
        node.mNext = current.mNext
        current.mNext = node

        print("Елемент успішно додано після середнього.")

    def delete(self, item):
        """
        Видаляє перший знайдений елемент із заданим значенням.
        :param item: значення елемента, який потрібно видалити
        """
        if self.empty():
            print("Список порожній.")
            return

        current = self.mFirst
        previous = None

        while True:
            if current.mItem == item:

                if previous is None:
                    if current.mNext == self.mFirst:
                        self.mFirst = None
                    else:
                        last = self.mFirst

                        while last.mNext != self.mFirst:
                            last = last.mNext

                        self.mFirst = current.mNext
                        last.mNext = self.mFirst
                else:
                    previous.mNext = current.mNext

                print("Елемент успішно видалено.")
                return

            previous = current
            current = current.mNext

            if current == self.mFirst:
                break

        print("Елемент не знайдено.")

    def get_size(self):
        """
        Визначає кількість елементів у списку.
        :return: кількість елементів списку
        """
        if self.empty():
            return 0

        count = 0
        current = self.mFirst

        while True:
            count += 1
            current = current.mNext

            if current == self.mFirst:
                break

        return count

    def create_calendar(self):
        """
        Створює календар із назвами дванадцяти місяців року.
        """
        self.mFirst = None

        months = [
            "Січень",
            "Лютий",
            "Березень",
            "Квітень",
            "Травень",
            "Червень",
            "Липень",
            "Серпень",
            "Вересень",
            "Жовтень",
            "Листопад",
            "Грудень",
        ]

        for month in months:
            self.appendToEndList(month)

        print("Календар успішно створено.")


def main():
    my_list = LinkedList()

    while True:
        print("\n========== МЕНЮ ==========")
        print("1. Додати елемент у кінець списку")
        print("2. Вивести список")
        print("3. Додати елемент після середнього")
        print("4. Видалити певний елемент")
        print("5. Визначити розмір списку")
        print("6. Створити календар")
        print("0. Вихід")
        print("==========================")

        choice = input("Оберіть дію: ")

        if choice == "1":
            value = input("Введіть значення: ")
            my_list.appendToEndList(value)
            print("Елемент додано.")

        elif choice == "2":
            my_list.print_list()

        elif choice == "3":
            value = input("Введіть новий елемент: ")
            my_list.insert_after_middle(value)

        elif choice == "4":
            value = input("Введіть елемент для видалення: ")
            my_list.delete(value)

        elif choice == "5":
            print("Розмір списку:", my_list.get_size())

        elif choice == "6":
            my_list.create_calendar()

        elif choice == "0":
            print("Завершення програми.")
            break

        else:
            print("Неправильний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
