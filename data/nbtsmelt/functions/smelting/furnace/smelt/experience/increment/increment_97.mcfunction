execute store result score #nbtsmelt.recipe.stored.amount nbtsmelt.var run data get storage nbtsmelt:furnace_inv Furnace.RecipeAmount97
scoreboard players add #nbtsmelt.recipe.stored.amount nbtsmelt.var 1
execute store result block ~ ~ ~ RecipeAmount97 int 1 run scoreboard players get #nbtsmelt.recipe.stored.amount nbtsmelt.var
scoreboard players operation #nbtsmelt.recipe.stored.used_size nbtsmelt.const -= #nbtsmelt.recipe.stored.used_size nbtsmelt.var
