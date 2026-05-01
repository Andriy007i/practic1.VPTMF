import datetime

print("Завдання 1: Вивід від 1 до 10")
for i in range(1, 11):
    print(i, end=" ")
print("\n") 

print("Завдання 2: Числа та їх квадрати")
numbers = list(range(1, 21))  # Створюємо список від 1 до 20

for num in numbers:
    square = num ** 2
    print(f"Число: {num:2} | Квадрат: {square:3}")


print("Завдання 3: Розрахунок віку")
try:
    birth_year = int(input("Введіть ваш рік народження: "))
    current_year = datetime.date.today().year
    age = current_year - birth_year
    
    if age >= 0:
        print(f"Ваш вік: {age} років.")
    else:
        print("Здається, ви ще не народилися!")
except ValueError:
    print("Помилка! Будь ласка, введіть число (рік).")

