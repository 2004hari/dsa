def print_vowel(vowel):
    char = vowel.lower()
    match char:
        case 'a':
            print("A is a vowel")
        case 'e':
            print("E is a vowel")
        case 'i':
            print("I is a vowel")
        case 'o':
            print("O is a vowel")
        case 'u':
            print("U is a vowel")
        case _:
            print(f"{char} is not a vowel")

print_vowel('a')
print_vowel('b')
print_vowel('E')