def is_leap_year(year):
    print("Checking year:", year)  # Debugging line to track the year being checked

    # Check if the year is divisible by 4
    if year % 4 == 0:
        # If divisible by 4, check if it is divisible by 100
        if year % 100 == 0:
            # If divisible by 100, check if it is also divisible by 400
            if year % 400 == 0:
                # Divisible by 400, it's a leap year
                return True
            else:
                # Divisible by 100 but not by 400, it's not a leap year
                return False
        else:
            # Divisible by 4 but not by 100, it's a leap year
            return True
    else:
        # Not divisible by 4, it's not a leap year
        return False

# Test case: 2004 is a leap year
print(is_leap_year(2004))  # Should print True
