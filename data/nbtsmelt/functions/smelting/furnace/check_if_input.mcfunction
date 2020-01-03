# Author: PeerHeer
#
# Checks if there is input in Slot0 of the furnace.

# Initialize variables.
scoreboard players set #nbtsmelt.smelting.has_cooktime nbtsmelt.var 0
scoreboard players set #nbtsmelt.success nbtsmelt.var 0

# Check if the first slot is occupied.
execute store success score #nbtsmelt.success nbtsmelt.var store success score #nbtsmelt.smelting.has_input nbtsmelt.var if data block ~ ~ ~ Items[{Slot:0b}]

# If Slot0 is occupied, check for BurnTime.
execute if score #nbtsmelt.success nbtsmelt.var matches 1 run function nbtsmelt:smelting/furnace/check_if_burntime

# If Slot0 is not occupied, reset variables.
execute if score #nbtsmelt.smelting.has_input nbtsmelt.var matches 0 run scoreboard players set @s nbtsmelt.count 0
execute if score #nbtsmelt.smelting.has_input nbtsmelt.var matches 0 run scoreboard players set @s nbtsmelt.cook 0

# If Slot0 is not occupied or there is no fuel, make the furnace idle.
execute if score #nbtsmelt.success nbtsmelt.var matches 0 run function nbtsmelt:marker/make_idle

# If there is still CookTime left, make the furnace busy.
execute if score #nbtsmelt.smelting.has_cooktime nbtsmelt.var matches 1 run function nbtsmelt:marker/make_busy

# Kills marker when no furnace is at its block.
execute unless block ~ ~ ~ minecraft:furnace run kill @s