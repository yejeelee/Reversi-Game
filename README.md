# Reversi-Game

**Project Description:**

Built Reversi game with simple game theory.
This game has GUI using Processing and Python programming.

User can play against computer AI for this Reversi game. 

**Instruction of the Game**
- need to download Processing3 for python if don’t have one
- Open the ‘reversi_game.pyde’ file to start the Processing3 and click the ‘Play’ button
    - Black tile is the User
    - White Tile is the Computer
    - Black tile goes first. Click on the legal spot then tile will show up.
    - If there is no legal move, it will display on Console with ’No legal move for computer!’
    - If there is no legal move, switch player. 
    - If both don’t have legal move, game is over.
- When you are done playing, it will display the score and who wins.
- If you want to keep record of this game, write down your name as display shows.
- To see the scores, open the ‘scores.txt’ file.

**Computer AI move**

Instead of choosing random legal move, there is a simple game theory to determine the best legal move.
Realized that taking the corner spot is very important.
So, if there's legal move in the corner, choose that legal move.
If there isn't and there is a legal move in the edges, then choose that spot as a legal move.
if there isn't, choose the spots in the very middle area. 
for example, if its 8 X 8 board, (0 ~ 7)X(0 ~ 7)
then any legal move that exist in  middle 4X4 square, x(2 ~ 5) and y(2 ~ 5) is the best option.
The reason is that if I put a tile in row 1 or 6 or col 1 or 6, the player can have the edge spot or the corner spot. If none of them exist then pick those risky spot left.

**Testing**

Used pytest(testing framework for python) to test all classes which are Board, Computer AI, Game Controller, Tile and Tiles.

**To resize the board of the game**

- Originally, it is 8x8
- Open ‘reversi_game.pyde’ and change the ’SPOT’ variable.
- For example, if you want to play 4x4, change the ’SPOT’ to 4.
