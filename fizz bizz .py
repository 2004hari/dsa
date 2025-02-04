def fizzBuzz(n):
    result = []  # to store the value
    
    for i in range(1, n + 1):  
        if i % 3 == 0 and i % 5 == 0: 
            # Divide by both 3 and 5
            result.append("FizzBuzz")
        elif i % 3 == 0:  
            # Divide by 3
            result.append("Fizz")
        elif i % 5 == 0:  
            # Divide by 5
            result.append("Buzz")
        else: 
            # Not divisible
            result.append(str(i)) 

    return result  

print(fizzBuzz(15))  
