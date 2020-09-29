import random

class tictactoe:
    
    def __init__(self):
        self.board = [
            ["n", "n", "n"],
            ["n", "n", "n"],
            ["n", "n", "n"],
            [0]
        ]

        self.running = True
        self.turn = "X"

    def insert_piece(self, x, y, piece):
        self.board[x][y] = piece

    def is_occupied(self, x, y):
        return not self.board[x][y] == "n"

    def show_board(self):
        print("            Y")
        print("        0   1   2")
        print("")
        print("   0    {} | {} | {}".format(self.board[0][0], self.board[0][1], self.board[0][2]))
        print("       ----------")
        print("X  1    {} | {} | {}".format(self.board[1][0], self.board[1][1], self.board[1][2]))
        print("       ----------")
        print("   2    {} | {} | {}".format(self.board[2][0], self.board[2][1], self.board[2][2]))

    def is_winner(self, piece):
        return (self.board[0][0] == piece and self.board[0][1] == piece and self.board[0][2] == piece) or (self.board[0][0] == piece and self.board[1][0] == piece and self.board[2][0] == piece) or (self.board[0][0] == piece and self.board[0][1] == piece and self.board[0][2] == piece) or (self.board[1][0] == piece and self.board[1][1] == piece and self.board[1][2] == piece) or (self.board[2][0] == piece and self.board[2][1] == piece and self.board[2][2] == piece) or (self.board[0][1] == piece and self.board[1][1] == piece and self.board[2][1] == piece) or (self.board[0][1] == piece and self.board[1][1] == piece and self.board[2][1] == piece) or (self.board[0][2] == piece and self.board[1][2] == piece and self.board[2][2] == piece) or (self.board[0][0] == piece and self.board[1][1] == piece and self.board[2][2] == piece) or (self.board[2][0] == piece and self.board[1][1] == piece and self.board[0][2] == piece)
        
    def is_tie(self):
        return not(self.board[0][0] == "n" or self.board[0][1] == "n" or self.board[0][2] == "n" or self.board[1][0] == "n" or self.board[1][1] == "n" or self.board[1][2] == "n" or self.board[2][0] == "n" or self.board[2][1] == "n" or self.board[2][2] == "n")

    def start(self):
        while self.running:
            if self.is_tie():
                self.show_board()
 
                print("")
                print("It's a tie!")

                self.running = False
                break

            print("")
            self.show_board()
            print("")
            print("it's {}'s turn!".format(self.turn))

            x_move = int(input("({}) 0-2 X: ".format(self.turn)))

            while not(x_move >= 0 and x_move <= 2):
                print("Between 0 - 2 only!")
                x_move = int(input("({}) 0-2 X: ".format(self.turn)))

            y_move = int(input("({}) 0-2 Y: ".format(self.turn)))

            while not(y_move >= 0 and y_move <= 2):
                print("Between 0 - 2 only!")
                y_move = int(input("({}) 0-2 Y: ".format(self.turn)))
            
            if not self.is_occupied(x_move, y_move):
                self.insert_piece(x_move, y_move, self.turn)

                if self.is_winner(self.turn):
                    self.show_board()
                    print("")

                    print("{} has won!".format(self.turn))

                    self.running = False
                    break

                if self.turn == "X":
                    self.turn = "O"
                else:
                    self.turn = "X"
            else:
                print("")
                print("That part is occupied! Please find another one")

game = tictactoe()
game.start()