input = input("Enter a word or phrase to check if it's a palindrome: ")

def is_palindrome(s):
    # Remove spaces and convert to lowercase 
    s = s.replace(" ", "").lower()
    
    # Compare the string with its reverse
    return s == s[::-1]
# input is a palindrome or not 
if is_palindrome(input):
    print( input ," is a palindrome!")
else:
    print(input ,"is not a palindrome.")
