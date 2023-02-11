#> peerheer.nbtsmelting:states/checking/change_state_to_checking
#
# Author: PeerHeer
#
# Change to the CHECKING state by removing all other state tags and adding the CHECKING state tag.

tag @s remove peerheer.nbtsmelting.entity.marker.state.idle
tag @s remove peerheer.nbtsmelting.entity.marker.state.smelting
tag @s add peerheer.nbtsmelting.entity.marker.state.checking

say Change to CHECKING!