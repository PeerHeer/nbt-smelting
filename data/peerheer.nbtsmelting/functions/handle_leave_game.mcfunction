#> peerheer.nbtsmelting:handle_leave_game
#>
#> Author:
#>    PeerHeer (https://github.com/PeerHeer)
#>
#> Description:
#>    Schedule periodic ticking functions.

# Revoke advancement in case player left before it was revoked.
advancement revoke @s only peerheer.nbtsmelting:inventory_changed

# Reset rotation change in case player left before scheduled function executed.
function peerheer.nbtsmelting:player/reset_rotation_change

# Reset leave game score.
scoreboard players set @s peerheer.nbtsmelting.leave_game 0
