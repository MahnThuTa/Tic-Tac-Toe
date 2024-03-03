# Tic-Tac-Toe

#### Video Demo:  `<URL HERE>`


#### Description:

* This project is a game; Tic Tac Toe game. Two players are allowed. I used OOP since it is better for recalling variable. The board function is used to create a game board with the positions taken. I also used Tabulate for a better design rather than using "|". Then it prints out the board in a grid view. The looping function for the looping and os.system is to clear the terminal after each loop so the terminal won't mess with boards and inputs. The "nt" means that your OS(Operating System) is Microsoft Window. In Microsoft Window; we use "cls" to clear the terminal but we use "clear" in other OS(Operating System). play_game is the function where we start our game. It will ask the user for input and if the user type "quit" the program will exit automatically. If the user input a digit; the program will excute the replace_position function that replaces X or O in that digit's position. The checking_turn function is to check the player is X or O. X for player 1 and O for player 2. check_winner function checks if one of the players has won by importing check_spots function from check_spots file and it clears the whole terminal, prints out the winner and quit the program. If there is no winner, you can rematch by typing "yes" but if you don't want a rematch and wants to quit the program; You can just simply type "no". I used classmethod to to recreate a whole new program. This is my project for CS50, I hope you all like it and don't mind about my grammar, I am still learnig😊.


#### Features:

* Replace the input number with O or X up to their turn

* The game ends if a player has won.

* Tie if no one wins.

* The terminal clear after each input.


#### How to use:

* Players have to input number between 1 to 9 up to their turn.

* If the game is tie you can rematch by typing "yes" otherwise "no".
