class Connect_4_Game: 
    def __init__(self):
        # we first establish identifires for what symbols
        # the player has control over
        self.Player_1 = 'X'
        self.Player_2 = 'O'

        # We then start creating our game settings
        # which includes colums rows, our board, turns
        # and the last input
        
        self.Colums = 7 
        self.Rows = 6

        self.Board = [[' ' for _ in range(self.Colums)] for _ in range(self.Rows)]
        self.Turns = 0 
        self.last_Input = [-1,-1]

    # we now create afunction to display the board to the client
    def DisplayBoard(self):
        print("\n")
        for i in range(self.Colums): 
            print(f" ({i + 1}) ", end = "")
        print("\n")

        for x in range(self.Rows):
            print('|', end = "")
            for i in range(self.Colums):
                print(f" {self.Board[x][i]}  |", end = "")
            print("\n")

        print(f" {'-' * 35}\n")
    # now we will make a function to decide which persons turn it is
    # we will handle this using our self.turns and will sloley depend on the number
    # of turn 
    def which_turn(self):
        players = [self.Player_1, self.Player_2]
        return players[self.Turns % 2]
        
    def Turn(self, colum):
        for i in range(self.Rows-1, -1, -1):
            if self.Board[i][colum] == " ":
                self.Board[i][colum] = self.which_turn()
                self.last_Input = [i, colum]

                self.Turns += 1
                return True
        return False
    
    def in_bounds(self, r, c):
        return (r >= 0 and r < self.Rows and c >= 0 and c < self.Colums)
    
    def Win_Condition(self):
        last_row = self.last_Input[0]
        last_col = self.last_Input[1]
        last_letter = self.Board[last_row][last_col]

        direction = [[[-1, 0], 0, True], 
                      [[1, 0], 0, True], 
                      [[0, -1], 0, True],
                      [[0, 1], 0, True],
                      [[-1, -1], 0, True],
                      [[1, 1], 0, True],
                      [[-1, 1], 0, True],
                      [[1, -1], 0, True]]
        
        for i in range(4):
            for x in direction:
                r = last_row + (x[0][0] * (i+1))
                c = last_col + (x[0][1] * (i+1))

                if x[2] and self.in_bounds(r, c) and self.Board[r][c] == last_letter:
                    x[1] += 1
                else:
                    x[2] = False
        for i in range(0,7,2):
            if direction[i][1] + direction[i+1][1] >=3:
                self.DisplayBoard()
                print(f"{last_letter} is the winner") 
                return last_letter
        return False

# Create a central function to start our game
# and handle the state of the game
def StartGame():
    Die = False
    Client_Game = Connect_4_Game()
    Client_Game.DisplayBoard()
     
    while not Die:
        Client_Game.DisplayBoard()
        
        client_Valid_move = False
        while not client_Valid_move: 
            Client_Move = input(f"{Client_Game.which_turn()}'s turn, pick a column (1-7): ")
            try:
                client_Valid_move = Client_Game.Turn(int(Client_Move) - 1)
            
            except:
                print(f"Invalid move, please choose a number between 1 and  {Client_Game.Colums}")

        Die = Client_Game.Win_Condition()

        if not any(' ' in x for x in Client_Game.Board):
            print("The game is a draw")
            return
# loop our game so the player has active
# and multiple inputs
if __name__ == '__main__':
    StartGame()