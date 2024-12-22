import random

def get_word():
  """Selects a random word from a list."""
  words = ["python", "hangman", "programming", "computer", "science"]
  return random.choice(words)

def display_board(word_guess, guessed_letters):
  """Displays the current state of the game."""
  print("Current word:", end=" ")
  for letter in word_guess:
    if letter in guessed_letters:
      print(letter, end=" ")
    else:
      print("_", end=" ")
  print()

def play_hangman():
  """Main game loop."""
  word = get_word()
  word_guess = "_" * len(word)
  guessed_letters = []
  attempts = 6

  while attempts > 0:
    display_board(word_guess, guessed_letters)
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
      print("Invalid input. Please enter a single letter.")
      continue

    if guess in guessed_letters:
      print("You already guessed that letter.")
      continue

    guessed_letters.append(guess)

    if guess in word:
      print("Correct!")
      word_guess = "".join([letter if letter in guessed_letters else "_" for letter in word])
    else:
      print("Incorrect!")
      attempts -= 1

    if word_guess == word:
      print("Congratulations! You won!")
      break

  if attempts == 0:
    print("You lost! The word was:", word)

if __name__ == "__main__":
  play_hangman()
