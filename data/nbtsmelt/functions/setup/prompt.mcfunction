# Author: PeerHeer
#
# Sends a prompt to the player every 10 seconds that can be clicked to install the datapack.

tellraw @a ["",{"text":"NBT Smelting loaded! Click this text to install the datapack (must be OP level 3 or higher).","color":"green","clickEvent":{"action":"run_command","value":"/function nbtsmelt:setup/install"},"hoverEvent":{"action":"show_text","value":["Install datapack"]}}]
schedule function nbtsmelt:setup/prompt 10s