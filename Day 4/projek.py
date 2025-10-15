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

computer_choice=random.randint(0,2)
if choiceInt==computer_choice:
    print("Draw")
    print("Your Choice : ")
    print(idk[choiceInt])
    print("computer choice : ")
    print(idk[computer_choice])
elif choiceInt - computer_choice == -2 or choiceInt -computer_choice ==1 :
    print("you win")
    print("Your choice : " )
    print(idk[choiceInt])
    print("computer choice : ")
    print(idk[computer_choice])
elif choiceInt - computer_choice == -1 or choiceInt -computer_choice ==2 :
    print("you lose")
    print(" your choice : ")
    print(idk[choiceInt])
    print("computer choide : ")
    print(idk[computer_choice])
else : 
    print("error")