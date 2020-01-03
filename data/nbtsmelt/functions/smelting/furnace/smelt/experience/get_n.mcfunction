# Author: PeerHeer
#
# Gets the new RecipesUsed index.

# Var is decreased by one per index. Const is the final index.
scoreboard players operation #nbtsmelt.recipe.stored.used_size nbtsmelt.var = #nbtsmelt.recipe.stored.used_size nbtsmelt.const

# Copy the ExperienceRecipe to Temp.
data modify storage nbtsmelt:furnace_recipes Temp.ExperienceRecipe set from storage nbtsmelt:playerdb.output root.player.Recipe.ExperienceRecipe

# Start checking at index 0 and continue until the RecipesUsedSize is reached.
execute if score #nbtsmelt.recipe.stored.used_size nbtsmelt.var matches 1.. run function nbtsmelt:smelting/furnace/smelt/experience/check/check_0

# Stores the new index in a score.
scoreboard players operation @s nbtsmelt.stored = #nbtsmelt.recipe.stored.used_size nbtsmelt.const

# If the recipe was not found, create a new RecipesUsed entry.
execute if score #nbtsmelt.recipe.location_not_equal nbtsmelt.var matches 1 run function nbtsmelt:smelting/furnace/smelt/experience/set_recipe