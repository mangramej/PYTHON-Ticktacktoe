class TickTackToe:
    def __init__(self):
        self.board = {
            "A1": "-",
            "A2": "-",
            "A3": "-",
            "B1": "-",
            "B2": "-",
            "B3": "-",
            "C1": "-",
            "C2": "-",
            "C3": "-"
        }


    def display_board(self):
        print(
f"""
    1     2     3
A [ {self.board["A1"]} ] [ {self.board["A2"]} ] [ {self.board["A3"]} ]
B [ {self.board["B1"]} ] [ {self.board["B2"]} ] [ {self.board["B3"]} ]
C [ {self.board["C1"]} ] [ {self.board["C2"]} ] [ {self.board["C3"]} ]
""")


    def place_choice(self, player, choice):
        try: self.board[choice]
        except KeyError:                print("Out of bounds");     return False

        if self.board[choice] != "-":   print("Invalid slot");      return False

        self.board[choice] = player.symbol;                         return True


    def verify_win(self, player):
        if (self.board["A1"] == f"{player}" and 
            self.board["A2"] == f"{player}" and 
            self.board["A3"] == f"{player}" or
            self.board["B1"] == f"{player}" and 
            self.board["B2"] == f"{player}" and 
            self.board["B3"] == f"{player}" or
            self.board["C1"] == f"{player}" and 
            self.board["C2"] == f"{player}" and 
            self.board["C3"] == f"{player}" or ### END OF HORIZONTAL CHECKER ###
            self.board["A1"] == f"{player}" and 
            self.board["B1"] == f"{player}" and 
            self.board["C1"] == f"{player}" or
            self.board["A2"] == f"{player}" and 
            self.board["B2"] == f"{player}" and 
            self.board["C2"] == f"{player}" or
            self.board["A3"] == f"{player}" and 
            self.board["B3"] == f"{player}" and 
            self.board["C3"] == f"{player}" or ### END OF VERTICAL CHECKER ###
            self.board["A1"] == f"{player}" and 
            self.board["B2"] == f"{player}" and 
            self.board["C3"] == f"{player}" or
            self.board["A3"] == f"{player}" and 
            self.board["B2"] == f"{player}" and 
            self.board["C1"] == f"{player}" ### END OF DIAGONAL CHECKER ###
            ):
            return True
        return False


    def is_draw(self):
        draw = True
        for slot in self.board:
            if self.board[slot] == "-":
                draw = False
                break
        return draw


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def __str__(self):
        return self.symbol


def start():
    game        = TickTackToe()
    player1     = Player("x")
    player2     = Player("o")
    player_turn = player1
    prev_turn   = player1
    while True:
        if game.verify_win(prev_turn): game.display_board(); print(f"Player {prev_turn}: wins!"); break
        if game.is_draw(): game.display_board(); print("Game is draw!"); break

        game.display_board()
        input_choice = str(input(f"{player_turn}> ")).upper()
        
        if player_turn == player1:
            if game.place_choice(player1, input_choice): player_turn = player2; prev_turn = player1
        
        elif player_turn == player2:
            if game.place_choice(player2, input_choice): player_turn = player1; prev_turn = player2


if __name__ == "__main__":
    start()