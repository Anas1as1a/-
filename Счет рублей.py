
number = input("Введите число: ")
if number.isdigit():
    number = int(number)
    if number % 10 == 0 or number % 10 == 5 or number % 10 == 6 or number % 10 == 7 or number % 10 == 8 or number % 10 == 9 or number > 10:
        ending = "ей"
    elif number % 10 == 1 or number % 10 == 21 or number % 10 == 31 or number % == 41 or number % == 51 or number % == 61 or number % 10 == 71 or number % == 81 or number % == 91:
        ending = "ь"
    else number % 10 == 22 or number % 10 = 32 or number % == 42 or number % 10 == 52 or number % 10 == 62 or number % 10 == 72 or number % 10 == 82 or number % 10 == 92:
        ending = "я"
    print(number, "рубл" + ending)
else:
    print("Неккоректный ввод")