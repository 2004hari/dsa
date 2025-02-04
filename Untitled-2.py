def print_vowel(character):
    char = character.lower()
    if char == 'a':
        print("A is a vowel")
    elif char == 'e':
        print("E is a vowel")
    elif char == 'i':
        print("I is a vowel")
    elif char == 'o':
        print("O is a vowel")
    elif char == 'u':
        print("U is a vowel")
    else:
        print(f"{character} is not a vowel")

print_vowel('a')
print_vowel('b')
print_vowel('E')