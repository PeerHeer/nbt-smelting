# Author: PeerHeer
#
# Changes the item in the output slot from nothing to the right item.

# Append a dummy item to the Items list.
data modify block ~ ~ ~ Items append value {Slot:2b, id:"minecraft:stone", Count:1b}

# Put the appropriate id and tag into the item.
data modify block ~ ~ ~ Items[{Slot:2b}].id set from storage nbtsmelt:playerdb.output root.player.Recipe.Output.Item.id
data modify block ~ ~ ~ Items[{Slot:2b}].tag set from storage nbtsmelt:playerdb.output root.player.Recipe.Output.Item.tag