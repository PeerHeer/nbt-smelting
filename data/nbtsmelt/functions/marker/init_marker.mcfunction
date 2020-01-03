# Author: PeerHeer
#
# Initialize the marker entity.

# Assign a unique ID to the marker.
scoreboard players operation @s nbtsmelt.id = #nbtsmelt.marker.id.increment nbtsmelt.id
scoreboard players add #nbtsmelt.marker.id.increment nbtsmelt.id 1

# Initialize scores.
# CookTime
scoreboard players set @s nbtsmelt.cook 0
# Output item Count
scoreboard players set @s nbtsmelt.out 0
# RecipeLocation/Amount index
scoreboard players set @s nbtsmelt.stored -1
