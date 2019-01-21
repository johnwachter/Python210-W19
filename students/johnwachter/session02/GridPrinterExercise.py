#Title: Lab GridPrinterExercise.py
#Change Log: (Who, When, What)
#JWachter, 2019-01-19, created file and printed basic grid in part 1 of exercise

#Data
plusminusrow = '+''-''-''-''-''+''-''-''-''-''+'
piperow = '|'' '' '' '' ''|' ' '' '' '' ''|''\n'
newline = '\n'

"This is part 1 of the exercise"
print("Part 1")
def printgrid_1():
    """Print a 2x2 grid"""
    print(plusminusrow + newline + piperow*4 + plusminusrow + newline + piperow*4 +plusminusrow)
printgrid_1()
"This is part 2 of the exercise"
print("Part 2")
def printgrid_2(n):
    """
    Print the visual of a 1x1 grid
    :param n: the number of rows in the grid represented by the pipe '|' symbol
    :return: Returns True so as to return at least something which follows Pythonic convention.
    """
    print(plusminusrow + newline + piperow*n + plusminusrow + newline + piperow*n + plusminusrow)
    return True
printgrid_2(1)


"This is part 3 of the exercise"
print("Part 3")
def printgrid_3(n_rowsandcolumns = 4, n_sizedunit = 1):
    """
    Print the visual of a grid based, whose size is based on arguments fed to parameters in the function.
    :param n_rowsandcolumns: Represents the number of times the grid will be repeated across (columns) and down (rows)
    :param n_sizedunit: Represents the number of minus '-' symbols that appear across the row of the grid
    :return: Returns True so as to return at least something which follows Pythonic convention.
    """
    minussymbol = '-'
    plusminusrow2 = ('+' + minussymbol * n_sizedunit)
    piperow2 = '|' + ' ' * n_sizedunit
    grid = (plusminusrow2*n_rowsandcolumns + '+' + newline + piperow2*n_rowsandcolumns + '|' + newline + piperow2 * n_rowsandcolumns + '|' + newline + piperow2 * n_rowsandcolumns + '|' + newline + piperow2 * n_rowsandcolumns + '|' + newline)
    print(grid*n_rowsandcolumns, end=plusminusrow2*n_rowsandcolumns +'+')
    return True
printgrid_3(4, 9)

