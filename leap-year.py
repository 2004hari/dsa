def is_leap_year(year):
    print("Checking year:", year)  # Debugging line
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap_year(2004))  # Should print True
