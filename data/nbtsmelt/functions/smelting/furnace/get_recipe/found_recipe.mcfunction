# Author: PeerHeer
#
# Triggered when a recipe is found.

# Set success to 1.
scoreboard players set #nbtsmelt.success nbtsmelt.var 1

# Reset the CookTime of the entity if the recipe changed.
execute unless score #nbtsmelt.recipe.id nbtsmelt.var = @s nbtsmelt.recipe run scoreboard players set @s nbtsmelt.cook 0

# Set the new recipe equal to the ID of the recipe that was found.
scoreboard players operation @s nbtsmelt.recipe = #nbtsmelt.recipe.id nbtsmelt.var

# Add/remove tags.
function nbtsmelt:marker/make_busy
tag @s add nbtsmelt.marker.recipe
tag @s remove nbtsmelt.marker.no_recipe

# Check the BurnTime in the furnace and handle CookTime.
function nbtsmelt:smelting/furnace/smelt/burntime/check_burntime