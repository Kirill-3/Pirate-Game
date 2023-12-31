"""
This file contains the functions related to the player's merchant ship.

Do not change the function definitions, only the function bodies. You may add
additional functions if you wish.
"""

# enter any imports you feel are relevant here
# sys is imported just to use sys.exit() as opposed to quit().
# pylint gave an error when using quit().
import sys
# Imported so that I can call the print_grid function.
import setup_game


def get_user_direction():
    """
    This function should ask the user for a direction to move in
    ("N"/"E"/"S"/"W"), and return it.
    :return: The direction the user chose (a single character string).
    :rtype: string
    """

    # your code here for getting the user direction
    direction = str(input("Enter a direction to move in (N, E, S, W): "))
    # return the direction the user entered:
    return direction


def get_new_player_position(player_position, direction, grid):
    """
    This function should calculate what will be the new position of the
    merchant ship, based on its current position and the direction the user
    chose. Note that this function shouldn't move the player, just work out
    where their new position will be (so you can use this new position to work
    out whether they will hit a rock, or the pirate etc).

    Note: most "human" coordinates read across (x axis) then up (y axis).
    Depending on how you created the grid, this may not always be the case when
    we access the 2D lists :-)

    Note2: You should handle the ship attempting to move off the edge of the
    grid. You can make the movement behave as if the grid is toroidal
    ('wraparound'), OR you can make the edges 'bounded' so the player cannot
    move off them. There's a question in the report about how you handle this.

    :param player_position: The player's current position
    :type player_position: tuple
    :param direction: The direction the player wants to move in (N/E/S/W)
    :type direction: string
    :param grid: The 2D game board
    :type grid: list
    :return: The player's updated position (tuple of two integers)
    :rtype: tuple
    """

    # your code to calculate the new position here
    # This code works for valid inputs, but for invalid
    # inputs, it will ask for another input but then crash.
    # The same happpens if the player attempts to move off the grid.
    if direction == "N":
        new_player_position = player_position[0]-1, player_position[1]
        if new_player_position[0] < 0:
            print("Invalid, choose a different direction")
            return get_user_direction()
    elif direction == "S":
        new_player_position = player_position[0]+1, player_position[1]
        if new_player_position[0] > 9:
            print("Invalid, choose a different direction")
            return get_user_direction()
    elif direction == "W":
        new_player_position = player_position[0], player_position[1]-1
        if new_player_position[1] < 0:
            print("Invalid, choose a different direction")
            return get_user_direction()
    elif direction == "E":
        new_player_position = player_position[0], player_position[1]+1
        if new_player_position[1] > 9:
            print("Invalid, choose a different direction")
            return get_user_direction()
    else:
        print("Invalid, choose either 'N', 'E', 'S', or 'W'")
        return get_user_direction()

    return new_player_position


def move_player(grid, old_player_position, new_player_position):
    """
    This function should move the player; it can be done simply by removing "M"
    from the old position and putting it in the new position.

    The function doesn't need to return anything, as the grid can be updated
    "in place", but you can return the grid or anything else you need if
    you like.

    :param grid: The 2D gameboard
    :type grid: list
    :param old_player_position: the player's current position (two integers)
    :type old_player_position: tuple
    :param new_player_position: the new player position (tuple of 2 integers)
    :type new_player_position: tuple
    :return:
    """

    # your code to move the player here
    # Obtain X and Y coordinates for the players
    # old and new position.
    newX = new_player_position[1]
    newY = new_player_position[0]
    oldX = old_player_position[1]
    oldY = old_player_position[0]
    # Place the player in the new position,
    # and an empty space in the old position.
    grid[newY][newX] = "M"
    grid[oldY][oldX] = "."
    player_position = (newY, newX)

    return grid, player_position


def kill_player(grid, old_player_position, new_player_position):
    """
    This function should 'kill' the player; it's actually very similar to
    moving the player: it can be done simply by removing "M" from the old
    position and putting "X" in the new position.

    The function doesn't need to return anything, as the grid can be updated
    "in place", but you can return the grid or anything else you need if
    you like.

    :param grid: The 2D gameboard
    :type grid: list
    :param old_player_position: the player's current position
    :type old_player_position: tuple
    :param new_player_position: the new player position
    :return:
    """

    # your code to kill the player here
    # Obtain X and Y coordinates for the players
    # old and new position.
    # If there is a rock in the players new position,
    # Place an "X" there and end the game.
    oldY, oldX = old_player_position
    newY, newX = new_player_position
    if grid[newY][newX] == "*":
        grid[newY][newX] = "X"
        grid[oldY][oldX] = "."
        print("Game over, you have hit a rock.")
        setup_game.print_grid(grid)
        print("Ending game...")
        sys.exit()
    return grid
