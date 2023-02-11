#> peerheer.nbtsmelting:mark_block/mark/mark_furnace
#
# Author: PeerHeer
#
# Signals that the block was found and marks it with a marker entity.

# Signal that a block has been found.
scoreboard players set #nbtsmelting.entity.found_block peerheer.global 1

# Summon marker entity.
function peerheer.nbtsmelting:marker/summon/furnace_marker
