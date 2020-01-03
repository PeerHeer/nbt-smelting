# Author: PeerHeer
#
# Check if the furnace still has BurnTime left.

# Check block data.
execute store success score #nbtsmelt.smelting.not_burning nbtsmelt.var if data block ~ ~ ~ {BurnTime:0s}


# If the furnace is not burning, check if there is any fuel in the furnace.
execute if score #nbtsmelt.smelting.not_burning nbtsmelt.var matches 1 run function nbtsmelt:smelting/furnace/check_if_fuel

# If the furnace is burning, check if the count of items has changed since the last check.
execute if score #nbtsmelt.smelting.not_burning nbtsmelt.var matches 0 run function nbtsmelt:smelting/furnace/check_input/check_count