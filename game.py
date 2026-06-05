import random
import os

def clear():  # Clears the terminal
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")
global blocked
global legal
global playerposcol 
global playerposrow 
global player2poscol 
global player2posrow 
global removedcorridor
global corridors
global move
global turn
global win
global admin
global Board

corridors = { #[row][column]
0: [1, 3, 5],
1: [0, 2, 4, 6],
2: [1, 3, 5],
3: [0, 2, 4, 6],
4: [1, 3, 5],
5: [0, 2, 4, 6],
6: [1, 3, 5],
}
rules = {
    -1: [],
    0: ["Welcome to the ()! Your goal is to prevent the entity from escaping.", "The entity copies your movement in the opposite direction, so be careful.", "The only ways to successfully stop the entity are to either escape and lock the entity inside the cavern forever or banish the entity with a scroll of banishment", "If you have any other queries; Type 'rules' as your action."],# 3 parts
    1: ["Your goal is to escape this maze by finding a key and bringing it into the exit room.", "To do this you must search every room you find until you locate the keyroom and the exit room."], # How to play game / 2 parts
    2: ["A snake room is aroom where a snake hides in. If you search this room then you will be chased into a random adjacent room.", "A scroll room contains a scroll of banishment which will let you banish an enemy.", "A keyroom has a key in it that unlocks the exit", "If you bring a key to this room you win", "This room has nothing of importance for you", "| and - and corridors you can travel through to get from room to room"], # What each room does / 5 parts
    3: ["The key allows you to escape the dungeon when brought to the exit room", "The scroll of banishment allows you to banish an enemy from this world. If that enemy if a snake it will make the room a empty room. If you manage to banish the entity you win"], # What each item does / 2 parts
    4: ["Inside the () resides the entity", "The entity is trying to become a perfect replica of you so it can escape into the world", "After you make 60 actions it will have perfectly copied you and will escape leaving you trapped forever", "If it manages to catch up to you before then it will be able to copy you instantly and will then escape.", "It moves in the opposite direction of your movements when it can but if it can't it will move randomly.", "If you take a passive action like checking your map or searching the room you are in it will move randomly", "If you are in the same room as it and take a passive action it will copy you and you will lose.", "If you are in the same room but choose to move into a different room you won't be punished."], # What the entity does / 7 parts
    5: ["0 is a empty room, 1 is the keyroom, 2 is the exitroom, 3 is a room with a scroll of banishment, 4 is a snakeroom, X is an inaccesible room", "no"], # rooms / 1 part
    6: ["move: You can move through an adjacent corridor to another room", "map: You chcek and update your map with the findings you have gathered so far", "search: You search the room you are in to discover what type of room it is or you use the item you are holding.", "restart: If the game is impossible to win for whatever reason this will reset the map"], # actions / 4 parts
}

def ruless(rule):
    match rule:
        case 0:
            for i in range(0,3):
                print(rules[rule][i])
        case 1:
            for i in range(0,2):
                print(rules[rule][i])
        case 2:
            for i in range(0,6):
                print(rules[rule][i])
        case 3:
            for i in range(0,2):
                print(rules[rule][i])
        case 4:
            for i in range(0,8):
                print(rules[rule][i])
        case 5:
            print(rules[rule][i])
        case 6:
            for i in range(0,4):
                print(rules[rule][i])
        case "restart": 
            print("You need to type restart as an action.")

randmove = ["left", "right", "down", "up"]
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
turn = 0
placementcol = [0, 2, 4, 6]
placementrow = [0, 2, 4, 6]
move = "jim"
removedcorridor = [0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6]
random.shuffle(removedcorridor)
win = 0
admin = 0
legal = 1
playerposcol = 0
playerposrow = 0
newquiz = True
player2poscol = 6
player2posrow = 6
random.shuffle(placementcol)
random.shuffle(placementrow)
rooms = [
    "X", 2, 1, 1, 3, 2, 4, 0, 5, 0, 0, 0, 0, 0, 0, 0 
]
random.shuffle(rooms)
if rooms[0] == "X" or rooms[15] == "X":
    random.shuffle(rooms)
