for i in range(0, 99):
    nxt = i + 1
    if i == 0:
        content =\
        """execute store success score #nbtsmelt.recipe.location_not_equal nbtsmelt.var run data modify storage nbtsmelt:furnace_inv Furnace.RecipeLocation{index} set from storage nbtsmelt:furnace_recipes Temp.ExperienceRecipe
execute if score #nbtsmelt.recipe.location_not_equal nbtsmelt.var matches 0 run function nbtsmelt:smelting/furnace/smelt/experience/increment/increment_{index}
scoreboard players remove #nbtsmelt.recipe.stored.used_size nbtsmelt.var 1
execute if score #nbtsmelt.recipe.location_not_equal nbtsmelt.var matches 1 if score #nbtsmelt.recipe.stored.used_size nbtsmelt.var matches 1.. run function nbtsmelt:smelting/furnace/smelt/experience/check/check_{nxt}
""".format(index=i,nxt=nxt)
    elif i == 98:
        content =\
        """execute store success score #nbtsmelt.recipe.location_not_equal nbtsmelt.var run data modify storage nbtsmelt:furnace_inv Furnace.RecipeLocation{index} set from storage nbtsmelt:furnace_recipes Temp.ExperienceRecipe
execute if score #nbtsmelt.recipe.location_not_equal nbtsmelt.var matches 0 run function nbtsmelt:smelting/furnace/smelt/experience/increment/increment_{index}
""".format(index=i)
    else:
        content =\
        """execute store success score #nbtsmelt.recipe.location_not_equal nbtsmelt.var run data modify storage nbtsmelt:furnace_inv Furnace.RecipeLocation{index} set from storage nbtsmelt:furnace_recipes Temp.ExperienceRecipe
execute if score #nbtsmelt.recipe.location_not_equal nbtsmelt.var matches 0 run function nbtsmelt:smelting/furnace/smelt/experience/increment/increment_{index}
scoreboard players remove #nbtsmelt.recipe.stored.used_size nbtsmelt.var 1
execute if score #nbtsmelt.recipe.location_not_equal nbtsmelt.var matches 1 if score #nbtsmelt.recipe.stored.used_size nbtsmelt.var matches 1.. run function nbtsmelt:smelting/furnace/smelt/experience/check/check_{nxt}
""".format(index=i,nxt=nxt)

    with open('check_{}.mcfunction'.format(i), 'w') as f:
        f.write(content)