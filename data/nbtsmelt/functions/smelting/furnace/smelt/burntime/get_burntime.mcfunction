# Author: PeerHeer
#
# Returns the amount of BurnTime to be set.

# Put the ID inside the HandItems of the predicate entity.
data modify entity @s HandItems[0].id set from storage nbtsmelt:furnace_inv Fuel.id

# Initialize the BurnTime to 0.
scoreboard players set #nbtsmelt.smelting.burntime nbtsmelt.var 0

# Check all predicates for fuel.
execute if predicate nbtsmelt:burntime/50ticks run scoreboard players set #nbtsmelt.smelting.burntime nbtsmelt.var 50
execute if score #nbtsmelt.smelting.burntime nbtsmelt.var matches 0 if predicate nbtsmelt:burntime/67ticks run scoreboard players set #nbtsmelt.smelting.burntime nbtsmelt.var 67
execute if score #nbtsmelt.smelting.burntime nbtsmelt.var matches 0 if predicate nbtsmelt:burntime/100ticks run scoreboard players set #nbtsmelt.smelting.burntime nbtsmelt.var 100
execute if score #nbtsmelt.smelting.burntime nbtsmelt.var matches 0 if predicate nbtsmelt:burntime/150ticks run scoreboard players set #nbtsmelt.smelting.burntime nbtsmelt.var 1500
execute if score #nbtsmelt.smelting.burntime nbtsmelt.var matches 0 if predicate nbtsmelt:burntime/200ticks run scoreboard players set #nbtsmelt.smelting.burntime nbtsmelt.var 200
execute if score #nbtsmelt.smelting.burntime nbtsmelt.var matches 0 if predicate nbtsmelt:burntime/300ticks run scoreboard players set #nbtsmelt.smelting.burntime nbtsmelt.var 300
execute if score #nbtsmelt.smelting.burntime nbtsmelt.var matches 0 if predicate nbtsmelt:burntime/1200ticks run scoreboard players set #nbtsmelt.smelting.burntime nbtsmelt.var 1200
execute if score #nbtsmelt.smelting.burntime nbtsmelt.var matches 0 if predicate nbtsmelt:burntime/1600ticks run scoreboard players set #nbtsmelt.smelting.burntime nbtsmelt.var 1600
execute if score #nbtsmelt.smelting.burntime nbtsmelt.var matches 0 if predicate nbtsmelt:burntime/2400ticks run scoreboard players set #nbtsmelt.smelting.burntime nbtsmelt.var 2400
execute if score #nbtsmelt.smelting.burntime nbtsmelt.var matches 0 if predicate nbtsmelt:burntime/4000ticks run scoreboard players set #nbtsmelt.smelting.burntime nbtsmelt.var 4000
execute if score #nbtsmelt.smelting.burntime nbtsmelt.var matches 0 if predicate nbtsmelt:burntime/16000ticks run scoreboard players set #nbtsmelt.smelting.burntime nbtsmelt.var 16000
execute if score #nbtsmelt.smelting.burntime nbtsmelt.var matches 0 if predicate nbtsmelt:burntime/20000ticks run scoreboard players set #nbtsmelt.smelting.burntime nbtsmelt.var 20000