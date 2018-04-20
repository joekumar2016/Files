import random
import os
import time
import urllib.request


def main():
    word = choose_word()
    print(word)

    # generate board from word
    board = generate_board(word, [])

    # set solved flag to false
    solved = False

    solved_letters = []
    guessed_letters = []
    won = False
    guesses_left = 5
    clear = lambda: os.system('cls')

    # do until the board is solved
    while not solved and guesses_left > 0:

        # print the board and get user's guess
        time.sleep(2)
        clear()
        print("Guesses left: {}".format(guesses_left))
        print(" ".join(board))
        guess = input("Enter guess: ")

        # if the letter has already been guessed, restart the loop
        if guess in guessed_letters:
            print("Already guessed that")
        # if the letter is correct, append it to the board and restart the loop
        elif guess in word:
            print("Yes!")
            solved_letters.append(guess)
            guessed_letters.append(guess)
            board = generate_board(word, solved_letters)

            if not "_" in board:
                solved = True
                won = True

        # if the letter is incorrect, restart the loop
        else:
            print("No")
            guesses_left -= 1

    if won:
        print("Congratulations! You won!")
    else:
        print("Sorry, you lost. Better luck next time.")

    input("Press enter to exit")


def generate_board(word, solved_letters):
    board = []

    # if there are no solved letters, generate a blank board
    # if there are solved letters, replace the blanks with the letters
    if len(solved_letters) == 0:
        for letter in word:
            board.append("_")
    else:
        for letter in word:
            if letter in solved_letters:
                board.append(letter)
            else:
                board.append("_")

    return board


def choose_word():
    try:
        with open("words.txt") as f:
            words = f.readlines()
        words = [x.strip() for x in words]
    except FileNotFoundError:
        print("No file found")
        words = ["Dog", "Cat", "Bird", "Lizard"]

    word = random.choice(words).lower()
    return word


if __name__ == '__main__':
    main()