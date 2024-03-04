from project import TicTacToe


def test_checking_turn():
    game = TicTacToe()
    assert game.checking_turn(0) == "X"
    assert game.checking_turn(1) == "O"

def test_replace_position():
    game = TicTacToe()
    game.places = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    assert game.replace_position("1") == {1: "X", 2: "2", 3: "3",
                                           4: "4", 5: "5", 6: "6",
                                           7: "7", 8: "8", 9: "9"}
    assert game.places == [2, 3, 4, 5, 6, 7, 8, 9]

def test_replace_position_invalid():
    game = TicTacToe()
    game.places = [2, 3, 4, 5, 6, 7, 8, 9]
    assert game.replace_position("invalid") == None
    assert game.places == [2, 3, 4, 5, 6, 7, 8, 9]

def test_check_winner():
    game = TicTacToe()
    assert game.check_winner() == None
