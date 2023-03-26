#> peerheer.nbtsmelting:states/idle/advancements/block_clicked/furnace_clicked
#>
#> Author:
#>    PeerHeer (https://github.com/PeerHeer)
#>
#> Description:
#>    Handles clicking of furnace. Signals that the player possibly has the furnace GUI open.

say clicked furnace

# Revoke advancement
advancement revoke @s only peerheer.nbtsmelting:block_clicked/furnace_clicked

# Remove GUI open tag, since the GUI was possibly reopened.
tag @s remove peerheer.nbtsmelting.player.possible_gui_open.blast_furnace
tag @s remove peerheer.nbtsmelting.player.possible_gui_open.furnace
tag @s remove peerheer.nbtsmelting.player.possible_gui_open.smoker

# Process interaction.
execute at @s as @e[type=minecraft:marker, tag=peerheer.nbtsmelting.entity.marker.state.idle, distance=..9] at @s run function peerheer.nbtsmelting:states/idle/gui_interaction/interacted/interacted_with_furnace

# Signal that this player possibly has the furnace GUI open.
tag @s add peerheer.nbtsmelting.player.possible_gui_open.furnace

# Schedule functions after triggering the advancement.
function peerheer.nbtsmelting:states/idle/advancements/block_clicked/schedule_functions_after_trigger
