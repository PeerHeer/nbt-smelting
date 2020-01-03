# By: shraavan97
# 24 Nov 2019
#
#> Lists all players...

tellraw @s [{"text":"UID: ", "color": "gold", "bold": "true"}, {"text": "RecipeID", "color":"dark_aqua"}]
execute store result score $size nbtsmelt.temp if data storage nbtsmelt:playerdb.global root.players[]
execute if score $size nbtsmelt.temp matches 1.. run function nbtsmelt:playerdb/_list_iter
