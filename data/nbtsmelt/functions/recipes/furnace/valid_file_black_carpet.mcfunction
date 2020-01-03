# Reset Temp
data modify storage nbtsmelt:furnace_recipes Temp set value {}

# Input
data modify storage nbtsmelt:furnace_recipes Temp.Input.Count set value 1b

# Output
data modify storage nbtsmelt:furnace_recipes Temp.Output.Count set value 2b
data modify storage nbtsmelt:furnace_recipes Temp.Output.Item set value {id:"minecraft:coal"}

# Exp reward
data modify storage nbtsmelt:furnace_recipes Temp.ExperienceRecipe set value "nbtsmelt:valid_file_exp"

# Cooking time
data modify storage nbtsmelt:furnace_recipes Temp.CookingTime set value 5s

# Add to DB
scoreboard players set #nbtsmelt.recipe.id nbtsmelt.var 15
function nbtsmelt:playerdb/put_entry