for i in range(0,6):
    random.shuffle(corridors[removedcorridor[i]])

class room():
    def __init__(self, id, poscol, posrow, new, type): #pos = position, new = bool; has the room has been entered before, 
        self.id = id
        self.new = True
        self.poscol = poscol
        self.posrow = posrow
        self.searched = False
        match rooms[id]:
            case "X":                                     ##################   FIX ROWS OF SPECIAL AND BASIC ROOMS (Partially done (Not truely random))
                self.type = "X" #Excludedroom 1
            case 1:
                self.type = 3 #Scrollroom 2
            case 2:
                self.type = 4 #Snakeroom 2
            case 3:
                self.type = 1 #Keyroom 1
            case 4:
                self.type = 2 #Exitroom 1
            case 5:
                self.type = 5 #quiz 1
            case 0:
                self.type = 0

    def newcheck(self, poscol, posrow):
        if self.poscol == poscol and self.posrow == posrow:
            if self.new == True:
                print("You have moved to a new room")
                self.new = False
            else:
                print("You have arrived in a familiar room")
                if self.searched == True:
                    match self.type:
                        case 1: 
                            print("You notice the skeleton in the corner of the room") # key room
                        case 2:
                            print("You notice the locked trapdoor in the ceiling") # exit room
                        case 3: 
                            print("You notice a pedastal in the center of the room") # Scroll room
                        case 4: 
                            print("You hear the faint rustling of a snake") # Snake room
                        case 5: 
                            print("You notice the statue in the center") # Quiz room

    def searchcheck(self, poscol, posrow):
        if self.poscol == poscol and self.posrow == posrow:
            self.searched = True
            match self.type:
                case 4:
                    scare = random.choice(randmove)
                    print("You stumble across a snake and escape to an adjacent room")
                    P1.move(playerposcol, playerposrow, scare)
                case 3:
                    print("This room has a scroll resting on a pedestal")
                    pickup = input("Would you like to replace your current item with this item?")
                    match pickup:
                            case "Y"|"y"|"yes"|"Yes"|"YES":
                                P1.itempickup("scroll")
                            case "N"|"n"|"no"|"No"|"NO":
                                print("You leave the scroll on its pedastal")
                case 1:
                    print("This room has a key!")
                    pickup = input("Would you like to replace your current item with this item?")
                    match pickup:
                            case "Y"|"y"|"yes"|"Yes"|"YES":
                                P1.itempickup("key")
                            case "N"|"n"|"no"|"No"|"NO":
                                print("You leave the key in the room")
                case 2:
                    print["This room has a locked trapdoor in the ceiling."]
                case 5:
                    print("This room has a statue in the center")
                    quiz = input("Do you approach the statue? (Type no if you dont want to)")
                    if quiz != "no": 
                        rooom[7].quiz
                case _:
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
                        if "y" in escape: 
                            P1.win
                        match escape:
                            case "Y"|"y"|"yes"|"Yes"|"YES":
                                P1.win
                    else: 
                        print("Your item has no use here")
                case _:
                    print("This room is empty. Would you like to leave your item here?")
                    placeitem = input("Would you like to use the key and escape?")
                    if "y" in placeitem: 
                        self.item = item

    def mapupdate(self, poscol, posrow):
        if self.searched == True:
            Board[self.posrow][self.poscol] = self.type
        elif self.new == False:
            Board[self.posrow][self.poscol] = "0"
        else:
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

    def quiz(self):
        quizwin = False
        if newquiz == True:
            match self.id:
                case 0|1|2|3:
                    Q1 = input("How may people are in the Yr11 CPT class?")
                    Q2 = input("What is 7^4?")
                    Q3 = input("what is sin(30)?")
                    if Q1 == "9" and Q2 == "2401" and Q3 == "0.5":
                        quizwin = True
                        newquiz = False
                    else:
                        print("The light in the statue's eyes dims")
                        print("You must have failed its test")
                        newquiz = False
                case 4|5|6|7:
                    Q1 = input("What is the best theme in Visual Studio Code?")
                    Q2 = input("The sequel to 'Hollow Knight' is 'Hollow Knight:...'")
                    Q3 = input("What game does the creator have over 3000 hours in")
                    if Q1 == "Matrix CRT" and Q2 == "Silksong" and Q3 == "Terraria":
                        quizwin = True
                        newquiz = False
                    else:
                        print("The light in the statue's eyes dims")
                        print("You must have failed its test")
                        newquiz = False
                case 8|9|10|11:
                    Q1 = input("How many trees are in the lower Kilgour quad?")
                    Q2 = input("How long is a normal CPT period in seconds?")
                    Q3 = input("How many seconds are in the 'Never Gonna Give You Up' music video by Rick Astley?")
                    if Q1 == "2" and Q2 == "3300" and (Q3 == "213" or Q3 == "214"):
                        quizwin = True
                        newquiz = False
                    else:
                        print("The light in the statue's eyes dims")
                        print("You must have failed its test")
                        newquiz = False
                case 12|13|14|15:
                    Q1 = input("What is the name of the studio that created 'Hollow Knight'")
                    Q2 = input("")
                    Q3 = input("What is the creature that haunts this cavern names by the surface dwellers?")
                    if Q1 == "Team Cherry" and Q2 == "" and Q3 == "The entity":
                        quizwin = True
                        newquiz = False
                    else:
                        print("The light in the statue's eyes dims")
                        print("You must have failed its test")
                        newquiz = False
            if quizwin == True:
                print("The statue's eyes shine brighter for a moment.")
                print("A trophy materialises in the statues hands.")
                pickup = input("Would you like to replace your current item with this item?")
                match pickup:
                    case "Y"|"y"|"yes"|"Yes"|"YES":
                        P1.itempickup("Trophy")
                        print("The light in the statue's eyes dims")
                        quizwin = False
                    case "N"|"n"|"no"|"No"|"NO":
                        print("You leave the trophy in the statue's arms")
        else:
            if quizwin == True: 
                pickup = input("Would you like to replace your current item with this item?")
                match pickup:
                    case "Y"|"y"|"yes"|"Yes"|"YES":
                        P1.itempickup("Trophy")
                        quizwin = False
                    case "N"|"n"|"no"|"No"|"NO":
                        print("You leave the trophy in the statue's arms")
        print("The statue remains motionless")
