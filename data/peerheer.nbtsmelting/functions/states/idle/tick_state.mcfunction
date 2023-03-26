#> peerheer.nbtsmelting:states/idle/tick_state
#>
#> Author:
#>    PeerHeer (https://github.com/PeerHeer)
#>
#> Description:
#>    Tick all IDLE markers.

# Kill marker if block is destroyed.
execute if entity @a[distance=..9, limit=1] run function peerheer.nbtsmelting:marker/kill_marker_if_block_destroyed

# Check if there are any adjacent hoppers/droppers.
function peerheer.nbtsmelting:states/idle/hopper_dropper_checks/check_hopper_dropper

# Remove all tags if there is no player nearby that possibly has a smelter GUI open.
execute if entity @s[tag=peerheer.nbtsmelting.entity.marker.block.furnace] unless entity @a[distance=..9, tag=peerheer.nbtsmelting.player.possible_gui_open.furnace, limit=1] run function peerheer.nbtsmelting:states/idle/gui_interaction/remove_tags
execute if entity @s[tag=peerheer.nbtsmelting.entity.marker.block.blast_furnace] unless entity @a[distance=..9, tag=peerheer.nbtsmelting.player.possible_gui_open.blast_furnace, limit=1] run function peerheer.nbtsmelting:states/idle/gui_interaction/remove_tags
execute if entity @s[tag=peerheer.nbtsmelting.entity.marker.block.smoker] unless entity @a[distance=..9, tag=peerheer.nbtsmelting.player.possible_gui_open.smoker, limit=1] run function peerheer.nbtsmelting:states/idle/gui_interaction/remove_tags
