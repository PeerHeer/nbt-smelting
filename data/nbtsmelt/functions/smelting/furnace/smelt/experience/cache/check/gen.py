for i in range(0,99):
    content =\
"""execute store success score #nbtsmelt.recipe.location_not_equal nbtsmelt.var run data modify storage nbtsmelt:furnace_recipes Temp.ExperienceRecipe set from storage nbtsmelt:furnace_inv Furnace.RecipeLocation{index}
execute if score #nbtsmelt.recipe.location_not_equal nbtsmelt.var matches 0 run function nbtsmelt:smelting/furnace/smelt/experience/increment/increment_{index}
""".format(index=i)

    with open('check_{}.mcfunction'.format(i), 'w') as f:
        f.write(content)