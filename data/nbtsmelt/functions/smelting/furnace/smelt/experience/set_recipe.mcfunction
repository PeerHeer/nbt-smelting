# Author: PeerHeer
#
# Creates a new entry for RecipeUsed.

# If there are no recipes yet, modify the block and set the RecipesUsedSize to 1.
execute if score #nbtsmelt.recipe.stored.used_size nbtsmelt.const matches 0 run function nbtsmelt:smelting/furnace/smelt/experience/set/modify_block
# If there are already recipes, merge data with the block and do not modify RecipesUsedSize.
execute if score #nbtsmelt.recipe.stored.used_size nbtsmelt.const matches 1.. run function nbtsmelt:smelting/furnace/smelt/experience/set/merge_block