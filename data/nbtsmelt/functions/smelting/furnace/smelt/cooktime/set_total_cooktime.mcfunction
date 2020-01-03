# Author: PeerHeer
#
# Sets the CookTimeTotal.

# Get the recipe from the database.
scoreboard players operation $in.uid nbtsmelt.io = @s nbtsmelt.recipe
function nbtsmelt:playerdb/fast_get

# Store the total cooktime in the block and in a score.
data modify block ~ ~ ~ CookTimeTotal set from storage nbtsmelt:playerdb.output root.player.Recipe.CookingTime
execute store result score @s nbtsmelt.cttotal run data get storage nbtsmelt:playerdb.output root.player.Recipe.CookingTime