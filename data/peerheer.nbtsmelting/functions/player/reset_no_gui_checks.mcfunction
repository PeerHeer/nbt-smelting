#> peerheer.nbtsmelting:player/reset_rotation_change
#>
#> Author:
#>    PeerHeer (https://github.com/PeerHeer)
#>
#> Description:
#>    Sets the player's previous rotation equal to its current rotation so the rotation check
#>    will not detect a change.

# Get current rotation.
execute store result score @s peerheer.nbtsmelting.rotation.0 run data get entity @s Rotation[0] 100
execute store result score @s peerheer.nbtsmelting.rotation.1 run data get entity @s Rotation[1] 100

# Store current rotation into previous rotation.
scoreboard players operation @s peerheer.nbtsmelting.rotation.0.prev = @s peerheer.nbtsmelting.rotation.0
scoreboard players operation @s peerheer.nbtsmelting.rotation.1.prev = @s peerheer.nbtsmelting.rotation.1

# Reset scores.
scoreboard players reset @s peerheer.nbtsmelting.jump
scoreboard players reset @s peerheer.nbtsmelting.sneak_time
