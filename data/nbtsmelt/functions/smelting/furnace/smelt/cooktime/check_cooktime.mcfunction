# Author: PeerHeer
#
# Handles CookTime.

# If there is no cooktime yet, set the total cooktime for the recipe.
execute if score @s nbtsmelt.cook matches 0 run function nbtsmelt:smelting/furnace/smelt/cooktime/set_total_cooktime

# Add one to the cooktime.
scoreboard players add @s nbtsmelt.cook 1

# Store the new CookTime in the block.
execute store result block ~ ~ ~ CookTime short 1 run scoreboard players get @s nbtsmelt.cook

# If the CookTime exceeds the CookTimeTotal, output an item.
execute if score @s nbtsmelt.cook >= @s nbtsmelt.cttotal run function nbtsmelt:smelting/furnace/smelt/output/put_item