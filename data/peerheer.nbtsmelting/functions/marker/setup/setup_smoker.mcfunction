#> peerheer.nbtsmelting:marker/setup/setup_smoker
#>
#> Author:
#>    PeerHeer (https://github.com/PeerHeer)
#>
#> Description:
#>    Set up the smoker marker for operation.

# Add smoker tag.
tag @s add peerheer.nbtsmelting.entity.marker.block.smoker

# Set custon name, used for debugging.
data modify entity @s CustomName set value '{"text":"peerheer.nbtsmelting.entity.marker.block.smoker"}'

# Execute shared setup procedure.
function peerheer.nbtsmelting:marker/setup/shared/setup_shared
