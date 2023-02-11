
# Revoke advancement
advancement revoke @s only peerheer.nbtsmelting:block_clicked/blast_furnace_clicked

# Set checking state to all in-range idle markers.
execute at @s as @e[type=minecraft:marker, tag=peerheer.nbtsmelting.entity.marker.state.idle, tag=peerheer.nbtsmelting.entity.marker.block.blast_furnace, distance=..9] run function peerheer.nbtsmelting:states/checking/change_state_to_checking
