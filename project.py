import tabulate, os
from check_spots import check_spots


def main():
    game = TicTacToe()
    game.looping()
    

class TicTacToe():
    def __init__(self):    
        self.position = {1: "1", 2: "2", 3: "3",
                    4: "4", 5: "5", 6: "6",
                    7: "7", 8: "8", 9: "9"}
        self.places = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.turn = 0
        
        
    def board(self, position):
        game_board = [[position[1],position[2],position[3]],
                    [position[4],position[5],position[6]],
                    [position[7],position[8],position[9]]]
        
        print(tabulate.tabulate(game_board, tablefmt="grid"))


    def looping(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            self.board(self.position)
            self.substitute()
            self.tie()
            
            
    def substitute(self):
        player_count = str((self.turn % 2) + 1)
        self.user_input = input(f"Player {player_count}'s turn: ").lower().strip()
        if self.user_input == "quit":
            exit()
        elif self.user_input.isdigit() and int(self.user_input) in self.places:
            self.places.remove(int(self.user_input))
            if int(self.user_input) not in self.places:
                self.position[int(self.user_input)] = self.checking_turn(self.turn)
                self.check_winner()
                self.turn += 1
                
                
    def checking_turn(self, turn):
        if turn % 2 == 0:
            return "X"
        else:
            return "O"


    def check_winner(self):
        if check_spots(self.position) == True:
            if self.checking_turn(self.turn) == "O":
                self.position[int(self.user_input)] = self.checking_turn(self.turn)
                os.system("cls" if os.name == "nt" else "clear")
                self.board(self.position)
                exit("Player 2 wins!")
                
            elif self.checking_turn(self.turn) == "X":
                self.position[int(self.user_input)] = self.checking_turn(self.turn)
                os.system("cls" if os.name == "nt" else "clear")
                self.board(self.position)
                exit("Player 1 wins!")
                
            else:
                exit("Tie")
    
    
    def tie(self):
        if self.places == []:
            self.position[int(self.user_input)] = self.checking_turn(self.turn)
            os.system("cls" if os.name == "nt" else "clear")
            choice = input("Tie. Do you want a rematch? ").strip().lower()
            if choice == "no":
                exit()
            elif choice == "yes":
                self.rematch()
              
                
    @classmethod
    def rematch(cls):
        return cls()


if __name__ == "__main__":
    main()