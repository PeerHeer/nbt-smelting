#> peerheer.nbtsmelting:player/check_rotation_change
#>
#> Author:
#>    PeerHeer (https://github.com/PeerHeer)
#>
#> Description:
#>    Check if rotation change occurred by comparing current rotation to previous rotation.
#>    If the player rotates, it is impossible for them to be inside a GUI, so the tak for possibly having a GUI open is removed.

# Set previous rotation.
scoreboard players operation @s peerheer.nbtsmelting.rotation.0.prev = @s peerheer.nbtsmelting.rotation.0
scoreboard players operation @s peerheer.nbtsmelting.rotation.1.prev = @s peerheer.nbtsmelting.rotation.1

# Get current rotation.
execute store result score @s peerheer.nbtsmelting.rotation.0 run data get entity @s Rotation[0] 100
execute store result score @s peerheer.nbtsmelting.rotation.1 run data get entity @s Rotation[1] 100

# Compare previous and current rotation. If they are not equal, the player rotated and the tag is removed.
execute unless score @s peerheer.nbtsmelting.rotation.0 = @s peerheer.nbtsmelting.rotation.0.prev run function peerheer.nbtsmelting:player/remove_gui_tags
execute unless score @s peerheer.nbtsmelting.rotation.1 = @s peerheer.nbtsmelting.rotation.1.prev run function peerheer.nbtsmelting:player/remove_gui_tags
