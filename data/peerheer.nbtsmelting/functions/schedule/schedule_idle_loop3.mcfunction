#> peerheer.nbtsmelting:schedule_2t
#
# Author: PeerHeer
#
# Process some markers in IDLE state.

# Process some idle markers.
execute as @e[tag=peerheer.nbtsmelting.entity.marker.state.idle] if score @s peerheer.nbtsmelting.idle_loop matches 3 at @s if entity @p[distance=..9] run function peerheer.nbtsmelting:states/idle/tick_state

# Schedule function again.
schedule function peerheer.nbtsmelting:schedule/schedule_idle_loop3 10t replace
