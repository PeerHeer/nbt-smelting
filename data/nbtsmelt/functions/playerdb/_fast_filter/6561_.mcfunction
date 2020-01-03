# By: shraavan97
# 19 Nov 2019
#
#> Filters list, split @ 3**13

execute if score $uid nbtsmelt.temp matches 6561..1594322 run function nbtsmelt:playerdb/_fast_filter/6561_1594322
execute if score $uid nbtsmelt.temp matches 1594323.. run function nbtsmelt:playerdb/_fast_filter/1594323_