import random
import os

def clear():  # Clears the terminal
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")

global removedcorridor
global corridors

turn = 0
placementcol = [0, 2, 4, 6]
placementrow = [0, 2, 4, 6]

removedcorridor = [0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6]
random.shuffle(removedcorridor)

corridors = { #[row][column]
0: [1, 3, 5],
1: [0, 2, 4, 6],
2: [1, 3, 5],
3: [0, 2, 4, 6],
4: [1, 3, 5],
5: [0, 2, 4, 6],
6: [1, 3, 5],
}

global admin
admin = 0

for i in range(0,6):
    random.shuffle(corridors[removedcorridor[i]])


#for i in range(0,5):
#    if corridors[removedcorridor[i][0]] == self.poscol-1:
#        legal = 0
#        break
#    else: 
#        legal = 1


randmove = ["left", "right", "down", "up"]
global Board
Board = {
    0: ["0", '-', "?", "-", "?", "-", "?"],
    1: ["|", " ", "|", " ", "|", " ", "|"],
    2: ["?", "-", "?", "-", "?", "-", "?"],
    3: ["|", " ", "|", " ", "|", " ", "|"],
    4: ["?", "-", "?", "-", "?", "-", "?"],
    5: ["|", " ", "|", " ", "|", " ", "|"],
    6: ["?", "-", "?", "-", "?", "-", "?"],
}

Map = {
    0: ["0", '-', "?", "-", "?", "-", "?"],
    1: ["|", " ", "|", " ", "|", " ", "|"],
    2: ["?", "-", "?", "-", "?", "-", "?"],
    3: ["|", " ", "|", " ", "|", " ", "|"],
    4: ["?", "-", "?", "-", "?", "-", "?"],
    5: ["|", " ", "|", " ", "|", " ", "|"],
    6: ["?", "-", "?", "-", "?", "-", "?"],
}



rules = {
    -1: [],
    0: ["Welcome to the ()! Your goal is to escape by finding a key and bringing it to the exitroom. You must be careful of the entity. It copies your movement in the opposite direction.", "no"],
    1: ["Your goal is to escape this maze by finding a key and bringing it into the exit room.", "no"], # How to play game / 
    2: ["snakeroom", "scrollroom", "keyroom", "exitroom", "emptyroom"], # What each room does
    3: ["key", ""], # What each item does
    4: [""], # What each enemy does
    5: ["0 is a empty room, 1 is the keyroom, 2 is the exitroom, 3 is a room with a scroll of banishment, 4 is a snakeroom, X is an inaccesible room", "no"], # how
    6: [""], # actions
}

global blocked
global legal
legal = 1
global playerposcol 
global playerposrow 
playerposcol = 0
playerposrow = 0
global player2poscol 
global player2posrow 
player2poscol = 6
player2posrow = 6
random.shuffle(placementcol)
random.shuffle(placementrow)


#excludedroom = random.randrange(0, 16)
#snakeroom = random.randrange(0, 16)
#snakeroom1 = random.randrange(0, 16)
#exitroom = random.randrange(0, 16)
#scrollroom = random.randrange(0, 16)
#scrollroom1 = random.randrange(0, 16)
#keyroom = random.randrange(0, 16)

#while exitroom == keyroom:
#    keyroom = random.randrange(0, 16)
#while exitroom == excludedroom or excludedroom == keyroom:
#    excludedroom = random.randrange(0, 16)

#rooms = [
#    snakeroom, snakeroom1, scrollroom, scrollroom1, excludedroom, keyroom, exitroom, 0, 0, 0, 0, 0, 0, 0, 0, 0 
#]

