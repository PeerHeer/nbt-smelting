#> peerheer.nbtsmelting:mark_block/advancements/blast_furnace_placed
#>
#> Author:
#>    PeerHeer (https://github.com/PeerHeer)
#>
#> Description:
#>    Looks for a placed blast furnace.

# Revoke advancement.
advancement revoke @s only peerheer.nbtsmelting:block_placed/blast_furnace_placed

# Initialise found_block score to 0.
# The score is set to 1 if the block is found.
scoreboard players set #nbtsmelting.entity.found_block peerheer.global 0

# Start searching for the placed block.
function peerheer.nbtsmelting:mark_block/find_block/blast_furnace/coords0
