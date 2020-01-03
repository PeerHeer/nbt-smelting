# Author: PeerHeer
#
# Removes fuel and sets the BurnTime.

# Get the amount of BurnTime to be set.
function nbtsmelt:smelting/furnace/smelt/burntime/check_entity

# Check the fuel count.
execute store result score #nbtsmelt.smelting.fuel.count nbtsmelt.var run data get block ~ ~ ~ Items[{Slot:1b}].Count

# If one piece of fuel is left, remove the whole item.
execute if score #nbtsmelt.smelting.fuel.count nbtsmelt.var matches 1 run function nbtsmelt:smelting/furnace/smelt/fuel/remove_all_fuel

# If more than one piece of fuel is left, remove one from the Count.
execute if score #nbtsmelt.smelting.fuel.count nbtsmelt.var matches 2.. run function nbtsmelt:smelting/furnace/smelt/fuel/remove_one_fuel

# Put the furnace in a lit blockstate.
function nbtsmelt:smelting/furnace/smelt/set_lit

# Set the BurnTime.
execute store result block ~ ~ ~ BurnTime short 1 run scoreboard players get #nbtsmelt.smelting.burntime nbtsmelt.var


