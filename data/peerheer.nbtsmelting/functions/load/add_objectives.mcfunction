#> peerheer.nbtsmelting:load/add_objectives
#>
#> Author:
#>    PeerHeer (https://github.com/PeerHeer)
#>
#> Description:
#>    Add objectives.

# Objective used to distribute idle smelters over different scheduling loops.
scoreboard objectives add peerheer.nbtsmelting.idle_loop dummy

# Used to revoke inventory_changed advancement when player joins the game.
scoreboard objectives add peerheer.nbtsmelting.leave_game minecraft.custom:minecraft.leave_game

# Used to check if player rotation changed. If it did, the player cannot be in a GUI.
scoreboard objectives add peerheer.nbtsmelting.rotation.0 dummy
scoreboard objectives add peerheer.nbtsmelting.rotation.1 dummy
scoreboard objectives add peerheer.nbtsmelting.rotation.0.prev dummy
scoreboard objectives add peerheer.nbtsmelting.rotation.1.prev dummy

# Used to check if player jumped or sneaked. If it did, the player cannot be in a GUI.
scoreboard objectives add peerheer.nbtsmelting.jump minecraft.custom:minecraft.jump
scoreboard objectives add peerheer.nbtsmelting.sneak_time minecraft.custom:minecraft.sneak_time

# Used to check if slots are occupied.
scoreboard objectives add peerheer.nbtsmelting.slot.input.is_occupied dummy
scoreboard objectives add peerheer.nbtsmelting.slot.fuel.is_occupied dummy
scoreboard objectives add peerheer.nbtsmelting.slot.output.is_occupied dummy
