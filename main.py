from Stack import Stack
from Queue import Queue
from Deque import Deque


def stack_menu(stack: Stack):
    """Меню для виконання операцій над стеком."""

    while True:
        print("\n========== СТЕК ==========")
        print("1. Додати елемент (Push)")
        print("2. Видалити елемент (Pop)")
        print("3. Визначити розмір")
        print("4. Вивести стек")
        print("0. Повернутися назад")
        print("==========================")

        choice = input("Оберіть дію: ")

        if choice == "1":
            value = input("Введіть значення: ")
            stack.push(value)
            print("Елемент додано до стека.")

        elif choice == "2":
            item = stack.pop()

            if item is None:
                print("Стек порожній.")
            else:
                print("Видалений елемент:", item)

        elif choice == "3":
            print("Розмір стека:", stack.size())

        elif choice == "4":
            stack.print_stack()

        elif choice == "0":
            break

        else:
            print("Неправильний вибір. Спробуйте ще раз.")


def queue_menu(queue: Queue):
    """Меню для виконання операцій над чергою."""

    while True:
        print("\n========== ЧЕРГА ==========")
        print("1. Додати елемент")
        print("2. Видалити елемент")
        print("3. Визначити розмір")
        print("4. Вивести чергу")
        print("0. Повернутися назад")
        print("===========================")

        choice = input("Оберіть дію: ")

        if choice == "1":
            value = input("Введіть значення: ")
            queue.enqueue(value)
            print("Елемент додано до черги.")

        elif choice == "2":
            item = queue.dequeue()

            if item is None:
                print("Черга порожня.")
            else:
                print("Видалений елемент:", item)

        elif choice == "3":
            print("Розмір черги:", queue.size())

        elif choice == "4":
            queue.print_queue()

        elif choice == "0":
            break

        else:
            print("Неправильний вибір. Спробуйте ще раз.")


def deque_menu(deque: Deque):
    """Меню для виконання операцій над деком."""

    while True:
        print("\n========== ДЕК ==========")
        print("1. Додати елемент ліворуч")
        print("2. Додати елемент праворуч")
        print("3. Видалити елемент ліворуч")
        print("4. Видалити елемент праворуч")
        print("5. Визначити розмір")
        print("6. Вивести дек")
        print("0. Повернутися назад")
        print("=========================")

        choice = input("Оберіть дію: ")

        if choice == "1":
            value = input("Введіть значення: ")
            deque.push_left(value)
            print("Елемент додано ліворуч.")

        elif choice == "2":
            value = input("Введіть значення: ")
            deque.push_right(value)
            print("Елемент додано праворуч.")

        elif choice == "3":
            item = deque.pop_left()

            if item is None:
                print("Дек порожній.")
            else:
                print("Видалений елемент:", item)

        elif choice == "4":
            item = deque.pop_right()

            if item is None:
                print("Дек порожній.")
            else:
                print("Видалений елемент:", item)

        elif choice == "5":
            print("Розмір дека:", deque.size())

        elif choice == "6":
            deque.print_deque()

        elif choice == "0":
            break

        else:
            print("Неправильний вибір. Спробуйте ще раз.")


def main():
    """Головна функція програми."""

    stack = Stack()
    queue = Queue()
    deque = Deque()

    # example data
    arr = [10, 20, 30, 40, 50]

    for item in arr:
        stack.push(item)
        queue.enqueue(item)
        deque.push_left(item)

    # work menu

    while True:
        print("\n========== ГОЛОВНЕ МЕНЮ ==========")
        print("1. Робота зі стеком")
        print("2. Робота з чергою")
        print("3. Робота з деком")
        print("0. Вихід")
        print("==================================")

        choice = input("Оберіть дію: ")

        if choice == "1":
            stack_menu(stack)

        elif choice == "2":
            queue_menu(queue)

        elif choice == "3":
            deque_menu(deque)

        elif choice == "0":
            print("Завершення програми.")
            break

        else:
            print("Неправильний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
