# Add tags.
tag @s add global.ignore
tag @s add peerheer.nbtsmelting.entity.marker
tag @s add peerheer.nbtsmelting.entity.marker.state.idle

# Set NBT data.
data merge entity @s {data: {PreviousInputItem: {}}}

# Set the idle loop that the entity will be ticked on.
scoreboard players operation @s peerheer.nbtsmelting.idle_loop = #peerheer.nbtsmelting.idle_loop peerheer.global

# Set the global idle loop score.
scoreboard players add #peerheer.nbtsmelting.idle_loop peerheer.global 1
execute if score #peerheer.nbtsmelting.idle_loop peerheer.global matches 4.. run scoreboard players set #peerheer.nbtsmelting.idle_loop peerheer.global 0

# Check if there are hoppers or droppers adjacent. If so, go to CHECKING.
function peerheer.nbtsmelting:states/idle/hopper_dropper_checks/check_dropper
execute if entity @s[tag=!peerheer.nbtsmelting.entity.marker.hopper_dropper] run function peerheer.nbtsmelting:states/idle/hopper_dropper_checks/check_hopper