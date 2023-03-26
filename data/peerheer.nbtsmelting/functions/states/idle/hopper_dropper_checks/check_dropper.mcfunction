# Check for droppers for the input and fuel item.
# Chose not to check for triggered state:
# 1. It takes 1 tick for the item to be transferred.
# 2. It would require checking for ALL IDLE markers even when players are not in range.
execute if block ~ ~1 ~ minecraft:dropper[facing=down] run function peerheer.nbtsmelting:states/idle/hopper_dropper_checks/found_input_hopper_dropper
execute if block ~ ~-1 ~ minecraft:dropper[facing=up] run function peerheer.nbtsmelting:states/idle/hopper_dropper_checks/found_fuel_hopper_dropper
execute if block ~ ~ ~1 minecraft:dropper[facing=north] run function peerheer.nbtsmelting:states/idle/hopper_dropper_checks/found_fuel_hopper_dropper
execute if block ~ ~ ~-1 minecraft:dropper[facing=south] run function peerheer.nbtsmelting:states/idle/hopper_dropper_checks/found_fuel_hopper_dropper
execute if block ~-1 ~ ~ minecraft:dropper[facing=east] run function peerheer.nbtsmelting:states/idle/hopper_dropper_checks/found_fuel_hopper_dropper
execute if block ~1 ~ ~ minecraft:dropper[facing=west] run function peerheer.nbtsmelting:states/idle/hopper_dropper_checks/found_fuel_hopper_dropper
