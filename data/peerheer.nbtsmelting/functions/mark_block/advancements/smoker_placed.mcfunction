#> peerheer.nbtsmelting:mark_block/advancements/smoker_placed
#>
#> Author:
#>    PeerHeer (https://github.com/PeerHeer)
#>
#> Description:
#>    Looks for a placed smoker.

# Revoke advancement.
advancement revoke @s only peerheer.nbtsmelting:block_placed/smoker_placed

# Initialise found_block score to 0.
# The score is set to 1 if the block is found.
scoreboard players set #nbtsmelting.entity.found_block peerheer.global 0

# Start searching for the placed block.
function peerheer.nbtsmelting:mark_block/find_block/smoker/coords0
