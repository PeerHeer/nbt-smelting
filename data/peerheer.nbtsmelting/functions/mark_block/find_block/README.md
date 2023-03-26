# Finding a block around the player
Each subdirectory contains 43 functions that check coordinates around the player for a placed block. If one of the functions succeeds, the next functions are not executed.

The functions execute from closest coordinates to furthest coordinates, because it is more likely for a player to place the block closer to themselves. In that situation, fewer functions would execute.

In the best case, only 21 commands will be executed in addition to the commands necessary to summon and set up the marker. In the worst case, this is 902. In survival/adventure, the maximum will be lower because the player cannot reach as far as in creative.

This is all necessary because ray casting is not fast enough: when the player is rapidly moving the screen while placing the block the ray can miss that block.
