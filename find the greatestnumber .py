def greaternumber(a,b,c):
    if a>b & a>c: 
        print("  a is greater than b and c ")
    elif b>c & c>b:
        print ("  b is greater than a and c ")
    elif c>b & c>a:
        print(" c is greater than a and b")
    else:
        print(" given number is equal ")
        
greaternumber(1,2,2)    