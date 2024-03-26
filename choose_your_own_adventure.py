name = input("Type your name: ")
print("Welcome, " + name + " to this adventure.!")

def handle_invalid_input():
    choice = input("Invalid option. Press 'R' to repeat or 'E' to exit: ").lower()
    if choice == "r":
        return True
    elif choice == "e":
        print("Thank you for playing the game.", name)
        exit()
    else:
        return handle_invalid_input()    

answer = input("You are in a dirt road, it has come to an end and you can go left or right. Which way do you want to go? ")

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around or swim to swim across: ") 

    if answer == "swim":
        print("You swim acrross and were eaten by an alligator you lost the game.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.") 
    else:
        print("Not a valid option. You lose.")
        if not handle_invalid_input():
            exit()    

elif answer == "right":
   answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back)")   

   if answer == "back":
        print("You go back and lose the game")
   elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you want to talk to him? (yes/no)?")
        if answer == "yes":
            print("You talk with the stranger and they give you gold. You win!")
        elif answer == "no":
            print("You ignore the stranger and they are offended You lose.")
        else:
            print("Not a valid option. You lose.") 
            if not handle_invalid_input():
                exit()   
   else:
        print("Not a valid option. You lose.")
        if not handle_invalid_input():
            exit()


else:
    print("Not a valid option. You lose.")
    if not handle_invalid_input():
        exit()

print("Thank you for playing the game.", name)    



