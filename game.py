import random
import os

def clear():  # Clears the terminal
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


placement = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
]
random.shuffle(placement)

print("jim")
excludedroom = random.randrange(0, 16)
snakeroom = random.randrange(0, 16)
snakeroom1 = random.randrange(0, 16)
exitroom = random.randrange(0, 16)
scrollroom = random.randrange(0, 16)
scrollroom1 = random.randrange(0, 16)
keyroom = random.randrange(0, 16)
print("jim")

while exitroom == keyroom:
    keyroom = random.randrange(0, 16)
print("jim")
while exitroom == excludedroom or excludedroom == keyroom or excludedroom == 0:
    excludedroom = random.randrange(0, 16)


rooms = [
    snakeroom, snakeroom1, scrollroom, scrollroom1, excludedroom, keyroom, exitroom
]

class room():
    def __init__(self, id, pos, type, new): #pos = position, new = bool; has the room has been entered before, 
        self.id = id
        self.new = new
        for i in range(0, 7):
            if id == rooms[i]:
                self.type = rooms[i]
                print(rooms[i])
            else: 
                self.pos = pos
    
    def move(self, pos, new):
        #self.new = new
        if new == True:
            print("you have moved to a new room")
            new = False
        else:
            print("You have arrived in a familiar room")
    
    def search(self, pos, type):

        match type:
            case rooms[0] or rooms[1]:
                scare = random.range(0,4)
            case rooms[2] or rooms[3]:
                scroll += 1
            case rooms[5]:
                print("This room has a key!")
            case rooms[7]:
                print["this"]
        for i in range(0, 7):
            if type == rooms[i]:

                print("")




for i in range(0, 16):
    rom = room("rom", i, placement[i], True)




playerpos = 0

for i in range(0,20):
    move = int(input("Please give a number from 1 to 16: "))-1
    if -1 < move < 16:
        if move == playerpos + 4 or move == playerpos - 4 or move == playerpos + 1 or move == playerpos - 1: 
            playerpos = move
    room.move(rom, playerpos, )