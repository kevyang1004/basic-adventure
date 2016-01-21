from sys import exit


# This moves us to that place
def in_front_of_the_parking_lot():
    print "Oh, many zombies are running toward me..."
    print "But, I can kill all the zombies with this rifle!!"
    print "Bang, bang, bang!!!!!!!"
    print "Eww, blood"
    print "There is a radio."
    print "Are you going to get a radio or not?"

# It let us choose from the choices
    choice = raw_input("> ")

# If this choice was typed, those things will happen
    if choice == "yes":
        print "........Is..there.....anyone..who...survived?"
        print "..There....is...a refuge...in..Time Square"
        print "Oh!!! there was another surviver!"
        print "I gotta go to the Time Square!"
        print "And I gotta take that car and drive through"
        in_the_car()

# Other things beside if choice. That will happen
    else:
        dead("WAAAAA... you just killed by the zombi....")


# explain what happen in that place
def road():
    print "You're driving the car..."
    print "There are many zombies out there"
    print "I need a rifle!! I should go back and get rifle!"
    start()


# explaing what happen in that place
def in_the_car():
    print "Ohhhh!!!! there is the U.S. army! I'm saved!!!!"
    print "Soldier: Hello sir, how old are you?"
    print "Um..I'm 22 years old. Why are you asking?"
    print "Soldier: Then, you have to be in the army. Come on!!!"
    army_camp()


# explain what happen in that place
def army_camp():
    print "General: Welcome to the army camp!"
    print "General: We are going to kill all the zombies!"
    print "Yeahhhhhh~!!!"
    print "General: What do you want to be between attacker or driver?"

# give us the choices to choose
    choice = raw_input("> ")

# choice 1. The thing under the choice, will happen
    if choice == "attacker":
        print "General: We will be facing the zombies and kill them!!"
        in_the_truck()

# choice 2. The thing under the choice, will happen
    elif choice == "driver":
        print "General: You are going to drive through the place where zombies live"
        driver_seat()

# Other any answers beside those two choices, will happen
    else:
        dead("You're so weak!!! get out of the army!!!!")


# explain what happen in that place
def in_the_truck():
    print "I'm so afraid..."
    print "~crashhhh~"
    print "Soldier: Zombies just attacked the truck!! Get out your rifle and shoot them!!"
    print "Will you go and fight with zombies or hide?"

# choices to choose to go through the game
    choice = raw_input("> ")

# choice 1.
    if choice == "fight":
        print "Bang, bang, bang!"
        print "There is the Time Square! let's go there.."
        Time_Square()

# choice 2.
    elif choice == "hide":
        print "I'm so afraid of them.. this is the bomb! let's use it!"
        print "--------Booooooooom--------"
        print "General: Wow...what's your name!"
        print "I'm Steve, sir!"
        print "General: Ok.. I will remember your name. Let's go back to the camp!"
        General_room()

# Other any answers beside those two choices
    else:
        dead("Zombi just took yout head out")


# explain what happen in that place
def Time_Square():
    print "Finally... I got to the Time Square!"
    print "But I can't find the survivers..."
    print "Suddenly zombi came out and take your head off!!"
    dead("It was your destiny from the beginning")


# explain what happen in that place
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


# beginning of the game
def start():
    print "You're at the parking lot"
    print "You can hear the screaming sound of zombies"
    print "There is a rifle and car"
    print "which one would you take?"

# choice to choose
    choice = raw_input("> ")

# explain what happen if we choose that answer
    if choice == "rifle":
        print "I'm gonna kill all the zombies hahaha"
        in_front_of_the_parking_lot()

# explain what happen if we choose that answer
    elif choice == "car":
        print "Ok, let's get out of here!"
        road()

# Other any answers will be dead.
    else:
        dead("I'm starving...")


# make the game beginning
start()
