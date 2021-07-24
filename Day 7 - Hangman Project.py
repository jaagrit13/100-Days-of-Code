import random
import hangmanart as ha
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

lives = 6
display = []
endgame = False

for i in range(len(chosen_word)):
    display.append("_")

while not endgame and  lives > 0:
    guess = input("Guess a letter: ").lower()

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
    if guess not in chosen_word:
        lives -= 1
    print(" ".join(display))
    print(stages[lives])

    if "_" not in display:
        endgame = True
        print("You win.")
if lives == 0:
    print("You lose.")
