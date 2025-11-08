print("=" * 60)
print("Практика: Запуск Python локально")
print("=" * 60)

# 1. Работа со строками
author = "Данте Алигьери"
print(f"\n1. Автор: {author}")
print(f"   Длина имени: {len(author)} символов")
print(f"   Заглавными: {author.upper()}")

# 2. Работа со списками
works = ["Божественная комедия", "Новая жизнь", "Пир"]
print(f"\n2. Произведения Данте:")
for i, work in enumerate(works, start=1):
    print(f"   {i}. {work}")

# 3. Словарь
info = {
    "имя": "Данте Алигьери",
    "годы": "1265-1321",
    "город": "Флоренция"
}
print(f"\n3. Информация:")
for key, value in info.items():
    print(f"   {key}: {value}")


# 4. Функция
def count_vowels(text):
    """Подсчитывает гласные в тексте"""
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

result = count_vowels("Божественная комедия")
print(f"\n4. Гласных букв: {result}")

print("\n" + "=" * 60)
print("✅ Практика завершена!")
print("=" * 60)