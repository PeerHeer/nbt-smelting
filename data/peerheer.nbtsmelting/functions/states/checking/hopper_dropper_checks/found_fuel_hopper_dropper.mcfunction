#> peerheer.nbtsmelting:states/checking/found_hopper_dropper/found_fuel_hopper_dropper
#
# Author: PeerHeer
#
# Called when a hopper or dropper faces into a side or bottom of the block.
# Sets a tag to save this state and signals that there is a hopper or dropper going into the fuel slot.

# Set tag.
tag @s add peerheer.nbtsmelting.entity.marker.hopper_dropper
tag @s add peerheer.nbtsmelting.entity.marker.fuel_hopper_dropper

# Signal that there is a hopper or dropper facing into the fuel slot.
scoreboard players set #nbtsmelting.entity.found_fuel_hopper_dropper peerheer.global 1
