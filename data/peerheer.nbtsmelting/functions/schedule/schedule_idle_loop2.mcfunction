#> peerheer.nbtsmelting:schedule/schedule_idle_loop2
#>
#> Author:
#>    PeerHeer (https://github.com/PeerHeer)
#>
#> Description:
#>    Schedule loop for IDLE markers with loop score 2.

# Process IDLE markers with loop score 2.
execute as @e[tag=peerheer.nbtsmelting.entity.marker.state.idle] if score @s peerheer.nbtsmelting.idle_loop matches 2 at @s run function peerheer.nbtsmelting:states/idle/tick_state

# Reschedule function.
schedule function peerheer.nbtsmelting:schedule/schedule_idle_loop2 10t replace
