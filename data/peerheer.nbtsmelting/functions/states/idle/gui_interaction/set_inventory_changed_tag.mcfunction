#> peerheer.nbtsmelting:states/idle/gui_interaction/set_inventory_changed_tag
#>
#> Author:
#>    PeerHeer (https://github.com/PeerHeer)
#>
#> Description:
#>    Sets inventory_changed tags.

# Set has_player_inventory_changed_tag when the player already has the tag.
# Used to distinguish between a first-time trigger and subsequent triggers.
tag @s[tag=peerheer.nbtsmelting.entity.marker.player_inventory_changed] add peerheer.nbtsmelting.entity.marker.has_player_inventory_changed_tag

# Set inventory changed tag.
tag @s add peerheer.nbtsmelting.entity.marker.player_inventory_changed
