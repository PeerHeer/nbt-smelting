# By: shraavan97
# 20 Nov 2019
#
#> Iter

# tellraw
tellraw @s [{"nbt":"root.players[-1].uid", "storage":"nbtsmelt:playerdb.global", "color": "gold"}, {"text": ": "}, {"nbt":"root.players[-1].Recipe.ID", "storage":"nbtsmelt:playerdb.global", "color": "dark_aqua"}]

# iterate list
data modify storage nbtsmelt:playerdb.global root.players prepend from storage nbtsmelt:playerdb.global root.players[-1]
data remove storage nbtsmelt:playerdb.global root.players[-1]

# ensure we don't over iterate
scoreboard players remove $size nbtsmelt.temp 1
execute if score $size nbtsmelt.temp matches 1.. run function nbtsmelt:playerdb/_list_iter
