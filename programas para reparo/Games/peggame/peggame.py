""" Find solution to the Peg Game.

The holes are numbered as follows,

            1,1


         2,1  2,2


      3,1  3,2  3,3


    4,1  4,2  4,3  4,4


 5,1  5,2  5,3  5,4  5,5

 Initially, all holes have pegs except one.  To make a valid move requires
 the configuration (peg1, peg2, hole1) in a straight line, horizontally or
 diagonally. Move peg1 to hole1 and remove peg2 from the board. When no more
 moves are possible, the game is over. If only one peg is left, you won. """

from sys import exit
from string import split
from random import randint
from UserDict import UserDict
class MyDict(UserDict):
   def __getitem__(self,arg):
      if self.data.has_key(arg):
         return self.data[arg]
      else:
         return 'OFF'     # return 'OFF' if off the board
def makelist(board):                     # Make a list of possible moves
   npeg = 0                              # Number of pegs remaining
   possible = []                         # Possible Moves
   for i in range(0,5):
      for j in range(0,i+1):
         if board[(i,j)] == "PEG": npeg = npeg + 1
         else:continue

         if board[(i-1,j)] == "PEG" and board[(i-2,j)] == "EMPTY":       #   Up
            possible.append((i,j,i-2,j))

         if board[(i+1,j)] == "PEG" and board[(i+2,j)] == "EMPTY":       #   Down
            possible.append((i,j,i+2,j))

         if board[(i,j-1)] == "PEG" and board[(i,j-2)] == "EMPTY":       #   Left
            possible.append((i,j,i,j-2))

         if board[(i,j+1)] == "PEG" and board[(i,j+2)] == "EMPTY":       #   Right
            possible.append((i,j,i,j+2))

         if board[(i-1,j-1)] == "PEG" and board[(i-2,j-2)] == "EMPTY":   #   Up left
            possible.append((i,j,i-2,j-2))

         if board[(i+1,j+1)] == "PEG" and board[(i+2,j+2)] == "EMPTY":   #   Down right
            possible.append((i,j,i+2,j+2))
   return (npeg,possible)

def main():
   while 1:
      init = raw_input("Enter Coordinates of Empty Hole (1,1 to 5,5):")
      if init == '' : init = '1,1'
      row,col = split(init,",")
      row = int(row); col = int(col)
      if 1 <= row <= 5 and 1 <= col <= row: break
      if 1 <= row <= 5 and 1 <= col <= 5 and col > row :
         row,col = col,row        # Swap
         break
   print ('Start With Empty Hole At %d,%d') % (row,col)
   init = row-1,col-1             # Convert to 0-based indices
   ngame = 0                      # Number of games played
   while 1:                       # Each iteration is a new game
      board = MyDict()
      moves = []                  # Save moves to be displayed in case we win
      for i in range(0,5):
         for j in range(0,i+1):
            board[(i,j)] = "PEG"    # Put a peg in all the holes
      board[init] = "EMPTY"         # Empty hole at beginning of game
      ngame = ngame + 1
      while 1:                      # Each iteration is a move within a game
         npeg,possible = makelist(board)
         num = len(possible)
         if num == 0:               # No more moves are possible
            if npeg == 1:           # Only 1 peg remains, you won
               for i,j,i2,j2 in moves:
                  print ("Move %d,%d --> %d,%d") % (i+1,j+1,i2+1,j2+1)
               print ("You won! %d Games Have Been Played") % ngame
               exit()
            else: break             # The game was lost
         else:
            ir = randint(0,num-1)          # Randomly pick a move
            i,j,i2,j2 = possible[ir]       # Move is from i,j to i2,j2
            board[(i,j)] = "EMPTY"
            board[((i+i2)/2,(j+j2)/2)] = "EMPTY"
            board[(i2,j2)] = "PEG"
            moves.append((i,j,i2,j2))      # Save moves in case we win this game

main()
