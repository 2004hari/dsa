def stupid_number(n,l):
    latter="qwertyuiopasdfghjklzxcvbnm"
    
    passwords =  []
    for  char1 in range (1,n+1):
        for char2 in range (1,n+1):
            for char3 in range (l):
                for  char4 in range (l):
                    for char5 in range (1,n+1):
                        if char5 > char1 and char5 > char2:
                            password= str(char1) +str(char2) +latter[char3] +latter[char4] +str(char5)
                            passwords. append(password)
                            print (" ".join(passwords))                            
l = int(input(" entert the number "))                            
n= int ( input ("entert the number"))
stupid_number(n,l)