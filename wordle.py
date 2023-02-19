from math import remainder
from letter_state import LetterState


class Wordle:

    MAX_ATTEMPTS = 6
    WORD_LENGTH = 5
    WORD_FORMAT = []
    VOIDED_LETTER = "*"

    def __init__(self, secret: str, wordformat: list[int]):
        self.secret: str = secret.title()
        self.attempts = []
        self.WORD_FORMAT = wordformat
        self.WORD_LENGTH = sum(wordformat) + len(wordformat) - 1

    def attempt(self, word: str):
        word = word.title()
        self.attempts.append(word)

    def guess(self, word: str):
        elementword = word.title()
        elementwordarray = elementword.split(" ")

        # Initialize the results array with all GREY letters.
        result = [LetterState(x) for x in elementwordarray]

        # Make a copy of the secret so we can cross out 'used' letters.
        remaining_secret = self.secret.split(" ")

        # First, check for GREEN letters.
        for i in range(len(remaining_secret)):
            element = result[i]
            if element.character == remaining_secret[i]:
                element.is_in_position = True
                remaining_secret[i] = self.VOIDED_LETTER

        # Loop again and check for YELLOW letters.
        for i in range(len(remaining_secret)):
            element = result[i]

            # Skip this letter if it is already in the right place.
            if element.is_in_position:
                continue

            # Otherwise, check if the letter is in the word, and void that index.
            for j in range(len(remaining_secret)):
                if element.character == remaining_secret[j]:
                    remaining_secret[j] = self.VOIDED_LETTER
                    element.is_in_word = True
                    break

        return result

    @property
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret

    @property
    def remaining_attempts(self) -> int:
        return self.MAX_ATTEMPTS - len(self.attempts)

    @property
    def can_attempt(self):
        return self.remaining_attempts > 0 and not self.is_solved
