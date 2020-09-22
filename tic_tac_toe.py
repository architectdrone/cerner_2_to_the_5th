#cerner_2^5_2020
board, X_turn = [[" " for x in range(3)] for y in range(3)], True #Initialize variables
while not ((board[0][0] == board[0][1] == board[0][2] != " ") or (board[1][0] == board[1][1] == board[1][2] != " ") or (board[2][0] == board[2][1] == board[2][2] != " ") or (board[0][0] == board[1][0] == board[2][0]!= " ") or (board[0][1] == board[1][1] == board[2][1]!= " ") or (board[0][2] == board[1][2] == board[2][2]!= " ") or (board[0][0] == board[1][1] == board[2][2]!= " ") or (board[2][0] == board[1][1] == board[0][2]!= " ") ): #Ensure win state is not reached
    print(f"\n\n\n\n{board[0][0]}|{board[1][0]}|{board[2][0]}\n-----\n{board[0][1]}|{board[1][1]}|{board[2][1]}\n-----\n{board[0][2]}|{board[1][2]}|{board[2][2]}")
    turn_symbol = ("X","O")[int(X_turn := not X_turn)] #Determine who is next
    x, y = int(input(f"\n{turn_symbol}(x)> ")), int(input(f"{turn_symbol}(y)> ")) #Get input from the user
    if (board[x][y] != " "): continue #Do not allow overwriting of a previously set space
    board[x][y] = turn_symbol #Add the symbol to the required spot
print(f"{turn_symbol} won, fair and square!") #Announce to winner

'''
TIC TAC TOE in 8 lines.
Axises are zero indexed.
PS C:\dev\personal> python .\tic_tac_toe.py
 | |
-----
 | |
-----
 | |
X(x)> 1
X(y)> 1




 | |
-----
 |X|
-----
 | |
O(x)> 2
O(y)> 2




 | |
-----
 |X|
-----
 | |O
X(x)> 0
X(y)> 2




 | |
-----
 |X|
-----
X| |O
O(x)> 1
O(y)> 2




 | |
-----
 |X|
-----
X|O|O
X(x)> 2
X(y)> 0
X won, fair and square!
'''
