# By: shraavan97
# 14 Nov 2019
#
#> Resets DB. Called from minecraft:load

data modify storage nbtsmelt:playerdb.global root set value {}
data modify storage nbtsmelt:playerdb.output root set value {}
data modify storage nbtsmelt:playerdb.temp root set value {}
