print('''          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure")
choice_1 = input("You are at a crossroad.Where would you go (Left or Right)? \n ").lower()
if choice_1 == "Left":
    print("You Died \n Never turn left at crossroad.")
else:
    input("You have come across a lake.You need to cross the lake.\nWhat would you do(Swim or Wait of the coming boat)?\n").lower()
    if choice_1 == "Swim":
        print("You Died \n Killed by lake monster.")
    else:
        input("You got on the other side safely.There are three doors in front of you.\nWhich Door will you pick(Red,Green,Blue)?\n").lower()
        if choice_1 == "Red":
            print("You Died \nYou were burned to death.")
        elif choice_1 == "Green":
            print("You Died \nYou were poisoned to death.")
        else:
            print("You found the treasure!")