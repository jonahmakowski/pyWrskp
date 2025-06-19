"""
Early prototype of the sudoku solver, witten by Marek Makowski.
A simple 'brute force' algorithm was implemented; the prototype appears to work, but
enhancements and testing is desired (cf comments at the bottom of this file).
"""

import numpy as np


class Board:
    def __init__(self, nrows=9, ncols=9):
        self.nrows = nrows
        self.ncols = ncols
        self.board = np.zeros((nrows, ncols), dtype="i1")
        self.finished = False  # True, if all slots filled
        self.depth = 0  # current depth of the recursion
        self.debug = 0  # debug level
        self.nzeros = 0  # number of non-zeros (i.e., predefined slots)

    def define_tst(self, board=None):  # define a board for testing
        #   [5, 3, 0, 0, 7, 0, 0, 0, 0],
        if board != None:
            self.board = board
        elif board == None:
            self.board = [
                [
                    5,
                    3,
                    0,
                    0,
                    7,
                    0,
                    1,
                    0,
                    0,
                ],  # slot in col 6 set to 1 (to assure a unique solution?)
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 0, 0],
            ]

    # return true if num fits to the board cell at position (row, col)
    # checks all rows, then cols, then boxes
    def accepted(self, num, row, col):
        for j in range(0, self.ncols):  # check all cols in the row
            if self.board[row][j] == num:  # already in the row
                return False  # cannot accept a duplicate
        for i in range(0, self.nrows):  # check all rows in the column
            if self.board[i][col] == num:  # already in the column
                return False  # cannot accept a duplicate
        # positions of first row/col y0/x0 of the box to which (row,col) belongs
        y0 = (row // 3) * 3  # there are 3 rows in each box
        x0 = (col // 3) * 3  # there are 3 col in each box
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[y0 + i][x0 + j] == num:  # already in the box
                    return False  # cannot accept a duplicate in the square
        return True  # new entry num can be accepted

    # fill the board by recursively trying to insert entries in empty slots by rows and cols
    def solve(self):
        if self.debug > 2:
            print("recursion depth = ", self.depth)
        if self.finished:
            return
        for row in range(0, self.nrows):
            for col in range(0, self.ncols):
                if self.board[row][col] == 0:  # skip already filled slots/cells
                    for num in range(1, 10):
                        if self.accepted(num, row, col):
                            self.board[row][
                                col
                            ] = num  # fill and continue with next free slot
                            if self.debug and row == 8:
                                print("reached 8-th row, now at col = ", str(col))
                                self.print()
                            if row == self.nrows - 1 and row == col:
                                self.finished = True  # all slots filled
                                print(
                                    "Finished: all slots assigned. The recursion depth = ",
                                    self.depth,
                                )
                                # self.print()
                                return
                            if self.finished:
                                print(
                                    "ERROR: should not come here after all slots are filled."
                                )
                                print(
                                    "num = ",
                                    str(num),
                                    " row = ",
                                    str(row),
                                    " col = ",
                                    str(col),
                                )
                                return
                            self.depth += 1
                            self.solve()  # try the next free slot(s)
                            # retuns here from the lower recursion level
                            self.depth -= 1
                            if self.finished:
                                return
                            self.board[row][
                                col
                            ] = 0  # current board is infeasible, reset the slot and continue
                            # loop for numbers ends here
                        # loop for columns ends here
                    # loop for rows ends here
                    return  # continue with the next free slot

    def info(self):
        self.nzeros = 0
        for row in range(0, self.nrows):
            for col in range(0, self.ncols):
                if self.board[row][col] > 0:  # skip already filled slots/cells
                    self.nzeros += 1
        print(
            "The board has ",
            str(self.nzeros),
            "defined slots, i.e., ",
            str(round(self.nzeros / 81.0, 3)),
            " density.",
        )

    def print(self, comm=None):
        if comm:
            print(comm)
        for row in range(0, self.nrows):
            print(" row[" + str(row) + "]: ", self.board[row])


if __name__ == "__main__":
    board = Board()
    board.define_tst()
    board.info()
    board.print("Initial board:")
    board.solve()
    board.print("Filled board:")

    print("Finished.")
    print(
        "\nInfo: this is an early prototype of the sudoku solver. The following enhancements are desired/planned:"
    )
    print("\t* Code review; refactorization, if desired.")
    print(
        "\t* Input the board definition in flexible formats (currently the definition is hard-coded)"
    )
    print("\t* Handling infeasible board definitions.")
    print("\t* Handling non-unique solutions.")
    print("\t* Extensive testing, especially on hard problems.")
    print(
        "\t* Consider improvements to the solver algorithm, if needed for hard problems."
    )
    print("\t* Optional integration with the board generator (to be developed).")
    print("\t* User-friendly output (maybe through the Web browser).")
    print(
        "\t* Optional integration (as hint/checker) with the user-control interactive solver."
    )
