#> peerheer.nbtsmelting:marker/summon/furnace_marker
#>
#> Author:
#>    PeerHeer (https://github.com/PeerHeer)
#>
#> Description:
#>    Summon a furnace marker and set it up.

# Summon marker entity at block.
execute summon minecraft:marker at @s run function peerheer.nbtsmelting:marker/setup/setup_furnace
