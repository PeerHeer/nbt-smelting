These files are used to determine which recipe should be chosen: the recipe with the largest `tag` compound length is chosen as the recipe to use.

Each recipe has one file in this folder and the ID of the chosen recipe is set when the `tag` compound length is greater than the current largest length (initialized to 0). The greater length is then set as the current largest length.