class player:
    def __init__(self, poscol, posrow):
        self.poscol = poscol
        self.posrow = posrow
        self.item = 0

    def win():
        global win
        print("ggbrouwinnicejobiguess")
        win = 1

    def itempickup(self, item):
        self.item = item

    def P2movecheck(self):
        if self.item == "Trophy":
            print("The entity is in column:", player2poscol)
            print("The entity is in row:", player2posrow)

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
                        for i in range(0,16):
                            if rooms[i] == "X":
                                if rooom[i].posrow == posrow and rooom[i].poscol == poscol-2:
                                    for i in range(0,16):
                                        rooom[i].mapupdate(poscol-1, posrow)
                                    legal = 0
                                    break
                        if legal == 0:  
                            break
                        for i in range(0,6):
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
                        for i in range(0,16):
                            if rooms[i] == "X":
                                if rooom[i].posrow == posrow and rooom[i].poscol == poscol+2:
                                    for i in range(0,16):
                                        rooom[i].mapupdate(poscol+1, posrow)
                                    legal = 0
                                    break
                        if legal == 0:  
                            break
                        for i in range(0,6):
                            if removedcorridor[i] == posrow:
                                if corridors[removedcorridor[i]][0] == self.poscol+1:
                                    blocked = "yes"
                        if blocked == "yes":
                            legal = 0
                            for i in range(0,16):
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
                        for i in range(0,16):
                            if rooms[i] == "X":
                                if rooom[i].posrow == posrow+2 and rooom[i].poscol == poscol:
                                    for i in range(0,16):
                                        rooom[i].mapupdate(poscol, posrow+1)
                                    legal = 0
                                    break
                        if legal == 0:  
                            break
                        for i in range(0,6):
                            if removedcorridor[i] == self.posrow+1:
                                if corridors[removedcorridor[i]][0] == self.poscol:
                                    blocked = "yes"
                        if blocked == "yes":
                            legal = 0
                            for i in range(0,16):
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
                        for i in range(0,16):
                            if rooms[i] == "X":
                                if rooom[i].posrow == posrow-2 and rooom[i].poscol == poscol:
                                    for i in range(0,16):
                                        rooom[i].mapupdate(poscol, posrow-1)
                                    legal = 0
                                    break
                        if legal == 0:  
                            break
                        for i in range(0,6):
                            if removedcorridor[i] == self.posrow-1:
                                if corridors[removedcorridor[i]][0] == self.poscol:
                                    blocked = "yes"
                        if blocked == "yes":
                            legal = 0
                            for i in range(0,16):
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
                    blocked = "no"
                    match move:
                        case "left":
                            for i in range(0,6):
                                if removedcorridor[i] == self.posrow:
                                    if corridors[removedcorridor[i]][0] == self.poscol-1:
                                        blocked = "yes"
                            if blocked == "yes":
                                move = random.choice(randmove)
                            else:
                                if self.poscol +2 > 7:
                                    move = random.choice(randmove)
                                elif placementcol[0] == poscol+2 and placementrow[0] == posrow:
                                    random.choice(randmove)
                                else:
                                    self.poscol +=2
                                    break
                        case "right":
                            for i in range(0,6):
                                if removedcorridor[i] == self.posrow:
                                    if corridors[removedcorridor[i]][0]== self.poscol-1:
                                        blocked = "yes"
                            if blocked == "yes":
                                move = random.choice(randmove)
                            else:
                                if self.poscol -2 < 0:
                                    move = random.choice(randmove)
                                elif placementcol[0] == poscol-2 and placementrow[0] == posrow:
                                    random.choice(randmove)
                                else:
                                    self.poscol -=2
                                    break
                        case "down":
                            for i in range(0,6):
                                if removedcorridor[i] == self.posrow-1:
                                    if corridors[removedcorridor[i]][0] == self.poscol:
                                        blocked = "yes"
                            if blocked == "yes":
                                move = random.choice(randmove)
                            else:
                                if self.posrow - 2 < 0:
                                    move = random.choice(randmove)
                                elif True:
                                    for i in range(0,16):
                                        for i in range(0,16):
                                            if rooms[i] == "X":
                                                if rooom[i].posrow == posrow-2 and rooom[i].poscol == poscol:
                                                    move = random.choice(randmove)
                                                    break
                                else: 
                                    self.posrow -=2
                                    break
                        case "up":
                            for i in range(0,6):
                                    if removedcorridor[i] == self.posrow+1:
                                        if corridors[removedcorridor[i]][0] == self.poscol:
                                            blocked = "yes"
                            if blocked == "yes":
                                move = random.choice(randmove)
                            else:
                                if self.posrow +2 > 7:
                                    move = random.choice(randmove)
                                elif placementcol[0] == poscol and placementrow[0] == posrow+2:
                                    move = random.choice(randmove)
                                else:
                                    self.posrow +=2
                                    break
                        case _:
                            move = random.choice(randmove)
                    x += 1
                    if x > 100:
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
        global admin
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
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"
]

