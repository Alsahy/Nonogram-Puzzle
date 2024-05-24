import cv2
import numpy as np
White = (255, 255, 255)
Black = (0, 0, 0)

def print_rectangels(img, offset, cell_unit, N, solution):
    """
    Prints the rectangles of the black cells on the figure
    :param img: the object of the image
    :param offset: offset of the drawing to leave area to the clues
    :param cell_unit: the lenght of the side of the cell
    :param N: the lenght of the side of the puzzle
    :param solution: the sent solution
    :return: img: the final object of the image
    """
    for row in range(N):
        for col in range(N):
            img = cv2.rectangle(img, # the image object
                                (offset+col*cell_unit, offset+row*cell_unit), # start position
                                (offset+(col+1)*cell_unit, offset+(row+1)*cell_unit), # end position
                                White if solution[row][col] == 0 else Black, # color
                                -1) # fill if -1 and line width if another positive value

            if solution[row][col] == 1:
              img = cv2.rectangle(img,
                                  (offset+col*cell_unit, offset+row*cell_unit),
                                  (offset+(col+1)*cell_unit, offset+(row+1)*cell_unit),
                                  White,
                                  3)
    return img

def print_lines(img, offset, cell_unit, N, solution):
    """
        Prints the seperating lines on the figure
        :param img: the object of the image
        :param offset: offset of the drawing to leave area to the clues
        :param cell_unit: the lenght of the side of the cell
        :param N: the lenght of the side of the puzzle
        :param solution: the sent solution
        :return: img: the final object of the image
    """

    return img

def print_row_clues(img, offset, cell_unit, N, solution, row_clues):
    """
        Prints the rectangles of the black cells on the figure
        :param img: the object of the image
        :param offset: offset of the drawing to leave area to the clues
        :param cell_unit: the lenght of the side of the cell
        :param N: the lenght of the side of the puzzle
        :param solution: the sent solution
        :param row_clues: the clues on the side
        :return: img: the final object of the image
    """
    def string_row_clue(a_row_clue):
        """
        turns the clue from a list to a string
        :param a_row_clue:
        :return: the string of the clue
        """
        s = ""
        return s

    return img

def print_col_clues(img, offset, cell_unit, N, solution, col_clues):
    """
        Prints the rectangles of the black cells on the figure
        :param img: the object of the image
        :param offset: offset of the drawing to leave area to the clues
        :param cell_unit: the lenght of the side of the cell
        :param N: the lenght of the side of the puzzle
        :param solution: the sent solution
        :param col_clues: the clues above
        :return: img: the final object of the image
    """
    def string_col_clue(a_col_clue):
        """
            turns the clue from a list to a string
            :param a_col_clue:
            :return: the string of the clue
        """
        s = ""
        for number in a_col_clue:
            s = s + str(n) + '\n'
        return s

    font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX  # text type
    for clue in col_clues:
        cv.putText(img, "clue", (120, 490), font, 1.5, (255, 255, 255), 2)