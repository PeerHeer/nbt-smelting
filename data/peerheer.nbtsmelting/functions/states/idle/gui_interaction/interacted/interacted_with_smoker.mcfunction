#> peerheer.nbtsmelting:states/idle/gui_interaction/interacted/interacted_with_smoker
#>
#> Author:
#>    PeerHeer (https://github.com/PeerHeer)
#>
#> Description:
#>    Adds interacted tag to the smoker. Remove inventory_changed tag if there are no nearby players with smoker GUI open.

# Signal that player interacted with smoker.
tag @s[tag=peerheer.nbtsmelting.entity.marker.block.smoker] add peerheer.nbtsmelting.entity.marker.player_interacted

# Remove inventory_changed tag if there are no players nearby that have an open GUI.
# We can do this because we only care about changed inventory after the GUI is opened.
execute if entity @s[tag=peerheer.nbtsmelting.entity.marker.block.blast_furnace] unless entity @a[tag=peerheer.nbtsmelting.player.possible_gui_open.blast_furnace, distance=..9, limit=1] run function peerheer.nbtsmelting:states/idle/gui_interaction/remove_tags
execute if entity @s[tag=peerheer.nbtsmelting.entity.marker.block.furnace] unless entity @a[tag=peerheer.nbtsmelting.player.possible_gui_open.furnace, distance=..9, limit=1] run function peerheer.nbtsmelting:states/idle/gui_interaction/remove_tags
execute if entity @s[tag=peerheer.nbtsmelting.entity.marker.block.smoker] unless entity @a[tag=peerheer.nbtsmelting.player.possible_gui_open.smoker, distance=..9, limit=1] run tag @s remove peerheer.nbtsmelting.entity.marker.player_inventory_changed
