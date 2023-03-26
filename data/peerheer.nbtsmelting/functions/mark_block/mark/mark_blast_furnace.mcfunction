#> peerheer.nbtsmelting:mark_block/mark/mark_blast_furnace
#>
#> Author:
#>    PeerHeer (https://github.com/PeerHeer)
#>
#> Description:
#>    Mark a blast furnace by summoning the marker entity.

# Signal that a block has been found.
scoreboard players set #nbtsmelting.entity.found_block peerheer.global 1

# Summon marker entity.
function peerheer.nbtsmelting:marker/summon/blast_furnace_marker
