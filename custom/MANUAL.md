# Recipe Parser
## Name
`recipe_parser.py` - used to parse JSON files into recipes.

## Usage
`python recipe_parser.py [-h] [-ns NAMESPACE] [-nr] [-v] [-r] [-e EXCLUDE] [-i INCLUDE] path data_path`

## Description

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

# Recipe Deleter
## Description
The recipe deleter can be used to delete recipes.

## Usage
`python recipe_deleter.py [-h] [-ns NAMESPACE] [-v] string_id data_path`