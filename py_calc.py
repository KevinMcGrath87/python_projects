# DATA TYPES

#Strings

#Integers.

# Floating points

# Booleans


print(type("x"));

numberThatIsAString = str(34);

print(numberThatIsAString);  

def toDigitSum(twoDigitNumber):
    stringVersion = str(twoDigitNumber)
    if len(stringVersion) > 2:
        return "number is too long"
    elif len(stringVersion) < 2:
        return "number is too short needs to be 2 digits"
    else :
        return int(stringVersion[0])+int(stringVersion[1])
    

print(toDigitSum(54))