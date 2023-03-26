#> peerheer.nbtsmelting:player/check_if_player_not_in_gui_entry
#>
#> Author:
#>    PeerHeer (https://github.com/PeerHeer)
#>
#> Description:
#>    Entry point for checking change in rotation.

# Check if rotation change occurred.
execute as @a run function peerheer.nbtsmelting:player/check_if_player_not_in_gui

# Reschedule function.
schedule function peerheer.nbtsmelting:player/check_if_player_not_in_gui_entry 20t replace