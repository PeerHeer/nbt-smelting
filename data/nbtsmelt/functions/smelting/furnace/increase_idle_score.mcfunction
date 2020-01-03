scoreboard players add @s nbtsmelt.idle 1
execute if score @s nbtsmelt.idle matches 10 run function nbtsmelt:smelting/furnace/reset_idle_score