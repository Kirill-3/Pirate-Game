"""
This file contains the functions that setup the game: creating a grid, placing
rocks and ships. You will need to finish these functions.

Do not change the function definitions, only the function bodies. You may add
additional functions if you wish.
"""

# enter any imports you feel are relevant here
import random


def select_difficulty():
    """
    This function allows the user to input a difficulty, and then returns it
    if it is valid. Validation checks ensure that the user input is between
    1 and 10, and that the input is an integer.

    :return: the user input difficulty
    :rtype: integer
    """
# Code adapted from:
# https://www.digitalocean.com/community/tutorials/python-valueerror-exception-handling-examples

# Code inside of the "try" statement is executed first, allowing an input and
# then checking if it is between 1 and 10.
# If it isn't, the function is called, and the code will be executed again.
# If valid, difficulty is returned and the function ends.
# If an exception is raised from the input,
# in this case a ValueError from not inputting an integer,
# the code inside the "except" statement is executed.
    try:
        difficulty = int(input("Select a difficulty (1-10): "))
        if difficulty < 1 or difficulty > 10:
            print("Invalid input.")
            return select_difficulty()
        return difficulty
    except ValueError:
        print("Invalid input.")
        return select_difficulty()


def create_grid(size):
    """
    This function creates a square grid where each side is as long as 'size'.
    The grid should be held in a two-dimensional list: that is, a
    list-of-lists. Each item in the outer list will be another list of the same
    size. The outer list holds the rows, the inner list holds each cell in a
    row. At the end of the function, this grid should be returned.

    :param size: the size of a side of the square grid
    :type size: int
    :return: a two-dimensional list representing the game grid
    :rtype: list
    """

    # put your code to create the grid here

    # Create an empty list, "grid"
    grid = []

    for _ in range(size):
        # Create an empty list, "row"
        row = []
        # Loop over every point in the row and add a "."
        for _ in range(size):
            row.append(".")
        # Add the row to the grid
        grid.append(row)

    return grid


def add_rocks(grid, difficulty):
    """
    This functions adds rocks(*) to the grid, then returns the updated grid.
    The number of rocks should be: 15 minus the difficulty level. For
    example, at difficulty 10 there would only be 5 rocks. The rocks should be
    randomly placed.
    :param grid: A 2D list that represents the game board
    :type grid: list
    :param difficulty: The game difficulty
    :type difficulty: int
    :return: The updated 2D game board
    :rtype: list
    """

    # put your code here:
    numRocks = 15 - difficulty
    # Generate a random coordinate on the grid, and place a rock there.
    # Do this 15 minus difficulty times.
    for _ in range(0, numRocks):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        grid[x][y] = "*"
    return grid


def place_player(grid):
    """
    This function places the merchant ship ("M") at a random position in the
    grid, then returns the updated grid and the player position. Remember the
    ship should not be placed on the same square as a rock or the pirates.
    The player position should be returned as two integers in a tuple.
    :param grid: The 2D gameboard
    :type grid: list
    :return: The updated 2D gameboard, and player position.
    :rtype: list, tuple
    """

    # your code for placing the player here
    # While isSuccess is false, generate a random x and y coordinate.
    # If the generated coordinates have a rock on them,
    # continue to the next iteration of the loop.
    # Else place the player on the grid, set isSuccess to true.
    isSuccess = False
    while not isSuccess:
        randomX = random.randint(0, 9)
        randomY = random.randint(0, 9)
        if grid[randomX][randomY] == "*":
            continue
        grid[randomX][randomY] = "M"
        player_position = randomX, randomY
        isSuccess = True

    return grid, player_position


def place_enemy(grid):
    """
    This function places the pirate ship ("P") at a random position in the
    grid, then returns the updated grid and the pirate position. Remember the
    ship should not be placed on the same square as a rock or the merchant
    ship. The pirate position should be returned as two integers in a tuple.

    Optional Note: does this function do anything similar to place_player and
    add_rocks? Is there any duplicate code that could be moved out to an
    additional function?

    :param grid: The 2D gameboard
    :type grid: list
    :return: The updated 2D gameboard, and enemy position.
    :rtype: list, tuple
    """

    # your code for placing the enemy here
    # Essentially the same code as above,
    # could probably be moved to an external function.
    isSuccess = False
    while not isSuccess:
        randomX = random.randint(0, 9)
        randomY = random.randint(0, 9)
        if grid[randomY][randomX] == "*":
            continue
        if grid[randomX][randomY] == "M":
            continue
        grid[randomX][randomY] = "P"
        enemy_position = randomX, randomY
        isSuccess = True
    # returns two values, the updated grid and the enemy_position:
    return grid, enemy_position


def print_grid(grid):
    """
    Prints the grid. You'll need to call this function several times throughout
    the game. This function doesn't need to return anything, just print out to
    command line.
    :param grid: The 2D gameboard
    :type grid: list
    :return: None
    """

    # your code for printing the grid here
    # Iterate over each row and print it.
    for row in grid:
        print(row)
