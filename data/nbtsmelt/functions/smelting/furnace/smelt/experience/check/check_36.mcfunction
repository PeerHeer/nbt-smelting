execute store success score #nbtsmelt.recipe.location_not_equal nbtsmelt.var run data modify storage nbtsmelt:furnace_inv Furnace.RecipeLocation36 set from storage nbtsmelt:furnace_recipes Temp.ExperienceRecipe
execute if score #nbtsmelt.recipe.location_not_equal nbtsmelt.var matches 0 run function nbtsmelt:smelting/furnace/smelt/experience/increment/increment_36
scoreboard players remove #nbtsmelt.recipe.stored.used_size nbtsmelt.var 1
execute if score #nbtsmelt.recipe.location_not_equal nbtsmelt.var matches 1 if score #nbtsmelt.recipe.stored.used_size nbtsmelt.var matches 1.. run function nbtsmelt:smelting/furnace/smelt/experience/check/check_37
