# Author: PeerHeer
#
# Forceload chunks in all dimensions.
# Forceloading the chunks is required for loading a sign and the predicate entity.

# Checks if chunk is forceloaded.
execute in minecraft:overworld store success score #nbtsmelt.chunk_loaded nbtsmelt.var run forceload query -30000000 8000

# If chunk is not forceloaded, forceload it.
execute if score #nbtsmelt.chunk_loaded nbtsmelt.var matches 0 in minecraft:the_nether run forceload add -30000000 8000
execute if score #nbtsmelt.chunk_loaded nbtsmelt.var matches 0 in minecraft:overworld run forceload add -30000000 8000
execute if score #nbtsmelt.chunk_loaded nbtsmelt.var matches 0 in minecraft:the_end run forceload add -30000000 8000

# Set the sign.
execute unless block -29999995 0 8005 minecraft:oak_wall_sign run setblock -29999995 0 8005 minecraft:oak_wall_sign

# Fill a layer of bedrock.
fill -30000000 1 8000 -29999985 1 8015 minecraft:bedrock

# Summon the predicate entity.
execute unless entity 0-24e1-1d91-0-4954143 run function nbtsmelt:summon/predicate_entity