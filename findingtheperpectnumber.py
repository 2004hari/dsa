
def is_perfect_number(num):
    #  less than 2
    if num < 2:
        return False


    sum_of_divisors = 0

    # Find all divisors 
    for i in range(1, num):  
        if num % i == 0:  
            sum_of_divisors += i  

    # is sum of divisors equals the numbe
    return sum_of_divisors == num

# input function
num = int(input("Enter a number: "))
if is_perfect_number(num):
    print(num, "is a Perfect Number!")
else:
    print(num, "is NOT a Perfect Number.")
