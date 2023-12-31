"""
This file contains the functions related to the player's merchant ship.

Do not change the function definitions, only the function bodies. You may add
additional functions if you wish.
"""

# enter any imports you feel are relevant here
# sys is imported just to use sys.exit() as opposed to quit().
# pylint gave an error when using quit().
import sys
import numpy
# Imported so that I can call the print_grid function.
import setup_game


def get_new_enemy_position(enemy_position, player_position):
    """
    I've filled in this function for you, do not change it.
    This function computes the enemy's next position, based on where the player
    is. This doesn't actually move the enemy ship, just tells you where
    the enemy's next move should be.

    Note that it handles the positions as two integers, (row, column). i.e.
    down then across. If you have handled the coordinates differently in your
    code that's fine, but in your main code you may need to handle how you pass
    the positions to this function, and how you handle the results of this
    function. If you get it wrong you may see the pirates running away from the
    merchant ship :-)

    Also note: this code works whether you use a toroidal ("wraparound") grid
    or a bounded grid, but it may possibly affect the difficulty...

    There is a question about this function you should answer in your report.

    :param enemy_position: The enemy's position (row, column)
    :param player_position: The player's position (row, column)
    :return: The enemy's updated position (row, column)
    :rtype: tuple
    """

    # \ just allows us to split a statement over two lines
    row = \
        enemy_position[0] + numpy.sign(player_position[0] - enemy_position[0])
    column = \
        enemy_position[1] + numpy.sign(player_position[1] - enemy_position[1])
    new_enemy_position = (row, column)

    return new_enemy_position


def has_caught_player(enemy_position, player_position):
    """
    This function should determine whether the pirates have caught the
    merchant ship. It should return a boolean: True if caught, False if still
    safe. If the pirate ship is at the same position as the merchant ship, or
    any of the spaces *adjacent* to the merchant ship, then it has caught it.
    (For the purposes of this game, "adjacent" is all 8 spaces around the ship
    - so including diagonals).
    :param enemy_position:
    :param player_position:
    :return: whether the player is caught
    :rtype: bool
    """

    # your code here.
    # Checks if the enemy's X and Y
    # coordinates are one less or more than
    # the players X and Y coordinates.
    # If both are, the enemy must be adjacent,
    # setting caught to true.
    caught = False
    y, x = player_position
    y1, x1 = enemy_position

    if x1 in range(x-1, x+2) and y1 in range(y-1, y+2):
        caught = True
    return caught


def move_enemy(grid, old_enemy_position, new_enemy_position):
    """
    This function should move the enemy; it can be done simply by removing "P"
    from the old position and putting it in the new position.

    The function doesn't need to return anything, as the grid can be updated
    "in place", but you can return the grid or anything else you need if
    you like.

    Tip: what this functions does is very similar to move_player, except with
    a "P" instead of an "M".

    :param grid: The 2D gameboard
    :type grid: list
    :param old_enemy_position: the enemy's current position (two integers)
    :type old_enemy_position: tuple
    :param new_enemy_position: the new enemy position (tuple of 2 integers)
    :type new_enemy_position: tuple
    :return:
    """

    # your code to move the pirates here
    # These next two functions are almost identical
    # to move_player and kill_player.
    newX = new_enemy_position[1]
    newY = new_enemy_position[0]
    oldX = old_enemy_position[1]
    oldY = old_enemy_position[0]
    grid[newY][newX] = "P"
    grid[oldY][oldX] = "."
    enemy_position = (newY, newX)

    return grid, enemy_position


def kill_enemy(grid, old_enemy_position, new_enemy_position):
    """
    This function should 'kill' the enemy; it's actually very similar to moving
    the enemy: it can be done simply by removing "P" from the old position and
    putting "W" in the new position.

    The function doesn't need to return anything, as the grid can be updated
    "in place", but you can return the grid or anything else you need if
    you like.
    :param grid: The 2D gameboard
    :type grid: list
    :param old_enemy_position: the enemy's current position (two integers)
    :type old_enemy_position: tuple
    :param new_enemy_position: the new enemy position (tuple of 2 integers)
    :type new_enemy_position: tuple
    :return:
    """

    # your code to sink the pirates here
    oldY, oldX = old_enemy_position
    newY, newX = new_enemy_position
    if grid[newY][newX] == "*":
        grid[newY][newX] = "W"
        grid[oldY][oldX] = "."
        print("You win! The pirates have hit a rock.")
        setup_game.print_grid(grid)
        print("Ending game...")
        sys.exit()
    return grid
