import sys
import random

words_list = ['fortnite'] #pre-made list of our words to guess
accepted_input = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word_guess = random.choice(words_list)
word_to_guess = []
for i in range(0, len(word_guess)):
    word_to_guess.append(word_guess[i])
currently = []
for i in word_to_guess:  # fill in our currently guessed list with "_"
    currently.append("_")
guess_letters = []
guesses = 0


#make sure the program will work if we run it using old versions of Python
if sys.version_info[0] < 3:
    input = raw_input

def hangman_graphic(guesses):
    print("")
    print("Currently you know: ", end=" ")
    for i in range(0, len(currently)):
        print(currently[i], end=" ")
    print("")
    print("You have already tried letters:", end=" ")
    for i in range(0, len(guess_letters)):
        print(guess_letters[i], end=" ")
    print("")
    if guesses == -1: # you won graphic
        print("       0      ")
        print("     ~~|~~    ")
        print("      / \     ")
        print("You just saved me!")
        print("You won!")
    elif guesses == 0:
        print("________      ")
        print("|      |      ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif guesses == 1:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif guesses == 2:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /       ")
        print("|             ")
        print("|             ")
    elif guesses == 3:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|      ")
        print("|             ")
        print("|             ")
    elif guesses == 4:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|             ")
        print("|             ")
    elif guesses == 5:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|     /       ")
        print("|             ")
    else:   # you lost graphic
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|     / \     ")
        print("|             ")
        print("The noose tightens around your neck, and you feel the")
        print("sudden urge to urinate.")
        print("GAME OVER!")

def guess_input():
    global guesses
    global currently
    global word_to_guess

    while True:
        user_input = input("Please input your guess (a single letter): ")
        if user_input in accepted_input:
            if user_input in guess_letters:
                print("You have already inputted this letter before, be more attentive!")
            else:
                guess_letters.append(user_input)
                if user_input in word_to_guess:
                    print("Well done, you guessed the right letter")
                    for i in range(0, len(word_to_guess)):
                        if word_to_guess[i] == user_input:
                            currently[i] = user_input
                else:
                    print("Ops, there is no such letter in our word")
                    guesses = guesses + 1

        else:
            print("INPUT ERROR! Please input single letter in range a-z")

        if guesses > 5: #game over you lost
            hangman_graphic(guesses)
            break
        elif "_" in currently: #keep playing
            hangman_graphic(guesses)
        else: #game over you WON
            hangman_graphic(-1)
            break


def hangman():
    hangman_graphic(guesses)
    guess_input()


if __name__ == "__main__":
    hangman()
    print("END!")
