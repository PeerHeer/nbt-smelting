# By: shraavan97
# 19 Nov 2019
#
#> Filters list, split @ 3**4

execute if score $uid nbtsmelt.temp matches ..80 run function nbtsmelt:playerdb/_fast_filter/1_80
execute if score $uid nbtsmelt.temp matches 81.. run function nbtsmelt:playerdb/_fast_filter/81_
