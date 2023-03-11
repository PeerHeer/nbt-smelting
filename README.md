# NBT Smelting
A datapack that allows the user to smelt items using input and output NBT data and item count, without altering the behaviour of normal Funaces, Blasting Furnaces and Smokers.

# Why?
In vanilla minecraft, there is no way to use NBT on items as input or output using custom recipes in a datapack.

This datapack allows the user to do just that, using the vanilla smelters (Furnace, Blast Furnace, Smoker).

# Recipes

# Functionality and performance
When the player places a smelter, it is marked by a marker entity.

## IDLE smelters
### Functionality
- Smelters that are IDLE check their block every 10 ticks (0.5s at 20tps).
- If the block that they are marking is destroyed, they will kill themselves.

### Performance
- The checking is divided over 4 loops that are offset by 1 tick, which divides the load of all IDLE smelters over 4 ticks instead of just one.
- This means that smelters that do nothing are very efficient: you can have hundreds of them and this datapack will not significantly affect overall performance.
- In a test with 1331 IDLE smelters, the average tick speed was 6ms (9ms max) without a nearby player or 7ms (12ms max) if a player is nearby, in an otherwise empty world.

## CHECKING smelters
### Functionality
- Smelters that are CHECKING check if they can smelt every tick.
- Smelters can only be CHECKING if:
    - A player is within 9 blocks AND a player interacted with a nearby smelter --> a player may have opened the smelter GUI.
        - _Possible optimisation_: only go to CHECKING if the player has a smeltable item or a fuel in inventory. Requires extra tag on markers and inventory_changed advancement to check items picked up while in GUI.
        - _Possible optimisation_: only go to CHECKING if a player changes their inventory in addition to having opened the GUI --> only then do they move an item to a smelter slot. Requires CHECKING and SMELTING states to be processed in the same tick for the same marker entity + extra tag on markers + inventory_changed advancement.
    - The smelter is adjacent to a dropper or hopper that can input items --> the smelter may be able to smelt items provided by these blocks.
        - _Possible optimisation_: only go to CHECKING if the hopper can make the smelter actually smelt. I.e. if there is a hopper for input and none for fuel and there is no fuel in the fuel slot, then it is impossible for the smelter to start smelting without player interaction.

### Performance
- When in the CHECKING state, we **cannot**:
    - Assume the player is out of the GUI when moving: they may be pushed by a mob or in water, or they may be falling.
    - Use raycasting for player interaction: the ray may miss if the player is falling or otherwise moving quickly while interacting with the smelter.