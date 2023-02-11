
# Revoke advancement
advancement revoke @s only peerheer.nbtsmelting:block_clicked/smoker_clicked

# Set checking state to all in-range idle markers.
execute at @s as @e[type=minecraft:marker, tag=peerheer.nbtsmelting.entity.marker.state.idle, tag=peerheer.nbtsmelting.entity.marker.block.smoker, distance=..9] run function peerheer.nbtsmelting:states/checking/change_state_to_checking
