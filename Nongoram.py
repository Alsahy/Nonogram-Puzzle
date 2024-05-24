# Documentation reciepe:
#     def func(param1, param2):
#         """
#             Does pla pla pla
#             param1: the row lists
#             param2: the column lists
#             returns:
#                 a_list: pla
#         """
from draw_functions import *

class Nonogram:
    def __init__(self, size=5):
        """
        Initialization for the Nonogram Object
        :param size: the lenght of the side of the grid
        :param rows: a list of lists, each one represents the number on the side of each row
        :param cols: a list of lists, each one represents the number above of each column
        :param puzzle: 2d empty list, represnting a white grid, 0 means white, 1 means black
        """
        self.size = size
        self.rows=[[]*size] # should be like this [[1], [2, 2], [3], [4], [5]]
        self.cols=[[]*size] # should be like this [[1], [2, 2], [3], [4], [5]]
        self.puzzle=[[0 for i in range(size)] for j in range(size)]
        solved = False

    def set_rows(self, rows):
        """
        sets the rows by the user
        :param rows: the rows user wants to set
        """
        self.rows = rows

    def set_cols(self, cols):
        """
        sets the columns by the user
        :param cols: the columns user wants to set
        """
        self.cols = cols

    def get_a_row(self, row_idx, puzzle):
        """
        Gets a row from the rows on the side
        :param puzzle: the passed state to the function
        :return: the row on the side in a list
        """
        row = []
        cnt = 0
        for i in range(self.size):
            if cnt > 0 and puzzle[row_idx][i] == 0:
                row.append(cnt)
                cnt = 0
            elif puzzle[row_idx][i] == 1:
                cnt += 1

        if cnt > 0:
            row.append(cnt)

        return row

    def get_a_col(self, col_idx, puzzle):
        """
        Gets a column from the columns above
        :param puzzle: the passed state to the function
        :return: the column above in a list
        """
        col = []
        cnt = 0
        for i in range(self.size):
            if cnt > 0 and puzzle[i][col_idx] == 0:
                col.append(cnt)
                cnt = 0
            elif puzzle[i][col_idx] == 1:
                cnt += 1

        if cnt > 0:
            col.append(cnt)

        return col

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
    def visualize_nonogram(self, solution, row_clues, col_clues):
        """
        Prints the puzzle in beautiful form
        :param solution: 2d list representing the current state of the puzzle
        :param row_clues: the clues on the side
        :param col_clues: the clues above
        """
        N = len(solution)
        size = 750

        img = np.zeros([size, size, 3], np.uint8)  # create image
        img = cv2.rectangle(img, (0, 0), (size, size), White, -1)
        offset = int(size * 0.3)
        size = size - offset
        cell_unit = int(size / (N))

        img = print_rectangels(img, offset, cell_unit, N, solution)
        # img = print_lines(img, offset, cell_unit, N, solution)
        # img = print_row_clues(img, offset, cell_unit, N, solution)
        # img = print_col_clues(img, offset, cell_unit, N, solution)

        cv2.imshow('image', img)  # show your work by window
        cv2.waitKey(0)  # wait key from keyboard
        cv2.destroyAllWindows()  # close any opened window
