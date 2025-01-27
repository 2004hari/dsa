numbers = [10, -5, 12, 0, 15, -8, 20]

# using the for loop below code to generate the positive numbers
for num in numbers:
    if num < 0:
        # If the number is negative skip to next 
        continue
    elif num == 0:
        # If the number is zero break the loop
        print("Zero encountered, stopping the loop.")
        break
    else:
        #print the positive
        print("Positive number:", num)