class room():
    def __init__(self, id, poscol, posrow, new, type): #pos = position, new = bool; has the room has been entered before, 
        self.id = id
        self.new = new
        self.poscol = poscol
        self.posrow = posrow
        self.searched = False
        match id:
            case 0:                                     ##################   FIX ROWS OF SPECIAL AND BASIC ROOMS (Partially done (Not truely random))
                self.type = "X" #Excludedroom
            case 2|1:
                self.type = 3 #Scrollroom
            case 4|3:
                self.type = 4 #Snakeroom
            case 5:
                self.type = 1 #Keyroom
            case 6:
                self.type = 2 #Exitroom
            case 7:
                self.type = 5 #quiz
            case 8|9|10|11|12|13|14|15:
                self.type = 0


    def newcheck(self, poscol, posrow):
        if self.poscol == poscol and self.posrow == posrow:
            if self.id == 0:
                print("no")
            else:
                if self.new == True:
                    print("You have moved to a new room")
                    self.new = False
                else:
                    print("You have arrived in a familiar room")


    def searchcheck(self, poscol, posrow):
        if self.poscol == poscol and self.posrow == posrow:
            self.searched = True
            match id:
                case 0|1:
                    scare = random.choice(randmove)
                    print("You stumble across a snake and escape to an adjacent room")
                    P1.move(scare)
                case 2|3:
                    print("This room has a scroll resting on a pedestal")
                    pickup = input("Would you like to replace your current item with this item?")
                    match pickup:
                            case "Y"|"y"|"yes"|"Yes"|"YES":
                                P1.itempickup("scroll")
                            case "N"|"n"|"no"|"No"|"NO":
                                print("You leave the scroll on its pedastal")
                case 5:
                    print("This room has a key!")
                    pickup = input("Would you like to replace your current item with this item?")
                    match pickup:
                            case "Y"|"y"|"yes"|"Yes"|"YES":
                                P1.itempickup("key")
                            case "N"|"n"|"no"|"No"|"NO":
                                print("You leave the key in the room")
                case 6:
                    print["This room has a locked door in the corner."]
                case 7|8|9|10|11|12|13|14|15:
                    print("This room is empty. How unremarkable.")

    def useitem(self, poscol, posrow, item):
        if self.poscol == poscol and self.posrow == posrow:
            match id:
                case 4|3:
                    if item == "scroll":
                        print("You banish the snake leaving the room empty.")
                        P1.itempickup("Nothing")
                case 2|1:
                    print("Your item has no use here")
                case 5:
                    print("Your item has no use here")
                case 6:
                    if item == "Key":
                        print("This room has a locked door in the corner")
                        escape = input("Would you like to use the key and escape?")
                        match escape:
                            case "Y"|"y"|"yes"|"Yes"|"YES":
                                P1.win
                    else: 
                        print("Your item has no use here")
                case 7|8|9|10|11|12|13|14|15:
                    print("This room is empty. How unremarkable.")

    def mapupdate(self, poscol, posrow):
        if admin ==0: 
            match poscol: 
                case 0|2|4|6:
                    match posrow: 
                        case 0|2|4|6:
                            if self.poscol == poscol and self.posrow == posrow:
                                if self.searched == True:
                                    Board[posrow][poscol] = self.type 
                                else:
                                    Board[posrow][poscol] = "0"
                        case 1|3|5:
                            Board[posrow][poscol] = " "
                case 1|3|5:
                    match posrow: 
                        case 0|2|4|6:
                            Board[posrow][poscol] = " "
                        case 1|3|5: 
                            Board[posrow][poscol] = " "

    def Boardupdate(self):
        Map[self.posrow][self.poscol] = self.type
        for i in range(0,6):
            Map[removedcorridor[i]][corridors[removedcorridor[i]][0]] = " "




