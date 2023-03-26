#> peerheer.nbtsmelting:states/process_state

# Reset score for indicating that occupied slots were checked this tick.
scoreboard players set #peerheer.nbtsmelting.block.occupied_slots_checked peerheer.global 0

# If a player is inside the GUI and changed his inventory, check for occupied slots.
execute if entity @s[tag=peerheer.nbtsmelting.entity.marker.state.idle, tag=peerheer.nbtsmelting.entity.marker.player_interacted, tag=peerheer.nbtsmelting.entity.marker.player_inventory_changed] run function peerheer.nbtsmelting:states/idle/check_occupied_slots

# If the furnace has inputs for both slots attached by hoppers or droppers, check for occupied slots.
execute if entity @s[tag=peerheer.nbtsmelting.entity.marker.state.idle, tag=peerheer.nbtsmelting.entity.marker.input_hopper_dropper, tag=peerheer.nbtsmelting.entity.marker.fuel_hopper_dropper] unless score #peerheer.nbtsmelting.block.occupied_slots_checked peerheer.global matches 1 run function peerheer.nbtsmelting:states/idle/check_occupied_slots
