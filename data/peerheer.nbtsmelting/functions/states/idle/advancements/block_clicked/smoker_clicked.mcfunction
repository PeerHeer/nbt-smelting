#> peerheer.nbtsmelting:states/idle/advancements/block_clicked/smoker_clicked
#>
#> Author:
#>    PeerHeer (https://github.com/PeerHeer)
#>
#> Description:
#>    Handles clicking of smoker. Signals that the player possibly has the smoker GUI open.

say clicked smoker

# Revoke advancement
advancement revoke @s only peerheer.nbtsmelting:block_clicked/smoker_clicked

# Remove GUI open tag, since the GUI was possibly reopened.
tag @s remove peerheer.nbtsmelting.player.possible_gui_open.blast_furnace
tag @s remove peerheer.nbtsmelting.player.possible_gui_open.furnace
tag @s remove peerheer.nbtsmelting.player.possible_gui_open.smoker

# Process interaction.
execute at @s as @e[type=minecraft:marker, tag=peerheer.nbtsmelting.entity.marker.state.idle, distance=..9] at @s run function peerheer.nbtsmelting:states/idle/gui_interaction/interacted/interacted_with_smoker

# Signal that this player possibly has the smoker GUI open.
tag @s add peerheer.nbtsmelting.player.possible_gui_open.smoker

# Schedule functions after triggering the advancement.
function peerheer.nbtsmelting:states/idle/advancements/block_clicked/schedule_functions_after_trigger
