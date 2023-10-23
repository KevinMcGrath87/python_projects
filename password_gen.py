import random



letters = int(input("how many letters will your password contain?"))
numbers = int(input("how many numbers will your password contain"))
symbols = int(input("how many symbols?"))

letters_choice = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_choice = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_choice = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

arrayfrom = [letters_choice,numbers_choice,symbols_choice]
password = ""
for index in range(0, (letters+numbers+symbols)):
    select_from = arrayfrom[random.randint(0,len(arrayfrom)-1)]
    password = password + select_from[random.randint(0,len(select_from)-1)]

print (password)

