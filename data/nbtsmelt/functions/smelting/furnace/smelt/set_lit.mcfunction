# Author: PeerHeer
#
# Changes the blockstate of the furnace to lit.

# Copy all of the furnace NBT to storage.
data modify storage nbtsmelt:furnace_inv Furnace set from block ~ ~ ~ {}

# Set a lit furnace.
execute if block ~ ~ ~ minecraft:furnace[facing=north] run setblock ~ ~ ~ minecraft:furnace[facing=north, lit=true] replace
execute if block ~ ~ ~ minecraft:furnace[facing=east] run setblock ~ ~ ~ minecraft:furnace[facing=east, lit=true] replace
execute if block ~ ~ ~ minecraft:furnace[facing=south] run setblock ~ ~ ~ minecraft:furnace[facing=south, lit=true] replace
execute if block ~ ~ ~ minecraft:furnace[facing=west] run setblock ~ ~ ~ minecraft:furnace[facing=west, lit=true] replace

# Copy the furnace NBT back from storage into the block.
data modify block ~ ~ ~ {} merge from storage nbtsmelt:furnace_inv Furnace
