# Author: PeerHeer
#
# Finds recipes applicable to the current input and output items.

# Initialize the recipe ID to -1.
scoreboard players set #nbtsmelt.recipe.id nbtsmelt.var -1

# Copy input and output slots into storage.
data modify storage nbtsmelt:furnace_inv CheckRecipes set value []
data modify storage nbtsmelt:furnace_inv CheckRecipes append from block ~ ~ ~ Items[{Slot:0b}]
data modify storage nbtsmelt:furnace_inv CheckRecipes append from block ~ ~ ~ Items[{Slot:2b}]

# Check recipes using the predicate entity.
execute unless entity 0-24e1-1d91-0-4954143 run function nbtsmelt:summon/predicate_entity
execute as 0-24e1-1d91-0-4954143 run function nbtsmelt:smelting/furnace/get_recipe/check_recipes/check_recipes_start


# Execute functions depending on whether a recipe is found.
execute unless score #nbtsmelt.recipe.id nbtsmelt.var matches 0.. run function nbtsmelt:smelting/furnace/get_recipe/recipe_not_found
execute if score #nbtsmelt.recipe.id nbtsmelt.var matches 0.. run function nbtsmelt:smelting/furnace/get_recipe/found_recipe