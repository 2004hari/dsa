word = "sak"
n = 3  # Length of the word

for i in range(n):  
    # removing the gap in sentences
    sub = "" 
    for j in range(i + 1):  
        sub += word[j] 
    print(sub)

# for print ak , k, a
for i in range(1, n):  
    sub = ""  
    for j in range(i, n):  
        sub += word[j] 
    print(sub)
