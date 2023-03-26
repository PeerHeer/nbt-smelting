#> peerheer.nbtsmelting:marker/setup/shared/add_tags
#>
#> Author:
#>    PeerHeer (https://github.com/PeerHeer)
#>
#> Description:
#>    Add tags to the marker when summoned.

# Global ignore tag, tells other datapacks not to interact with this entity.
tag @s add global.ignore
# Tag used to identify that the marker belongs to the NBT Smelting datapack.
tag @s add peerheer.nbtsmelting.entity.marker
# Summoned markers start in the idle state.
tag @s add peerheer.nbtsmelting.entity.marker.state.idle
