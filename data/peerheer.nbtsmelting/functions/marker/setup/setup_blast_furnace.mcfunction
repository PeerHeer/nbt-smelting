#> peerheer.nbtsmelting:marker/setup/setup_blast_furnace
#>
#> Author:
#>    PeerHeer (https://github.com/PeerHeer)
#>
#> Description:
#>    Set up the blast furnace marker for operation.

# Add blast furnace tag.
tag @s add peerheer.nbtsmelting.entity.marker.block.blast_furnace

# Set custom name, used for debugging.
data modify entity @s CustomName set value '{"text":"peerheer.nbtsmelting.entity.marker.block.blast_furnace"}'

# Execute shared setup procedure.
function peerheer.nbtsmelting:marker/setup/shared/setup_shared
