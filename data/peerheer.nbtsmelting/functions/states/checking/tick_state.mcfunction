#> peerheer.nbtsmelting:states/checking/tick_state
#
# Author: PeerHeer
#
# Called every tick for markers with the CHECKING state.

# Kill marker if block is destroyed.
function peerheer.nbtsmelting:marker/kill_marker_if_block_destroyed

# Check for hoppers and droppers.
# The score is set to 1 if a hopper or dropper is found.
scoreboard players set #nbtsmelting.entity.found_fuel_hopper_dropper peerheer.global 0
scoreboard players set #nbtsmelting.entity.found_input_hopper_dropper peerheer.global 0

# Check for droppers for the input and fuel item.
execute if block ~ ~1 ~ minecraft:dropper[facing=down] run function peerheer.nbtsmelting:states/checking/found_hopper_dropper/found_input_hopper_dropper
execute if block ~ ~-1 ~ minecraft:dropper[facing=up] run function peerheer.nbtsmelting:states/checking/found_hopper_dropper/found_fuel_hopper_dropper
execute if block ~ ~ ~1 minecraft:dropper[facing=north] run function peerheer.nbtsmelting:states/checking/found_hopper_dropper/found_fuel_hopper_dropper
execute if block ~ ~ ~-1 minecraft:dropper[facing=south] run function peerheer.nbtsmelting:states/checking/found_hopper_dropper/found_fuel_hopper_dropper
execute if block ~-1 ~ ~ minecraft:dropper[facing=east] run function peerheer.nbtsmelting:states/checking/found_hopper_dropper/found_fuel_hopper_dropper
execute if block ~1 ~ ~ minecraft:dropper[facing=west] run function peerheer.nbtsmelting:states/checking/found_hopper_dropper/found_fuel_hopper_dropper

# Check for hoppers for the input or fuel item.
execute if block ~ ~1 ~ minecraft:hopper[facing=down] run function peerheer.nbtsmelting:states/checking/found_hopper_dropper/found_input_hopper_dropper
execute if block ~ ~ ~1 minecraft:hopper[facing=north] run function peerheer.nbtsmelting:states/checking/found_hopper_dropper/found_fuel_hopper_dropper
execute if block ~ ~ ~-1 minecraft:hopper[facing=south] run function peerheer.nbtsmelting:states/checking/found_hopper_dropper/found_fuel_hopper_dropper
execute if block ~-1 ~ ~ minecraft:hopper[facing=east] run function peerheer.nbtsmelting:states/checking/found_hopper_dropper/found_fuel_hopper_dropper
execute if block ~1 ~ ~ minecraft:hopper[facing=west] run function peerheer.nbtsmelting:states/checking/found_hopper_dropper/found_fuel_hopper_dropper

# Remove hopper/dropper tag if not found.
execute if score #nbtsmelting.entity.found_input_hopper_dropper peerheer.global matches 0 run tag @s remove peerheer.nbtsmelting.entity.marker.input_hopper_dropper
execute if score #nbtsmelting.entity.found_fuel_hopper_dropper peerheer.global matches 0 run tag @s remove peerheer.nbtsmelting.entity.marker.fuel_hopper_dropper

# Go back to idle if no hoppers and droppers are found AND if no players are in the vicinity.
# We need to be mindful of players because one can still have the GUI open while the other removes the hopper/dropper.
execute at @s[tag=!peerheer.nbtsmelting.entity.marker.input_hopper_dropper, tag=!peerheer.nbtsmelting.entity.marker.fuel_hopper_dropper] unless entity @p[distance=..9] run function peerheer.nbtsmelting:states/idle/change_state_to_idle

# Indicate that state was processed.
scoreboard players set #nbtsmelting.entity.is_processed peerheer.global 1
