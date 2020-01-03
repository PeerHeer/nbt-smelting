# Author: PeerHeer
#
# Marks the found furnace block with an entity.

# Set found_furnace to true to halt the search.
scoreboard players set #nbtsmelt.found_furnace nbtsmelt.var 1

# Summon marker.
function nbtsmelt:summon/furnace_marker

# Initialize the marker.
execute as @e[distance=..0.01, tag=nbtsmelt.furnace_marker, limit=1] run function nbtsmelt:marker/init_marker