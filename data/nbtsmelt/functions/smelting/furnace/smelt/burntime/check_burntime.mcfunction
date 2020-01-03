# Author: PeerHeer
#
# Removes fuel if the furnace is not yet burning. Then check the current CookTime.

function nbtsmelt:marker/make_busy
execute if score #nbtsmelt.smelting.not_burning nbtsmelt.var matches 1 run function nbtsmelt:smelting/furnace/smelt/fuel/remove_fuel
function nbtsmelt:smelting/furnace/smelt/cooktime/check_cooktime