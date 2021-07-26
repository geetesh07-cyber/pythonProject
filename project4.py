rock = '''

_______---' __)
             (___)
              (_) 
              (__)
              ---.
      (___)'''

paper = '''

_______
---' __)__ __) ___) ___)---.__)'''

scissors = '''

_______
---' __)__ __) __) (__)---.(___)'''

rps = [rock, paper, scissors]

import random

print("Welcome to Rock, Paper, Scissors Game!")

choice = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer = random.randint(0, len(rps)-1)

print(f"\nYou choose:\n{rps[choice]} \nComputer choose: \n{rps[computer]}")

if (choice == 0) and (computer == 1):

 print("You choose Rock and Computer choose Paper, \nComputer Win!")
elif (choice == 0) and (computer == 2):

 print("You choose Rock and Computer choose Scissors, \nYou Win!")
elif (choice == 1) and (computer == 0):

 print("You choose Paper and Computer choose Rock, \nYou Win!")
elif (choice == 2) and (computer == 0):

 print("You choose Scissors and Computer choose Rock, \nComputer Win!")
elif (choice == 1) and (computer == 2):

 print("You choose Paper and Computer choose Scissors, \nComputer win!")
elif (choice == 2) and (computer == 1):

 print("You choose Scissors and Computer choose Paper, \nYou win!")
else:

 print("You are the same. Please do it again")


