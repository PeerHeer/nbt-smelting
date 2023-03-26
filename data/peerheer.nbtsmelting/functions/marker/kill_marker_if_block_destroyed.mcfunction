#> peerheer.nbtsmelting:marker/kill_marker_if_block_destroyed
#>
#> Author:
#>    PeerHeer (https://github.com/PeerHeer)
#>
#> Description:
#>    Kills the marker when its block is destroyed.

# If the block was destroyed, kill the marker.
execute if entity @s[tag=peerheer.nbtsmelting.entity.marker.block.furnace] unless block ~ ~ ~ minecraft:furnace run kill @s
execute if entity @s[tag=peerheer.nbtsmelting.entity.marker.block.blast_furnace] unless block ~ ~ ~ minecraft:blast_furnace run kill @s
execute if entity @s[tag=peerheer.nbtsmelting.entity.marker.block.smoker] unless block ~ ~ ~ minecraft:smoker run kill @s
