# Reset scores.
scoreboard players set #peerheer.nbtsmelting.block.found_input_hopper_dropper peerheer.global 0
scoreboard players set #peerheer.nbtsmelting.block.found_fuel_hopper_dropper peerheer.global 0

# Check for hoppers and droppers adjacent & pointing into the smelter block.
function peerheer.nbtsmelting:states/idle/hopper_dropper_checks/check_hopper
function peerheer.nbtsmelting:states/idle/hopper_dropper_checks/check_dropper

# If no hoppers or droppers were found, remove tags.
execute if score #peerheer.nbtsmelting.block.found_input_hopper_dropper peerheer.global matches 0 run function peerheer.nbtsmelting:states/idle/hopper_dropper_checks/did_not_find_input_hopper_dropper
execute if score #peerheer.nbtsmelting.block.found_fuel_hopper_dropper peerheer.global matches 0 run function peerheer.nbtsmelting:states/idle/hopper_dropper_checks/did_not_find_fuel_hopper_dropper
execute if score #peerheer.nbtsmelting.block.found_input_hopper_dropper peerheer.global matches 0 if score #peerheer.nbtsmelting.block.found_fuel_hopper_dropper peerheer.global matches 0 run tag @s remove peerheer.nbtsmelting.entity.marker.hopper_dropper
