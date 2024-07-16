import random

class Hangman:
    def __init__(self):
        self.words = [
            "apple", "banana", "cherry", "dog", "elephant", 
            "grape", "orange", "pineapple", "strawberry", "watermelon"
        ]
        self.word_to_guess = random.choice(self.words)
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        self.max_attempts = 6

    def display_word(self):
        display = ""
        for letter in self.word_to_guess:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        return display.strip()

    def display_hint(self):
        return f"The first letter is: {self.word_to_guess[0].upper()}"

    def play(self):
        print(self.display_hint())
        
        while True:
            print(self.display_word())
            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue

            if guess in self.guessed_letters:
                print("You already guessed that letter.")
                continue

            self.guessed_letters.add(guess)

            if guess not in self.word_to_guess:
                self.incorrect_guesses += 1
                print(f"Incorrect guess! Attempts remaining: {self.max_attempts - self.incorrect_guesses}")

            if self.incorrect_guesses >= self.max_attempts:
                print(f"Game over! The word was {self.word_to_guess}.")
                break

            if set(self.word_to_guess) <= self.guessed_letters:
                print(f"Congratulations! You guessed the word: {self.word_to_guess}.")
                break

# Start the game
hangman_game = Hangman()
hangman_game.play()
