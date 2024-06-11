#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import os
# opening the mail file

PATH = './Input/Letters/starting_letter.txt'
# PATH = os.path.abspath(PATH)
with open(PATH, 'r') as file:
    lines = file.readlines()
    header = lines[0]
    with open('./Input/Names/invited_names.txt', 'r') as listOfNames:
        nameList = listOfNames.readlines()
        for name in nameList:
            name = name.strip()
            newHeader = header.replace('[name]', name)
            newHeader.strip()
            lines[0] = (newHeader)
            total = ''
            for line in lines:
                total = total + line

            print(total)
            filename = name + ".txt"
            with open(filename, 'w') as newFile:
                newFile.write(total)
                


            





            

    # header = lines[0]
    # print(header)