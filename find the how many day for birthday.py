def day_of_year(date):
    
    year, month, day = map(int, date.split('-')) 
    # Convert "YYYY-MM-DD" to integers

    # Days in each month 
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    #Check if it's a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29  

    
    day_number = sum(days_in_month[:month-1]) + day

    return day_number


print(day_of_year("2020-03-01"))  

