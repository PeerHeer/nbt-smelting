#> peerheer.nbtsmelting:states/checking/tick_state
#
# Author: PeerHeer
#
# Called every tick for markers with the CHECKING state.

# TODO: most of these checks can be done at a lower frequency

# Kill marker if block is destroyed.
function peerheer.nbtsmelting:marker/kill_marker_if_block_destroyed

# Check for hoppers and droppers.
# The score is set to 1 if a hopper or dropper is found.
scoreboard players set #nbtsmelting.entity.found_fuel_hopper_dropper peerheer.global 0
scoreboard players set #nbtsmelting.entity.found_input_hopper_dropper peerheer.global 0

# Check for droppers for the input and fuel item.
execute if block ~ ~1 ~ minecraft:dropper[facing=down] run function peerheer.nbtsmelting:states/checking/hopper_dropper_checks/found_input_hopper_dropper
execute if block ~ ~-1 ~ minecraft:dropper[facing=up] run function peerheer.nbtsmelting:states/checking/hopper_dropper_checks/found_fuel_hopper_dropper
execute if block ~ ~ ~1 minecraft:dropper[facing=north] run function peerheer.nbtsmelting:states/checking/hopper_dropper_checks/found_fuel_hopper_dropper
execute if block ~ ~ ~-1 minecraft:dropper[facing=south] run function peerheer.nbtsmelting:states/checking/hopper_dropper_checks/found_fuel_hopper_dropper
execute if block ~-1 ~ ~ minecraft:dropper[facing=east] run function peerheer.nbtsmelting:states/checking/hopper_dropper_checks/found_fuel_hopper_dropper
execute if block ~1 ~ ~ minecraft:dropper[facing=west] run function peerheer.nbtsmelting:states/checking/hopper_dropper_checks/found_fuel_hopper_dropper

# Check for hoppers for the input or fuel item.
execute if block ~ ~1 ~ minecraft:hopper[facing=down] run function peerheer.nbtsmelting:states/checking/hopper_dropper_checks/found_input_hopper_dropper
execute if block ~ ~ ~1 minecraft:hopper[facing=north] run function peerheer.nbtsmelting:states/checking/hopper_dropper_checks/found_fuel_hopper_dropper
execute if block ~ ~ ~-1 minecraft:hopper[facing=south] run function peerheer.nbtsmelting:states/checking/hopper_dropper_checks/found_fuel_hopper_dropper
execute if block ~-1 ~ ~ minecraft:hopper[facing=east] run function peerheer.nbtsmelting:states/checking/hopper_dropper_checks/found_fuel_hopper_dropper
execute if block ~1 ~ ~ minecraft:hopper[facing=west] run function peerheer.nbtsmelting:states/checking/hopper_dropper_checks/found_fuel_hopper_dropper

# Remove hopper/dropper tag if not found.
execute if score #nbtsmelting.entity.found_input_hopper_dropper peerheer.global matches 0 run function peerheer.nbtsmelting:states/checking/hopper_dropper_checks/remove_hopper_dropper_tags
execute if score #nbtsmelting.entity.found_fuel_hopper_dropper peerheer.global matches 0 run function peerheer.nbtsmelting:states/checking/hopper_dropper_checks/remove_hopper_dropper_tags

# Go back to idle if no hoppers and droppers are found AND if no players are in the vicinity.
# We need to be mindful of players because one can still have the GUI open while the other removes the hopper/dropper, or the hopper/dropper can
# be removed by a non-player (such as an explosion).
execute at @s[tag=!peerheer.nbtsmelting.entity.marker.hopper_dropper] unless entity @p[distance=..9] run function peerheer.nbtsmelting:states/idle/change_state_to_idle

# Start running checks.
execute if entity @s[tag=peerheer.nbtsmelting.entity.marker.state.checking] run function peerheer.nbtsmelting:states/checking/checks/check_input_item_exists

# Indicate that state was processed.
scoreboard players set #nbtsmelting.entity.is_processed peerheer.global 1
