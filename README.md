# CPT-
Game based on hunt the wumpus

# ideas
environment: 
4 by 4 board
24 pathways
16 pathways between the rooms
15 rooms


types of rooms
- snake * 2
- exit * 1
- key * 1 
- banishment scroll * 2
- empty * 9


actions:
map - opens and updates the map
move - move through a pathway to a adjacent room
search/use - search the room for enemies, keys or an exit, if a key is held it is used, if a banishment scroll is held it banishes the enemy in that room

enemies/objects:
antiplayer - starts in opposite room to player, moves in opposite direction of player movement is possible if not doesnt move, moves in a random direction if the map or search actions are taken, if it is in a room adjacent to the player it will move into that room, if the player takes a non movement action in the same room the player loses
scare enemy - starts in 2 rooms, forces player to run in a random direction when player searches the room it is in (does not move)




# Journal
## 4-5-2026:
- Analysed task 
- Discussed potential ideas


## 6-5-2026
- built functions for rooms
- created functions for player actions