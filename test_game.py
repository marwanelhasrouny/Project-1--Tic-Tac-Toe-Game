import unittest
from game import *

class TestProject(unittest.TestCase):

    def test_main():
        assert main()
    def test_intro():
        assert intro()
    def test_create_grid():
        assert create_grid()
    def test_sym():
        assert sym()
    def test_startGamming():
        assert startGamming()
    def test_isFull():
        assert isFull()
    def test_outOfBoard():
        assert outOfBoard()
    def test_printPretty(board):
        assert printPretty(board)
    def test_isWinner(board, symbol_1, symbol_2, count):
        assert isWinner(board, symbol_1, symbol_2, count)
    def test_illegal(board, symbol_1, symbol_2, row, column):
        assert illegal(board, symbol_1, symbol_2, row, column)
    def test_report(count, winner, symbol_1, symbol_2):
        assert report(count, winner, symbol_1, symbol_2)

if __name__ == "__main__":
    unittest.main()