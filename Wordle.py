import random 
import sys
from termcolor import colored # type: ignore
import nltk
from nltk.corpus import words

def print_menu():
    print("1. Play Wordle")
    print("Write a 5 letter word to guess the word!\n")


def read_rand_word():
    with open("testword.txt") as f:
        words = f.read().splitlines()
    return random.choice(words)

nltk.data.path.append('/work/words')
word_list = words.words()
words_five = [word for word in word_list if len(word) == 5]
print_menu()
#word = read_rand_word() # read a random word from the file
word - random.choice(words_five)
print(word)
play_again = ""
while play_again != "q":
    for attempt in range (1,7): # 6 attempts
        guess = input().lower()

        sys.stdout.write('\x1b[1A') # move cursor up one linebenji

        sys.stdout.write('\x1b[2K') # clear line

        for i in range(min(len(guess),5)):
            if guess [i] == word[i]:
                print (colored (guess[i], 'green'), end = "")
            elif guess[i] in word:
                print (colored (guess[i], 'yellow'), end = "")
            else:
                print (colored (guess[i], 'red'), end = "")
        print()


        if guess == word:
            print(colored(f"\nYou guessed the word in {attempt} attempts!", 'red'))
            break
        elif attempt == 6:
            print(colored(f"\nYou did not guess the word. The word was {word}", 'red'))
            break
play_again = input("Press 'q' to quit or any other key to play again: ")
            

