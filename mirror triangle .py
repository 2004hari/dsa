def print_mirrored_triangle(size):
    
    for i in range(1, size + 1):
        for j in range(size - i):
            print(" ", end="")  
        for k in range(i):
            print("* ", end="")  
        print() 
    
    # Lower part triangle
    for i in range(size, 0, -1):
        for j in range(size - i):
            print(" ", end="")  
        for k in range(i):
            print("* ", end="")  
        print()  

size = 7
print_mirrored_triangle(size)
