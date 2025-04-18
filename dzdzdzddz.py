try:
    user_input = input("Введіть число: ")
    number = int(user_input)
    print("Ви ввели ціле число:", number)
except ValueError:
    print("Помилка:введене значення не можна конвертувати в ціле")
