from typing import List
from letter_state import LetterState
from wordle import Wordle
from colorama import Fore
import random


def main():
    returned = choose_word("data\shortelemental_words.txt")
    chosenword = returned[0]
    possiblewordlist = [x.name for x in returned[1]]

    secret = chosenword.name
    wordformat = chosenword.formating
    wordle = Wordle(secret, wordformat)

    cringe = []
    for digit in wordformat:
        cringe.append(digit * "_")
    blankformat = " ".join(cringe)

    #print(secret)
    display_results(wordle, wordformat)

    while wordle.can_attempt:
        x = input("\nType your guess: ").title()

        if [len(i) for i in x.split()] != wordformat:
            print(
                Fore.RED
                + f"Word must be in {blankformat} format!"
                + Fore.RESET
            )
            continue

        if not (x in possiblewordlist):
            print(
                Fore.RED
                + f"Word must be a real word!"
                + Fore.RESET
            )
            continue

        wordle.attempt(x)
        display_results(wordle, wordformat)

    if wordle.is_solved:
        print("You've solved the puzzle.")
    else:
        print("You failed to solve the puzzle!")
        print(f"The secret word was: {wordle.secret}")

class Word: # record to replace 2 dimensional list
        def __init__(self, name, formating, format_count, mode):
            self.name = name
            self.formating = formating
            self.format_count = format_count
            self.mode = mode

def choose_word(filepath: str):
    def total_words(file): # number of words
        with open(file, "r") as f:
            for count, line in enumerate(f):
                pass
        return count + 1

    # IMPORT AND COUNT IF SET TO RETURN LEN
    lst = [] # 'database'
    f = open(filepath) # supposed to be elemental_words file
    for i in range(total_words(filepath)):
        line = f.readline()[:-1] # -1 to exclude \n
        formating = [len(i) for i in line.split()] # e.g Ba Co N -> [2, 2, 1]
        lst.append(Word(line, formating, 0, 0))
    f.close()

    format_lst = [word.formating for word in lst]

    for word in lst:
        word.format_count = format_lst.count(word.formating)
        if word.format_count == 1:
            word.mode = "challenge" # only has 1 attempt
        else:
            word.mode = "wordle" # wordle with 2 twists

    lst1 = [word for word in lst if word.mode == "wordle"]
    chosenword = random.choice(lst1)
    return [chosenword, lst1]


def display_results(wordle: Wordle, wordformat : List[int]):
    print("\nYour results so far...")
    print(f"You have {wordle.remaining_attempts} attempts remaining.\n")

    lines = []

    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        lines.append(colored_result_str)
        # lines.append(word)

    for _ in range(wordle.remaining_attempts):
        # lines.append(" ".join(["_"] * wordle.WORD_LENGTH))
        line = []
        for digit in wordformat:
            line.append(digit * "_")
        lines.append(" ".join(line))

    draw_border_around(lines, size=wordle.WORD_LENGTH)


def convert_result_to_color(result: List[LetterState]):
    result_with_color = []
    for element in result:
        if element.is_in_position:
            color = Fore.GREEN
        elif element.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE
        colored_letter = color + element.character + Fore.RESET
        result_with_color.append(colored_letter)
    return " ".join(result_with_color)


def draw_border_around(lines: List[str], size: int = 9, pad: int = 1):
 
    content_length = size + pad * 2
    top_border = "┌" + "─" * content_length + "┐"
    bottom_border = "└" + "─" * content_length + "┘"
    space = " " * pad
    print(top_border)

    for line in lines:
        print("│" + space + line + space + "│")

    print(bottom_border)


if __name__ == "__main__":
    main()
