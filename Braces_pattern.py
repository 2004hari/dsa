def Braces(n):
    for i in range(0,n,1):
        for j in range(0,i+1,1):
            print(j*'{' + j*'}',end='')
    print()
Braces(3)   

print('hi')