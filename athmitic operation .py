def calculator(a, b, choice):
    if choice == 'a':
        return str(a) + "a" + str(b) + " = " + str(a + b)
    elif choice == 's':
        return str(a) + "s" + str(b) + " = " + str(a - b)
    elif choice == 'm':
        return str(a) + "m" + str(b) + " = " + str(a * b)
    elif choice == 'd':
        if b != 0:
            return str(a) + "d" + str(b) + " = " + str(a / b)
        else:
            return "Error: Division by zero!"
    elif choice == 'u':
        return str(a) + "u" + str(b) + " = " + str(a % b)
    else:
        return "Invalid operation!"

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
choice = input("Enter operation (a for addition, s for subtraction, m for multiplication, d for division, u for modulus): ").strip().lower()

print(calculator(a, b, choice))
