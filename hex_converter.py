import math

def hexConverter(inputString):
    hexChar = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g']
    # takking the floor of int/16 we get x such that x*16 'fits' int.
    # if x is...greater than or equal to 16 ....
    integer = int(inputString)
    def largestPower(integer):
        carry = integer
        x=0
        while carry >= 16:
            x += 1
            carry = math.floor(integer/(16**x))
        return x

    largestExponent = largestPower(integer)
    print("largest exponent is", largestExponent)

    def hexed(integer,largestExponent=largestExponent):
        hexArray = []
        while largestExponent >= 0:
            print("sixteen to largestexp is", str(16**largestExponent))
            print("after division" ,math.floor(integer/(16**largestExponent)))
            hexArray.append(hexChar[math.floor(integer/(16**largestExponent))])
            integer = integer - math.floor(integer/16**largestExponent)*(16**largestExponent)
            largestExponent -=1
        print(hexArray)
        return hexArray
    
    characters = hexed(integer, largestExponent)

    string = ''
    for char in characters:
        string = string + char
    
    print(string)
    return(string)



hexConverter(input())

