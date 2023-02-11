#> peerheer.nbtsmelting:states/checking/found_hopper_dropper/found_input_hopper_dropper
#
# Author: PeerHeer
#
# Called when a hopper or dropper faces into the top of the block.
# Sets a tag to save this state and signals that there is a hopper or dropper going into the input slot.

# Set tag.
tag @s add peerheer.nbtsmelting.entity.marker.input_hopper_dropper

# Signal that there is a hopper or dropper facing into the input slot.
scoreboard players set #nbtsmelting.entity.found_input_hopper_dropper peerheer.global 1
