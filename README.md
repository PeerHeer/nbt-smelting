# NBT smelting
A datapack that allows the user to smelt items using input and output NBT data and item count, without altering the behaviour of normal Funaces, Blasting Furnaces or Smokers.

# Why?
In vanilla minecraft, there is no way to use NBT on items as input or output using custom recipes in a datapack. This datapack aims to solve this issue.

Using this datapack, it is possible to:
- add `nbt` to the input and/or output of a recipe;
- add `count` to the input and/or output of a recipe.

This can be done using custom recipes made by the user.

# Recipes
Recipes should be located in json files and use the [same format](https://minecraft.gamepedia.com/Recipe#JSON_format) as normal recipes, with some additions:
- `"nbt"` can now be added inside `ingredient` and `result` tags. It follows the same format as the [`item`](https://minecraft.gamepedia.com/Template:Nbt_inherit/conditions/item/template) compound in Loot Table conditions.
- `"count"` can now be added inside `ingredient` and `result` tags. Count is a single integer. For the `ingredient` tag, it specifies how many ingredients should be cooked when the `cookingtime` reaches its maximum. For the `result` tag, it specifies how many output items should be added to the output when the `cookingtime` reaches its maximum.

Recipes can be added using the provided `recipe_parser.py` file and can be deleted using the `recipe_deleter.py` file, located in the `custom` folder. These files require [Python 3.8](https://www.python.org/downloads/release/python-381/) to be installed on your system. Documentation on the Recipe Parser and Recipe Deleter can be found in [`custom/MANUAL.md`](https://github.com/PeerHeer/nbt-smelting/blob/master/custom/MANUAL.md).

**NOTE:** Currently, only the Furnace block is supported. The Blasting Furnace and Smoker will be added in the future.

# Performance
This datapack adds about 7 to 8 mspt per 32 active furnaces. It is adviced not to have a lot of furnaces active at the same time.

# Planned features
- Add Blasting Furnace and Smoker support
- Correctly delete overridden recipes
