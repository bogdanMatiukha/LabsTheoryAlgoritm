# 2.1 Списки (list)
L = [3, 1, 4, 1, 5]
print("Початковий список:", L)
print("Елемент L[2]:", L[2])

L.append(9)
L.extend([2, 6])
L.insert(1, 100)
print("Після додавання:", L)

L.remove(1)
popped = L.pop()
del L[0]
print("Після видалення:", L, "| Видалено pop():", popped)

L.sort()
print("Відсортований список:", L)
print("Довжина списку:", len(L))
print("Слайсинг L[1:4]:", L[1:4])

# 2.2 Кортежі (tuple)
t = (1, 2, 3)
print("\nКортеж t:", t)
print("Доступ t[0]:", t[0])
try:
    t[0] = 99
except TypeError as e:
    print("Помилка при зміні кортежу:", e)

t_concat = t + (4, 5)
t_repeat = t * 2
print("Конкатенація:", t_concat)
print("Повторення:", t_repeat)
print("Кількість 2 в t:", t.count(2))
print("Індекс елемента 3 в t:", t.index(3))

# 2.3 Множини (set)  
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

s1.add(10)
s1.discard(10)

print("\nМножини s1 та s2:", s1, s2)
print("Об'єднання (|):", s1 | s2, "Метод:", s1.union(s2))
print("Перетин (&):", s1 & s2, "Метод:", s1.intersection(s2))
print("Різниця (-):", s1 - s2, "Метод:", s1.difference(s2))
print(
    "Симетрична різниця (^):",
    s1 ^ s2,
    "Метод:",
    s1.symmetric_difference(s2),
)
print("Чи є {1, 2} підмножиною s1?:", {1, 2} <= s1)

# 2.4 Словники (dict)
d = {"a": 1, "b": 2}
print("\nПочатковий словник:", d)
print("Значення за ключем 'a':", d.get("a"))
d["c"] = 3
d.update({"b": 20, "d": 4})
d.pop("a")
print("Оновлений словник:", d)
print("Ключі списком:", list(d.keys()))
print("Значення списком:", list(d.values()))
