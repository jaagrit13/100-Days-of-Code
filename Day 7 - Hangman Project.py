import random
import hangmanart as ha
import hangmanword as hw
chosen_word = random.choice(hw.word_list)
word_length = len(chosen_word)
# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

lives = 6
display = []
endgame = False
print(ha.logo)

for i in range(len(chosen_word)):
    display.append("_")

while not endgame and  lives > 0:
    guess = input("Guess a letter: ").lower()

    if guess in display:
      print("You've already guessed {}".format(guess))

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
    if guess not in chosen_word:
        print("You guessed {}, that's not in the word. You lose a life.".format(guess))
        lives -= 1
    print(" ".join(display))
    print(ha.stages[lives])

    if "_" not in display:
        endgame = True
        print("You win.")
if lives == 0:
    print("You lose.")
