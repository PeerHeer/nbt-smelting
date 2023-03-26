#> peerheer.nbtsmelting:player/reset_no_gui_checks_entry
#>
#> Author:
#>    PeerHeer (https://github.com/PeerHeer)
#>
#> Description:
#>    Entry point for resetting the player rotation change.
#>    Called when a player interacts with a smelter to avoid detecting a rotation change while the player is in the GUI.

execute as @a run function peerheer.nbtsmelting:player/reset_no_gui_checks
