import random
from hangman_art import logo, stages
from hangman_words import word_list

end_of_the_game = False
lives = 6

chosen_word = random.choice(word_list)

display = []
for letter in chosen_word:
  display.append('_')

print(logo)
#Testing code
#print(f'The solution is {chosen_word}.')
print(f"{' '.join(display)}")

while not end_of_the_game:
  guess = input("Guess a letter: ").lower()

  for letter in range(0, len(chosen_word)):
    if guess == chosen_word[letter]:
      display[letter] = guess
  
  if guess not in chosen_word:
    lives -= 1

  print(f"{' '.join(display)}")
  print(stages[lives])

  if '_' not in display:
    end_of_the_game = True
    print("You won.")
  elif lives == 0:
    end_of_the_game = True
    print("You lose.")