class player:
    def __init__(self, poscol, posrow):
        self.poscol = poscol
        self.posrow = posrow
        self.item = "Nothing"

    def win():
        print("ggbrouwinnicejobiguess")

    def itempickup(self, item):
        self.item = item

    def move(self, poscol, posrow, move):
        self.poscol = poscol
        self.posrow = posrow
        global blocked
        global playerposcol
        global playerposrow
        global player2poscol
        global player2posrow
        global legal
        global removedcorridor
        global corridors
        legal = 1
        while legal == 1:
            blocked = "no"
            if self == P1:
                match move:
                    case "left":
                        if placementcol[0] == poscol-2 and placementrow[0] == posrow:
                            legal = 0
                            break
                        for i in range(0,5):
                            if removedcorridor[i] == posrow:
                                if corridors[removedcorridor[i]][0] == self.poscol-1:
                                    blocked = "yes"
                        if blocked == "yes":
                            legal = 0
                            for i in range(0,16):
                                rooom[i].mapupdate(poscol-1, posrow)
                            break
                        else: 
                            legal = 1
                        if self.poscol-2 < 0:
                            legal = 0
                            break
                        else:
                            self.poscol -=2
                            legal = 1
                            playerposcol = self.poscol
                            playerposrow = self.posrow
                            break
                    case "right":
                        if placementcol[0] == poscol+2 and placementrow[0] == posrow:
                            legal = 0
                            break
                        for i in range(0,5):
                            if removedcorridor[i] == posrow:
                                if corridors[removedcorridor[i]][0] == self.poscol+1:
                                    blocked = "yes"
                        if blocked == "yes":
                                legal = 0
                                rooom[i].mapupdate(poscol+1, posrow)
                                break
                        else:
                            legal = 1
                        if self.poscol+2 > 7:
                            legal = 0
                            break
                        else:
                            self.poscol +=2
                            legal = 1
                            playerposcol = self.poscol
                            playerposrow = self.posrow
                            break
                    case "down":
                        if placementcol[0] == poscol and placementrow[0] == posrow+2:
                            legal = 0
                            break
                        for i in range(0,5):
                            if removedcorridor[i] == self.posrow+1:
                                if corridors[removedcorridor[i]][0] == self.poscol:
                                    blocked = "yes"
                        if blocked == "yes":
                            legal = 0
                            rooom[i].mapupdate(poscol, posrow+1)
                            break
                        else: 
                            legal = 1
                        if self.posrow+2 > 7:
                            legal = 0
                            break
                        else:
                            self.posrow +=2
                            legal = 1
                            playerposcol = self.poscol
                            playerposrow = self.posrow
                            break
                    case "up":
                        if placementcol[0] == poscol and placementrow[0] == posrow-2:
                            legal = 0
                            break
                        for i in range(0,5):
                            if removedcorridor[i] == self.posrow-1:
                                if corridors[removedcorridor[i]][0] == self.poscol:
                                    blocked = "yes"
                        if blocked == "yes":
                            legal = 0
                            rooom[i].mapupdate(poscol, posrow-1)
                            break
                        else: 
                            legal = 1
                        if self.posrow-2 < 0:
                            legal = 0
                            break
                        else:
                            self.posrow -=2
                            legal=1
                            playerposcol = self.poscol
                            playerposrow = self.posrow
                            break
            else: 
                x = 0
                while move != "no":
                    match move:
                        case "left":
                            for i in range(0,5):
                                if removedcorridor[i] == self.posrow:
                                    if corridors[[removedcorridor[i]][0]] == self.poscol-1:
                                        blocked = "yes"
                            if blocked == "yes":
                                move = random.choice(randmove)
                            else:
                                if self.poscol +2 > 7:
                                    move = random.choice(randmove)
                                else:
                                    self.poscol +=2
                                    break
                        case "right":
                            for i in range(0,5):
                                if removedcorridor[i] == self.posrow:
                                    if corridors[[removedcorridor[i]][0]] == self.poscol-1:
                                        blocked = "yes"
                            if blocked == "yes":
                                move = random.choice(randmove)
                            else:
                                if self.poscol -2 < 0:
                                    move = random.choice(randmove)
                                else:
                                    self.poscol -=2
                                    break
                        case "down":
                            for i in range(0,5):
                                if removedcorridor[i] == self.posrow-1:
                                    if corridors[[removedcorridor[i]][0]] == self.poscol:
                                        blocked = "yes"
                            if blocked == "yes":
                                move = random.choice(randmove)
                            else:
                                if self.posrow +2 > 7:
                                    move = random.choice(randmove)
                                else: 
                                    self.posrow +=2
                                    break
                        case "up":
                            for i in range(0,5):
                                    if removedcorridor[i] == self.posrow-1:
                                        if corridors[[removedcorridor[i]][0]] == self.poscol:
                                            blocked = "yes"
                            if blocked == "yes":
                                move = random.choice(randmove)
                            else:
                                if self.posrow -2 < 0:
                                    move = random.choice(randmove)
                                else:
                                    self.posrow -=2
                                    break
                        case _:
                            move = random.choice(randmove)
                    x += 1
                    if x > 20:
                        break
                player2poscol = self.poscol
                player2posrow = self.posrow
                break




    def search(self, poscol, posrow):
        if self.item == 0:
            for i in range(0,16):
                rooom[i].searchcheck(poscol, posrow)
        else: 
            for i in range(0,16):
                rooom[i].useitem(poscol, posrow, self.item)



    def map(self, poscol, posrow):
        if admin == 0:
            for i in range(0,16):
                rooom[i].mapupdate(poscol, posrow)
            print("You check your map")
            for x in range(0,7): 
                for i in range(0,7):
                    print(Board[x][i], end="")
                print("")
        else:
            for x in range(0,7): 
                for i in range(0,7):
                    print(Map[x][i], end="")
                print("")
    
    def deathcheck(self, poscol, posrow):
        if self == P1:
            P2.deathcheck(poscol, posrow)
        else:
            if self.poscol == poscol and self.posrow == posrow:
                print("You have died")


