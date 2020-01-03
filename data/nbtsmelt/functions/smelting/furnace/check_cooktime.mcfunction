# Author: PeerHeer
#
# Reduces the cooktime of the marker according to the block CookTime.

#function nbtsmelt:smelting/furnace/reduce_cooktime
#function nbtsmelt:smelting/furnace/reset_cooktime
execute store result score @s nbtsmelt.cook run data get block ~ ~ ~ CookTime
