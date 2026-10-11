import re

text = "Unicode: тестирование, перевірка, тест."

# 1. Список слів у нижньому регістрі без пунктуації
words_list = re.findall(r"\w+", text.lower())
print("1. Список слів:", words_list)

# 2. Множина унікальних слів
unique_words_set = set(words_list)
print("2. Множина унікальних слів:", unique_words_set)

# 3. Кортеж слів, відсортованих за довжиною
words_sorted_by_len = tuple(sorted(words_list, key=len))
print("3. Кортеж слів (сортування за довжиною):", words_sorted_by_len)

# 4. Словник частот появи слів
word_freq = {}
for word in words_list:
    word_freq[word] = word_freq.get(word, 0) + 1
print("4. Словник частот:", word_freq)

# 5. Статистика
total_words = len(words_list)
unique_words_count = len(unique_words_set)
top_5_frequent = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5]

print("\n--- Статистика тексту ---")
print(f"Загальна кількість слів: {total_words}")
print(f"Кількість унікальних слів: {unique_words_count}")
print(f"Топ-5 найчастіших слів: {top_5_frequent}")
