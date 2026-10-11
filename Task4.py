numbers = [101, 202, 303, 202, 101]

# 1. Видалення дублікатів зі збереженням порядку
seen = set()
no_duplicates = []
for num in numbers:
    if num not in seen:
        seen.add(num)
        no_duplicates.append(num)
print("1. Без дублікатів (із збереженням порядку):", no_duplicates)

# 2. Множина парних чисел
even_numbers_set = {num for num in numbers if num % 2 == 0}
print("2. Множина парних чисел:", even_numbers_set)

# 3. Кортеж перших п'яти мінімальних чисел
sorted_numbers = sorted(numbers)
first_5_min_tuple = tuple(sorted_numbers[:5])
print("3. Кортеж 5 мінімальних чисел:", first_5_min_tuple)

# 4. Словник позиція -> значення
pos_val_dict = {i: val for i, val in enumerate(numbers)}
print("4. Словник (позиція -> значення):", pos_val_dict)

# 5. Статистика
total_count = len(numbers)
duplicates_count = total_count - len(set(numbers))
min_val = min(numbers) if numbers else None
max_val = max(numbers) if numbers else None

print("\n--- Статистика числового списку ---")
print(f"Загальна кількість елементів: {total_count}")
print(f"Кількість дублікатів: {duplicates_count}")
print(f"Мінімальне значення: {min_val}")
print(f"Максимальне значення: {max_val}")
