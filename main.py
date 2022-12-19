
waht = input("Выбирете действие? (+,-,*,/,%,**): ")

a = float( input("Введите первое число:"))
b = float(input("Введите второе число"))

if waht == "+":
    c = a + b
    print("Результат: ", str(c))
elif  waht == "-":
    c = a - b
    print("Результат: " + str(c))
elif waht == "*":
    c = a * b
    print("Результат: " + str(c))
elif waht == "/":
    c = a / b
    print("Результат: " + str(c))
elif waht == "%":
    c = a % b
    print("Результат: " + str(c))
elif waht == "**":
    c = a ** b
    print("Результат: " + str(c))
else:
    print("неверная операция")