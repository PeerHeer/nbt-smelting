# By: shraavan97
# 14 Nov 2019
#
# Modified by: PeerHeer
#
# Put a recipe in the PlayerDB.

# Put the entry inside the PlayerDB.
data modify storage nbtsmelt:playerdb.global root.players append value {}
execute store result storage nbtsmelt:playerdb.global root.players[-1].uid int 1 run scoreboard players get #nbtsmelt.recipe.id nbtsmelt.var
data modify storage nbtsmelt:playerdb.global root.players[-1].Recipe set from storage nbtsmelt:furnace_recipes Temp

# Convert UID to bits.
scoreboard players operation $uid nbtsmelt.temp = #nbtsmelt.recipe.id nbtsmelt.var
function nbtsmelt:playerdb/uid_to_bits
