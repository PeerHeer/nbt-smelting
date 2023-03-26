#> peerheer.nbtsmelting:schedule/schedule_1t
#>
#> Author:
#>    PeerHeer (https://github.com/PeerHeer)
#>
#> Description:
#>    Schedule loop every tick.

# Handle when the player rejoins the game.
execute as @a[scores={peerheer.nbtsmelting.leave_game=1..}] at @s run function peerheer.nbtsmelting:handle_leave_game

# Process all markers (except IDLE ones).
execute as @e[type=minecraft:marker, tag=peerheer.nbtsmelting.entity.marker] at @s run function peerheer.nbtsmelting:states/process_state

# Reschedule the function.
schedule function peerheer.nbtsmelting:schedule/schedule_1t 1t replace
