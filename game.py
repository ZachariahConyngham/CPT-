import random
import os

def clear():  # Clears the terminal
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")

turn = 0
placementcol = [0, 1, 2, 3]
placementrow = [0, 1, 2, 3]
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




global legal
legal = 1
global playerposcol 
global playerposrow 
playerposcol = 0
playerposrow = 0
random.shuffle(placementcol)
random.shuffle(placementrow)

P1map = [

]


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
        match poscol:
            case 0:
                self.poscol = poscol
            case 1:
                self.poscol = poscol+1
            case 2: 
                self.poscol = poscol+2
            case 3:
                self.poscol = poscol+3
        match posrow:
            case 0:
                self.posrow = posrow
            case 1:
                self.posrow = posrow+1
            case 2: 
                self.posrow = posrow+2
            case 3:
                self.posrow = posrow+3
        match id:
            case 0|1:
                self.type = 4 #Snakeroom
            case 2|3:
                self.type = 3 #Scrollroom
            case 4:
                self.type = -1 #Excludedroom
            case 5:
                self.type = 1 #Keyroom
            case 6:
                self.type = 2 #Exitroom
            case 7:
                self.type = 5 #quiz
            case 8|9|10|11|12|13|14|15:
                self.type = 0


#        for i in range(0, 16):
#            #print("wes")
#            #print(i)
#            #print(rooms[i])
#            if id == rooms[i]:
#                self.type = rooms[i]
#                print(rooms[i])
#            else: 
#                self.pos = pos

    def movecheck(self, poscol, posrow):
        if self.id == 4:
            print("no")
        if self.new == True:
            print("You have moved to a new room")
            self.new = False
        else:
            print("You have arrived in a familiar room")

    def searchcheck(self, poscol, posrow):
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

            case 6:
                print["This room has a locked door in the corner."]
            case 7|8|9|10|11|12|13|14|15:
                print("This room is empty. How unremarkable.")

    def useitem(self, poscol, posrow, item):
        match id:
            case 0|1:
                if item == "scroll":
                    print("You banish the snake leaving the room empty.")
                    P1.itempickup("Nothing")
            case 2|3:
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
        print(self.type)
        print(self.id)
        Board[posrow][poscol] = self.type 






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
        global playerposcol
        global playerposrow
        global legal
        if self == P1:
            match move:
                case "left":
                    if self.poscol-2 < 0:
                        legal=0
                    else:
                        self.poscol -=2
                        legal = 1
                case "right":
                    if self.poscol+2 > 7:
                        legal=0
                    else:
                        self.poscol +=2
                        legal = 1
                case "down":
                    if self.posrow+2 > 7:
                        legal=0
                    else:
                        self.posrow +=2
                        legal = 1
                case "up":
                    if self.posrow-2 < 0:
                        legal=0
                    else:
                        self.posrow -=2
                        legal=1
            playerposcol = self.poscol
            playerposrow = self.posrow
        else: 
            match move:
                case "left":
                    self.poscol +=2
                case "right":
                    self.poscol -=2
                case "down":
                    self.posrow +=2
                case "up":
                    self.posrow -=2


    def search(self, poscol, posrow, item):
        if item == 0:
            rom.searchcheck(playerposcol, playerposrow)
        else: 
            rom.useitem(playerposcol, playerposrow, self.item)

    def map(self, poscol, posrow):
        rom.mapupdate(poscol, posrow)
        print("You check your map")
        for x in range(0,7): 
            for i in range(0,7):
                print(Board[x][i], end="")
            print("")
    
    def deathcheck(self, poscol, posrow):
        if self.poscol == poscol and self.posrow == posrow:
            print("die")


rooom = [
    "a", "b",   "c", "d", "e", "f","g","h","i","j","k","l","m","n","o","p"
]
#rom = room("rom", 0, placement[0], True)
z = 0
for x in range (0, 4):
    for i in range(0, 4):
        rom = room(z, placementcol[i], placementrow[x], True, "no") 
        z += 1



P1 = player(0, 0)
P2 = player(6, 6)
P1.itempickup("Nothing")
turn = 0
while turn < 40:
    action = input("What would you like to do: ")
    match action:
        case "move":
            mve = 1
            while mve == 1:
                move = input("Would you like to move up, down, right or left. If you would like to cancel, please type cancel: ")
                
                if move == "left" or move == "right" or move == "up" or move == "down":
                    P1.move(playerposcol, playerposrow, move)
                    mve = 0
                    if legal == 1:
                        turn+=1
                        rom.movecheck(playerposcol, playerposrow)
                    else:
                        mve = 1
                elif move == "cancel": 
                    mve = 0
                if mve == 1:
                    print("That is not a direction you may move in. Please choose another direction.")
        case "search"|"use":
            P1.search(playerposcol, playerposrow, )
            turn+=1
        case "map":
#            P2.deathcheck()
            P1.map(playerposcol, playerposrow)
            turn+=1
