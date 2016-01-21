from sys import exit


#this let us know that this is the beginning
def start():
    print "You can hear the screaming sound of zombies"
    print "You're at the parking lot
    print "There is a rifle and car"
    print "which one would you take?"

#This makes the choice that we can choose
    choice = raw_input("> ")

#This let us know what happen if we choose rifle
    if choice == "rifle":
        print "I'm gonna kill all the zombies hahaha"
        in_front_of_the_parking_lot()

#This let us know what happen if we choose car
    elif choice == "car":
        print "Ok, let's get out of here!"
        road()

#This let us know what happen if we choose another one
    else:
        dead("I'm starving...")


start()

#This moves us to that place
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


def road():
    print "You're driving the car..."
    print "There are many zombies out there"
    print "I need a rifle!! I should go back to "
    start()


def in_the_car():
    print "Ohhhh!!!! there is the U.S. army! I'm saved!!!!"
    print "Soldier: Hello sir, how old are you?"
    print "Um..I'm 22 years old. Why are you asking?"
    print "Soldier: Then, you have to be in the army. Come on!!!"
