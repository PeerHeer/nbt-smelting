# Author: PeerHeer
#
# Checks the last used RecipesUsed index.

# Copy all the furnace NBT to storage.
data modify storage nbtsmelt:furnace_inv Furnace set from block ~ ~ ~ {}

# Get the ExperienceRecipe from the database.
data modify storage nbtsmelt:furnace_recipes Temp.ExperienceRecipe set from storage nbtsmelt:playerdb.output root.player.Recipe.ExperienceRecipe

# Get RecipesUsedSize.
execute store result score #nbtsmelt.recipe.stored.used_size nbtsmelt.const run data get storage nbtsmelt:furnace_inv Furnace.RecipesUsedSize

# Get the index that was used last time.
scoreboard players operation #nbtsmelt.recipe.stored.index nbtsmelt.var = @s nbtsmelt.stored

# Initialize location_not_equal to 1.
scoreboard players set #nbtsmelt.recipe.location_not_equal nbtsmelt.var 1

# If the last used index is within the RecipeUsedSize, check that index.
execute if score #nbtsmelt.recipe.stored.index nbtsmelt.var < #nbtsmelt.recipe.stored.used_size nbtsmelt.const run function nbtsmelt:smelting/furnace/smelt/experience/check_cache

# If the recipe was not found, get the new index.
execute if score #nbtsmelt.recipe.location_not_equal nbtsmelt.var matches 1 run function nbtsmelt:smelting/furnace/smelt/experience/get_n