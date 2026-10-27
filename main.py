class HashTable:
    """Клас для роботи з хеш-таблицею фільмів."""

    def __init__(self, size=10):
        """Створює порожню хеш-таблицю заданого розміру."""
        self.size = size
        self.table = {}

    def hash_function(self, key):
        """Обчислює індекс комірки за назвою фільму."""
        return sum(ord(char) for char in key) % self.size

    def add(self, name, year):
        """Додає фільм до таблиці або оновлює його рік випуску."""
        index = self.hash_function(name)

        if index not in self.table:
            self.table[index] = []

        for film in self.table[index]:
            if film[0].lower() == name.lower():
                film[1] = year
                print("Фільм оновлено.")
                return

        self.table[index].append([name, year])
        print("Фільм додано.")

    def search(self, name):
        """Знаходить фільм за назвою та повертає його дані."""
        index = self.hash_function(name)

        for film in self.table.get(index, []):
            if film[0].lower() == name.lower():
                return film

        return None

    def delete(self, name):
        """Видаляє фільм за назвою з хеш-таблиці."""
        index = self.hash_function(name)

        for film in self.table.get(index, []):
            if film[0].lower() == name.lower():
                self.table[index].remove(film)

                if not self.table[index]:
                    del self.table[index]

                print("Фільм видалено.")
                return

        print("Фільм не знайдено.")

    def show(self):
        """Виводить усі зайняті комірки хеш-таблиці."""
        print("\nХеш-таблиця:")

        if not self.table:
            print("Таблиця порожня.")
            return

        for index, films in sorted(self.table.items()):
            print(f"{index}: ", end="")

            for film in films:
                print(f"[{film[0]}, {film[1]}]", end=" ")

            print()


def main():
    """Запускає меню та обробляє команди користувача."""
    hash_table = HashTable()

    while True:
        print("\n=== МЕНЮ ===")
        print("1. Переглянути хеш-таблицю")
        print("2. Додати фільм")
        print("3. Знайти фільм")
        print("4. Видалити фільм")
        print("5. Вийти")

        choice = input("Виберіть дію: ")

        if choice == "1":
            hash_table.show()

        elif choice == "2":
            name = input("Назва фільму: ")
            try:
                year = int(input("Рік випуску: "))
                hash_table.add(name, year)
            except ValueError:
                print("Рік повинен бути числом.")

        elif choice == "3":
            name = input("Введіть назву фільму: ")
            film = hash_table.search(name)

            if film:
                print(f"Знайдено: {film[0]}, рік випуску: {film[1]}")
            else:
                print("Фільм не знайдено.")

        elif choice == "4":
            name = input("Введіть назву фільму для видалення: ")
            hash_table.delete(name)

        elif choice == "5":
            print("Завершення програми.")
            break

        else:
            print("Невірний пункт меню.")


if __name__ == "__main__":
    main()
