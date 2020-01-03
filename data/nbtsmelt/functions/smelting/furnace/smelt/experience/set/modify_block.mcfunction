# Author: PeerHeer
#
# Modify the block and set the RecipesUsedSize to 1.

data modify storage nbtsmelt:furnace_recipes StoredRecipe set value {RecipeAmount0:1, RecipeLocation0:"", RecipesUsedSize:1s}
data modify storage nbtsmelt:furnace_recipes StoredRecipe.RecipeLocation0 set from storage nbtsmelt:furnace_recipes Temp.ExperienceRecipe
data modify block ~ ~ ~ {} merge from storage nbtsmelt:furnace_recipes StoredRecipe