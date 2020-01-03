# Author: PeerHeer
#
# Triggers when a furnace is placed.
# Calls check_coords/furnace/coords0.mcfunction to check surrounding coordinates.

# Revoke advancement.
advancement revoke @s only nbtsmelt:furnace_placed

# Initialize found_furnace.
scoreboard players set #nbtsmelt.found_furnace nbtsmelt.var 0

# Check surrounding coordinates.
function nbtsmelt:check_coords/furnace/coords0