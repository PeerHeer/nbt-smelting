# Author: PeerHeer
#
# Compares the ID and tag to the ID and tag of the previous check.

# Place the ID and tag into storage.
data modify storage nbtsmelt:furnace_inv Temp set value {}
data modify storage nbtsmelt:furnace_inv Temp.id set from block ~ ~ ~ Items[{Slot:0b}].id
data modify storage nbtsmelt:furnace_inv Temp.tag set from block ~ ~ ~ Items[{Slot:0b}].tag

# Let a sign resolve the NBT.
data modify block -29999995 0 8005 Text1 set value '{"nbt":"Temp","storage":"nbtsmelt:furnace_inv"}'

# Copy it into the CustoName of the marker and store the success of the operation.
execute store success score #nbtsmelt.smelting.not_same_id nbtsmelt.var run data modify entity @s CustomName set from block -29999995 0 8005 Text1

# If the ID and tag are not the same, check for new recipes.
execute if score #nbtsmelt.smelting.not_same_id nbtsmelt.var matches 1 run function nbtsmelt:smelting/furnace/get_recipe/check_recipes

# If the ID and tag are the same, handle BurnTime and CookTime.
execute if score #nbtsmelt.smelting.not_same_id nbtsmelt.var matches 0 if entity @s[tag=nbtsmelt.marker.busy] run function nbtsmelt:smelting/furnace/smelt/burntime/check_burntime