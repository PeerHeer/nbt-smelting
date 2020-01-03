# By: shraavan97
# 17 Nov 2019
#
#> Get Data: Output in nbtsmelt:playerdb.output out.player

#define entity @s
#

scoreboard players operation $uid nbtsmelt.temp = $in.uid nbtsmelt.io

function nbtsmelt:playerdb/filter
function nbtsmelt:playerdb/_get/bit0

execute store result score $uid nbtsmelt.temp run data get storage nbtsmelt:playerdb.output root.player.uid
execute unless score $uid nbtsmelt.temp = $in.uid nbtsmelt.io run data modify storage nbtsmelt:playerdb.output root.player set value {}
data modify storage nbtsmelt:playerdb.output root.leftover set value []
execute if data storage nbtsmelt:playerdb.temp root.leftover run data modify storage nbtsmelt:playerdb.output root.leftover set from storage nbtsmelt:playerdb.temp root.leftover
data modify storage nbtsmelt:playerdb.temp root set value {}
