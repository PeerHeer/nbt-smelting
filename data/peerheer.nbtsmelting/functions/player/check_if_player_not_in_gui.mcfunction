
# Check if player rotation changed.
function peerheer.nbtsmelting:player/check_if_rotation_changed

# Check if player jumped & reset score.
execute if score @s peerheer.nbtsmelting.jump matches 1.. run function peerheer.nbtsmelting:player/remove_gui_tags
scoreboard players reset @s peerheer.nbtsmelting.jump

# Check if player sneaked & reset score.
execute if score @s peerheer.nbtsmelting.sneak_time matches 1.. run function peerheer.nbtsmelting:player/remove_gui_tags
scoreboard players reset @s peerheer.nbtsmelting.sneak_time
