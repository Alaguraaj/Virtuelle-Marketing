import time
import random


def print_pause(message, time_length):
    print(message)
    time.sleep(.1*time_length)


def intro(option):
    print_pause("You find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.", 2)
    print_pause("Rumor has it that a "+ option + " is somewhere around here, and has been "
                "terrifying the nearby village.", 2)
    print_pause("In front of you is a house.",2)
    print_pause("To your right is a dark cave.",2)
    print_pause("In your hand you hold your trusty (but not very effective) dagger. \n",2)


def fight(items,option):
    if "sword" in items:
        print_pause("As the "+ option +" moves to attack, you unsheath your new sword.", 2)
        print_pause("The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.",2)
        print_pause("But the "+ option +" takes one look at your shiny new toy and runs away!",2)
        print_pause("You have rid the town of the "+ option +". You are victorious!",2)
    else:
        print_pause("You do your best...", 2)
        print_pause("but your dagger is no match for the "+ option +".", 2)
        print_pause("You have been defeated!", 2)
    return

def cave(items,option):
    if "sword" in items:
        print_pause("You peer cautiously into the cave.",2)
        print_pause("You've been here before, and gotten all"
                    " the good stuff. It's just an empty cave"
                    " now.",2)
        print_pause("You walk back to the field.\n",2)
    else:
        print_pause("You peer cautiously into the cave.", 2)
        print_pause("It turns out to be only a very small cave",2)
        print_pause("Your eye catches a glint of metal behind a rock.",2)
        print_pause("You have found the magical Sword of Ogoroth!",2)
        items.append("sword")
    #print_pause(items,2)
        print_pause("You discard your silly old dagger and take the sword with you.",2)
        print_pause("You walk back out to the field.",2)
    field(items,option)

def house(items,option):
    print_pause("You approach the door of the house.", 2)
    print_pause("You are about to knock when the door opens and out steps a " +option+".", 2)
    print_pause("Eep! This is the "+option+"'s house!", 2)
    print_pause("The "+option+" attacks you!", 2)
    #print(items)
    if items != ['sword']:
        print_pause("You feel a bit under-prepared for this, what with only having a tiny dagger.", 2)
    player_choice = input("Would you like to (1) fight or (2) run away? \n")
    if player_choice == '1':
        fight(items,option)
    elif player_choice == "2":
        print_pause("You run back into the field. Luckily, you don't seem to have been followed.", 2)
        field(items,option)
    else:
        print_pause("Unfortunately you enter the house again by choosing wrong number", 2)
        house(items,option)

def field(items,option):
    print_pause("Enter 1 to knock on the door of the house. \nEnter 2 to peer into the cave. ", 2)
    print_pause("What would you like to do? ", 2)
    player = input("(Please enter 1 or 2).\n")
    if player == '1':
        house(items,option)
    elif player =='2':
        cave(items,option)
    else:
        print_pause("Sorry. It is not available. Please enter 1 or 2",2)
        field(items,option)

def play_again():
    play_again_y_n=input("Would you like to play again? (y/n) \n").lower()
    if play_again_y_n == 'y':
        print_pause("Excellent! Restarting the game ...",3)
        play_game()
    elif play_again_y_n == "n":
        print_pause("Thanks for playing! See you next time",3)
    else:
        play_again()



def play_game():
    items=[]
    option = random.choice(["wicked fairie", "pirate", "dragon", "troll",
                            "gorgon"])
    intro(option)
    field(items,option)
    play_again()

play_game()
