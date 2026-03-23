def Summ(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

def Minus(a, b):
    result = a - b
    print(f"{a} - {b} = {result}")

def Mult(a, b):
    print("")

def Delenie(a, b):
    print("")


chisloA = int(input("Введите число А: "))
chisloB = int(input("Введите число Б: "))

print("Выберите действие:\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n")

deistvie = input()

if deistvie.lower() == "1" or "сложение":
    Summ(chisloA, chisloB)

elif deistvie.lower() == "2" or "вычитание":
    Minus(chisloA, chisloB)

elif deistvie.lower() == "3" or "умножение":
    Mult(chisloA, chisloB)

elif deistvie.lower() == "4" or "деление":
    Delenie(chisloA, chisloB)

else:
    print("Введены некорректные данные или выбрано некорректное действие!")
