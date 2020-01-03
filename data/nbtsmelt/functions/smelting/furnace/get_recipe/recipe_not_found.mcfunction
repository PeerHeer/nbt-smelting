# Author: PeerHeer
#
# Triggered when no recipe corresponds to the inputs in the furnace.

# Set success to 1.
scoreboard players set #nbtsmelt.success nbtsmelt.var 0

# Reset the recipe ID.
scoreboard players set @s nbtsmelt.recipe -1

# Add/remove tags.
function nbtsmelt:marker/make_idle
tag @s remove nbtsmelt.marker.recipe
tag @s add nbtsmelt.marker.no_recipe

# Reset the CookTime of the marker entity.
scoreboard players set @s nbtsmelt.cook 0