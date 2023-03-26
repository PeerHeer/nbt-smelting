#> peerheer.nbtsmelting:marker/setup/shared/setup_shared
#>
#> Author:
#>    PeerHeer (https://github.com/PeerHeer)
#>
#> Description:
#>    Set up the marker for operation.

# Add the necessary tags to the marker.
function peerheer.nbtsmelting:marker/setup/shared/add_tags

# Set NBT data.
data merge entity @s {data: {PreviousInputItem: {}}}

# Set the idle loop that the entity will be ticked on.
scoreboard players operation @s peerheer.nbtsmelting.idle_loop = #peerheer.nbtsmelting.idle_loop peerheer.global

# Set the global idle loop score so the next entity uses a different idle loop.
scoreboard players add #peerheer.nbtsmelting.idle_loop peerheer.global 1
execute if score #peerheer.nbtsmelting.idle_loop peerheer.global matches 4.. run scoreboard players set #peerheer.nbtsmelting.idle_loop peerheer.global 0

# Check which slots are occupied.
# Check is done to support copying blocks.
execute store success score @s peerheer.nbtsmelting.slot.input.is_occupied run data get block ~ ~ ~ Items[{Slot: 0b}]
execute store success score @s peerheer.nbtsmelting.slot.fuel.is_occupied run data get block ~ ~ ~ Items[{Slot: 1b}]
execute store success score @s peerheer.nbtsmelting.slot.output.is_occupied run data get block ~ ~ ~ Items[{Slot: 2b}]

# Check if there are hoppers or droppers adjacent.
function peerheer.nbtsmelting:states/idle/hopper_dropper_checks/check_hopper_dropper

# Check if there are any occupied slots.
function peerheer.nbtsmelting:states/idle/check_occupied_slots