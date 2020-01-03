# Author: PeerHeer
#
# Sets the ID and tag to the CustomName of the marker.

# Place the ID and tag into storage.
data modify storage nbtsmelt:furnace_inv Temp set value {}
data modify storage nbtsmelt:furnace_inv Temp.id set from block ~ ~ ~ Items[{Slot:0b}].id
data modify storage nbtsmelt:furnace_inv Temp.tag set from block ~ ~ ~ Items[{Slot:0b}].tag

# Let a sign resolve the NBT.
data modify block -29999995 0 8005 Text1 set value '{"nbt":"Temp","storage":"nbtsmelt:furnace_inv"}'

# Copy it into the CustoName of the marker.
data modify entity @s CustomName set from block -29999995 0 8005 Text1

# Check for new recipes.
function nbtsmelt:smelting/furnace/get_recipe/check_recipes