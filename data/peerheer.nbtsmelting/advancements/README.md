# Advancements

## block_clicked
These advancements are used to detect if a player right-clicked on a furnace, smoker or blast furnace.

If the right-click is detected, the state of any IDLE marker entity corresponding to the clicked block in a 9 block radius around the player is set to CHECKING.

This is done because the player might have opened the GUI of any of these blocks.

Ray casting might be too slow in edge cases (such as the player falling beyond the furnace block in a single tick), which is why it is not used.

## block_placed
Detect if the player places a furnace, smoker or blast furnace.

If placement is detected, we search all coordinates around the player for an unoccupied block.

Ray casting is too slow if the player moves the mouse fast enough while placing the block, so it is not used.

## global
Part of the Smithing data pack guidelines.

Signals that this pack is installed.

Requires **PeerHeer Utils** to work, because the parent advancement is in that datapack.
