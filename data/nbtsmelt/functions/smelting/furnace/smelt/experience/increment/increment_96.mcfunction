execute store result score #nbtsmelt.recipe.stored.amount nbtsmelt.var run data get storage nbtsmelt:furnace_inv Furnace.RecipeAmount96
scoreboard players add #nbtsmelt.recipe.stored.amount nbtsmelt.var 1
execute store result block ~ ~ ~ RecipeAmount96 int 1 run scoreboard players get #nbtsmelt.recipe.stored.amount nbtsmelt.var
scoreboard players operation #nbtsmelt.recipe.stored.used_size nbtsmelt.const -= #nbtsmelt.recipe.stored.used_size nbtsmelt.var
