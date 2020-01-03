# Author: PeerHeer
#
# Checks all idle furnaces every 5 ticks.

# Check all idle furnaces.
execute as @e[tag=nbtsmelt.furnace_marker, tag=nbtsmelt.marker.idle] at @s run function nbtsmelt:smelting/furnace/check_if_input

# Reschedule function.
schedule function nbtsmelt:smelting/furnace/idle_check 5t