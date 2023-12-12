import random

def Not_found(incorrect):
    from hangman_art import stages
    print(str(stages[incorrect]))

from hangman_words import word_list
chosen_word = random.choice(word_list)
hangman_not_done = True
incorrect = 0
guess = ""
length = len(chosen_word)
towin = length
blanks = []
display = []
for i in range(0,length):
    blanks.append("_")

from hangman_art import logo, stages
print(logo)
print(f"\nThe word is {' '.join(blanks)}") 

while hangman_not_done:
     guess = input(f"\n Guess a letter:").lower()
     counthelper = 0
     found = False
     if guess in display:
         print(f"You have already guessed {guess}")
     else:
         display.append(guess)
         for letter in chosen_word:
             if letter == guess:
                 blanks[counthelper] = guess
                 towin -= 1
                 found = True
             counthelper += 1   
         print(f"{' '.join(blanks)}")
         if found == False:
             incorrect += 1
             Not_found(6 - incorrect)
             if incorrect == 6:
                 print("Game Over!")
                 hangman_not_done = False
         else:
             print(stages[6 - incorrect])
         if towin == 0:
             hangman_not_done = False
             print(f"You win and you had {incorrect} incorrect guesses.")