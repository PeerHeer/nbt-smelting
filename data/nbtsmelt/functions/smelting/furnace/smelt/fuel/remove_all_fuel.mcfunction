# Author: PeerHeer
#
# Removes all fuel from the furnace.

# Check if the fuel is a lava bucket.
execute store success score #nbtsmelt.smelting.fuel.is_lava nbtsmelt.var if data block ~ ~ ~ Items[{Slot:1b, id:"minecraft:lava_bucket"}]

# If the fuel is a lava bucket, replace it with a normal bucket.
execute if score #nbtsmelt.smelting.fuel.is_lava nbtsmelt.var matches 1 run data modify block ~ ~ ~ Items[{Slot:1b}].id set value "minecraft:bucket"

# If the fuel is not a lava bucket, remove the entire fuel slot.
execute if score #nbtsmelt.smelting.fuel.is_lava nbtsmelt.var matches 0 run data remove block ~ ~ ~ Items[{Slot:1b}]

