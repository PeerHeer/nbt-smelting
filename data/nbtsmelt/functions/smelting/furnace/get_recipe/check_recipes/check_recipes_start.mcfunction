# Author: PeerHeer
#
# Gets the recipe based on input and output items.

# Copy the input and output items to the HandItems of the predicate entity.
data modify entity @s HandItems set from storage nbtsmelt:furnace_inv CheckRecipes

# Initialize variables.
execute store result score #nbtsmelt.recipe.id.length nbtsmelt.var run data get storage nbtsmelt:furnace_inv CheckRecipes[0].id
scoreboard players set #nbtsmelt.recipe.tag.max_length nbtsmelt.var 0

# Traverse function tree to find the right recipe.
execute if score #nbtsmelt.recipe.id.length nbtsmelt.var matches 13..26 run function nbtsmelt:smelting/furnace/get_recipe/get_length/13_26
execute if score #nbtsmelt.recipe.id.length nbtsmelt.var matches 27..40 run function nbtsmelt:smelting/furnace/get_recipe/get_length/27_40