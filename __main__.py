"""
This file contains the function calls to execute the game.
This should be the only place you have code outside of functions, and the more
code within functions the better. You should call the functions defined in the
other modules (setup_game, player_actions, enemy_actions). You are free to
define additional functions and modules if needed, but these should be in
addition to existing functions, rather than replacements.

Note: to call functions from other modules, you need to
include the module name; e.g. setup_game.create_grid()
"""

# sys is imported just to use sys.exit() as opposed to quit().
# pylint gave an error when using quit().
import sys
import setup_game
import player_actions
import enemy_actions
# add any other imports you feel are relevant here

if __name__ == "__main__":
    print("PIRATES!")
    difficulty = setup_game.select_difficulty()
    grid = setup_game.create_grid(10)
    grid = setup_game.add_rocks(grid, difficulty)
    grid, player_position = setup_game.place_player(grid)
    grid, enemy_position = setup_game.place_enemy(grid)

    while True:
        setup_game.print_grid(grid)
        direction = player_actions.get_user_direction()

        new_player_position = (
            player_actions.get_new_player_position
            (player_position, direction, grid)
        )

        old_player_position = player_position

        grid = (
            player_actions.kill_player
            (grid, old_player_position, new_player_position)
        )

        grid, player_position = (
            player_actions.move_player
            (grid, old_player_position, new_player_position)
        )

        new_enemy_position = (
            enemy_actions.get_new_enemy_position
            (enemy_position, player_position)
        )

        old_enemy_position = enemy_position

        grid = (
            enemy_actions.kill_enemy
            (grid, old_enemy_position, new_enemy_position)
        )

        grid, enemy_position = (
            enemy_actions.move_enemy
            (grid, old_enemy_position, new_enemy_position)
        )

        isCaught = (
            enemy_actions.has_caught_player
            (enemy_position, player_position)
        )

        if isCaught:
            setup_game.print_grid(grid)
            newX = new_player_position[1]
            newY = new_player_position[0]
            grid[newY][newX] = "X"
            print("Game over, your ship has been captured by pirates.")
            setup_game.print_grid(grid)
            print("Ending game...")
            sys.exit()
