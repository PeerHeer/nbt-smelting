
# Revoke advancement
# advancement revoke @s only peerheer.nbtsmelting:inventory_changed
say inv changed

# Set checking state to all in-range idle markers.
execute at @s as @e[type=minecraft:marker, tag=peerheer.nbtsmelting.entity.marker.state.idle, tag=peerheer.nbtsmelting.entity.marker.player_interacted, distance=..9] run tag @s add peerheer.nbtsmelting.entity.marker.player_inventory_changed

schedule function peerheer.nbtsmelting:states/idle/gui_interaction/check_inventory_changed_advancement 1t append