z = 0
for x in range (0, 4):
    for i in range(0, 4):
        rooom[z] = room(z, placementcol[i], placementrow[i-x], True, "no") 
        z += 1



P1 = player(0, 0)
P2 = player(6, 6)
P1.itempickup(0)
turn = 0

def rulles():
    for i in range(0,4):
        print(rules[0][i])
    input("When you are ready to enter the (); Press Enter.")


def gamestart():
    clear()
    global blocked
    global legal
    global playerposcol 
    global playerposrow 
    global player2poscol 
    global player2posrow 
    global removedcorridor
    global corridors
    global move
    global turn
    global win
    global admin
    global Board
    global Map
    randmove = ["left", "right", "down", "up"]
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
    for i in range(0,16):
        rooom[i].Boardupdate()
    turn = 0
    placementcol = [0, 2, 4, 6]
    placementrow = [0, 2, 4, 6]
    move = "jim"
    removedcorridor = [0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6]
    random.shuffle(removedcorridor)
    win = 0
    admin = 0
    legal = 1
    playerposcol = 0
    playerposrow = 0
    newquiz = True
    player2poscol = 6
    player2posrow = 6
    random.shuffle(placementcol)
    random.shuffle(placementrow)
    rooms = [
        "X", 2, 1, 1, 3, 2, 4, 0, 5, 0, 0, 0, 0, 0, 0, 0 
    ]
    random.shuffle(rooms)
    if rooms[0] == "X" or rooms[15] == "X":
        random.shuffle(rooms)
    for i in range(0,6):
        random.shuffle(corridors[removedcorridor[i]])
    while turn < 70:
        if win == 1: 
            break
        else:
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
                        move = "0"
                        input("When you are ready to continue press enter.")
                case "search"|"use":
                    P2.deathcheck(playerposcol, playerposrow)
                    P1.search(playerposcol, playerposrow)
                    turn+=1
                    P2.move(player2poscol, player2poscol, random.choice(randmove))
                    P1.P2movecheck()
                    input("When you are ready to continue press enter.")
                case "map":
                    P2.deathcheck(playerposcol, playerposrow)
                    P1.map(playerposcol, playerposrow)
                    P2.move(player2poscol, player2posrow, random.choice(randmove))
                    turn+=1
                    P1.P2movecheck()
                    input("When you are ready to continue press enter.")
                case "rules"|"help":
                    rule = 1
                    print("What rules are you confused about?")
                    print("Please enter the number that corresponds to your query: 1; What is the goal of the game. 2; What each type of room does. ")
                    print("3; What each item does. 4; What the entity is capable of. 5; How to read the map. ", "6; What each action does. ")
                    print("If you are softlocked and cannot beat the game type 'restart' as an action")
                    rule = int(input("Enter number here: "))
                    while rule != "0":
                        ruless(rule)
                        print("If you are confused about any other rules please enter the number. If you are done enter '0'.")
                        rule = input("Input number here: ")
                case "admin":
                    print("Welcome Admin.")
                    #rooom[i].Boardupdate()
                    admin = 1
                case "trophy":
                    P1.itempickup("Trophy")
                case "restart":
                    break
            clear()

rulles()
gamestart()

if win == 1:
    print("Great job!")
    print("You have managed to prevent the entity from escaping!")
    print("Unluckily the entity you trapped isnt the only one")
    print("There are many more hiding away in their own caves")
    print("But you can stop them by going and stopping the others aswell")
else:
    print("You have fail to prevent the entity from escaping either due to foolishness or just bad luck.")
    print("It is loose upon the world")
    print("Luckily for you by itself it can only cause minimal to moderate amont of destruction")
    print("But there are others just like it hiding in their own caves")

playagain = input("Would you like to attempt to stop a different entity?")
if "y" in playagain:
    gamestart()
elif "n" in playagain:
    print("I see.")
    print("You would rather let the world burn then risk your own life.")
    playagain = input("Are you sure this is what you really want?")
    if "y" in playagain:
        gamestart()
    elif "n" in playagain:
        print("I respect your decision.")
        print("Goodbye")