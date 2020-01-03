# By: shraavan97
# 18 Nov 2019


scoreboard players operation $bit nbtsmelt.temp = $uid nbtsmelt.temp
scoreboard players operation $bit nbtsmelt.temp %= $3 nbtsmelt.int
execute if score $bit nbtsmelt.temp matches 0 run data modify storage nbtsmelt:playerdb.temp root.filtered9 append from storage nbtsmelt:playerdb.temp root.filtered8[{bit9:0b}]
execute if score $bit nbtsmelt.temp matches 0 run data modify storage nbtsmelt:playerdb.temp root.leftover append from storage nbtsmelt:playerdb.temp root.filtered8[{bit9:1b}]
execute if score $bit nbtsmelt.temp matches 0 run data modify storage nbtsmelt:playerdb.temp root.leftover append from storage nbtsmelt:playerdb.temp root.filtered8[{bit9:2b}]
execute if score $bit nbtsmelt.temp matches 1 run data modify storage nbtsmelt:playerdb.temp root.filtered9 append from storage nbtsmelt:playerdb.temp root.filtered8[{bit9:1b}]
execute if score $bit nbtsmelt.temp matches 1 run data modify storage nbtsmelt:playerdb.temp root.leftover append from storage nbtsmelt:playerdb.temp root.filtered8[{bit9:0b}]
execute if score $bit nbtsmelt.temp matches 1 run data modify storage nbtsmelt:playerdb.temp root.leftover append from storage nbtsmelt:playerdb.temp root.filtered8[{bit9:2b}]
execute if score $bit nbtsmelt.temp matches 2 run data modify storage nbtsmelt:playerdb.temp root.filtered9 append from storage nbtsmelt:playerdb.temp root.filtered8[{bit9:2b}]
execute if score $bit nbtsmelt.temp matches 2 run data modify storage nbtsmelt:playerdb.temp root.leftover append from storage nbtsmelt:playerdb.temp root.filtered8[{bit9:0b}]
execute if score $bit nbtsmelt.temp matches 2 run data modify storage nbtsmelt:playerdb.temp root.leftover append from storage nbtsmelt:playerdb.temp root.filtered8[{bit9:1b}]
scoreboard players operation $uid nbtsmelt.temp /= $3 nbtsmelt.int
execute store result score $size nbtsmelt.temp if data storage nbtsmelt:playerdb.temp root.filtered9[]
execute if score $size nbtsmelt.temp matches 0..1 run data modify storage nbtsmelt:playerdb.output root.player set from storage nbtsmelt:playerdb.temp root.filtered9[0]
execute if score $size nbtsmelt.temp matches 2.. run function nbtsmelt:playerdb/_get/bit10