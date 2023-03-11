
# Revoke advancement
advancement revoke @s only peerheer.nbtsmelting:block_placed/dropper_placed

# Set checking state to all in-range idle markers.
execute at @s as @e[type=minecraft:marker, tag=peerheer.nbtsmelting.entity.marker.state.idle, distance=..9] at @s run function peerheer.nbtsmelting:states/idle/hopper_dropper_checks/check_dropper
