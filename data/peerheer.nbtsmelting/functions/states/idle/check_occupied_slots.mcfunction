# Check if slots are occupied.
execute store success score @s peerheer.nbtsmelting.slot.input.is_occupied run data get block ~ ~ ~ Items[{Slot: 0b}]
execute store success score @s peerheer.nbtsmelting.slot.fuel.is_occupied run data get block ~ ~ ~ Items[{Slot: 1b}]

# If both slots are occupied, start checking for recipes.
execute if score @s peerheer.nbtsmelting.slot.input.is_occupied matches 1 if score @s peerheer.nbtsmelting.slot.fuel.is_occupied matches 1 run say Both occupied!

# Indicate that slots were checked.
scoreboard players set #peerheer.nbtsmelting.block.occupied_slots_checked peerheer.global 1
