import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print(game_images[choice])

choice2 = random.randint(0,2)

print("Computer Chose:\n")
print(game_images[choice2])

if choice >= 3 or choice < 0:
    print("You typed an invalid number, you lose!")
elif choice == choice2:
    print("Its's a draw")
elif choice == 0 and choice2 == 2:
    print("You win!")
elif choice == 0 and choice2 == 1:
    print("You lose!")
elif choice == 1 and choice2 == 2:
    print("You lose!")
elif choice == 1 and choice2 == 0:
    print("You win!")
elif choice == 2 and choice2 == 1:
    print("You win!")
elif choice == 2 and choice2 == 0:
    print("You lose!")
