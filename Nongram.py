# Documentation reciepe:
#     def func(param1, param2):
#         """
#             Does pla pla pla
#             param1: the row lists
#             param2: the column lists
#             returns:
#                 a_list: pla
#         """

class Nonogram:
    def __init__(self, size = 5, rows = [[]*5], cols = [[]*5], puzzle = [[0 for i in range(size)] for j in range(size)]):
        """
        Initialization for the Nonogram Object
        :param size: the lenght of the side of the grid
        :param rows: a list of lists, each one represents the number on the side of each row
        :param cols: a list of lists, each one represents the number above of each column
        :param puzzle: 2d empty list, represnting a white grid, 0 means white, 1 means black
        """
        size = size
        rows = rows # should be like this [[1], [2, 2], [3], [4], [5]]
        cols = cols # should be like this [[1], [2, 2], [3], [4], [5]]
        puzzle = puzzle
        solved = False

    # 1
    def generate_puzzle(self):
        """
        generates a solution represents the puzzle and changes rows and cols for "self"
        """
        pass

    # 1
    def is_complete(self):
        """
        checks if the puzzle solved in right way or not
        """
        pass

    # 4
    def solve(self):
        """
        solves the puzzle using backtracking
        """
        current_state = [[0 for i in range(size)] for j in range(size)]

        # 2
        def is_valid(state):
            """
            Checks if the current state in the backtracking case is valid or not
            :param state: the state we want to check
            """
            pass

        # 2
        def backtrack(current_state):
            """
            The recursive function
            :param current_state:
            :return:
            """
            pass
        pass

    # 2
    def print_puzzle(self, puzzle):
        """
        Prints the puzzle in beautiful form
        :param puzzle: 2d list representing the current state of the puzzle
        """