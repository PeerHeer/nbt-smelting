# By: shraavan97
# 17 Nov 2019
#
#> Save data

execute if data storage nbtsmelt:playerdb.output root.player run data modify storage nbtsmelt:playerdb.output root.leftover append from storage nbtsmelt:playerdb.output root.player
data modify storage nbtsmelt:playerdb.global root.players set from storage nbtsmelt:playerdb.output root.leftover

data modify storage nbtsmelt:playerdb.output root.leftover set value []
data modify storage nbtsmelt:playerdb.output root.player set value {}
