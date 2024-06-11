import math
import random

# pick a random word for the player to guess against and assign to a variable "chose_word".
# have the player input a letter to be the guess letter. (or possibly allow the player to input their guess)
# guess should be normalized to lowercase..

# verify whether the letter is in the chosen_word string and at what position in the string it is in .


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']





word_list_string = "peyote, auspicious, languid, captious, torpid, specious, ostensibly, casuist "
word_list = word_list_string.split(", ")

chosen_word = word_list[random.randint(0, len(word_list)-1)]

# max_guesses = len(chosen_word)

# while loop checks to see if every letter has been guessed or not if not keeps playing until number of max guesses is hit
def guess():
    g = input("guess a letter ")
    g.lower()
    return(g)

def game(guess_number= 0,word_list = word_list):
    print(guess_number)
    chosen_word = word_list[random.randint(0, len(word_list)-1)]
    max_guesses = 7
    print(max_guesses)
    hangman_string = "_ "*len(chosen_word)

    while guess_number != max_guesses:
        print(hangman_string)
        guessed_letter = guess()
        hit = False
        for count, letter in enumerate(chosen_word):
            if letter == guessed_letter:
                hangman_string = hangman_string[:count*2] + guessed_letter + hangman_string[(count*2)+1:]
                hit = True
        if "_" not in hangman_string:
            print("you win!")
            print(chosen_word)
            playflag = input("Play again (Y|N?)")
            if(playflag.lower())=="y":
                game()
            else:
                return
        elif guess_number >= max_guesses:
            print("you Lose")
            playflag = input("Play again (Y|N?)")
            if(playflag.lower())=="y":
                game()
            else:
                return

        else: 
            if hit == False:
                guess_number += 1
                remaining = max_guesses-guess_number
                print("Incorrect", f" guesses remaining: {remaining}")
            if guess_number > 0:
                print(HANGMANPICS[guess_number-1])
            continue

if(__name__ == "__main__"):
    game()
        
        