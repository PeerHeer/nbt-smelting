scoreboard players set #nbtsmelt.recipe.tag.length nbtsmelt.var 0
execute if score #nbtsmelt.recipe.tag.length nbtsmelt.var >= #nbtsmelt.recipe.tag.max_length nbtsmelt.var run scoreboard players set #nbtsmelt.recipe.id nbtsmelt.var 3
execute if score #nbtsmelt.recipe.tag.length nbtsmelt.var >= #nbtsmelt.recipe.tag.max_length nbtsmelt.var run scoreboard players operation #nbtsmelt.recipe.tag.max_length nbtsmelt.var = #nbtsmelt.recipe.tag.length nbtsmelt.var
