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

## 8-5-2026
- Documentation and planning
- Started creating the player class

## 11-5-2026
- fixed move function
- started data dictionary

## 14-5-2026
- worked on comparison of procedural language and object oriented approach
- 

## 15-5-2026
- Worked on DFD
- Worked on the map function

## 18-5-2026
- Reworked room class
- Worked on success criteria

## 20-5-2026
- Coded the corridors

## 22-5-2026
- worked on fixing the bug where is couldn't move from room to room

## 27-5-2026
- Worked on fixing the bugs with the anti-players movement

## 1-6-2026
- Worked on the quiz

## 3-6-2026
- Created replayablilty and lore
- 

## 5-6-2026
- Worked on testing and evaluation documentation
- White box testing