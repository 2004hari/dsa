def is_armstrong(number):

    num_str = str(number)
    num_digits = len(num_str)
    

    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    return sum_of_powers == number


num = 153
if is_armstrong(num):
    print("these is the armstrong number")
else:
    print(" these is not a arm strong number")
