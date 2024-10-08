import os
class TikTakToe:
    def __init__(self):
        self.curr_player = "X"
        self.topleft = "1"
        self.topmid = "2"
        self.topright = "3"
        self.midleft = "4"
        self.middle = "5"
        self.midright = "6"
        self.bottomleft = "7"
        self.bottommid = "8"
        self.bottomright = "9"
        self.available_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def print_board(self):
        print("     |     |     ")
        print(f"  {self.topleft}  |  {self.topmid}  |  {self.topright}  ")
        print("_____|_____|_____")
        print("     |     |     ")
        print(f"  {self.midleft}  |  {self.middle}  |  {self.midright}  ")
        print("_____|_____|_____")
        print("     |     |     ")
        print(f"  {self.bottomleft}  |  {self.bottommid}  |  {self.bottomright}  ")
        print("     |     |     ")
        print()
        return

    @staticmethod
    def clear_screen():
        # Check the operating system and run the appropriate command
        if os.name == 'nt':  # For Windows
            os.system('cls')
        else:  # For macOS/Linux (Unix-based)
            os.system('clear')

    def win_check(self):
        if self.bottomleft == self.bottommid == self.bottomright:
            return True
        elif self.midleft == self.middle == self.midright:
            return True
        elif self.topleft == self.topmid == self.topright:
            return True
        elif self.bottomleft == self.midleft == self.topleft:
            return True
        elif self.bottommid == self.middle == self.topmid:
            return True
        elif self.bottomright == self.midright == self.topright:
            return True
        elif self.topleft == self.middle == self.bottomright:
            return True
        elif self.topright == self.middle == self.bottomleft:
            return True
        else:
            return False
        
    def player_turn(self):
        move = input("Input a number corresponding to the square you want: ")
        
        if move.isdigit():
            move = int(move)

            if move in self.available_moves:
                if move == 1:
                    self.topleft = self.curr_player
                elif move == 2:
                    self.topmid = self.curr_player
                elif move == 3:
                    self.topright = self.curr_player
                elif move == 4:
                    self.midleft = self.curr_player
                elif move == 5:
                    self.middle = self.curr_player
                elif move == 6:
                    self.midright = self.curr_player
                elif move == 7:
                    self.bottomleft = self.curr_player
                elif move == 8:
                    self.bottommid = self.curr_player
                elif move == 9:
                    self.bottomright = self.curr_player

                self.available_moves.remove(move)
                
                self.curr_player = "O" if self.curr_player == "X" else "X"
            else:
                print("Invalid move. The position is already taken or out of range.")
        else:
            print("Please enter a valid number.")

game = TikTakToe()
game.clear_screen()
while True:
    print(f"It is {game.curr_player}'s turn")
    print()
    game.print_board()
    game.player_turn()
    if game.win_check():
        winner = "O" if game.curr_player == "X" else "X"  # Previous player is the winner
        print(f"AND WE HAVE A WINNER: {winner}!!!")
        break
    elif len(game.available_moves) == 0:
        print("DRAW")
        break
    game.clear_screen()
