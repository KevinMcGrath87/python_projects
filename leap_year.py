def isLeapYear(integer=input("write the year you want to check as a positive integer.")):
    integer = int(integer)
    if(integer % 4 == 0):
        if(integer % 100 != 0):
            return(f"the year {integer} is a leap year")
        elif (integer % 400 == 0):
            return(f"the year {integer} is a leap year")
        else:
            return(f"the year {integer} is not a leap year")
    else:
        return(f"the year {integer} is not a leap year")
    
print(isLeapYear())