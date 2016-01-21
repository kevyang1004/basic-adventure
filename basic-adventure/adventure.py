from sys import exit


# This moves us to that place
def in_front_of_the_parking_lot():
    print "Oh, many zombies are running toward me..."
    print "But, I can kill all the zombies with this rifle!!"
    print "Bang, bang, bang!!!!!!!"
    print "Eww, blood"
    print "There is a radio."
    print "Are you going to get a radio or not?"

    choice = raw_input("> ")

    if choice == "yes":
        print "........Is..there.....anyone..who...survived?"
        print "..There....is...a refuge...in..Time Square"
        print "Oh!!! there was another surviver!"
        print "I gotta go to the Time Square!"
        print "And I gotta take that car and drive through"
        in_the_car()

    else:
        dead("WAAAAA... you just killed by the zombi....")


# This let us know that we are in the road
def road():
    print "You're driving the car..."
    print "There are many zombies out there"
    print "I need a rifle!! I should go back and get rifle!"
    start()


# This let us know that we are in the car
def in_the_car():
    print "Ohhhh!!!! there is the U.S. army! I'm saved!!!!"
    print "Soldier: Hello sir, how old are you?"
    print "Um..I'm 22 years old. Why are you asking?"
    print "Soldier: Then, you have to be in the army. Come on!!!"
    army_camp()


# This let us know that this we are in the army camp
def army_camp():
    print "General: Welcome to the army camp!"
    print "General: We are going to kill all the zombies!"
    print "Yeahhhhhh~!!!"
    print "General: What do you want to be between attacker or driver?"

    choice = raw_input("> ")

    if choice == "attacker":
        print "General: We will be facing the zombies and kill them!!"
        in_the_truck()

    elif choice == "driver":
        print "General: You are going to drive through the place where zombies live"
        driver_seat()

    else:
        dead("You're so weak!!! get out of the army!!!!")


# This let us know that we are in the truck
def in_the_truck():
    print "I'm so afraid..."
    print "~crashhhh~"
    print "Soldier: Zombies just attacked the truck!! Get out your rifle and shoot them!!"
    print "Will you go and fight with zombies or hide?"

    choice = raw_input("> ")

    if choice == "fight":
        print "Bang, bang, bang!"
        print "There is the Time Square! let's go there.."
        Time_Square()

    elif choice == "hide":
        print "I'm so afraid of them.. this is the bomb! let's use it!"
        print "--------Booooooooom--------"
        print "General: Wow...what's your name!"
        print "I'm Steve, sir!"
        print "General: Ok.. I will remember your name. Let's go back to the camp!"
        General_room()

    else:
        dead("Zombi just took yout head out")


# This let us know that we are in the Time Square
def Time_Square():
    print "Finally... I got to the Time Square!"
    print "But I can't find the survivers..."
    print "Suddenly zombi came out and take your head off!!"
    dead("It was your destiny from the beginning")


def General_room():
    print "I saw your good work... I think you could be the general after me..."
    print "You just became the general!!!"
    print "It's your world from now on.."
    print "Control your army well"
    print "We are believing you!! See Ya~"
    print "--------End----------"
    exit(0)


# This makes the game exit when the game is over
def dead(why):
    print why, "Game Over"
    exit(0)


# This let us know that this is the beginning
def start():
    print "You're at the parking lot"
    print "You can hear the screaming sound of zombies"
    print "There is a rifle and car"
    print "which one would you take?"

# This makes the choice that we can choose
    choice = raw_input("> ")

# This let us know what happen if we choose rifle
    if choice == "rifle":
        print "I'm gonna kill all the zombies hahaha"
        in_front_of_the_parking_lot()

# This let us know what happen if we choose car
    elif choice == "car":
        print "Ok, let's get out of here!"
        road()

# This let us know what happen if we choose another one
    else:
        dead("I'm starving...")


start()
