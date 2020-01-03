# Author: PeerHeer
#
# Removes fuel and sets the BurnTime.

# Put the ID of the fuel in storage.
data modify storage nbtsmelt:furnace_inv Fuel.id set from block ~ ~ ~ Items[{Slot:1b}].id

# Check if the predicate entity exists. If not, summon it.
execute unless entity 0-24e1-1d91-0-4954143 run function nbtsmelt:summon/predicate_entity

# Get the BurnTime to be set.
execute as 0-24e1-1d91-0-4954143 run function nbtsmelt:smelting/furnace/smelt/burntime/get_burntime