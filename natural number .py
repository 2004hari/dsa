n = int(input("Enter the value of n: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    total = 0
    for i in range(1, n + 1):  # Loop from  natural numbers from 1 to n
        total += i
    print("The sum of the first  natural number is ")
