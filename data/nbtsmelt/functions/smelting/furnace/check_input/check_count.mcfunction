# Author: PeerHeer
#
# Checks if the count of input and/or output items differ from the previous check.

# Compare the count of the input item.
scoreboard players set #nbtsmelt.smelting.input.same_count nbtsmelt.var 0
execute store result score #nbtsmelt.smelting.input.count nbtsmelt.var run data get block ~ ~ ~ Items[{Slot:0b}].Count
execute if score @s nbtsmelt.count = #nbtsmelt.smelting.input.count nbtsmelt.var run scoreboard players set #nbtsmelt.smelting.input.same_count nbtsmelt.var 1
scoreboard players operation @s nbtsmelt.count = #nbtsmelt.smelting.input.count nbtsmelt.var

# Compare the count of the output item.
scoreboard players set #nbtsmelt.smelting.output.same_count nbtsmelt.var 0
scoreboard players set #nbtsmelt.smelting.output.count nbtsmelt.var 0
execute store result score #nbtsmelt.smelting.output.count nbtsmelt.var run data get block ~ ~ ~ Items[{Slot:2b}].Count
execute if score @s nbtsmelt.out = #nbtsmelt.smelting.output.count nbtsmelt.var run scoreboard players set #nbtsmelt.smelting.output.same_count nbtsmelt.var 1
scoreboard players operation @s nbtsmelt.out = #nbtsmelt.smelting.output.count nbtsmelt.var

# If the count of the input item differs, edit the CustomName of the marker and search for a recipe.
execute if score #nbtsmelt.smelting.input.same_count nbtsmelt.var matches 0 run function nbtsmelt:smelting/furnace/check_input/set_id_to_customname

# If the count of output differs, edit the CustomName of the marker and search for a recipe.
execute if score #nbtsmelt.smelting.input.same_count nbtsmelt.var matches 1 if score #nbtsmelt.smelting.output.same_count nbtsmelt.var matches 0 run function nbtsmelt:smelting/furnace/check_input/set_id_to_customname

# If the count of input and output does not differ, check if the ID differs.
execute if score #nbtsmelt.smelting.input.same_count nbtsmelt.var matches 1 if score #nbtsmelt.smelting.output.same_count nbtsmelt.var matches 1 run function nbtsmelt:smelting/furnace/check_input/check_id
