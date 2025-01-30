
def get_absolute_value(number):
    if number < 0:  #  the number is negative
        return -number  
    else:
        return number  
  # without using the builtin funtion   

#addition and subtraction
def perform_operations(num1, num2):
    # to  addition
    addition_result = num1 + num2
    absolute_addition = get_absolute_value(addition_result)  

    #to  subtraction
    subtraction_result = num1 - num2
    absolute_subtraction = get_absolute_value(subtraction_result)  

    #
    print(absolute_addition)
    print(absolute_subtraction)


perform_operations(20, 15)       
perform_operations(20, -150)
