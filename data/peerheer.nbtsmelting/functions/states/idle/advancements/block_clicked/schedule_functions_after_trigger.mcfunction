
# Reset rotation after 10 ticks to avoid false positive rotation checking.
# Since the rotation check is not done every tick it can trigger when the player is still in the GUI, which we don't want.
schedule function peerheer.nbtsmelting:player/reset_no_gui_checks_entry 10t replace

# Replace scheduling function so we are guaranteed to have time to reset rotation before the check happens.
schedule function peerheer.nbtsmelting:player/check_if_player_not_in_gui_entry 20t replace
