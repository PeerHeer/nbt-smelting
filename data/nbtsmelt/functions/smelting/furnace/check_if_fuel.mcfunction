# Author: PeerHeer
#
# Checks if there is any fuel in Slot2 of the container.

# Get block data.
execute store success score #nbtsmelt.success nbtsmelt.var if data block ~ ~ ~ Items[{Slot:1b}]

# If the item is an empty bucket, counts as no fuel.
execute if data block ~ ~ ~ Items[{Slot:1b, id:"minecraft:bucket"}] run scoreboard players set #nbtsmelt.success nbtsmelt.var 0

# If there is no fuel in the furnace, check if it has any CookTime left.
execute if score #nbtsmelt.success nbtsmelt.var matches 0 if score @s nbtsmelt.cook matches 1.. run function nbtsmelt:smelting/furnace/check_cooktime

# If there is fuel in the furnace and the furnace has a recipe, check for a different recipe.
execute if score #nbtsmelt.success nbtsmelt.var matches 1 if entity @s[tag=nbtsmelt.marker.recipe] run function nbtsmelt:smelting/furnace/get_recipe/check_recipes

# If there is fuel in the furnace and the furnace has no recipe yet, check if the count of items has changed since the last check.
execute if score #nbtsmelt.success nbtsmelt.var matches 1 if entity @s[tag=nbtsmelt.marker.no_recipe] run function nbtsmelt:smelting/furnace/check_input/check_count

