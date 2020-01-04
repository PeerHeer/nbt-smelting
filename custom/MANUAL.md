# Recipe Parser
## Name
`recipe_parser.py` - used to parse JSON files into recipes.

## Usage
`python recipe_parser.py [-h] [-ns NAMESPACE] [-nr] [-v] [-r] [-e FILE_PATH] [-i FILE_PATH] path data_path`

## Description
The recipe parser parses recipes from JSON files. The files have the [same format as regular recipes](https://minecraft.gamepedia.com/Recipe#JSON_format) with some additions. For now, each `ingredient` and each `result` can have `nbt` and `count` fields. The recipe files are parsed according to their `ingredient` tag. For each `ingredient` item in a file, a new recipe is created with the ID `<filename>_<item_id>`.

For parsed recipes that contain items that are already used in vanilla recipes, the vanilla recipe will be (partially) replaced. When the `nbt` field in the `ingredient` is specified, the vanilla recipe will be converted to an NBT Smelting recipe and will only be applied to items that do not match the previously mentioned `nbt` field value.

## JSON Format
```json
{
    "type": "<type>",
    "ingredient": {
        "item": "<item>",
        "tag": "<tag>",
        "nbt": "{<nbt>}",
        "count": 0
    },
    "ingredient": [
        {
            "item": "<item>",
            "tag": "<tag>",
            "nbt": "{<nbt>}",
            "count": 0
        }
    ],
    "result": {
        "item": "<item>",
        "nbt": "{<nbt>}",
        "count": 0
    },
    "experience": 0.0,
    "cookingtime": 0
}
```

## Arguments
| Argument | Description |
|----------|-------------|
| `path`   | Path (relative to execution location) to the directory or file to parse. Other directories/files can be included with the `--include` option. Files/directories can be excluded using the `--exclude` option. All files with the `.json` extension will be parsed as recipe files. |
| `data_path` | Path (relative to the execution location) to the parent directory of the `data` folder. This folder should contain a namespace called `nbtsmelt` **or** a namespace defined with the `--namespace` option. |

## Options
| Option | Description |
|--------|-------------|
| `-h`, `--help` | Show a help message. |
| `-ns`, `--namespace` **_namespace_** | The datapack namespace that contains the NBT Smelting file structure and modules. Defaults to `nbtsmelt`. |
| `-nr`, `--no-replace` | When provided, the parser does **not** parse and replace recipes that already exist. |
| `-v`, `--verbose` | Increases the level of output verbosity. Its most notable feature is displaying reasons why the parsing of a recipe failed. |
| `-r`, `--recursive` | Parses a directory recursively, including all sub-directories and its files. |
| `-e`, `--exclude` **_filePath_** | Excludes a file or directory from parsing. Should be a path relative to the execution location. This option can be specified multiple times to exclude multiple files and directories. |
| `-e`, `--include` **_filePath_** | Includes a file or directory in the parsing. Should be a path relative to the execution location. This option can be specified multiple times to include multiple files and directories. |

## Errors
The parser will return with exit code 1 if at least one of the following conditions is met:
- The `data_path` is invalid.
- There are no files to parse in the included paths.

The parsing of a single recipe file will fail if at least one of the following conditions is met:
- The file contains invalid JSON.
- The recipe already exists and the `--no-replace` option is enabled.
- The `type` field is not specified or has an invaid value (must be `minecraft:smelting`, `minecraft:blasting` or `minecraft:smoking`).
- The `ingredient` field is not specified or has an invalid data type (must be `list` or `dict`).
- The `result` field is not specified or has an invalid data type (must be `dict`).
- The `experience` field is not specified, has an invalid value (must be > 0) or has an invalid data type (must be `int` or `float`).
- The `cookingtime` field has an invalid value (must be > 0)
- At least one `ingredient` does not contain an `item`, `tag` or `count` field.
- At least one `ingredient` contains an invalid `item` or `tag` field.
- At least one `ingredient` contains both an `item` and a `tag` field.
- At least one `ingredient` contains a `count` field with an invalid value (must be > 0 and < maximum stack size of the item).
- The `result` does not contain an `item` or `count` field.
- The `result` contains an `item` field with an invalid value.
- The `result` contains a `count` field with an invalid value (must be > 0 and < maximum stack size of the item).



# Recipe Deleter
## Description
The recipe deleter can be used to delete recipes.

## Usage
`python recipe_deleter.py [-h] [-ns NAMESPACE] [-v] string_id data_path`
