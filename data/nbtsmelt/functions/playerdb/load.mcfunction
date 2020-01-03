# By: shraavan97
# 14 Nov 2019
#
#> Creates Objs. Called from #minecraft:load

scoreboard objectives add nbtsmelt.uid dummy
scoreboard objectives add nbtsmelt.int dummy
scoreboard objectives add nbtsmelt.temp dummy
scoreboard objectives add nbtsmelt.io dummy

execute unless data storage nbtsmelt:playerdb.global root.players run data modify storage nbtsmelt:playerdb.global root.players set value []

scoreboard players set $2 nbtsmelt.int 2
scoreboard players set $3 nbtsmelt.int 3
