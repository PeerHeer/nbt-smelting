# Check for hoppers for the input or fuel item.
# Chose not to check for enabled state:
# It would require checking for ALL IDLE markers even when players are not in range.
execute if block ~ ~1 ~ minecraft:hopper[facing=down] run function peerheer.nbtsmelting:states/idle/hopper_dropper_checks/found_input_hopper_dropper
execute if block ~ ~ ~1 minecraft:hopper[facing=north] run function peerheer.nbtsmelting:states/idle/hopper_dropper_checks/found_fuel_hopper_dropper
execute if block ~ ~ ~-1 minecraft:hopper[facing=south] run function peerheer.nbtsmelting:states/idle/hopper_dropper_checks/found_fuel_hopper_dropper
execute if block ~-1 ~ ~ minecraft:hopper[facing=east] run function peerheer.nbtsmelting:states/idle/hopper_dropper_checks/found_fuel_hopper_dropper
execute if block ~1 ~ ~ minecraft:hopper[facing=west] run function peerheer.nbtsmelting:states/idle/hopper_dropper_checks/found_fuel_hopper_dropper
