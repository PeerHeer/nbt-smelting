# Author: PeerHeer
#
# Outputs an item into the output slot.
# Changes the count of the input slot and output slot.

# Reset CookTime of the marker and the furnace.
scoreboard players set @s nbtsmelt.cook 0
data modify block ~ ~ ~ CookTime set value 0s

# Get the recipe from the database.
scoreboard players operation $in.uid nbtsmelt.io = @s nbtsmelt.recipe
function nbtsmelt:playerdb/fast_get

# Calculate the new count of the input item.
scoreboard players operation #nbtsmelt.smelting.new_count nbtsmelt.var = @s nbtsmelt.count
execute store result score #nbtsmelt.recipe.input.count nbtsmelt.var run data get storage nbtsmelt:playerdb.output root.player.Recipe.Input.Count
scoreboard players operation #nbtsmelt.smelting.new_count nbtsmelt.var -= #nbtsmelt.recipe.input.count nbtsmelt.var
# If the new count is 0, remove the whole slot.
execute if score #nbtsmelt.smelting.new_count nbtsmelt.var matches 0 run data remove block ~ ~ ~ Items[{Slot:0b}]
# If the new count > 0, store into the Count of the input slot.
execute if score #nbtsmelt.smelting.new_count nbtsmelt.var matches 1.. store result block ~ ~ ~ Items[{Slot:0b}].Count byte 1 run scoreboard players get #nbtsmelt.smelting.new_count nbtsmelt.var

# Calculate the new count of the output item.
execute store result score #nbtsmelt.smelting.old_count nbtsmelt.var run data get block ~ ~ ~ Items[{Slot:2b}].Count
scoreboard players operation #nbtsmelt.smelting.new_count nbtsmelt.var = #nbtsmelt.smelting.old_count nbtsmelt.var
execute store result score #nbtsmelt.recipe.output.count nbtsmelt.var run data get storage nbtsmelt:playerdb.output root.player.Recipe.Output.Count
scoreboard players operation #nbtsmelt.smelting.new_count nbtsmelt.var += #nbtsmelt.recipe.output.count nbtsmelt.var
# If the old output count was 0, a new item is put inside the output slot.
execute if score #nbtsmelt.smelting.old_count nbtsmelt.var matches 0 run function nbtsmelt:smelting/furnace/smelt/output/change_output_item
# If the new count > 2, store it into the output slot Count.
execute if score #nbtsmelt.smelting.new_count nbtsmelt.var matches 2.. store result block ~ ~ ~ Items[{Slot:2b}].Count byte 1 run scoreboard players get #nbtsmelt.smelting.new_count nbtsmelt.var

# Handle dummy recipes for giving experience.
function nbtsmelt:smelting/furnace/smelt/experience/check_current