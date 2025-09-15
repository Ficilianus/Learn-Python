print('''
                              ______________                               
                        ,===:'.,            `-._                           
                             `:.`---.__         `-._                       
                               `:.     `--.         `.                     
                                 \.        `.         `.                   
                         (,,(,    \.         `.   ____,-`.,                
                      (,'     `/   \.   ,--.___`.'                         
                  ,  ,'  ,--.  `,   \.;'         `                         
                   `{D, {    \  :    \;                                    
                     V,,'    /  /    //                                    
                     j;;    /  ,' ,-//.    ,---.      ,                    
                     \;'   /  ,' /  _  \  /  _  \   ,'/                    
                           \   `'  / \  `'  / \  `.' /                     
                            `.___,'   `.__,'   `.__,'  
      ''')

print("Welcome to Treasure Island \nYour mission is to find the treasure ")
print("you have to make a decison to complete this game ")
print("=================================================================")
stepOn1=input("On a street you see two doors : a right door and left door.\nwhich one do you take? left or right?")
if stepOn1 =="left" :
    stepOn2=input("You continue walking forward and see a lake. There is also an old boad nearby. \nwhat do you do? swim or take a boat? ")
    if stepOn2=="take a boat":
        stepOn03=input("You arrive across the lake and there is a fort you enter the fort and find three doors : a red door, a yellow door and a blue door.\n wchich one do you choose, red , yellow or blue?")
        if stepOn03=="yellow" :
            print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[thx yaw]
*******************************************************************************
                  ''')
            print("Congratulations on entering the treasure room")
        elif stepOn03=="red":
            print("Inside there is a dragon and you are burned by its breath\n      GAME OVER")
        elif stepOn03=="blue" :
            print("This is a dark room and suddlenly you are caught in a poison arrow trap\n        GAME OVER")
        else :
            print("SYSTEM ERROR")
    elif stepOn2==("swim"): 
        print("You try to swim and when you are in the middle of the lake you are preyed upon by a carnivorous fish\n       GAME OVER")
    else :
        print("SYSTEM ERROR")
elif stepOn1=="right":
    print("On the road to the right there are several bandits hiding and you were caught\n      GAME OVER")
else :
    print("SYSTEM ERROR")