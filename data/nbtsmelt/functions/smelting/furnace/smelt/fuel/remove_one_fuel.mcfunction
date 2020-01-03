# Author: PeerHeer
#
# Removes one from the fuel count.

scoreboard players remove #nbtsmelt.smelting.fuel.count nbtsmelt.var 1
execute store result block ~ ~ ~ Items[{Slot:1b}].Count byte 1 run scoreboard players get #nbtsmelt.smelting.fuel.count nbtsmelt.var