rooom = [
    "a", "b", "c", "d", "e", "f","g","h","i","j","k","l","m","n","o","p"
]
#rom = room("rom", 0, placement[0], True)
z = 0
for x in range (0, 4):
    for i in range(0, 4):
        rooom[z] = room(z, placementcol[i], placementrow[i-x], True, "no") 
        z += 1

for i in range(0,16):
    rooom[i].Boardupdate()



P1 = player(0, 0)
P2 = player(6, 6)
P1.itempickup("Nothing")
turn = 0
while turn < 40:
    blocked = "no"
    action = input("What would you like to do: ")
    match action:
        case "move":
            mve = 1
            while mve == 1:
                move = input("Would you like to move up, down, right or left. If you would like to cancel, please type cancel: ")
                if move == "left" or move == "right" or move == "up" or move == "down":
                    #for i in range(0,16):
                    #    rooom[i].movecheck(playerposcol, playerposrow, move)
                    P1.move(playerposcol, playerposrow, move)
                    mve = 0
                    if legal == 1:
                        turn+=1
                        P2.move(player2poscol, player2posrow, move)
                        for i in range(0,16):
                            rooom[i].newcheck(playerposcol, playerposrow)
                    else:
                        mve = 1
                elif move == "cancel": 
                    mve = 0
                if mve == 1:
                    print("That is not a direction you may move in. Please choose another direction.")
                move = 0
                input("When you are ready to continue press enter.")
        case "search"|"use":
            P1.search(playerposcol, playerposrow)
            turn+=1
            P2.move(player2poscol, player2poscol, random.choice(randmove))
            input("When you are ready to continue press enter.")
        case "map":
#            P2.deathcheck()
            P1.map(playerposcol, playerposrow)
            P2.move(player2poscol, player2poscol, random.choice(randmove))
            turn+=1
            input("When you are ready to continue press enter.")
        case "rules":
            rule = 1
            print("What rules are you confused about?")
            print("Please enter the number that corresponds to your query: 1; What is the goal of the game. 2; How to read the map. 3; What actions you can take. 4; What each enemy and item does. ")
            rule = int(input("Enter number here: "))
            while rule != "0":
                print(rules[rule][0])
                print("If you are confused about any other rules please enter the number. If you are done enter '0'.")
                rule = input("Input number here: ")
        case "admin":
            print("Welcome Admin.")
            admin = 1
    clear()
    print(player2poscol)
    print(player2posrow)
