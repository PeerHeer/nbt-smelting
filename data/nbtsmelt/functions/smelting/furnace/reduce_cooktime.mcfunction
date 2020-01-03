scoreboard players remove @s nbtsmelt.cook 2
execute if score @s nbtsmelt.cook matches ..-1 run scoreboard players set @s nbtsmelt.cook 0
scoreboard players set #nbtsmelt.smelting.has_cooktime nbtsmelt.var 1