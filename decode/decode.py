
def decode(messageFilePath='coding_qual_input.txt'):
    def triangle(tier):
        if not(isinstance(tier, int)):
            return False
        elif(tier < 1):
            return False
        elif(tier == 1):
            tierNumber = 1
            return tierNumber
        elif( tier > 1):
            tierNumber = triangle(tier - 1) + tier
            return tierNumber
    messageFile = open(messageFilePath)
    numberWordDict = {}
    words = messageFile.readlines()
    print(words)
    for word in words:
        numberWordDict[word.split(' ')[0]] = word.split(' ')[1][0:-1]
    print(numberWordDict)
    print(len(numberWordDict))
    decodeList = []
    i = 1;
    while (triangle(i) <= len(numberWordDict)):
        key = str(triangle(i))
        print(key)
        decodeList.append(numberWordDict[key])
        i = i + 1
    message = ''
    for word in decodeList:
        message = message + " " + word
    return message

# if __name__ == "main":
#     message = input()
#     decode(message)
