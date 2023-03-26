#> peerheer.nbtsmelting:marker/setup/setup_furnace
#>
#> Author:
#>    PeerHeer (https://github.com/PeerHeer)
#>
#> Description:
#>    Set up the furnace marker for operation.

# Add furnace tag.
tag @s add peerheer.nbtsmelting.entity.marker.block.furnace

# Set custon name, used for debugging.
data modify entity @s CustomName set value '{"text":"peerheer.nbtsmelting.entity.marker.block.furnace"}'

# Execute shared setup procedure.
function peerheer.nbtsmelting:marker/setup/shared/setup_shared
