
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
# we giving the try and except fuction
try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()
# it do not allow the  letters and  bspecial characters in variables num1 and num2    

result = num1 + num2
# by the arithmetic operator + ad ht e two number num1 and num2
print(f"The sum of {num1} and {num2} is {result}.")
