#> peerheer.nbtsmelting:load/schedule_functions
#>
#> Author:
#>    PeerHeer (https://github.com/PeerHeer)
#>
#> Description:
#>    Schedule periodic ticking functions.

# Set variable for idle loop.
execute unless score #peerheer.nbtsmelting.idle_loop peerheer.global matches -2147483648..2147483647 run scoreboard players set #peerheer.nbtsmelting.idle_loop peerheer.global 0

# Ticking function triggerin every tick.
schedule function peerheer.nbtsmelting:schedule/schedule_1t 1t replace

# Function used to check if player rotation changed.
schedule function peerheer.nbtsmelting:player/check_if_player_not_in_gui_entry 20t replace

# Functions for distributing idle furnaces.
schedule function peerheer.nbtsmelting:schedule/schedule_idle_loop0 1t replace
schedule function peerheer.nbtsmelting:schedule/schedule_idle_loop1 2t replace
schedule function peerheer.nbtsmelting:schedule/schedule_idle_loop2 3t replace
schedule function peerheer.nbtsmelting:schedule/schedule_idle_loop3 4t replace
