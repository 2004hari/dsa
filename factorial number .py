
def calculate_factorial(n):
    # If the number is negative is not a factorial number
    if n < 0:
        return " is not a factorial number"
    
    # give factorial as 1 
    factorial = 1
    
    # Use a while loop
    while n > 1:
        factorial *= n  # Multiply current factorial by n
        n -= 1  # Decrease n by 1
        
    return factorial

def main():
    print("Welcome to the Factorial Calculator!")

    # Input
    while True:
        try:
            num = int(input("Please enter a non-negative integer to find its factorial: "))
            if num < 0:
                print("Please enter a non-negative number. Try again.")
                continue
            break  # Exit the loop 
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Call the funtion 
    result = calculate_factorial(num)

    
    print(f"The factorial of {num} is {result}")


main()
