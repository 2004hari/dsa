def findingthebignumber(n1, n2):
    # using the if else statement to find the biggest number of two  elements
    if n1 > n2:
        print("n1 is yhe biggest number")
    elif n2 > n1:
        print("n2 is the biggest number")
    else:
        print("Both numbers are equal")
try:
    n1=float(input("enter the first number") )   
    n2=float(input("enter the second number") )
except:
    print("please enter valid numbers")  
findingthebignumber(n1, n2)    
              