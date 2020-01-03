import argparse
import os
import re
import shutil

verbose = False
namespace = ""
data_path = ""
string_id = ""

def main(args):
    global string_id
    global verbose
    global namespace
    global data_path

    string_id = args.string_id
    verbose = args.verbose
    namespace = args.namespace
    data_path = args.data_path

    regex = re.compile(f"^{string_id}.*")

    path_to_namespace = os.path.join(data_path, 'data', namespace)

    # Delete files
    for root, dirs, files in os.walk(path_to_namespace):
        for d in dirs:
            result = re.match(regex, d)
            if result is not None:
                path_to_dir = os.path.join(root, d)
                if verbose:
                    print("Removing directory: " + path_to_dir)
                shutil.rmtree(path_to_dir)
        for f in files:
            result = re.match(regex, f)
            if result is not None:
                path_to_file = os.path.join(root, f)
                if verbose:
                    print("Removing file: " + path_to_file)
                os.remove(path_to_file)

    # Delete from function tag
    path_to_function_tags = os.path.join(path_to_namespace, 'tags', 'functions')
    function_tag_content = []
    function_tag_functions = []

    if os.path.exists(os.path.join(path_to_function_tags, 'recipes.json')):
        at_functions = False
        with open(os.path.join(path_to_function_tags, 'recipes.json'), 'r') as f:
            for line in f:
                if not at_functions:
                    function_tag_content.append(line)
                if '[' in line:
                    at_functions = True
                elif ']' in line:
                    functions_str = ',\n'.join(function_tag_functions)
                    function_tag_content.append(functions_str)
                    function_tag_content.append("\n" + line)
                    at_functions = False
                elif at_functions and string_id not in line:
                    line = line.rstrip()
                    if line != "":
                        line = line[:-1] if line[-1] == ',' else line
                        function_tag_functions.append(line)
                elif string_id in line and verbose:
                    print(f"Removing '{line.strip()}' from function tag...")

        with open(os.path.join(path_to_function_tags, 'recipes.json'), 'w') as f:
            f.write(''.join(function_tag_content))

    # Delete from check_recipes
    check_recipes_files = []
    blocks = ["furnace", "blasting_furnace", "smoker"]
    for block in blocks:
        path_to_get_recipe = os.path.join(path_to_namespace, 'functions', 'smelting', block, 'get_recipe')
        path_to_check_recipes = os.path.join(path_to_get_recipe, 'check_recipes')
        if os.path.exists(path_to_check_recipes):
            files = [os.path.join(path_to_check_recipes, f) for f in os.listdir(path_to_check_recipes)]
            check_recipes_files.extend(files)

    for check_recipes_file in check_recipes_files:
        has_id = False
        file_content = []
        with open(check_recipes_file, 'r') as f:
            for line in f:
                if string_id not in line:
                    file_content.append(line)
                else:
                    if verbose:
                        print(f"Removing '{line.strip()}' from file '{check_recipes_file}'...")
                    has_id = True
        if has_id:
            with open(check_recipes_file, 'w') as f:
                f.write(''.join(file_content))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("string_id", help="String ID of the recipe. Use to '<filename>_<item>' to delete a single input item or '<filename>' to delete all recipes of a file.")
    parser.add_argument("data_path", help="Relative path to the folder containing the 'data' folder of the datapack.")
    parser.add_argument("-ns", "--namespace", help="Namespace that contains the NBT smelting modules. Defaults to 'nbtsmelt'.", default="nbtsmelt")
    parser.add_argument("-v", "--verbose", help="Increases output verbosity.", action="store_true", default=False)
    args = parser.parse_args()
    main(args)