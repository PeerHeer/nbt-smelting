# Author: PeerHeer
#
# Merge data with the block and do not modify RecipesUsedSize.

data modify storage nbtsmelt:furnace_recipes StoredRecipe set value {RecipeAmount0:1, RecipeLocation0:""}
data modify storage nbtsmelt:furnace_recipes StoredRecipe.RecipeLocation0 set from storage nbtsmelt:furnace_recipes Temp.ExperienceRecipe
data modify block ~ ~ ~ {} merge from storage nbtsmelt:furnace_recipes StoredRecipe