def finding_thebiggestnumber(number):
    max_number = number[0]
    for num in number:
        if num > max_number:
            max_number = num
    return max_number
finding_thebiggestnumber(1245)
    