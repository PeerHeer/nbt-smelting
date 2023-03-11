# Compare to previous item. If same item and no recipe, stop checks.
# Else, look up the item in the recipe list.
# Finally, store current item in storage along with relevant scores.

# Clear storage.
data remove storage peerheer.nbtsmelting:storage PreviousInputItemBlock
data remove storage peerheer.nbtsmelting:storage PreviousInputItemEntity

# Copy item data from block to storage.
data modify storage peerheer.nbtsmelting:storage PreviousInputItemBlock set from block ~ ~ ~ Items[{Slot:0b}]
data modify storage peerheer.nbtsmelting:storage PreviousInputItemBlock.Count set value 0b

# Copy item data from entity to storage.
data modify storage peerheer.nbtsmelting:storage PreviousInputItemEntity set from entity @s data.PreviousInputItem

# Compare item data.
execute store success score #nbtsmelting.storage.compare_input_item peerheer.global run data modify storage peerheer.nbtsmelting:storage PreviousInputItemEntity set from storage peerheer.nbtsmelting:storage PreviousInputItemBlock

# If the item is the same, skip the recipe lookup step.
execute if score #nbtsmelting.storage.compare_input_item peerheer.global matches 0 run say SAME ITEM!

# Look up the recipe if the items are not the same.
execute if score #nbtsmelting.storage.compare_input_item peerheer.global matches 1 run say Look Up Recipe!

# Copy item from input slot into entity data.
data modify entity @s data.PreviousInputItem set from storage peerheer.nbtsmelting:storage PreviousInputItemBlock
