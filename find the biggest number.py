def findingthebignumber(n1, n2):
    # using the if else statement to find the biggest number of two  elements
    if n1 > n2:
        print("The biggest number is" , n1)
    elif n2 > n1:
        print("The biggest number" , n2)
    else:
        print("Both numbers are equal")
   # giving the exeception handling   
   # giving the float  vriable to find the number of elements in numbers  
try:
    n1=float(input("enter the first number") )   
    n2=float(input("enter the second number") )
except:
    print("please enter valid numbers")  
findingthebignumber(n1, n2)    
              