def start():
    print ("Hello, ", str(name))
    print ("You are in the foyer.")
    print ("There are doorways front, back, left and right.")
    direction = input ("Enter a choice? ")
    
    if  direction == "front":
        front()
            
    elif  direction == "right":
        right()
        
    elif  direction == "back":
        print  ("The front door is locked!")
        start()
        
    elif  direction == "left":
        left()
        
    else:
        print  ("I don't understand the" , direction, "direction.")
        start()

def front():
    print  ("You are in what looks like a dining room, maybe it's connected to a kitchen?")
    print  ("You look around but the room looks plain, but the plates and utensils are all ready at the table.")
    print  ("You hear a noise in the room over, past the door.")
    check = input("Do you open the door and see what the noise is, or go back to the foyer? check/foyer: ")
    if check == "check":
        print("You creak open the door and a mass of black filling the room turns towards you, and instantly jumps at you, killing you.")
        print("Game over.")
    if check == "foyer":
        start()

def table():
    print("The table has some papers, but nothing important looking, like a key. There is a little mat for cups though, you look under it and find the key!")
    print("You go to open the door, swing it open, and find the green grass behind the house")
    print("Running to the fence, you stumble but catch yourself.")
    print("You jump the fence, and find yourself on a street you recognize, safely.")
    print("You win. Game over")
    quit()
    
def lookforkey():
    lookwhere = input("Look in drawers, on table, or in the cabinets, or go back to the foyer? drawer/table/cabinet/foyer: ")
    if lookwhere == "drawer":
        print("The drawers are empty, apart from a thick layer of dust and a few dead flies.")
        lookforkey()
    if lookwhere == "cabinet":
        swigwhiskey = input("Nothing in the cabinet except some whiskey that is probably very well aged now. Take a swig? y/n: ")
        if swigwhiskey == "y":
            print("The cork won't open, nice try though.")
            lookforkey()
        if swigwhiskey == "n":
            lookforkey()
        else: print("I don't understand ", swigwhiskey)
    if lookwhere == "table":
            table()
    if lookwhere == "foyer":
            start()
    else: print ("I don't understand ", lookwhere)

def left():
    print("You are in the bedroom")
    print("This room is bare except for a bed, and everything is white, except for some red splotches across the carpet and a brown human-shaped stain on the bed.")
    goback = input("Look at the room some more, or go back to the foyer? look/back: ")
    if goback == "back":
        start()
    if goback == "look":
        print("There is some spider webs in the corner of the room above the bed, and mosquitoes across the red splotch. Could it be fresh blood? You're spooked by the room and go back to the foyer")
        start()
    else: print("I don't understand", goback)
    left()
        
def right():
    print("You are in the lounge room.")
    loungeroom = input ("Go back to the foyer, or go to the door in front of you? door/foyer: ")
    if loungeroom == "door":
        loungeroomdoorchoice = input("The door is locked. Look for a key? y/n: ")
        if loungeroomdoorchoice == "n":
            right()
        if loungeroomdoorchoice == "y":
            lookforkey()
        else: print("I don't understand ", loungeroomdoorchoice)
        right()
    if loungeroom == "foyer":
        start()
    else: print(" I don't recognize ", loungeroom )
    right()
name = input ("What is your name? ")

start()
