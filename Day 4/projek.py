import random
idk= ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
,
"""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
,
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]
choice=input(print("rock, paper, scissor ? : "))
choiceInt= 0
if choice=="rock":
    choiceInt=0
elif choice=="paper" :
    choiceInt=1
elif choice=="scissor" :
    choiceInt=2

computer_choice=random.randint(1,2)
if choiceInt==computer_choice:
    print("Draw")
    print("Your Choice : ")
    print(idk[choice])
    print("computer choice : ")
    print(idk[computer_choice])
elif choiceInt > choice :
    print("")