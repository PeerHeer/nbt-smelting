# TODO: this can be done less than every tick.

# Kill marker if block is destroyed.
function peerheer.nbtsmelting:marker/kill_marker_if_block_destroyed

# Indicate that state was processed.
scoreboard players set #nbtsmelting.entity.is_processed peerheer.global 1
