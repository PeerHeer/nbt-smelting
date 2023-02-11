#> peerheer.nbtsmelting:mark_block/advancements/furnace_placed
#
# Author: PeerHeer
#
# Called when a player places a furnace.
# Search for and mark the placed block.

# Revoke advancement.
advancement revoke @s only peerheer.nbtsmelting:block_placed/furnace_placed

# Initialise found_block score to 0.
# The score is set to 1 if the block is found.
scoreboard players set #nbtsmelting.entity.found_block peerheer.global 0

# Start searching for the placed block.
function peerheer.nbtsmelting:mark_block/find_block/furnace/coords0
