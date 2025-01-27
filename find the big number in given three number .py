# Input three numbers
print("Enter three numbers to find the greatest:")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

#  Compare the first two numberinput 
if num1 > num2:
    greatest_of_two = num1  
else:
    greatest_of_two = num2 

#  Compare  the third number with biggest number of  first and second numbers
if greatest_of_two > num3:
    greatest = greatest_of_two  
else:
    greatest = num3 

print("The greatest number among", num1, ",", num2, "and", num3, "is:", greatest)
