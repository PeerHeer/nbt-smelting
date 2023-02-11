#> peerheer.nbtsmelting:load
# Author: PeerHeer
#
# Send user feedback and add scheduling function.

# Check if PeerHeer Utils is loaded.
execute if score #utils.loaded peerheer.global matches 1 run tellraw @a ["",{"text": "[", "color": "dark_green"},{"text":"INFO","color":"green"},{"text":"] ","color":"dark_green"},{"text":"Loaded datapack "},{"text":"NBT Smelting","color":"yellow","hoverEvent":{"action":"show_text","value":["",{"text":"NBT Smelting"},{"text":"\n"},{"text":"Smelt items using NBT, item counts, enchantments and more!"}]}}]
execute unless score #utils.loaded peerheer.global matches 1 run tellraw @a ["",{"text": "[", "color": "dark_red"},{"text":"ERROR","color":"red"},{"text":"] ","color":"dark_red"},{"text":"You need to install the "},{"text": "PeerHeer Utils","color":"yellow"},{"text":" datapack to make "},{"text": "NBT Smelting","color":"yellow"},{"text":" work!"}]

# Schedule ticking function.
schedule function peerheer.nbtsmelting:schedule_1t 1t replace
