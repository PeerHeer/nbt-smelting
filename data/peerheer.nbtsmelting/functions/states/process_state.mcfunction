scoreboard players set #nbtsmelting.entity.is_processed peerheer.global 0

# Enter appropriate state according to tag. Only one state is processed per tick.
# Only do IDLE checks if player is at most 8 blocks away.
# 8 blocks because this is the distance at which a player is kicked out of the GUI.
execute if score #nbtsmelting.entity.is_processed peerheer.global matches 0 if entity @s[tag=peerheer.nbtsmelting.entity.marker.state.checking] run function peerheer.nbtsmelting:states/checking/tick_state
execute if score #nbtsmelting.entity.is_processed peerheer.global matches 0 if entity @s[tag=peerheer.nbtsmelting.entity.marker.state.smelting] run function peerheer.nbtsmelting:states/smelting/tick_state