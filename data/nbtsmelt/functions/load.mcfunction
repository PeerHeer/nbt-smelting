# Author: PeerHeer
#
# Triggered on reload.
# Resets and refills the recipe database.
# Calls setup functions.

function #nbtsmelt:setup
function nbtsmelt:playerdb/load
function nbtsmelt:playerdb/reset
function #nbtsmelt:recipes

# Used for unique IDs for the markers.
execute unless score #nbtsmelt.marker.id.increment nbtsmelt.id matches 0.. run scoreboard players set #nbtsmelt.marker.id.increment nbtsmelt.id 0

# Calls the install prompt if the datapack is not installed yet.
execute unless score #nbtsmelt.installed nbtsmelt.var matches 1 run function nbtsmelt:setup/prompt

# Calls the function for checking idle furnaces.
function nbtsmelt:smelting/furnace/idle_check