from project import TicTacToe


def test_checking_turn():
    game = TicTacToe()
    assert game.checking_turn(0) == "X"
    assert game.checking_turn(1) == "O"
    
def test_substitute():
    game = TicTacToe()
    assert game.tie() == None
    
def test_check_winner():
    game = TicTacToe()
    assert game.check_winner() == None