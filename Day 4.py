import random
moves=["Rock","Paper","Scissor"]
choice=input("Choose your move: Rock, Paper, Scissor: ")
print("User's choice: ", choice)
if choice=="Rock" or choice=="rock" or choice=="1":
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif choice=="Paper" or choice=="paper" or choice=="2":
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)

elif choice=="Scissor" or choice=="scissor" or choice=="3":
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)
computer_choice=random.choice(moves)
print("Computer's choice: ", computer_choice)
if computer_choice=="Rock":
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif computer_choice=="Paper":
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)

elif computer_choice=="Scissor":
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

print("Result:")
if (choice=="Rock" or choice=="rock" or choice=="1") and computer_choice=="Rock":
    print("draw!")
elif (choice=="Paper" or choice=="paper" or choice=="2") and computer_choice=="Paper":
    print("draw!")
elif (choice=="Scissor" or choice=="scissor" or choice=="3") and computer_choice=="Scissor":
    print("draw!")

elif (choice=="scissor" or choice=="scissor" or choice=="3") and computer_choice=="Rock":
    print("Computer won!")
elif (choice=="Rock" or choice=="rock" or choice=="1") and computer_choice=="Paper":
    print("Computer won!")
elif (choice=="paper" or choice=="paper" or choice=="2") and computer_choice=="Scissor":
    print("Computer won!")

elif (choice=="Paper" or choice=="paper" or choice=="2") and computer_choice=="Rock":
    print("You won!")
elif (choice=="Scissor" or choice == "scissor" or choice == "3") and computer_choice == "Paper":
    print("You won!")
elif (choice=="Rock" or choice == "rock" or choice == "1") and computer_choice == "Scissor":
    print("You won!")

else:
    print("wrong input")