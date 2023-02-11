#> peerheer.nbtsmelting:schedule_1t
#
# Author: PeerHeer
#
# Execute as all marker entities and reschedule the function.

# Execute as all markers.
execute as @e[type=minecraft:marker, tag=peerheer.nbtsmelting.entity.marker] at @s run function peerheer.nbtsmelting:states/process_state

# Schedule function again.
schedule function peerheer.nbtsmelting:schedule_1t 1t replace
