#> peerheer.nbtsmelting:mark_block/mark/mark_smoker
#>
#> Author:
#>    PeerHeer (https://github.com/PeerHeer)
#>
#> Description:
#>    Mark a smoker by summoning the marker entity.

# Signal that a block has been found.
scoreboard players set #nbtsmelting.entity.found_block peerheer.global 1

# Summon marker entity.
function peerheer.nbtsmelting:marker/summon/smoker_marker
