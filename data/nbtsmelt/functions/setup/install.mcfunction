# Author: PeerHeer
#
# Installs the datapack by calling all setup functions.

# Install datapack
function #nbtsmelt:setup

# Do cleanup
scoreboard players set #nbtsmelt.installed nbtsmelt.var 1
schedule clear nbtsmelt:setup/prompt
tellraw @a ["",{"text":"NBT comparisons installed successfully!","color":"green"}]