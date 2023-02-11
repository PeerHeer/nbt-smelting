# Kill marker if block is destroyed.
function peerheer.nbtsmelting:marker/kill_marker_if_block_destroyed

# Check for droppers for the input and fuel item.
# Chose not to check for triggered state:
# 1. It takes 1 tick for the item to be transferred.
# 2. It would require checking for ALL IDLE markers even when players are not in range.
execute if block ~ ~1 ~ minecraft:dropper[facing=down] run function peerheer.nbtsmelting:states/idle/found_hopper_dropper/found_input_hopper_dropper
execute if block ~ ~-1 ~ minecraft:dropper[facing=up] run function peerheer.nbtsmelting:states/idle/found_hopper_dropper/found_fuel_hopper_dropper
execute if block ~ ~ ~1 minecraft:dropper[facing=north] run function peerheer.nbtsmelting:states/idle/found_hopper_dropper/found_fuel_hopper_dropper
execute if block ~ ~ ~-1 minecraft:dropper[facing=south] run function peerheer.nbtsmelting:states/idle/found_hopper_dropper/found_fuel_hopper_dropper
execute if block ~-1 ~ ~ minecraft:dropper[facing=east] run function peerheer.nbtsmelting:states/idle/found_hopper_dropper/found_fuel_hopper_dropper
execute if block ~1 ~ ~ minecraft:dropper[facing=west] run function peerheer.nbtsmelting:states/idle/found_hopper_dropper/found_fuel_hopper_dropper

# Check for hoppers for the input or fuel item.
# Chose not to check for enabled state:
# It would require checking for ALL IDLE markers even when players are not in range.
execute if block ~ ~1 ~ minecraft:hopper[facing=down] run function peerheer.nbtsmelting:states/idle/found_hopper_dropper/found_input_hopper_dropper
execute if block ~ ~ ~1 minecraft:hopper[facing=north] run function peerheer.nbtsmelting:states/idle/found_hopper_dropper/found_fuel_hopper_dropper
execute if block ~ ~ ~-1 minecraft:hopper[facing=south] run function peerheer.nbtsmelting:states/idle/found_hopper_dropper/found_fuel_hopper_dropper
execute if block ~-1 ~ ~ minecraft:hopper[facing=east] run function peerheer.nbtsmelting:states/idle/found_hopper_dropper/found_fuel_hopper_dropper
execute if block ~1 ~ ~ minecraft:hopper[facing=west] run function peerheer.nbtsmelting:states/idle/found_hopper_dropper/found_fuel_hopper_dropper

# Indicate that state was processed.
scoreboard players set #nbtsmelting.entity.is_processed peerheer.global 1
