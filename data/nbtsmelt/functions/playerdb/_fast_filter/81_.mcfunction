# By: shraavan97
# 19 Nov 2019
#
#> Filters list, split @ 3**8

execute if score $uid nbtsmelt.temp matches 81..6560 run function nbtsmelt:playerdb/_fast_filter/81_6560
execute if score $uid nbtsmelt.temp matches 6561.. run function nbtsmelt:playerdb/_fast_filter/6561_