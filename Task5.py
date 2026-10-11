# Початковий список кортежів (ім'я, бал)
students_scores = [
    ("Богдан", 85),
    ("Артем", 92),
    ("Дана", 78),
    ("Ігор", 95),
    ("Михайло", 88),
]

# 1. Створення словника з кортежів
scores_dict = dict(students_scores)
print("Словник студентів та оцінок:", scores_dict)

# 2. Обчислення середнього балу
scores = list(scores_dict.values())
average_score = sum(scores) / len(scores) if scores else 0
print(f"Середній бал студентів: {average_score:.2f}")

# 3. Визначення та виведення найвищого балу
best_student, max_score = max(scores_dict.items(), key=lambda item: item[1])
print(f"Найвищий бал: {max_score} (Студент: {best_student})")
