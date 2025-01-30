# creating the funtion  
def is_multiple_of_27(n):
    return n % 27 == 0
# giving the input 


num = int(input("Enter a number: "))
# calling the function using the conditional statement

if is_multiple_of_27(num):
    print("is the multiple of 27")
else:
    print(" is not  a multiple of 27.")
