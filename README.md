# NBT smelting
A datapack that allows the user to smelt items using input and output NBT data and item count.

# Description
In vanilla minecraft, there is no way to use NBT on items as input or output using custom recipes in a datapack. This datapack aims to solve this issue.

Using this datapack, it is possible to:
- add `nbt` to the input and/or output of a recipe
- add `count` to the input and/or output of a recipe

# Adding recipes
Recipes should be located in json files and use the [same format](https://minecraft.gamepedia.com/Recipe#JSON_format) as normal recipes, with some additions:
- `"nbt"` can now be added inside `ingredient` and `result` tags. It follows the same format as the [`item`](https://minecraft.gamepedia.com/Template:Nbt_inherit/conditions/item/template) compound in Loot Table conditions.
- `"count"` can now be added inside `ingredient` and `result` tags. Count is a single integer. For the `ingredient` tag, it specifies how many ingredients should be cooked when the `cookingtime` reaches its maximum. For the `result` tag, it specifies how many output items should be added to the output when the `cookingtime` reaches its maximum.


Recipes can be added using the provided `recipe_parser.py` file and can be deleted using the `recipe_deleter.py` file. These files require [Python 3.8](https://www.python.org/downloads/release/python-381/) to be installed on your computer. Documentation on the Recipe Parser and Recipe Deleter can be found in [`MANUAL.md`](https://github.com/PeerHeer/nbt-smelting/blob/master/MANUAL.md).
