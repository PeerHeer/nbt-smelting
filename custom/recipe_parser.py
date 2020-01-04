import json
import argparse
import glob
import os
import sys
from enum import Enum

items_list = ["minecraft:acacia_boat",
"minecraft:acacia_button",
"minecraft:acacia_door",
"minecraft:acacia_fence",
"minecraft:acacia_fence_gate",
"minecraft:acacia_leaves",
"minecraft:acacia_log",
"minecraft:acacia_planks",
"minecraft:acacia_pressure_plate",
"minecraft:acacia_sapling",
"minecraft:acacia_sign",
"minecraft:acacia_slab",
"minecraft:acacia_stairs",
"minecraft:acacia_trapdoor",
"minecraft:acacia_wood",
"minecraft:activator_rail",
"minecraft:air",
"minecraft:allium",
"minecraft:andesite",
"minecraft:andesite_slab",
"minecraft:andesite_stairs",
"minecraft:andesite_wall",
"minecraft:anvil",
"minecraft:apple",
"minecraft:armor_stand",
"minecraft:arrow",
"minecraft:azure_bluet",
"minecraft:baked_potato",
"minecraft:bamboo",
"minecraft:barrel",
"minecraft:barrier",
"minecraft:bat_spawn_egg",
"minecraft:beacon",
"minecraft:bedrock",
"minecraft:beehive",
"minecraft:bee_nest",
"minecraft:beef",
"minecraft:beetroot",
"minecraft:beetroot_seeds",
"minecraft:beetroot_soup",
"minecraft:bell",
"minecraft:birch_boat",
"minecraft:birch_button",
"minecraft:birch_door",
"minecraft:birch_fence",
"minecraft:birch_fence_gate",
"minecraft:birch_leaves",
"minecraft:birch_log",
"minecraft:birch_planks",
"minecraft:birch_pressure_plate",
"minecraft:birch_sapling",
"minecraft:birch_sign",
"minecraft:birch_slab",
"minecraft:birch_stairs",
"minecraft:birch_trapdoor",
"minecraft:birch_wood",
"minecraft:black_banner",
"minecraft:black_bed",
"minecraft:black_carpet",
"minecraft:black_concrete",
"minecraft:black_concrete_powder",
"minecraft:black_dye",
"minecraft:black_glazed_terracotta",
"minecraft:black_shulker_box",
"minecraft:black_stained_glass",
"minecraft:black_stained_glass_pane",
"minecraft:black_terracotta",
"minecraft:black_wool",
"minecraft:blast_furnace",
"minecraft:blaze_powder",
"minecraft:blaze_rod",
"minecraft:blaze_spawn_egg",
"minecraft:blue_banner",
"minecraft:blue_bed",
"minecraft:blue_carpet",
"minecraft:blue_concrete",
"minecraft:blue_concrete_powder",
"minecraft:blue_dye",
"minecraft:blue_glazed_terracotta",
"minecraft:blue_ice",
"minecraft:blue_orchid",
"minecraft:blue_shulker_box",
"minecraft:blue_stained_glass",
"minecraft:blue_stained_glass_pane",
"minecraft:blue_terracotta",
"minecraft:blue_wool",
"minecraft:bone",
"minecraft:bone_block",
"minecraft:bone_meal",
"minecraft:book",
"minecraft:bookshelf",
"minecraft:bow",
"minecraft:bowl",
"minecraft:brain_coral",
"minecraft:brain_coral_block",
"minecraft:brain_coral_fan",
"minecraft:bread",
"minecraft:brewing_stand",
"minecraft:brick",
"minecraft:brick_slab",
"minecraft:brick_stairs",
"minecraft:brick_wall",
"minecraft:bricks",
"minecraft:brown_banner",
"minecraft:brown_bed",
"minecraft:brown_carpet",
"minecraft:brown_concrete",
"minecraft:brown_concrete_powder",
"minecraft:brown_dye",
"minecraft:brown_glazed_terracotta",
"minecraft:brown_mushroom",
"minecraft:brown_mushroom_block",
"minecraft:brown_shulker_box",
"minecraft:brown_stained_glass",
"minecraft:brown_stained_glass_pane",
"minecraft:brown_terracotta",
"minecraft:brown_wool",
"minecraft:bubble_coral",
"minecraft:bubble_coral_block",
"minecraft:bubble_coral_fan",
"minecraft:bucket",
"minecraft:cactus",
"minecraft:cake",
"minecraft:campfire",
"minecraft:carrot",
"minecraft:carrot_on_a_stick",
"minecraft:cartography_table",
"minecraft:carved_pumpkin",
"minecraft:cat_spawn_egg",
"minecraft:cauldron",
"minecraft:cave_spider_spawn_egg",
"minecraft:chain_command_block",
"minecraft:chainmail_boots",
"minecraft:chainmail_chestplate",
"minecraft:chainmail_helmet",
"minecraft:chainmail_leggings",
"minecraft:charcoal",
"minecraft:chest",
"minecraft:chest_minecart",
"minecraft:chicken",
"minecraft:chicken_spawn_egg",
"minecraft:chipped_anvil",
"minecraft:chiseled_quartz_block",
"minecraft:chiseled_red_sandstone",
"minecraft:chiseled_sandstone",
"minecraft:chiseled_stone_bricks",
"minecraft:chorus_flower",
"minecraft:chorus_fruit",
"minecraft:chorus_plant",
"minecraft:clay",
"minecraft:clay_ball",
"minecraft:clock",
"minecraft:coal",
"minecraft:coal_block",
"minecraft:coal_ore",
"minecraft:coarse_dirt",
"minecraft:cobblestone",
"minecraft:cobblestone_slab",
"minecraft:cobblestone_stairs",
"minecraft:cobblestone_wall",
"minecraft:cobweb",
"minecraft:cocoa_beans",
"minecraft:cod",
"minecraft:cod_bucket",
"minecraft:cod_spawn_egg",
"minecraft:command_block",
"minecraft:command_block_minecart",
"minecraft:comparator",
"minecraft:compass",
"minecraft:composter",
"minecraft:conduit",
"minecraft:cooked_beef",
"minecraft:cooked_chicken",
"minecraft:cooked_cod",
"minecraft:cooked_mutton",
"minecraft:cooked_porkchop",
"minecraft:cooked_rabbit",
"minecraft:cooked_salmon",
"minecraft:cookie",
"minecraft:cornflower",
"minecraft:cow_spawn_egg",
"minecraft:cracked_stone_bricks",
"minecraft:crafting_table",
"minecraft:creeper_banner_pattern",
"minecraft:creeper_head",
"minecraft:creeper_spawn_egg",
"minecraft:crossbow",
"minecraft:cut_red_sandstone",
"minecraft:cut_red_sandstone_slab",
"minecraft:cut_sandstone",
"minecraft:cut_sandstone_slab",
"minecraft:cyan_banner",
"minecraft:cyan_bed",
"minecraft:cyan_carpet",
"minecraft:cyan_concrete",
"minecraft:cyan_concrete_powder",
"minecraft:cyan_dye",
"minecraft:cyan_glazed_terracotta",
"minecraft:cyan_shulker_box",
"minecraft:cyan_stained_glass",
"minecraft:cyan_stained_glass_pane",
"minecraft:cyan_terracotta",
"minecraft:cyan_wool",
"minecraft:damaged_anvil",
"minecraft:dandelion",
"minecraft:dark_oak_boat",
"minecraft:dark_oak_button",
"minecraft:dark_oak_door",
"minecraft:dark_oak_fence",
"minecraft:dark_oak_fence_gate",
"minecraft:dark_oak_leaves",
"minecraft:dark_oak_log",
"minecraft:dark_oak_planks",
"minecraft:dark_oak_pressure_plate",
"minecraft:dark_oak_sapling",
"minecraft:dark_oak_sign",
"minecraft:dark_oak_slab",
"minecraft:dark_oak_stairs",
"minecraft:dark_oak_trapdoor",
"minecraft:dark_oak_wood",
"minecraft:dark_prismarine",
"minecraft:dark_prismarine_slab",
"minecraft:dark_prismarine_stairs",
"minecraft:daylight_detector",
"minecraft:dead_brain_coral",
"minecraft:dead_brain_coral_block",
"minecraft:dead_brain_coral_fan",
"minecraft:dead_bubble_coral",
"minecraft:dead_bubble_coral_block",
"minecraft:dead_bubble_coral_fan",
"minecraft:dead_bush",
"minecraft:dead_fire_coral",
"minecraft:dead_fire_coral_block",
"minecraft:dead_fire_coral_fan",
"minecraft:dead_horn_coral",
"minecraft:dead_horn_coral_block",
"minecraft:dead_horn_coral_fan",
"minecraft:dead_tube_coral",
"minecraft:dead_tube_coral_block",
"minecraft:dead_tube_coral_fan",
"minecraft:detector_rail",
"minecraft:diamond",
"minecraft:diamond_axe",
"minecraft:diamond_block",
"minecraft:diamond_boots",
"minecraft:diamond_chestplate",
"minecraft:diamond_helmet",
"minecraft:diamond_hoe",
"minecraft:diamond_horse_armor",
"minecraft:diamond_leggings",
"minecraft:diamond_ore",
"minecraft:diamond_pickaxe",
"minecraft:diamond_shovel",
"minecraft:diamond_sword",
"minecraft:diorite",
"minecraft:diorite_slab",
"minecraft:diorite_stairs",
"minecraft:diorite_wall",
"minecraft:dirt",
"minecraft:dispenser",
"minecraft:dolphin_spawn_egg",
"minecraft:donkey_spawn_egg",
"minecraft:dragon_breath",
"minecraft:dragon_egg",
"minecraft:dragon_head",
"minecraft:dried_kelp",
"minecraft:dried_kelp_block",
"minecraft:dropper",
"minecraft:drowned_spawn_egg",
"minecraft:egg",
"minecraft:elder_guardian_spawn_egg",
"minecraft:elytra",
"minecraft:emerald",
"minecraft:emerald_block",
"minecraft:emerald_ore",
"minecraft:enchanted_book",
"minecraft:enchanted_golden_apple",
"minecraft:enchanting_table",
"minecraft:end_crystal",
"minecraft:end_portal_frame",
"minecraft:end_rod",
"minecraft:end_stone",
"minecraft:end_stone_brick_slab",
"minecraft:end_stone_brick_stairs",
"minecraft:end_stone_brick_wall",
"minecraft:end_stone_bricks",
"minecraft:ender_chest",
"minecraft:ender_eye",
"minecraft:ender_pearl",
"minecraft:enderman_spawn_egg",
"minecraft:endermite_spawn_egg",
"minecraft:evoker_spawn_egg",
"minecraft:experience_bottle",
"minecraft:farmland",
"minecraft:feather",
"minecraft:fermented_spider_eye",
"minecraft:fern",
"minecraft:filled_map",
"minecraft:fire_charge",
"minecraft:fire_coral",
"minecraft:fire_coral_block",
"minecraft:fire_coral_fan",
"minecraft:firework_rocket",
"minecraft:firework_star",
"minecraft:fishing_rod",
"minecraft:fletching_table",
"minecraft:flint",
"minecraft:flint_and_steel",
"minecraft:flower_banner_pattern",
"minecraft:flower_pot",
"minecraft:fox_spawn_egg",
"minecraft:furnace",
"minecraft:furnace_minecart",
"minecraft:ghast_spawn_egg",
"minecraft:ghast_tear",
"minecraft:glass",
"minecraft:glass_bottle",
"minecraft:glass_pane",
"minecraft:glistering_melon_slice",
"minecraft:globe_banner_pattern",
"minecraft:glowstone",
"minecraft:glowstone_dust",
"minecraft:gold_block",
"minecraft:gold_ingot",
"minecraft:gold_nugget",
"minecraft:gold_ore",
"minecraft:golden_apple",
"minecraft:golden_axe",
"minecraft:golden_boots",
"minecraft:golden_carrot",
"minecraft:golden_chestplate",
"minecraft:golden_helmet",
"minecraft:golden_hoe",
"minecraft:golden_horse_armor",
"minecraft:golden_leggings",
"minecraft:golden_pickaxe",
"minecraft:golden_shovel",
"minecraft:golden_sword",
"minecraft:granite",
"minecraft:granite_slab",
"minecraft:granite_stairs",
"minecraft:granite_wall",
"minecraft:grass",
"minecraft:grass_block",
"minecraft:grass_path",
"minecraft:gravel",
"minecraft:gray_banner",
"minecraft:gray_bed",
"minecraft:gray_carpet",
"minecraft:gray_concrete",
"minecraft:gray_concrete_powder",
"minecraft:gray_dye",
"minecraft:gray_glazed_terracotta",
"minecraft:gray_shulker_box",
"minecraft:gray_stained_glass",
"minecraft:gray_stained_glass_pane",
"minecraft:gray_terracotta",
"minecraft:gray_wool",
"minecraft:green_banner",
"minecraft:green_bed",
"minecraft:green_carpet",
"minecraft:green_concrete",
"minecraft:green_concrete_powder",
"minecraft:green_dye",
"minecraft:green_glazed_terracotta",
"minecraft:green_shulker_box",
"minecraft:green_stained_glass",
"minecraft:green_stained_glass_pane",
"minecraft:green_terracotta",
"minecraft:green_wool",
"minecraft:grindstone",
"minecraft:guardian_spawn_egg",
"minecraft:gunpowder",
"minecraft:hay_block",
"minecraft:heart_of_the_sea",
"minecraft:heavy_weighted_pressure_plate",
"minecraft:honey_block",
"minecraft:honey_bottle",
"minecraft:honeycomb",
"minecraft:honeycomb_block",
"minecraft:hopper",
"minecraft:hopper_minecart",
"minecraft:horn_coral",
"minecraft:horn_coral_block",
"minecraft:horn_coral_fan",
"minecraft:horse_spawn_egg",
"minecraft:husk_spawn_egg",
"minecraft:ice",
"minecraft:infested_chiseled_stone_bricks",
"minecraft:infested_cobblestone",
"minecraft:infested_cracked_stone_bricks",
"minecraft:infested_mossy_stone_bricks",
"minecraft:infested_stone",
"minecraft:infested_stone_bricks",
"minecraft:ink_sac",
"minecraft:iron_axe",
"minecraft:iron_bars",
"minecraft:iron_block",
"minecraft:iron_boots",
"minecraft:iron_chestplate",
"minecraft:iron_door",
"minecraft:iron_helmet",
"minecraft:iron_hoe",
"minecraft:iron_horse_armor",
"minecraft:iron_ingot",
"minecraft:iron_leggings",
"minecraft:iron_nugget",
"minecraft:iron_ore",
"minecraft:iron_pickaxe",
"minecraft:iron_shovel",
"minecraft:iron_sword",
"minecraft:iron_trapdoor",
"minecraft:item_frame",
"minecraft:jack_o_lantern",
"minecraft:jukebox",
"minecraft:jungle_boat",
"minecraft:jungle_button",
"minecraft:jungle_door",
"minecraft:jungle_fence",
"minecraft:jungle_fence_gate",
"minecraft:jungle_leaves",
"minecraft:jungle_log",
"minecraft:jungle_planks",
"minecraft:jungle_pressure_plate",
"minecraft:jungle_sapling",
"minecraft:jungle_sign",
"minecraft:jungle_slab",
"minecraft:jungle_stairs",
"minecraft:jungle_trapdoor",
"minecraft:jungle_wood",
"minecraft:kelp",
"minecraft:ladder",
"minecraft:lantern",
"minecraft:lapis_block",
"minecraft:lapis_lazuli",
"minecraft:lapis_ore",
"minecraft:large_fern",
"minecraft:lava_bucket",
"minecraft:lead",
"minecraft:leather",
"minecraft:leather_boots",
"minecraft:leather_chestplate",
"minecraft:leather_helmet",
"minecraft:leather_horse_armor",
"minecraft:leather_leggings",
"minecraft:lectern",
"minecraft:lever",
"minecraft:light_blue_banner",
"minecraft:light_blue_bed",
"minecraft:light_blue_carpet",
"minecraft:light_blue_concrete",
"minecraft:light_blue_concrete_powder",
"minecraft:light_blue_dye",
"minecraft:light_blue_glazed_terracotta",
"minecraft:light_blue_shulker_box",
"minecraft:light_blue_stained_glass",
"minecraft:light_blue_stained_glass_pane",
"minecraft:light_blue_terracotta",
"minecraft:light_blue_wool",
"minecraft:light_gray_banner",
"minecraft:light_gray_bed",
"minecraft:light_gray_carpet",
"minecraft:light_gray_concrete",
"minecraft:light_gray_concrete_powder",
"minecraft:light_gray_dye",
"minecraft:light_gray_glazed_terracotta",
"minecraft:light_gray_shulker_box",
"minecraft:light_gray_stained_glass",
"minecraft:light_gray_stained_glass_pane",
"minecraft:light_gray_terracotta",
"minecraft:light_gray_wool",
"minecraft:light_weighted_pressure_plate",
"minecraft:lilac",
"minecraft:lily_of_the_valley",
"minecraft:lily_pad",
"minecraft:lime_banner",
"minecraft:lime_bed",
"minecraft:lime_carpet",
"minecraft:lime_concrete",
"minecraft:lime_concrete_powder",
"minecraft:lime_dye",
"minecraft:lime_glazed_terracotta",
"minecraft:lime_shulker_box",
"minecraft:lime_stained_glass",
"minecraft:lime_stained_glass_pane",
"minecraft:lime_terracotta",
"minecraft:lime_wool",
"minecraft:lingering_potion",
"minecraft:llama_spawn_egg",
"minecraft:loom",
"minecraft:magenta_banner",
"minecraft:magenta_bed",
"minecraft:magenta_carpet",
"minecraft:magenta_concrete",
"minecraft:magenta_concrete_powder",
"minecraft:magenta_dye",
"minecraft:magenta_glazed_terracotta",
"minecraft:magenta_shulker_box",
"minecraft:magenta_stained_glass",
"minecraft:magenta_stained_glass_pane",
"minecraft:magenta_terracotta",
"minecraft:magenta_wool",
"minecraft:magma_block",
"minecraft:magma_cream",
"minecraft:magma_cube_spawn_egg",
"minecraft:map",
"minecraft:melon",
"minecraft:melon_seeds",
"minecraft:melon_slice",
"minecraft:milk_bucket",
"minecraft:minecart",
"minecraft:mojang_banner_pattern",
"minecraft:mooshroom_spawn_egg",
"minecraft:mossy_cobblestone",
"minecraft:mossy_cobblestone_slab",
"minecraft:mossy_cobblestone_stairs",
"minecraft:mossy_cobblestone_wall",
"minecraft:mossy_stone_brick_slab",
"minecraft:mossy_stone_brick_stairs",
"minecraft:mossy_stone_brick_wall",
"minecraft:mossy_stone_bricks",
"minecraft:mule_spawn_egg",
"minecraft:mushroom_stem",
"minecraft:mushroom_stew",
"minecraft:music_disc_11",
"minecraft:music_disc_13",
"minecraft:music_disc_blocks",
"minecraft:music_disc_cat",
"minecraft:music_disc_chirp",
"minecraft:music_disc_far",
"minecraft:music_disc_mall",
"minecraft:music_disc_mellohi",
"minecraft:music_disc_stal",
"minecraft:music_disc_strad",
"minecraft:music_disc_wait",
"minecraft:music_disc_ward",
"minecraft:mutton",
"minecraft:mycelium",
"minecraft:name_tag",
"minecraft:nautilus_shell",
"minecraft:nether_brick",
"minecraft:nether_brick_fence",
"minecraft:nether_brick_slab",
"minecraft:nether_brick_stairs",
"minecraft:nether_brick_wall",
"minecraft:nether_bricks",
"minecraft:nether_quartz_ore",
"minecraft:nether_star",
"minecraft:nether_wart",
"minecraft:nether_wart_block",
"minecraft:netherrack",
"minecraft:note_block",
"minecraft:oak_boat",
"minecraft:oak_button",
"minecraft:oak_door",
"minecraft:oak_fence",
"minecraft:oak_fence_gate",
"minecraft:oak_leaves",
"minecraft:oak_log",
"minecraft:oak_planks",
"minecraft:oak_pressure_plate",
"minecraft:oak_sapling",
"minecraft:oak_sign",
"minecraft:oak_slab",
"minecraft:oak_stairs",
"minecraft:oak_trapdoor",
"minecraft:oak_wood",
"minecraft:observer",
"minecraft:obsidian",
"minecraft:ocelot_spawn_egg",
"minecraft:orange_banner",
"minecraft:orange_bed",
"minecraft:orange_carpet",
"minecraft:orange_concrete",
"minecraft:orange_concrete_powder",
"minecraft:orange_dye",
"minecraft:orange_glazed_terracotta",
"minecraft:orange_shulker_box",
"minecraft:orange_stained_glass",
"minecraft:orange_stained_glass_pane",
"minecraft:orange_terracotta",
"minecraft:orange_tulip",
"minecraft:orange_wool",
"minecraft:oxeye_daisy",
"minecraft:packed_ice",
"minecraft:painting",
"minecraft:panda_spawn_egg",
"minecraft:paper",
"minecraft:parrot_spawn_egg",
"minecraft:peony",
"minecraft:petrified_oak_slab",
"minecraft:phantom_membrane",
"minecraft:phantom_spawn_egg",
"minecraft:pig_spawn_egg",
"minecraft:pillager_spawn_egg",
"minecraft:pink_banner",
"minecraft:pink_bed",
"minecraft:pink_carpet",
"minecraft:pink_concrete",
"minecraft:pink_concrete_powder",
"minecraft:pink_dye",
"minecraft:pink_glazed_terracotta",
"minecraft:pink_shulker_box",
"minecraft:pink_stained_glass",
"minecraft:pink_stained_glass_pane",
"minecraft:pink_terracotta",
"minecraft:pink_tulip",
"minecraft:pink_wool",
"minecraft:piston",
"minecraft:player_head",
"minecraft:podzol",
"minecraft:poisonous_potato",
"minecraft:polar_bear_spawn_egg",
"minecraft:polished_andesite",
"minecraft:polished_andesite_slab",
"minecraft:polished_andesite_stairs",
"minecraft:polished_diorite",
"minecraft:polished_diorite_slab",
"minecraft:polished_diorite_stairs",
"minecraft:polished_granite",
"minecraft:polished_granite_slab",
"minecraft:polished_granite_stairs",
"minecraft:popped_chorus_fruit",
"minecraft:poppy",
"minecraft:porkchop",
"minecraft:potato",
"minecraft:potion",
"minecraft:powered_rail",
"minecraft:prismarine",
"minecraft:prismarine_brick_slab",
"minecraft:prismarine_brick_stairs",
"minecraft:prismarine_bricks",
"minecraft:prismarine_crystals",
"minecraft:prismarine_shard",
"minecraft:prismarine_slab",
"minecraft:prismarine_stairs",
"minecraft:prismarine_wall",
"minecraft:pufferfish",
"minecraft:pufferfish_bucket",
"minecraft:pufferfish_spawn_egg",
"minecraft:pumpkin",
"minecraft:pumpkin_pie",
"minecraft:pumpkin_seeds",
"minecraft:purple_banner",
"minecraft:purple_bed",
"minecraft:purple_carpet",
"minecraft:purple_concrete",
"minecraft:purple_concrete_powder",
"minecraft:purple_dye",
"minecraft:purple_glazed_terracotta",
"minecraft:purple_shulker_box",
"minecraft:purple_stained_glass",
"minecraft:purple_stained_glass_pane",
"minecraft:purple_terracotta",
"minecraft:purple_wool",
"minecraft:purpur_block",
"minecraft:purpur_pillar",
"minecraft:purpur_slab",
"minecraft:purpur_stairs",
"minecraft:quartz",
"minecraft:quartz_block",
"minecraft:quartz_pillar",
"minecraft:quartz_slab",
"minecraft:quartz_stairs",
"minecraft:rabbit",
"minecraft:rabbit_foot",
"minecraft:rabbit_hide",
"minecraft:rabbit_spawn_egg",
"minecraft:rabbit_stew",
"minecraft:rail",
"minecraft:ravager_spawn_egg",
"minecraft:red_banner",
"minecraft:red_bed",
"minecraft:red_carpet",
"minecraft:red_concrete",
"minecraft:red_concrete_powder",
"minecraft:red_dye",
"minecraft:red_glazed_terracotta",
"minecraft:red_mushroom",
"minecraft:red_mushroom_block",
"minecraft:red_nether_brick_slab",
"minecraft:red_nether_brick_stairs",
"minecraft:red_nether_brick_wall",
"minecraft:red_nether_bricks",
"minecraft:red_sand",
"minecraft:red_sandstone",
"minecraft:red_sandstone_slab",
"minecraft:red_sandstone_stairs",
"minecraft:red_sandstone_wall",
"minecraft:red_shulker_box",
"minecraft:red_stained_glass",
"minecraft:red_stained_glass_pane",
"minecraft:red_terracotta",
"minecraft:red_tulip",
"minecraft:red_wool",
"minecraft:redstone",
"minecraft:redstone_block",
"minecraft:redstone_lamp",
"minecraft:redstone_ore",
"minecraft:redstone_torch",
"minecraft:repeater",
"minecraft:repeating_command_block",
"minecraft:rose_bush",
"minecraft:rotten_flesh",
"minecraft:saddle",
"minecraft:salmon",
"minecraft:salmon_bucket",
"minecraft:salmon_spawn_egg",
"minecraft:sand",
"minecraft:sandstone",
"minecraft:sandstone_slab",
"minecraft:sandstone_stairs",
"minecraft:sandstone_wall",
"minecraft:scaffolding",
"minecraft:scute",
"minecraft:sea_lantern",
"minecraft:sea_pickle",
"minecraft:seagrass",
"minecraft:shears",
"minecraft:sheep_spawn_egg",
"minecraft:shield",
"minecraft:shulker_box",
"minecraft:shulker_shell",
"minecraft:shulker_spawn_egg",
"minecraft:silverfish_spawn_egg",
"minecraft:skeleton_horse_spawn_egg",
"minecraft:skeleton_skull",
"minecraft:skeleton_spawn_egg",
"minecraft:skull_banner_pattern",
"minecraft:slime_ball",
"minecraft:slime_block",
"minecraft:slime_spawn_egg",
"minecraft:smithing_table",
"minecraft:smoker",
"minecraft:smooth_quartz",
"minecraft:smooth_quartz_slab",
"minecraft:smooth_quartz_stairs",
"minecraft:smooth_red_sandstone",
"minecraft:smooth_red_sandstone_slab",
"minecraft:smooth_red_sandstone_stairs",
"minecraft:smooth_sandstone",
"minecraft:smooth_sandstone_slab",
"minecraft:smooth_sandstone_stairs",
"minecraft:smooth_stone",
"minecraft:smooth_stone_slab",
"minecraft:snow",
"minecraft:snow_block",
"minecraft:snowball",
"minecraft:soul_sand",
"minecraft:spawner",
"minecraft:spectral_arrow",
"minecraft:spider_eye",
"minecraft:spider_spawn_egg",
"minecraft:splash_potion",
"minecraft:sponge",
"minecraft:spruce_boat",
"minecraft:spruce_button",
"minecraft:spruce_door",
"minecraft:spruce_fence",
"minecraft:spruce_fence_gate",
"minecraft:spruce_leaves",
"minecraft:spruce_log",
"minecraft:spruce_planks",
"minecraft:spruce_pressure_plate",
"minecraft:spruce_sapling",
"minecraft:spruce_sign",
"minecraft:spruce_slab",
"minecraft:spruce_stairs",
"minecraft:spruce_trapdoor",
"minecraft:spruce_wood",
"minecraft:squid_spawn_egg",
"minecraft:stick",
"minecraft:sticky_piston",
"minecraft:stone",
"minecraft:stone_axe",
"minecraft:stone_brick_slab",
"minecraft:stone_brick_stairs",
"minecraft:stone_brick_wall",
"minecraft:stone_bricks",
"minecraft:stone_button",
"minecraft:stone_hoe",
"minecraft:stone_pickaxe",
"minecraft:stone_pressure_plate",
"minecraft:stone_shovel",
"minecraft:stone_slab",
"minecraft:stone_stairs",
"minecraft:stone_sword",
"minecraft:stray_spawn_egg",
"minecraft:string",
"minecraft:stripped_acacia_log",
"minecraft:stripped_acacia_wood",
"minecraft:stripped_birch_log",
"minecraft:stripped_birch_wood",
"minecraft:stripped_dark_oak_log",
"minecraft:stripped_dark_oak_wood",
"minecraft:stripped_jungle_log",
"minecraft:stripped_jungle_wood",
"minecraft:stripped_oak_log",
"minecraft:stripped_oak_wood",
"minecraft:stripped_spruce_log",
"minecraft:stripped_spruce_wood",
"minecraft:structure_block",
"minecraft:structure_void",
"minecraft:sugar",
"minecraft:sugar_cane",
"minecraft:sunflower",
"minecraft:sweet_berries",
"minecraft:tall_grass",
"minecraft:terracotta",
"minecraft:tipped_arrow",
"minecraft:tnt",
"minecraft:tnt_minecart",
"minecraft:torch",
"minecraft:totem_of_undying",
"minecraft:trader_llama_spawn_egg",
"minecraft:trapped_chest",
"minecraft:trident",
"minecraft:tripwire_hook",
"minecraft:tropical_fish",
"minecraft:tropical_fish_bucket",
"minecraft:tropical_fish_spawn_egg",
"minecraft:tube_coral",
"minecraft:tube_coral_block",
"minecraft:tube_coral_fan",
"minecraft:turtle_egg",
"minecraft:turtle_helmet",
"minecraft:turtle_spawn_egg",
"minecraft:vex_spawn_egg",
"minecraft:villager_spawn_egg",
"minecraft:vindicator_spawn_egg",
"minecraft:vine",
"minecraft:wandering_trader_spawn_egg",
"minecraft:water_bucket",
"minecraft:wet_sponge",
"minecraft:wheat",
"minecraft:wheat_seeds",
"minecraft:white_banner",
"minecraft:white_bed",
"minecraft:white_carpet",
"minecraft:white_concrete",
"minecraft:white_concrete_powder",
"minecraft:white_dye",
"minecraft:white_glazed_terracotta",
"minecraft:white_shulker_box",
"minecraft:white_stained_glass",
"minecraft:white_stained_glass_pane",
"minecraft:white_terracotta",
"minecraft:white_tulip",
"minecraft:white_wool",
"minecraft:witch_spawn_egg",
"minecraft:wither_rose",
"minecraft:wither_skeleton_skull",
"minecraft:wither_skeleton_spawn_egg",
"minecraft:wolf_spawn_egg",
"minecraft:wooden_axe",
"minecraft:wooden_hoe",
"minecraft:wooden_pickaxe",
"minecraft:wooden_shovel",
"minecraft:wooden_sword",
"minecraft:writable_book",
"minecraft:written_book",
"minecraft:yellow_banner",
"minecraft:yellow_bed",
"minecraft:yellow_carpet",
"minecraft:yellow_concrete",
"minecraft:yellow_concrete_powder",
"minecraft:yellow_dye",
"minecraft:yellow_glazed_terracotta",
"minecraft:yellow_shulker_box",
"minecraft:yellow_stained_glass",
"minecraft:yellow_stained_glass_pane",
"minecraft:yellow_terracotta",
"minecraft:yellow_wool",
"minecraft:zombie_head",
"minecraft:zombie_horse_spawn_egg",
"minecraft:zombie_pigman_spawn_egg",
"minecraft:zombie_spawn_egg",
"minecraft:zombie_villager_spawn_egg"]

tags_dict = {"minecraft:acacia_logs":["minecraft:acacia_log",
    "minecraft:acacia_wood",
    "minecraft:stripped_acacia_log",
    "minecraft:stripped_acacia_wood"],
"minecraft:anvil":["minecraft:anvil",
    "minecraft:chipped_anvil",
    "minecraft:damaged_anvil"],
"minecraft:arrows":["minecraft:arrow",
    "minecraft:tipped_arrow",
    "minecraft:spectral_arrow"],
"minecraft:banners":["minecraft:white_banner",
    "minecraft:orange_banner",
    "minecraft:magenta_banner",
    "minecraft:light_blue_banner",
    "minecraft:yellow_banner",
    "minecraft:lime_banner",
    "minecraft:pink_banner",
    "minecraft:gray_banner",
    "minecraft:light_gray_banner",
    "minecraft:cyan_banner",
    "minecraft:purple_banner",
    "minecraft:blue_banner",
    "minecraft:brown_banner",
    "minecraft:green_banner",
    "minecraft:red_banner",
    "minecraft:black_banner"],
"minecraft:beds":["minecraft:red_bed",
    "minecraft:black_bed",
    "minecraft:blue_bed",
    "minecraft:brown_bed",
    "minecraft:cyan_bed",
    "minecraft:gray_bed",
    "minecraft:green_bed",
    "minecraft:light_blue_bed",
    "minecraft:light_gray_bed",
    "minecraft:lime_bed",
    "minecraft:magenta_bed",
    "minecraft:orange_bed",
    "minecraft:pink_bed",
    "minecraft:purple_bed",
    "minecraft:white_bed",
    "minecraft:yellow_bed"],
"minecraft:birch_logs":["minecraft:birch_log",
    "minecraft:birch_wood",
    "minecraft:stripped_birch_log",
    "minecraft:stripped_birch_wood"],
"minecraft:boats":["minecraft:oak_boat",
    "minecraft:spruce_boat",
    "minecraft:birch_boat",
    "minecraft:jungle_boat",
    "minecraft:acacia_boat",
    "minecraft:dark_oak_boat"],
"minecraft:buttons":["#minecraft:wooden_buttons",
    "minecraft:stone_button"],
"minecraft:carpets":["minecraft:white_carpet",
    "minecraft:orange_carpet",
    "minecraft:magenta_carpet",
    "minecraft:light_blue_carpet",
    "minecraft:yellow_carpet",
    "minecraft:lime_carpet",
    "minecraft:pink_carpet",
    "minecraft:gray_carpet",
    "minecraft:light_gray_carpet",
    "minecraft:cyan_carpet",
    "minecraft:purple_carpet",
    "minecraft:blue_carpet",
    "minecraft:brown_carpet",
    "minecraft:green_carpet",
    "minecraft:red_carpet",
    "minecraft:black_carpet"],
"minecraft:coals":["minecraft:coal",
    "minecraft:charcoal"],
"minecraft:dark_oak_logs":["minecraft:dark_oak_log",
    "minecraft:dark_oak_wood",
    "minecraft:stripped_dark_oak_log",
    "minecraft:stripped_dark_oak_wood"],
"minecraft:doors":["#minecraft:wooden_doors",
    "minecraft:iron_door"],
"minecraft:fences":["#minecraft:wooden_fences",
    "minecraft:nether_brick_fence"],
"minecraft:fishes":["minecraft:cod",
    "minecraft:cooked_cod",
    "minecraft:salmon",
    "minecraft:cooked_salmon",
    "minecraft:pufferfish",
    "minecraft:tropical_fish"],
"minecraft:flowers":["#minecraft:small_flowers",
    "#minecraft:tall_flowers"],
"minecraft:jungle_logs":["minecraft:jungle_log",
    "minecraft:jungle_wood",
    "minecraft:stripped_jungle_log",
    "minecraft:stripped_jungle_wood"],
"minecraft:leaves":["minecraft:jungle_leaves",
    "minecraft:oak_leaves",
    "minecraft:spruce_leaves",
    "minecraft:dark_oak_leaves",
    "minecraft:acacia_leaves",
    "minecraft:birch_leaves"],
"minecraft:lectern_books":["minecraft:written_book",
    "minecraft:writable_book"],
"minecraft:logs":["#minecraft:dark_oak_logs",
    "#minecraft:oak_logs",
    "#minecraft:acacia_logs",
    "#minecraft:birch_logs",
    "#minecraft:jungle_logs",
    "#minecraft:spruce_logs"],
"minecraft:music_discs":["minecraft:music_disc_13",
    "minecraft:music_disc_cat",
    "minecraft:music_disc_blocks",
    "minecraft:music_disc_chirp",
    "minecraft:music_disc_far",
    "minecraft:music_disc_mall",
    "minecraft:music_disc_mellohi",
    "minecraft:music_disc_stal",
    "minecraft:music_disc_strad",
    "minecraft:music_disc_ward",
    "minecraft:music_disc_11",
    "minecraft:music_disc_wait"],
"minecraft:oak_logs":["minecraft:oak_log",
    "minecraft:oak_wood",
    "minecraft:stripped_oak_log",
    "minecraft:stripped_oak_wood"],
"minecraft:planks":["minecraft:oak_planks",
    "minecraft:spruce_planks",
    "minecraft:birch_planks",
    "minecraft:jungle_planks",
    "minecraft:acacia_planks",
    "minecraft:dark_oak_planks"],
"minecraft:rails":["minecraft:rail",
    "minecraft:powered_rail",
    "minecraft:detector_rail",
    "minecraft:activator_rail"],
"minecraft:sand":["minecraft:sand",
    "minecraft:red_sand"],
"minecraft:saplings":["minecraft:oak_sapling",
    "minecraft:spruce_sapling",
    "minecraft:birch_sapling",
    "minecraft:jungle_sapling",
    "minecraft:acacia_sapling",
    "minecraft:dark_oak_sapling"],
"minecraft:signs":["minecraft:oak_sign",
    "minecraft:spruce_sign",
    "minecraft:birch_sign",
    "minecraft:acacia_sign",
    "minecraft:jungle_sign",
    "minecraft:dark_oak_sign"],
"minecraft:slabs":["minecraft:stone_slab",
    "minecraft:smooth_stone_slab",
    "minecraft:stone_brick_slab",
    "minecraft:sandstone_slab",
    "minecraft:acacia_slab",
    "minecraft:birch_slab",
    "minecraft:dark_oak_slab",
    "minecraft:jungle_slab",
    "minecraft:oak_slab",
    "minecraft:spruce_slab",
    "minecraft:purpur_slab",
    "minecraft:quartz_slab",
    "minecraft:red_sandstone_slab",
    "minecraft:brick_slab",
    "minecraft:cobblestone_slab",
    "minecraft:nether_brick_slab",
    "minecraft:petrified_oak_slab",
    "minecraft:prismarine_slab",
    "minecraft:prismarine_brick_slab",
    "minecraft:dark_prismarine_slab",
    "minecraft:polished_granite_slab",
    "minecraft:smooth_red_sandstone_slab",
    "minecraft:mossy_stone_brick_slab",
    "minecraft:polished_diorite_slab",
    "minecraft:mossy_cobblestone_slab",
    "minecraft:end_stone_brick_slab",
    "minecraft:smooth_sandstone_slab",
    "minecraft:smooth_quartz_slab",
    "minecraft:granite_slab",
    "minecraft:andesite_slab",
    "minecraft:red_nether_brick_slab",
    "minecraft:polished_andesite_slab",
    "minecraft:diorite_slab",
    "minecraft:cut_sandstone_slab",
    "minecraft:cut_red_sandstone_slab"],
"minecraft:small_flowers":["minecraft:dandelion",
    "minecraft:poppy",
    "minecraft:blue_orchid",
    "minecraft:allium",
    "minecraft:azure_bluet",
    "minecraft:red_tulip",
    "minecraft:orange_tulip",
    "minecraft:white_tulip",
    "minecraft:pink_tulip",
    "minecraft:oxeye_daisy",
    "minecraft:cornflower",
    "minecraft:lily_of_the_valley",
    "minecraft:wither_rose"],
"minecraft:spruce_logs":["minecraft:spruce_log",
    "minecraft:spruce_wood",
    "minecraft:stripped_spruce_log",
    "minecraft:stripped_spruce_wood"],
"minecraft:stairs":["minecraft:oak_stairs",
    "minecraft:cobblestone_stairs",
    "minecraft:spruce_stairs",
    "minecraft:sandstone_stairs",
    "minecraft:acacia_stairs",
    "minecraft:jungle_stairs",
    "minecraft:birch_stairs",
    "minecraft:dark_oak_stairs",
    "minecraft:nether_brick_stairs",
    "minecraft:stone_brick_stairs",
    "minecraft:brick_stairs",
    "minecraft:purpur_stairs",
    "minecraft:quartz_stairs",
    "minecraft:red_sandstone_stairs",
    "minecraft:prismarine_brick_stairs",
    "minecraft:prismarine_stairs",
    "minecraft:dark_prismarine_stairs",
    "minecraft:polished_granite_stairs",
    "minecraft:smooth_red_sandstone_stairs",
    "minecraft:mossy_stone_brick_stairs",
    "minecraft:polished_diorite_stairs",
    "minecraft:mossy_cobblestone_stairs",
    "minecraft:end_stone_brick_stairs",
    "minecraft:stone_stairs",
    "minecraft:smooth_sandstone_stairs",
    "minecraft:smooth_quartz_stairs",
    "minecraft:granite_stairs",
    "minecraft:andesite_stairs",
    "minecraft:red_nether_brick_stairs",
    "minecraft:polished_andesite_stairs",
    "minecraft:diorite_stairs"],
"minecraft:stone_bricks":["minecraft:stone_bricks",
    "minecraft:mossy_stone_bricks",
    "minecraft:cracked_stone_bricks",
    "minecraft:chiseled_stone_bricks"],
"minecraft:tall_flowers":["minecraft:sunflower",
    "minecraft:lilac",
    "minecraft:peony",
    "minecraft:rose_bush"],
"minecraft:trapdoors":["#minecraft:wooden_trapdoors",
    "minecraft:iron_trapdoor"],
"minecraft:walls":["minecraft:cobblestone_wall",
    "minecraft:mossy_cobblestone_wall",
    "minecraft:brick_wall",
    "minecraft:prismarine_wall",
    "minecraft:red_sandstone_wall",
    "minecraft:mossy_stone_brick_wall",
    "minecraft:granite_wall",
    "minecraft:stone_brick_wall",
    "minecraft:nether_brick_wall",
    "minecraft:andesite_wall",
    "minecraft:red_nether_brick_wall",
    "minecraft:sandstone_wall",
    "minecraft:end_stone_brick_wall",
    "minecraft:diorite_wall"],
"minecraft:wooden_buttons":["minecraft:oak_button",
    "minecraft:spruce_button",
    "minecraft:birch_button",
    "minecraft:jungle_button",
    "minecraft:acacia_button",
    "minecraft:dark_oak_button"],
"minecraft:wooden_doors":["minecraft:oak_door",
    "minecraft:spruce_door",
    "minecraft:birch_door",
    "minecraft:jungle_door",
    "minecraft:acacia_door",
    "minecraft:dark_oak_door"],
"minecraft:wooden_fences":["minecraft:oak_fence",
    "minecraft:acacia_fence",
    "minecraft:dark_oak_fence",
    "minecraft:spruce_fence",
    "minecraft:birch_fence",
    "minecraft:jungle_fence"],
"minecraft:wooden_pressure_plates":["minecraft:oak_pressure_plate",
    "minecraft:spruce_pressure_plate",
    "minecraft:birch_pressure_plate",
    "minecraft:jungle_pressure_plate",
    "minecraft:acacia_pressure_plate",
    "minecraft:dark_oak_pressure_plate"],
"minecraft:wooden_slabs":["minecraft:oak_slab",
    "minecraft:spruce_slab",
    "minecraft:birch_slab",
    "minecraft:jungle_slab",
    "minecraft:acacia_slab",
    "minecraft:dark_oak_slab"],
"minecraft:wooden_stairs":["minecraft:oak_stairs",
    "minecraft:spruce_stairs",
    "minecraft:birch_stairs",
    "minecraft:jungle_stairs",
    "minecraft:acacia_stairs",
    "minecraft:dark_oak_stairs"],
"minecraft:wooden_trapdoors":["minecraft:acacia_trapdoor",
    "minecraft:birch_trapdoor",
    "minecraft:dark_oak_trapdoor",
    "minecraft:jungle_trapdoor",
    "minecraft:oak_trapdoor",
    "minecraft:spruce_trapdoor"],
"minecraft:wool":["minecraft:white_wool",
    "minecraft:orange_wool",
    "minecraft:magenta_wool",
    "minecraft:light_blue_wool",
    "minecraft:yellow_wool",
    "minecraft:lime_wool",
    "minecraft:pink_wool",
    "minecraft:gray_wool",
    "minecraft:light_gray_wool",
    "minecraft:cyan_wool",
    "minecraft:purple_wool",
    "minecraft:blue_wool",
    "minecraft:brown_wool",
    "minecraft:green_wool",
    "minecraft:red_wool",
    "minecraft:black_wool"]}

max_stack_sizes = {"minecraft:acacia_boat":1,
"minecraft:acacia_button":64,
"minecraft:acacia_door":64,
"minecraft:acacia_fence":64,
"minecraft:acacia_fence_gate":64,
"minecraft:acacia_leaves":64,
"minecraft:acacia_log":64,
"minecraft:acacia_planks":64,
"minecraft:acacia_pressure_plate":64,
"minecraft:acacia_sapling":64,
"minecraft:acacia_sign":16,
"minecraft:acacia_slab":64,
"minecraft:acacia_stairs":64,
"minecraft:acacia_trapdoor":64,
"minecraft:acacia_wood":64,
"minecraft:activator_rail":64,
"minecraft:air":64,
"minecraft:allium":64,
"minecraft:andesite":64,
"minecraft:andesite_slab":64,
"minecraft:andesite_stairs":64,
"minecraft:andesite_wall":64,
"minecraft:anvil":64,
"minecraft:apple":64,
"minecraft:armor_stand":16,
"minecraft:arrow":64,
"minecraft:azure_bluet":64,
"minecraft:baked_potato":64,
"minecraft:bamboo":64,
"minecraft:barrel":64,
"minecraft:barrier":64,
"minecraft:bat_spawn_egg":64,
"minecraft:beacon":64,
"minecraft:bedrock":64,
"minecraft:beehive":64,
"minecraft:bee_nest":64,
"minecraft:beef":64,
"minecraft:beetroot":64,
"minecraft:beetroot_seeds":64,
"minecraft:beetroot_soup":1,
"minecraft:bell":64,
"minecraft:birch_boat":1,
"minecraft:birch_button":64,
"minecraft:birch_door":64,
"minecraft:birch_fence":64,
"minecraft:birch_fence_gate":64,
"minecraft:birch_leaves":64,
"minecraft:birch_log":64,
"minecraft:birch_planks":64,
"minecraft:birch_pressure_plate":64,
"minecraft:birch_sapling":64,
"minecraft:birch_sign":16,
"minecraft:birch_slab":64,
"minecraft:birch_stairs":64,
"minecraft:birch_trapdoor":64,
"minecraft:birch_wood":64,
"minecraft:black_banner":16,
"minecraft:black_bed":1,
"minecraft:black_carpet":64,
"minecraft:black_concrete":64,
"minecraft:black_concrete_powder":64,
"minecraft:black_dye":64,
"minecraft:black_glazed_terracotta":64,
"minecraft:black_shulker_box":64,
"minecraft:black_stained_glass":64,
"minecraft:black_stained_glass_pane":64,
"minecraft:black_terracotta":64,
"minecraft:black_wool":64,
"minecraft:blast_furnace":64,
"minecraft:blaze_powder":64,
"minecraft:blaze_rod":64,
"minecraft:blaze_spawn_egg":64,
"minecraft:blue_banner":16,
"minecraft:blue_bed":1,
"minecraft:blue_carpet":64,
"minecraft:blue_concrete":64,
"minecraft:blue_concrete_powder":64,
"minecraft:blue_dye":64,
"minecraft:blue_glazed_terracotta":64,
"minecraft:blue_ice":64,
"minecraft:blue_orchid":64,
"minecraft:blue_shulker_box":64,
"minecraft:blue_stained_glass":64,
"minecraft:blue_stained_glass_pane":64,
"minecraft:blue_terracotta":64,
"minecraft:blue_wool":64,
"minecraft:bone":64,
"minecraft:bone_block":64,
"minecraft:bone_meal":64,
"minecraft:book":64,
"minecraft:bookshelf":64,
"minecraft:bow":1,
"minecraft:bowl":64,
"minecraft:brain_coral":64,
"minecraft:brain_coral_block":64,
"minecraft:brain_coral_fan":64,
"minecraft:bread":64,
"minecraft:brewing_stand":64,
"minecraft:brick":64,
"minecraft:brick_slab":64,
"minecraft:brick_stairs":64,
"minecraft:brick_wall":64,
"minecraft:bricks":64,
"minecraft:brown_banner":16,
"minecraft:brown_bed":1,
"minecraft:brown_carpet":64,
"minecraft:brown_concrete":64,
"minecraft:brown_concrete_powder":64,
"minecraft:brown_dye":64,
"minecraft:brown_glazed_terracotta":64,
"minecraft:brown_mushroom":64,
"minecraft:brown_mushroom_block":64,
"minecraft:brown_shulker_box":64,
"minecraft:brown_stained_glass":64,
"minecraft:brown_stained_glass_pane":64,
"minecraft:brown_terracotta":64,
"minecraft:brown_wool":64,
"minecraft:bubble_coral":64,
"minecraft:bubble_coral_block":64,
"minecraft:bubble_coral_fan":64,
"minecraft:bucket":16,
"minecraft:cactus":64,
"minecraft:cake":1,
"minecraft:campfire":64,
"minecraft:carrot":64,
"minecraft:carrot_on_a_stick":1,
"minecraft:cartography_table":64,
"minecraft:carved_pumpkin":64,
"minecraft:cat_spawn_egg":64,
"minecraft:cauldron":64,
"minecraft:cave_spider_spawn_egg":64,
"minecraft:chain_command_block":64,
"minecraft:chainmail_boots":1,
"minecraft:chainmail_chestplate":1,
"minecraft:chainmail_helmet":1,
"minecraft:chainmail_leggings":1,
"minecraft:charcoal":64,
"minecraft:chest":64,
"minecraft:chest_minecart":1,
"minecraft:chicken":64,
"minecraft:chicken_spawn_egg":64,
"minecraft:chipped_anvil":64,
"minecraft:chiseled_quartz_block":64,
"minecraft:chiseled_red_sandstone":64,
"minecraft:chiseled_sandstone":64,
"minecraft:chiseled_stone_bricks":64,
"minecraft:chorus_flower":64,
"minecraft:chorus_fruit":64,
"minecraft:chorus_plant":64,
"minecraft:clay":64,
"minecraft:clay_ball":64,
"minecraft:clock":64,
"minecraft:coal":64,
"minecraft:coal_block":64,
"minecraft:coal_ore":64,
"minecraft:coarse_dirt":64,
"minecraft:cobblestone":64,
"minecraft:cobblestone_slab":64,
"minecraft:cobblestone_stairs":64,
"minecraft:cobblestone_wall":64,
"minecraft:cobweb":64,
"minecraft:cocoa_beans":64,
"minecraft:cod":64,
"minecraft:cod_bucket":1,
"minecraft:cod_spawn_egg":64,
"minecraft:command_block":64,
"minecraft:command_block_minecart":1,
"minecraft:comparator":64,
"minecraft:compass":64,
"minecraft:composter":64,
"minecraft:conduit":64,
"minecraft:cooked_beef":64,
"minecraft:cooked_chicken":64,
"minecraft:cooked_cod":64,
"minecraft:cooked_mutton":64,
"minecraft:cooked_porkchop":64,
"minecraft:cooked_rabbit":64,
"minecraft:cooked_salmon":64,
"minecraft:cookie":64,
"minecraft:cornflower":64,
"minecraft:cow_spawn_egg":64,
"minecraft:cracked_stone_bricks":64,
"minecraft:crafting_table":64,
"minecraft:creeper_banner_pattern":1,
"minecraft:creeper_head":64,
"minecraft:creeper_spawn_egg":64,
"minecraft:crossbow":1,
"minecraft:cut_red_sandstone":64,
"minecraft:cut_red_sandstone_slab":64,
"minecraft:cut_sandstone":64,
"minecraft:cut_sandstone_slab":64,
"minecraft:cyan_banner":16,
"minecraft:cyan_bed":1,
"minecraft:cyan_carpet":64,
"minecraft:cyan_concrete":64,
"minecraft:cyan_concrete_powder":64,
"minecraft:cyan_dye":64,
"minecraft:cyan_glazed_terracotta":64,
"minecraft:cyan_shulker_box":64,
"minecraft:cyan_stained_glass":64,
"minecraft:cyan_stained_glass_pane":64,
"minecraft:cyan_terracotta":64,
"minecraft:cyan_wool":64,
"minecraft:damaged_anvil":64,
"minecraft:dandelion":64,
"minecraft:dark_oak_boat":1,
"minecraft:dark_oak_button":64,
"minecraft:dark_oak_door":64,
"minecraft:dark_oak_fence":64,
"minecraft:dark_oak_fence_gate":64,
"minecraft:dark_oak_leaves":64,
"minecraft:dark_oak_log":64,
"minecraft:dark_oak_planks":64,
"minecraft:dark_oak_pressure_plate":64,
"minecraft:dark_oak_sapling":64,
"minecraft:dark_oak_sign":16,
"minecraft:dark_oak_slab":64,
"minecraft:dark_oak_stairs":64,
"minecraft:dark_oak_trapdoor":64,
"minecraft:dark_oak_wood":64,
"minecraft:dark_prismarine":64,
"minecraft:dark_prismarine_slab":64,
"minecraft:dark_prismarine_stairs":64,
"minecraft:daylight_detector":64,
"minecraft:dead_brain_coral":64,
"minecraft:dead_brain_coral_block":64,
"minecraft:dead_brain_coral_fan":64,
"minecraft:dead_bubble_coral":64,
"minecraft:dead_bubble_coral_block":64,
"minecraft:dead_bubble_coral_fan":64,
"minecraft:dead_bush":64,
"minecraft:dead_fire_coral":64,
"minecraft:dead_fire_coral_block":64,
"minecraft:dead_fire_coral_fan":64,
"minecraft:dead_horn_coral":64,
"minecraft:dead_horn_coral_block":64,
"minecraft:dead_horn_coral_fan":64,
"minecraft:dead_tube_coral":64,
"minecraft:dead_tube_coral_block":64,
"minecraft:dead_tube_coral_fan":64,
"minecraft:detector_rail":64,
"minecraft:diamond":64,
"minecraft:diamond_axe":1,
"minecraft:diamond_block":64,
"minecraft:diamond_boots":1,
"minecraft:diamond_chestplate":1,
"minecraft:diamond_helmet":1,
"minecraft:diamond_hoe":1,
"minecraft:diamond_horse_armor":1,
"minecraft:diamond_leggings":1,
"minecraft:diamond_ore":64,
"minecraft:diamond_pickaxe":1,
"minecraft:diamond_shovel":1,
"minecraft:diamond_sword":1,
"minecraft:diorite":64,
"minecraft:diorite_slab":64,
"minecraft:diorite_stairs":64,
"minecraft:diorite_wall":64,
"minecraft:dirt":64,
"minecraft:dispenser":64,
"minecraft:dolphin_spawn_egg":64,
"minecraft:donkey_spawn_egg":64,
"minecraft:dragon_breath":64,
"minecraft:dragon_egg":64,
"minecraft:dragon_head":64,
"minecraft:dried_kelp":64,
"minecraft:dried_kelp_block":64,
"minecraft:dropper":64,
"minecraft:drowned_spawn_egg":64,
"minecraft:egg":16,
"minecraft:elder_guardian_spawn_egg":64,
"minecraft:elytra":1,
"minecraft:emerald":64,
"minecraft:emerald_block":64,
"minecraft:emerald_ore":64,
"minecraft:enchanted_book":1,
"minecraft:enchanted_golden_apple":64,
"minecraft:enchanting_table":64,
"minecraft:end_crystal":64,
"minecraft:end_portal_frame":64,
"minecraft:end_rod":64,
"minecraft:end_stone":64,
"minecraft:end_stone_brick_slab":64,
"minecraft:end_stone_brick_stairs":64,
"minecraft:end_stone_brick_wall":64,
"minecraft:end_stone_bricks":64,
"minecraft:ender_chest":64,
"minecraft:ender_eye":64,
"minecraft:ender_pearl":16,
"minecraft:enderman_spawn_egg":64,
"minecraft:endermite_spawn_egg":64,
"minecraft:evoker_spawn_egg":64,
"minecraft:experience_bottle":64,
"minecraft:farmland":64,
"minecraft:feather":64,
"minecraft:fermented_spider_eye":64,
"minecraft:fern":64,
"minecraft:filled_map":64,
"minecraft:fire_charge":64,
"minecraft:fire_coral":64,
"minecraft:fire_coral_block":64,
"minecraft:fire_coral_fan":64,
"minecraft:firework_rocket":64,
"minecraft:firework_star":64,
"minecraft:fishing_rod":1,
"minecraft:fletching_table":64,
"minecraft:flint":64,
"minecraft:flint_and_steel":1,
"minecraft:flower_banner_pattern":1,
"minecraft:flower_pot":64,
"minecraft:fox_spawn_egg":64,
"minecraft:furnace":64,
"minecraft:furnace_minecart":1,
"minecraft:ghast_spawn_egg":64,
"minecraft:ghast_tear":64,
"minecraft:glass":64,
"minecraft:glass_bottle":64,
"minecraft:glass_pane":64,
"minecraft:glistering_melon_slice":64,
"minecraft:globe_banner_pattern":1,
"minecraft:glowstone":64,
"minecraft:glowstone_dust":64,
"minecraft:gold_block":64,
"minecraft:gold_ingot":64,
"minecraft:gold_nugget":64,
"minecraft:gold_ore":64,
"minecraft:golden_apple":64,
"minecraft:golden_axe":1,
"minecraft:golden_boots":1,
"minecraft:golden_carrot":64,
"minecraft:golden_chestplate":1,
"minecraft:golden_helmet":1,
"minecraft:golden_hoe":1,
"minecraft:golden_horse_armor":1,
"minecraft:golden_leggings":1,
"minecraft:golden_pickaxe":1,
"minecraft:golden_shovel":1,
"minecraft:golden_sword":1,
"minecraft:granite":64,
"minecraft:granite_slab":64,
"minecraft:granite_stairs":64,
"minecraft:granite_wall":64,
"minecraft:grass":64,
"minecraft:grass_block":64,
"minecraft:grass_path":64,
"minecraft:gravel":64,
"minecraft:gray_banner":16,
"minecraft:gray_bed":1,
"minecraft:gray_carpet":64,
"minecraft:gray_concrete":64,
"minecraft:gray_concrete_powder":64,
"minecraft:gray_dye":64,
"minecraft:gray_glazed_terracotta":64,
"minecraft:gray_shulker_box":64,
"minecraft:gray_stained_glass":64,
"minecraft:gray_stained_glass_pane":64,
"minecraft:gray_terracotta":64,
"minecraft:gray_wool":64,
"minecraft:green_banner":16,
"minecraft:green_bed":1,
"minecraft:green_carpet":64,
"minecraft:green_concrete":64,
"minecraft:green_concrete_powder":64,
"minecraft:green_dye":64,
"minecraft:green_glazed_terracotta":64,
"minecraft:green_shulker_box":64,
"minecraft:green_stained_glass":64,
"minecraft:green_stained_glass_pane":64,
"minecraft:green_terracotta":64,
"minecraft:green_wool":64,
"minecraft:grindstone":64,
"minecraft:guardian_spawn_egg":64,
"minecraft:gunpowder":64,
"minecraft:hay_block":64,
"minecraft:heart_of_the_sea":64,
"minecraft:heavy_weighted_pressure_plate":64,
"minecraft:honey_block":64,
"minecraft:honey_bottle":16,
"minecraft:honeycomb":64,
"minecraft:honeycomb_block":64,
"minecraft:hopper":64,
"minecraft:hopper_minecart":1,
"minecraft:horn_coral":64,
"minecraft:horn_coral_block":64,
"minecraft:horn_coral_fan":64,
"minecraft:horse_spawn_egg":64,
"minecraft:husk_spawn_egg":64,
"minecraft:ice":64,
"minecraft:infested_chiseled_stone_bricks":64,
"minecraft:infested_cobblestone":64,
"minecraft:infested_cracked_stone_bricks":64,
"minecraft:infested_mossy_stone_bricks":64,
"minecraft:infested_stone":64,
"minecraft:infested_stone_bricks":64,
"minecraft:ink_sac":64,
"minecraft:iron_axe":1,
"minecraft:iron_bars":64,
"minecraft:iron_block":64,
"minecraft:iron_boots":1,
"minecraft:iron_chestplate":1,
"minecraft:iron_door":64,
"minecraft:iron_helmet":1,
"minecraft:iron_hoe":1,
"minecraft:iron_horse_armor":1,
"minecraft:iron_ingot":64,
"minecraft:iron_leggings":1,
"minecraft:iron_nugget":64,
"minecraft:iron_ore":64,
"minecraft:iron_pickaxe":1,
"minecraft:iron_shovel":1,
"minecraft:iron_sword":1,
"minecraft:iron_trapdoor":64,
"minecraft:item_frame":64,
"minecraft:jack_o_lantern":64,
"minecraft:jukebox":64,
"minecraft:jungle_boat":1,
"minecraft:jungle_button":64,
"minecraft:jungle_door":64,
"minecraft:jungle_fence":64,
"minecraft:jungle_fence_gate":64,
"minecraft:jungle_leaves":64,
"minecraft:jungle_log":64,
"minecraft:jungle_planks":64,
"minecraft:jungle_pressure_plate":64,
"minecraft:jungle_sapling":64,
"minecraft:jungle_sign":16,
"minecraft:jungle_slab":64,
"minecraft:jungle_stairs":64,
"minecraft:jungle_trapdoor":64,
"minecraft:jungle_wood":64,
"minecraft:kelp":64,
"minecraft:ladder":64,
"minecraft:lantern":64,
"minecraft:lapis_block":64,
"minecraft:lapis_lazuli":64,
"minecraft:lapis_ore":64,
"minecraft:large_fern":64,
"minecraft:lava_bucket":1,
"minecraft:lead":64,
"minecraft:leather":64,
"minecraft:leather_boots":1,
"minecraft:leather_chestplate":1,
"minecraft:leather_helmet":1,
"minecraft:leather_horse_armor":1,
"minecraft:leather_leggings":1,
"minecraft:lectern":64,
"minecraft:lever":64,
"minecraft:light_blue_banner":16,
"minecraft:light_blue_bed":1,
"minecraft:light_blue_carpet":64,
"minecraft:light_blue_concrete":64,
"minecraft:light_blue_concrete_powder":64,
"minecraft:light_blue_dye":64,
"minecraft:light_blue_glazed_terracotta":64,
"minecraft:light_blue_shulker_box":64,
"minecraft:light_blue_stained_glass":64,
"minecraft:light_blue_stained_glass_pane":64,
"minecraft:light_blue_terracotta":64,
"minecraft:light_blue_wool":64,
"minecraft:light_gray_banner":16,
"minecraft:light_gray_bed":1,
"minecraft:light_gray_carpet":64,
"minecraft:light_gray_concrete":64,
"minecraft:light_gray_concrete_powder":64,
"minecraft:light_gray_dye":64,
"minecraft:light_gray_glazed_terracotta":64,
"minecraft:light_gray_shulker_box":64,
"minecraft:light_gray_stained_glass":64,
"minecraft:light_gray_stained_glass_pane":64,
"minecraft:light_gray_terracotta":64,
"minecraft:light_gray_wool":64,
"minecraft:light_weighted_pressure_plate":64,
"minecraft:lilac":64,
"minecraft:lily_of_the_valley":64,
"minecraft:lily_pad":64,
"minecraft:lime_banner":16,
"minecraft:lime_bed":1,
"minecraft:lime_carpet":64,
"minecraft:lime_concrete":64,
"minecraft:lime_concrete_powder":64,
"minecraft:lime_dye":64,
"minecraft:lime_glazed_terracotta":64,
"minecraft:lime_shulker_box":64,
"minecraft:lime_stained_glass":64,
"minecraft:lime_stained_glass_pane":64,
"minecraft:lime_terracotta":64,
"minecraft:lime_wool":64,
"minecraft:lingering_potion":1,
"minecraft:llama_spawn_egg":64,
"minecraft:loom":64,
"minecraft:magenta_banner":16,
"minecraft:magenta_bed":1,
"minecraft:magenta_carpet":64,
"minecraft:magenta_concrete":64,
"minecraft:magenta_concrete_powder":64,
"minecraft:magenta_dye":64,
"minecraft:magenta_glazed_terracotta":64,
"minecraft:magenta_shulker_box":64,
"minecraft:magenta_stained_glass":64,
"minecraft:magenta_stained_glass_pane":64,
"minecraft:magenta_terracotta":64,
"minecraft:magenta_wool":64,
"minecraft:magma_block":64,
"minecraft:magma_cream":64,
"minecraft:magma_cube_spawn_egg":64,
"minecraft:map":64,
"minecraft:melon":64,
"minecraft:melon_seeds":64,
"minecraft:melon_slice":64,
"minecraft:milk_bucket":1,
"minecraft:minecart":1,
"minecraft:mojang_banner_pattern":1,
"minecraft:mooshroom_spawn_egg":64,
"minecraft:mossy_cobblestone":64,
"minecraft:mossy_cobblestone_slab":64,
"minecraft:mossy_cobblestone_stairs":64,
"minecraft:mossy_cobblestone_wall":64,
"minecraft:mossy_stone_brick_slab":64,
"minecraft:mossy_stone_brick_stairs":64,
"minecraft:mossy_stone_brick_wall":64,
"minecraft:mossy_stone_bricks":64,
"minecraft:mule_spawn_egg":64,
"minecraft:mushroom_stem":64,
"minecraft:mushroom_stew":1,
"minecraft:music_disc_11":1,
"minecraft:music_disc_13":1,
"minecraft:music_disc_blocks":1,
"minecraft:music_disc_cat":1,
"minecraft:music_disc_chirp":1,
"minecraft:music_disc_far":1,
"minecraft:music_disc_mall":1,
"minecraft:music_disc_mellohi":1,
"minecraft:music_disc_stal":1,
"minecraft:music_disc_strad":1,
"minecraft:music_disc_wait":1,
"minecraft:music_disc_ward":1,
"minecraft:mutton":64,
"minecraft:mycelium":64,
"minecraft:name_tag":64,
"minecraft:nautilus_shell":64,
"minecraft:nether_brick":64,
"minecraft:nether_brick_fence":64,
"minecraft:nether_brick_slab":64,
"minecraft:nether_brick_stairs":64,
"minecraft:nether_brick_wall":64,
"minecraft:nether_bricks":64,
"minecraft:nether_quartz_ore":64,
"minecraft:nether_star":64,
"minecraft:nether_wart":64,
"minecraft:nether_wart_block":64,
"minecraft:netherrack":64,
"minecraft:note_block":64,
"minecraft:oak_boat":1,
"minecraft:oak_button":64,
"minecraft:oak_door":64,
"minecraft:oak_fence":64,
"minecraft:oak_fence_gate":64,
"minecraft:oak_leaves":64,
"minecraft:oak_log":64,
"minecraft:oak_planks":64,
"minecraft:oak_pressure_plate":64,
"minecraft:oak_sapling":64,
"minecraft:oak_sign":16,
"minecraft:oak_slab":64,
"minecraft:oak_stairs":64,
"minecraft:oak_trapdoor":64,
"minecraft:oak_wood":64,
"minecraft:observer":64,
"minecraft:obsidian":64,
"minecraft:ocelot_spawn_egg":64,
"minecraft:orange_banner":16,
"minecraft:orange_bed":1,
"minecraft:orange_carpet":64,
"minecraft:orange_concrete":64,
"minecraft:orange_concrete_powder":64,
"minecraft:orange_dye":64,
"minecraft:orange_glazed_terracotta":64,
"minecraft:orange_shulker_box":64,
"minecraft:orange_stained_glass":64,
"minecraft:orange_stained_glass_pane":64,
"minecraft:orange_terracotta":64,
"minecraft:orange_tulip":64,
"minecraft:orange_wool":64,
"minecraft:oxeye_daisy":64,
"minecraft:packed_ice":64,
"minecraft:painting":64,
"minecraft:panda_spawn_egg":64,
"minecraft:paper":64,
"minecraft:parrot_spawn_egg":64,
"minecraft:peony":64,
"minecraft:petrified_oak_slab":64,
"minecraft:phantom_membrane":64,
"minecraft:phantom_spawn_egg":64,
"minecraft:pig_spawn_egg":64,
"minecraft:pillager_spawn_egg":64,
"minecraft:pink_banner":16,
"minecraft:pink_bed":1,
"minecraft:pink_carpet":64,
"minecraft:pink_concrete":64,
"minecraft:pink_concrete_powder":64,
"minecraft:pink_dye":64,
"minecraft:pink_glazed_terracotta":64,
"minecraft:pink_shulker_box":64,
"minecraft:pink_stained_glass":64,
"minecraft:pink_stained_glass_pane":64,
"minecraft:pink_terracotta":64,
"minecraft:pink_tulip":64,
"minecraft:pink_wool":64,
"minecraft:piston":64,
"minecraft:player_head":64,
"minecraft:podzol":64,
"minecraft:poisonous_potato":64,
"minecraft:polar_bear_spawn_egg":64,
"minecraft:polished_andesite":64,
"minecraft:polished_andesite_slab":64,
"minecraft:polished_andesite_stairs":64,
"minecraft:polished_diorite":64,
"minecraft:polished_diorite_slab":64,
"minecraft:polished_diorite_stairs":64,
"minecraft:polished_granite":64,
"minecraft:polished_granite_slab":64,
"minecraft:polished_granite_stairs":64,
"minecraft:popped_chorus_fruit":64,
"minecraft:poppy":64,
"minecraft:porkchop":64,
"minecraft:potato":64,
"minecraft:potion":1,
"minecraft:powered_rail":64,
"minecraft:prismarine":64,
"minecraft:prismarine_brick_slab":64,
"minecraft:prismarine_brick_stairs":64,
"minecraft:prismarine_bricks":64,
"minecraft:prismarine_crystals":64,
"minecraft:prismarine_shard":64,
"minecraft:prismarine_slab":64,
"minecraft:prismarine_stairs":64,
"minecraft:prismarine_wall":64,
"minecraft:pufferfish":64,
"minecraft:pufferfish_bucket":1,
"minecraft:pufferfish_spawn_egg":64,
"minecraft:pumpkin":64,
"minecraft:pumpkin_pie":64,
"minecraft:pumpkin_seeds":64,
"minecraft:purple_banner":16,
"minecraft:purple_bed":1,
"minecraft:purple_carpet":64,
"minecraft:purple_concrete":64,
"minecraft:purple_concrete_powder":64,
"minecraft:purple_dye":64,
"minecraft:purple_glazed_terracotta":64,
"minecraft:purple_shulker_box":64,
"minecraft:purple_stained_glass":64,
"minecraft:purple_stained_glass_pane":64,
"minecraft:purple_terracotta":64,
"minecraft:purple_wool":64,
"minecraft:purpur_block":64,
"minecraft:purpur_pillar":64,
"minecraft:purpur_slab":64,
"minecraft:purpur_stairs":64,
"minecraft:quartz":64,
"minecraft:quartz_block":64,
"minecraft:quartz_pillar":64,
"minecraft:quartz_slab":64,
"minecraft:quartz_stairs":64,
"minecraft:rabbit":64,
"minecraft:rabbit_foot":64,
"minecraft:rabbit_hide":64,
"minecraft:rabbit_spawn_egg":64,
"minecraft:rabbit_stew":1,
"minecraft:rail":64,
"minecraft:ravager_spawn_egg":64,
"minecraft:red_banner":16,
"minecraft:red_bed":1,
"minecraft:red_carpet":64,
"minecraft:red_concrete":64,
"minecraft:red_concrete_powder":64,
"minecraft:red_dye":64,
"minecraft:red_glazed_terracotta":64,
"minecraft:red_mushroom":64,
"minecraft:red_mushroom_block":64,
"minecraft:red_nether_brick_slab":64,
"minecraft:red_nether_brick_stairs":64,
"minecraft:red_nether_brick_wall":64,
"minecraft:red_nether_bricks":64,
"minecraft:red_sand":64,
"minecraft:red_sandstone":64,
"minecraft:red_sandstone_slab":64,
"minecraft:red_sandstone_stairs":64,
"minecraft:red_sandstone_wall":64,
"minecraft:red_shulker_box":64,
"minecraft:red_stained_glass":64,
"minecraft:red_stained_glass_pane":64,
"minecraft:red_terracotta":64,
"minecraft:red_tulip":64,
"minecraft:red_wool":64,
"minecraft:redstone":64,
"minecraft:redstone_block":64,
"minecraft:redstone_lamp":64,
"minecraft:redstone_ore":64,
"minecraft:redstone_torch":64,
"minecraft:repeater":64,
"minecraft:repeating_command_block":64,
"minecraft:rose_bush":64,
"minecraft:rotten_flesh":64,
"minecraft:saddle":1,
"minecraft:salmon":64,
"minecraft:salmon_bucket":1,
"minecraft:salmon_spawn_egg":64,
"minecraft:sand":64,
"minecraft:sandstone":64,
"minecraft:sandstone_slab":64,
"minecraft:sandstone_stairs":64,
"minecraft:sandstone_wall":64,
"minecraft:scaffolding":64,
"minecraft:scute":64,
"minecraft:sea_lantern":64,
"minecraft:sea_pickle":64,
"minecraft:seagrass":64,
"minecraft:shears":1,
"minecraft:sheep_spawn_egg":64,
"minecraft:shield":1,
"minecraft:shulker_box":64,
"minecraft:shulker_shell":64,
"minecraft:shulker_spawn_egg":64,
"minecraft:silverfish_spawn_egg":64,
"minecraft:skeleton_horse_spawn_egg":64,
"minecraft:skeleton_skull":64,
"minecraft:skeleton_spawn_egg":64,
"minecraft:skull_banner_pattern":1,
"minecraft:slime_ball":64,
"minecraft:slime_block":64,
"minecraft:slime_spawn_egg":64,
"minecraft:smithing_table":64,
"minecraft:smoker":64,
"minecraft:smooth_quartz":64,
"minecraft:smooth_quartz_slab":64,
"minecraft:smooth_quartz_stairs":64,
"minecraft:smooth_red_sandstone":64,
"minecraft:smooth_red_sandstone_slab":64,
"minecraft:smooth_red_sandstone_stairs":64,
"minecraft:smooth_sandstone":64,
"minecraft:smooth_sandstone_slab":64,
"minecraft:smooth_sandstone_stairs":64,
"minecraft:smooth_stone":64,
"minecraft:smooth_stone_slab":64,
"minecraft:snow":64,
"minecraft:snow_block":64,
"minecraft:snowball":16,
"minecraft:soul_sand":64,
"minecraft:spawner":64,
"minecraft:spectral_arrow":64,
"minecraft:spider_eye":64,
"minecraft:spider_spawn_egg":64,
"minecraft:splash_potion":1,
"minecraft:sponge":64,
"minecraft:spruce_boat":1,
"minecraft:spruce_button":64,
"minecraft:spruce_door":64,
"minecraft:spruce_fence":64,
"minecraft:spruce_fence_gate":64,
"minecraft:spruce_leaves":64,
"minecraft:spruce_log":64,
"minecraft:spruce_planks":64,
"minecraft:spruce_pressure_plate":64,
"minecraft:spruce_sapling":64,
"minecraft:spruce_sign":16,
"minecraft:spruce_slab":64,
"minecraft:spruce_stairs":64,
"minecraft:spruce_trapdoor":64,
"minecraft:spruce_wood":64,
"minecraft:squid_spawn_egg":64,
"minecraft:stick":64,
"minecraft:sticky_piston":64,
"minecraft:stone":64,
"minecraft:stone_axe":1,
"minecraft:stone_brick_slab":64,
"minecraft:stone_brick_stairs":64,
"minecraft:stone_brick_wall":64,
"minecraft:stone_bricks":64,
"minecraft:stone_button":64,
"minecraft:stone_hoe":1,
"minecraft:stone_pickaxe":1,
"minecraft:stone_pressure_plate":64,
"minecraft:stone_shovel":1,
"minecraft:stone_slab":64,
"minecraft:stone_stairs":64,
"minecraft:stone_sword":1,
"minecraft:stray_spawn_egg":64,
"minecraft:string":64,
"minecraft:stripped_acacia_log":64,
"minecraft:stripped_acacia_wood":64,
"minecraft:stripped_birch_log":64,
"minecraft:stripped_birch_wood":64,
"minecraft:stripped_dark_oak_log":64,
"minecraft:stripped_dark_oak_wood":64,
"minecraft:stripped_jungle_log":64,
"minecraft:stripped_jungle_wood":64,
"minecraft:stripped_oak_log":64,
"minecraft:stripped_oak_wood":64,
"minecraft:stripped_spruce_log":64,
"minecraft:stripped_spruce_wood":64,
"minecraft:structure_block":64,
"minecraft:structure_void":64,
"minecraft:sugar":64,
"minecraft:sugar_cane":64,
"minecraft:sunflower":64,
"minecraft:sweet_berries":64,
"minecraft:tall_grass":64,
"minecraft:terracotta":64,
"minecraft:tipped_arrow":64,
"minecraft:tnt":64,
"minecraft:tnt_minecart":1,
"minecraft:torch":64,
"minecraft:totem_of_undying":1,
"minecraft:trader_llama_spawn_egg":64,
"minecraft:trapped_chest":64,
"minecraft:trident":1,
"minecraft:tripwire_hook":64,
"minecraft:tropical_fish":64,
"minecraft:tropical_fish_bucket":1,
"minecraft:tropical_fish_spawn_egg":64,
"minecraft:tube_coral":64,
"minecraft:tube_coral_block":64,
"minecraft:tube_coral_fan":64,
"minecraft:turtle_egg":64,
"minecraft:turtle_helmet":1,
"minecraft:turtle_spawn_egg":64,
"minecraft:vex_spawn_egg":64,
"minecraft:villager_spawn_egg":64,
"minecraft:vindicator_spawn_egg":64,
"minecraft:vine":64,
"minecraft:wandering_trader_spawn_egg":64,
"minecraft:water_bucket":1,
"minecraft:wet_sponge":64,
"minecraft:wheat":64,
"minecraft:wheat_seeds":64,
"minecraft:white_banner":16,
"minecraft:white_bed":1,
"minecraft:white_carpet":64,
"minecraft:white_concrete":64,
"minecraft:white_concrete_powder":64,
"minecraft:white_dye":64,
"minecraft:white_glazed_terracotta":64,
"minecraft:white_shulker_box":64,
"minecraft:white_stained_glass":64,
"minecraft:white_stained_glass_pane":64,
"minecraft:white_terracotta":64,
"minecraft:white_tulip":64,
"minecraft:white_wool":64,
"minecraft:witch_spawn_egg":64,
"minecraft:wither_rose":64,
"minecraft:wither_skeleton_skull":64,
"minecraft:wither_skeleton_spawn_egg":64,
"minecraft:wolf_spawn_egg":64,
"minecraft:wooden_axe":1,
"minecraft:wooden_hoe":1,
"minecraft:wooden_pickaxe":1,
"minecraft:wooden_shovel":1,
"minecraft:wooden_sword":1,
"minecraft:writable_book":1,
"minecraft:written_book":1,
"minecraft:yellow_banner":16,
"minecraft:yellow_bed":1,
"minecraft:yellow_carpet":64,
"minecraft:yellow_concrete":64,
"minecraft:yellow_concrete_powder":64,
"minecraft:yellow_dye":64,
"minecraft:yellow_glazed_terracotta":64,
"minecraft:yellow_shulker_box":64,
"minecraft:yellow_stained_glass":64,
"minecraft:yellow_stained_glass_pane":64,
"minecraft:yellow_terracotta":64,
"minecraft:yellow_wool":64,
"minecraft:zombie_head":64,
"minecraft:zombie_horse_spawn_egg":64,
"minecraft:zombie_pigman_spawn_egg":64,
"minecraft:zombie_spawn_egg":64,
"minecraft:zombie_villager_spawn_egg":64}

vanilla_ingredients = {
    "minecraft:acacia_log": [
        "charcoal.json"
    ],
    "minecraft:acacia_wood": [
        "charcoal.json"
    ],
    "minecraft:beef": [
        "cooked_beef.json",
        "cooked_beef_from_smoking.json"
    ],
    "minecraft:birch_log": [
        "charcoal.json"
    ],
    "minecraft:birch_wood": [
        "charcoal.json"
    ],
    "minecraft:black_terracotta": [
        "black_glazed_terracotta.json"
    ],
    "minecraft:blue_terracotta": [
        "blue_glazed_terracotta.json"
    ],
    "minecraft:brown_terracotta": [
        "brown_glazed_terracotta.json"
    ],
    "minecraft:cactus": [
        "green_dye.json"
    ],
    "minecraft:chainmail_boots": [
        "iron_nugget_from_blasting.json",
        "iron_nugget_from_smelting.json"
    ],
    "minecraft:chainmail_chestplate": [
        "iron_nugget_from_blasting.json",
        "iron_nugget_from_smelting.json"
    ],
    "minecraft:chainmail_helmet": [
        "iron_nugget_from_blasting.json",
        "iron_nugget_from_smelting.json"
    ],
    "minecraft:chainmail_leggings": [
        "iron_nugget_from_blasting.json",
        "iron_nugget_from_smelting.json"
    ],
    "minecraft:chicken": [
        "cooked_chicken.json",
        "cooked_chicken_from_smoking.json"
    ],
    "minecraft:chorus_fruit": [
        "popped_chorus_fruit.json"
    ],
    "minecraft:clay": [
        "terracotta.json"
    ],
    "minecraft:clay_ball": [
        "brick.json"
    ],
    "minecraft:coal_ore": [
        "coal_from_blasting.json",
        "coal_from_smelting.json"
    ],
    "minecraft:cobblestone": [
        "stone.json"
    ],
    "minecraft:cod": [
        "cooked_cod.json",
        "cooked_cod_from_smoking.json"
    ],
    "minecraft:cyan_terracotta": [
        "cyan_glazed_terracotta.json"
    ],
    "minecraft:dark_oak_log": [
        "charcoal.json"
    ],
    "minecraft:dark_oak_wood": [
        "charcoal.json"
    ],
    "minecraft:diamond_ore": [
        "diamond_from_blasting.json",
        "diamond_from_smelting.json"
    ],
    "minecraft:emerald_ore": [
        "emerald_from_blasting.json",
        "emerald_from_smelting.json"
    ],
    "minecraft:gold_ore": [
        "gold_ingot.json",
        "gold_ingot_from_blasting.json"
    ],
    "minecraft:golden_axe": [
        "gold_nugget_from_blasting.json",
        "gold_nugget_from_smelting.json"
    ],
    "minecraft:golden_boots": [
        "gold_nugget_from_blasting.json",
        "gold_nugget_from_smelting.json"
    ],
    "minecraft:golden_chestplate": [
        "gold_nugget_from_blasting.json",
        "gold_nugget_from_smelting.json"
    ],
    "minecraft:golden_helmet": [
        "gold_nugget_from_blasting.json",
        "gold_nugget_from_smelting.json"
    ],
    "minecraft:golden_hoe": [
        "gold_nugget_from_blasting.json",
        "gold_nugget_from_smelting.json"
    ],
    "minecraft:golden_horse_armor": [
        "gold_nugget_from_blasting.json",
        "gold_nugget_from_smelting.json"
    ],
    "minecraft:golden_leggings": [
        "gold_nugget_from_blasting.json",
        "gold_nugget_from_smelting.json"
    ],
    "minecraft:golden_pickaxe": [
        "gold_nugget_from_blasting.json",
        "gold_nugget_from_smelting.json"
    ],
    "minecraft:golden_shovel": [
        "gold_nugget_from_blasting.json",
        "gold_nugget_from_smelting.json"
    ],
    "minecraft:golden_sword": [
        "gold_nugget_from_blasting.json",
        "gold_nugget_from_smelting.json"
    ],
    "minecraft:gray_terracotta": [
        "gray_glazed_terracotta.json"
    ],
    "minecraft:green_terracotta": [
        "green_glazed_terracotta.json"
    ],
    "minecraft:iron_axe": [
        "iron_nugget_from_blasting.json",
        "iron_nugget_from_smelting.json"
    ],
    "minecraft:iron_boots": [
        "iron_nugget_from_blasting.json",
        "iron_nugget_from_smelting.json"
    ],
    "minecraft:iron_chestplate": [
        "iron_nugget_from_blasting.json",
        "iron_nugget_from_smelting.json"
    ],
    "minecraft:iron_helmet": [
        "iron_nugget_from_blasting.json",
        "iron_nugget_from_smelting.json"
    ],
    "minecraft:iron_hoe": [
        "iron_nugget_from_blasting.json",
        "iron_nugget_from_smelting.json"
    ],
    "minecraft:iron_horse_armor": [
        "iron_nugget_from_blasting.json",
        "iron_nugget_from_smelting.json"
    ],
    "minecraft:iron_leggings": [
        "iron_nugget_from_blasting.json",
        "iron_nugget_from_smelting.json"
    ],
    "minecraft:iron_ore": [
        "iron_ingot.json",
        "iron_ingot_from_blasting.json"
    ],
    "minecraft:iron_pickaxe": [
        "iron_nugget_from_blasting.json",
        "iron_nugget_from_smelting.json"
    ],
    "minecraft:iron_shovel": [
        "iron_nugget_from_blasting.json",
        "iron_nugget_from_smelting.json"
    ],
    "minecraft:iron_sword": [
        "iron_nugget_from_blasting.json",
        "iron_nugget_from_smelting.json"
    ],
    "minecraft:jungle_log": [
        "charcoal.json"
    ],
    "minecraft:jungle_wood": [
        "charcoal.json"
    ],
    "minecraft:kelp": [
        "dried_kelp_from_smelting.json",
        "dried_kelp_from_smoking.json"
    ],
    "minecraft:lapis_ore": [
        "lapis_from_blasting.json",
        "lapis_from_smelting.json"
    ],
    "minecraft:light_blue_terracotta": [
        "light_blue_glazed_terracotta.json"
    ],
    "minecraft:light_gray_terracotta": [
        "light_gray_glazed_terracotta.json"
    ],
    "minecraft:lime_terracotta": [
        "lime_glazed_terracotta.json"
    ],
    "minecraft:magenta_terracotta": [
        "magenta_glazed_terracotta.json"
    ],
    "minecraft:mutton": [
        "cooked_mutton.json",
        "cooked_mutton_from_smoking.json"
    ],
    "minecraft:nether_quartz_ore": [
        "quartz.json",
        "quartz_from_blasting.json"
    ],
    "minecraft:netherrack": [
        "nether_brick.json"
    ],
    "minecraft:oak_log": [
        "charcoal.json"
    ],
    "minecraft:oak_wood": [
        "charcoal.json"
    ],
    "minecraft:orange_terracotta": [
        "orange_glazed_terracotta.json"
    ],
    "minecraft:pink_terracotta": [
        "pink_glazed_terracotta.json"
    ],
    "minecraft:porkchop": [
        "cooked_porkchop.json",
        "cooked_porkchop_from_smoking.json"
    ],
    "minecraft:potato": [
        "baked_potato.json",
        "baked_potato_from_smoking.json"
    ],
    "minecraft:purple_terracotta": [
        "purple_glazed_terracotta.json"
    ],
    "minecraft:quartz_block": [
        "smooth_quartz.json"
    ],
    "minecraft:rabbit": [
        "cooked_rabbit.json",
        "cooked_rabbit_from_smoking.json"
    ],
    "minecraft:red_sand": [
        "glass.json"
    ],
    "minecraft:red_sandstone": [
        "smooth_red_sandstone.json"
    ],
    "minecraft:red_terracotta": [
        "red_glazed_terracotta.json"
    ],
    "minecraft:redstone_ore": [
        "redstone_from_blasting.json",
        "redstone_from_smelting.json"
    ],
    "minecraft:salmon": [
        "cooked_salmon.json",
        "cooked_salmon_from_smoking.json"
    ],
    "minecraft:sand": [
        "glass.json"
    ],
    "minecraft:sandstone": [
        "smooth_sandstone.json"
    ],
    "minecraft:sea_pickle": [
        "lime_dye_from_smelting.json"
    ],
    "minecraft:spruce_log": [
        "charcoal.json"
    ],
    "minecraft:spruce_wood": [
        "charcoal.json"
    ],
    "minecraft:stone": [
        "smooth_stone.json"
    ],
    "minecraft:stone_bricks": [
        "cracked_stone_bricks.json"
    ],
    "minecraft:stripped_acacia_log": [
        "charcoal.json"
    ],
    "minecraft:stripped_acacia_wood": [
        "charcoal.json"
    ],
    "minecraft:stripped_birch_log": [
        "charcoal.json"
    ],
    "minecraft:stripped_birch_wood": [
        "charcoal.json"
    ],
    "minecraft:stripped_dark_oak_log": [
        "charcoal.json"
    ],
    "minecraft:stripped_dark_oak_wood": [
        "charcoal.json"
    ],
    "minecraft:stripped_jungle_log": [
        "charcoal.json"
    ],
    "minecraft:stripped_jungle_wood": [
        "charcoal.json"
    ],
    "minecraft:stripped_oak_log": [
        "charcoal.json"
    ],
    "minecraft:stripped_oak_wood": [
        "charcoal.json"
    ],
    "minecraft:stripped_spruce_log": [
        "charcoal.json"
    ],
    "minecraft:stripped_spruce_wood": [
        "charcoal.json"
    ],
    "minecraft:wet_sponge": [
        "sponge.json"
    ],
    "minecraft:white_terracotta": [
        "white_glazed_terracotta.json"
    ],
    "minecraft:yellow_terracotta": [
        "yellow_glazed_terracotta.json"
    ]
}


verbose = False
recursive = False
data_path = ""
namespace = ""
used_ids = []

supported_types = ["minecraft:smelting", "minecraft:blasting", "minecraft:smoking"]
type_to_block = {"minecraft:smelting": "furnace", "minecraft:blasting": "blasting_furnace", "minecraft:smoking": "smoker"}
default_cookingtime = {"minecraft:smelting": 200, "minecraft:blasting": 100, "minecraft:smoking": 100}


class Recipe():
    type = 'type'
    ingredient = 'ingredient'
    result = 'result'
    experience = 'experience'
    cookingtime = 'cookingtime'

    def __init__(self, file_json, file_path):
        self.name = file_path.split(os.sep)[-1].split('.')[0]
        self.type = file_json[Recipe.type]
        self.ingredients = self.get_ingredients(file_json[Recipe.ingredient])
        self.result = Result(file_json[Recipe.result])
        self.experience = file_json[Recipe.experience]
        self.cookingtime = self.get_cookingtime(file_json)
        self.exp_recipe_name = self.name + '_exp.json'
        self.block = type_to_block[self.type]
        self.items = self.get_all_items()

    def get_ingredients(self, ingredient_json):
        ingredients = []

        if isinstance(ingredient_json, dict):
            ingredients = [Ingredient(ingredient_json)]
        else:
            for ingredient in ingredient_json:
                ingredients.append(Ingredient(ingredient))

        return ingredients

    def get_cookingtime(self, file_json):
        if Recipe.cookingtime in file_json.keys():
            return file_json[Recipe.cookingtime]
        else:
            return default_cookingtime[self.type]

    def get_all_items(self):
        all_items = []

        for ingredient in self.ingredients:
            all_items.extend(ingredient.items)

        return all_items

    def get_exp_recipe(self):
        return\
f'''{{
    "type": "{self.type}",
    "group": "nbtsmelt:impossible",
    "ingredient": {{
        "item": "minecraft:bedrock"
    }},
    "result": "minecraft:bedrock",
    "experience": {self.experience},
    "cookingtime": 2147483647
}}
'''

    def get_input_predicate(self, item):
        pass

    def parse(self):
        for ingredient in self.ingredients:
            for item in ingredient.items:
                child_recipe = SingleItemRecipe(self, (item, ingredient.count, ingredient.nbt))
                child_recipe.parse_recipe()

        path_to_namespace = os.path.join(data_path, 'data', namespace)
        path_to_recipes = os.path.join(path_to_namespace, 'recipes')

        if not os.path.exists(path_to_recipes):
            os.makedirs(path_to_recipes)

        with open(os.path.join(path_to_recipes, self.exp_recipe_name), 'w') as f:
            f.write(self.get_exp_recipe())




class SingleItemRecipe():
    def __init__(self, parent_recipe, ingredient):
        self.name = parent_recipe.name + "_" + ingredient[0][10:]
        self.type = parent_recipe.type
        self.item, self.count, self.nbt = ingredient # (item, count, nbt)
        self.result = parent_recipe.result
        self.experience = parent_recipe.experience
        self.cookingtime = parent_recipe.cookingtime
        self.exp_recipe_name = parent_recipe.exp_recipe_name
        self.block = parent_recipe.block
        self.parent = parent_recipe
        self.recipe_id = None

    def parse_recipe(self):
        path_to_namespace = os.path.join(data_path, 'data', namespace)
        path_to_predicates = os.path.join(path_to_namespace, 'predicates', 'recipes', self.name)
        path_to_function_recipes = os.path.join(path_to_namespace, 'functions', 'recipes', self.block)
        path_to_get_recipe = os.path.join(path_to_namespace, 'functions', 'smelting', self.block, 'get_recipe')
        path_to_found_recipe = os.path.join(path_to_get_recipe, 'found_recipe')
        path_to_function_tags = os.path.join(path_to_namespace, 'tags', 'functions')
        path_to_check_recipes = os.path.join(path_to_get_recipe, 'check_recipes')

        if self.item in vanilla_ingredients:
            self.replace_vanilla_recipe()

        if not os.path.exists(path_to_predicates):
            os.makedirs(path_to_predicates)
        if not os.path.exists(path_to_function_recipes):
            os.makedirs(path_to_function_recipes)
        if not os.path.exists(path_to_found_recipe):
            os.makedirs(path_to_found_recipe)
        if not os.path.exists(path_to_function_tags):
            os.makedirs(path_to_function_tags)

        if os.path.exists(os.path.join(path_to_function_recipes, self.name + ".mcfunction")):
            self.recipe_id = get_recipe_id_from_file_path(os.path.join(path_to_function_recipes, self.name + ".mcfunction"))
        if self.recipe_id is None:
            self.recipe_id = self.get_recipe_id(path_to_function_recipes)

        with open(os.path.join(path_to_function_recipes, self.name + ".mcfunction"), 'w') as f:
            f.write(self.get_recipe_content())

        with open(os.path.join(path_to_predicates, "input.json"), 'w') as f:
            f.write(self.get_input_predicate())

        with open(os.path.join(path_to_predicates, "output.json"), 'w') as f:
            f.write(self.get_output_predicate())

        with open(os.path.join(path_to_found_recipe, self.name + ".mcfunction"), 'w') as f:
            f.write(self.get_found_recipe_content())

        function_tag_content = []
        function_tag_functions = []
        if os.path.exists(os.path.join(path_to_function_tags, 'recipes.json')):
            at_functions = False
            with open(os.path.join(path_to_function_tags, 'recipes.json'), 'r') as f:
                for line in f:
                    if not at_functions:
                        function_tag_content.append(line)
                    if '[' in line:
                        at_functions = True
                    elif ']' in line:
                        functions_str = ',\n'.join(function_tag_functions)
                        function_tag_content.append(functions_str)
                        function_tag_content.append("\n" + line)
                        at_functions = False
                    elif at_functions and self.name not in line:
                        line = line.rstrip()
                        if line != "":
                            line = line[:-1] if line[-1] == ',' else line
                            function_tag_functions.append(line)

        with open(os.path.join(path_to_function_tags, 'recipes.json'), 'w') as f:
            if function_tag_content == []:
                content = f'''"replace": false,
"values": [
    "{namespace}:recipes/{self.block}/{self.name}"
]'''
                f.write(content)
            else:
                for i, line in enumerate(function_tag_content):
                    if '[' in line:
                        if function_tag_functions == []:
                            function_tag_content.insert(i + 1, f"\"{namespace}:recipes/{self.block}/{self.name}\"\n")
                        else:
                            function_tag_content.insert(i + 1, f"\"{namespace}:recipes/{self.block}/{self.name}\",\n")
                        break
                f.write(''.join(function_tag_content))

        check_recipe_content = []
        with open(os.path.join(path_to_check_recipes, f'check_recipes_{len(self.item)}.mcfunction'), 'r') as f:
            for line in f:
                if self.name not in line:
                    check_recipe_content.append(line.strip())

        with open(os.path.join(path_to_check_recipes, f'check_recipes_{len(self.item)}.mcfunction'), 'w') as f:
            check_recipe_content.append(f"execute if predicate {namespace}:recipes/{self.name}/input if predicate {namespace}:recipes/{self.name}/output run function {namespace}:smelting/{self.block}/get_recipe/found_recipe/{self.name}")
            f.write('\n'.join(check_recipe_content))

    def get_recipe_id(self, path_to_function_recipes):
        for num in range(0, 1000):
            if num not in used_ids:
                used_ids.append(num)
                return num
        return None

    def get_input_predicate(self):
        if self.nbt is None:
            return\
f'''{{
    "condition": "minecraft:alternative",
    "terms": [
        {{
            "condition": "minecraft:entity_properties",
            "predicate": {{
                "equipment": {{
                    "mainhand": {{
                        "item": "{self.item}",
                        "count": {{
                            "min": {self.count}
                        }}
                    }}
                }}
            }},
            "entity": "this"
        }}
    ]
}}
'''
        else:
            return\
f'''{{
    "condition": "minecraft:alternative",
    "terms": [
        {{
            "condition": "minecraft:entity_properties",
            "predicate": {{
                "equipment": {{
                    "mainhand": {{
                        "item": "{self.item}",
                        "nbt": "{self.nbt}",
                        "count": {{
                            "min": {self.count}
                        }}
                    }}
                }}
            }},
            "entity": "this"
        }}
    ]
}}
'''

    def get_output_predicate(self):
        if self.result.nbt is None:
            return\
f'''{{
    "condition": "minecraft:alternative",
    "terms": [
        {{
            "condition": "minecraft:entity_properties",
            "predicate": {{
                "equipment": {{
                    "offhand": {{
                        "item": "{self.result.item}",
                        "count": {{
                            "max": {max_stack_sizes[self.result.item] - self.result.count}
                        }}
                    }}
                }}
            }},
            "entity": "this"
        }},
        {{
            "condition": "minecraft:entity_properties",
            "predicate": {{
                "equipment": {{
                    "offhand": {{
                        "item": "minecraft:air"
                    }}
                }}
            }},
            "entity": "this"
        }}
    ]
}}
'''
        else:
            return\
f'''{{
    "condition": "minecraft:alternative",
    "terms": [
        {{
            "condition": "minecraft:entity_properties",
            "predicate": {{
                "equipment": {{
                    "offhand": {{
                        "item": "{self.result.item}",
                        "nbt": "{self.result.nbt}",
                        "count": {{
                            "max": {max_stack_sizes[self.result.item] - self.result.count}
                        }}
                    }}
                }}
            }},
            "entity": "this"
        }},
        {{
            "condition": "minecraft:entity_properties",
            "predicate": {{
                "equipment": {{
                    "offhand": {{
                        "item": "minecraft:air"
                    }}
                }}
            }},
            "entity": "this"
        }}
    ]
}}
'''

    def get_recipe_content(self):
        if self.result.nbt is None:
            return\
f'''# Reset Temp
data modify storage nbtsmelt:furnace_recipes Temp set value {{}}

# Input
data modify storage nbtsmelt:furnace_recipes Temp.Input.Count set value {self.count}b

# Output
data modify storage nbtsmelt:furnace_recipes Temp.Output.Count set value {self.result.count}b
data modify storage nbtsmelt:furnace_recipes Temp.Output.Item set value {{id:"{self.result.item}"}}

# Exp reward
data modify storage nbtsmelt:furnace_recipes Temp.ExperienceRecipe set value "{namespace}:{self.exp_recipe_name[0:-5]}"

# Cooking time
data modify storage nbtsmelt:furnace_recipes Temp.CookingTime set value {self.cookingtime}s

# Add to DB
scoreboard players set #nbtsmelt.recipe.id nbtsmelt.var {self.recipe_id}
function {namespace}:playerdb/put_entry
'''
        else:
            return\
f'''# Reset Temp
data modify storage nbtsmelt:furnace_recipes Temp set value {{}}

# Input
data modify storage nbtsmelt:furnace_recipes Temp.Input.Count set value 1b

# Output
data modify storage nbtsmelt:furnace_recipes Temp.Output.Count set value {self.result.count}b
data modify storage nbtsmelt:furnace_recipes Temp.Output.Item set value {{id:"{self.result.item}", tag:{{{self.result.nbt}}}}}

# Exp reward
data modify storage nbtsmelt:furnace_recipes Temp.ExperienceRecipe set value "{namespace}:{self.exp_recipe_name[0:-5]}"

# Cooking time
data modify storage nbtsmelt:furnace_recipes Temp.CookingTime set value {self.cookingtime}s

# Add to DB
scoreboard players set #nbtsmelt.recipe.id nbtsmelt.var {self.recipe_id}
function {namespace}:playerdb/put_entry
'''

    def get_found_recipe_content(self):
        tag_length = get_nbt_tag_length(self.nbt)
        return\
f'''scoreboard players set #nbtsmelt.recipe.tag.length nbtsmelt.var {tag_length}
execute if score #nbtsmelt.recipe.tag.length nbtsmelt.var >= #nbtsmelt.recipe.tag.max_length nbtsmelt.var run scoreboard players set #nbtsmelt.recipe.id nbtsmelt.var {self.recipe_id}
execute if score #nbtsmelt.recipe.tag.length nbtsmelt.var >= #nbtsmelt.recipe.tag.max_length nbtsmelt.var run scoreboard players operation #nbtsmelt.recipe.tag.max_length nbtsmelt.var = #nbtsmelt.recipe.tag.length nbtsmelt.var
'''

    def replace_vanilla_recipe(self):
        path_to_minecraft_recipes = os.path.join(data_path, 'data', 'minecraft', 'recipes')
        path_to_custom_minecraft_recipes = os.path.join("minecraft", "recipes")

        if not os.path.exists(path_to_minecraft_recipes):
            os.makedirs(path_to_minecraft_recipes)

        json_files = vanilla_ingredients[self.item]

        for json_file in json_files:
            if os.path.isfile(os.path.join(path_to_minecraft_recipes, json_file)):
                with open(os.path.join(path_to_minecraft_recipes, json_file), 'r') as f:
                    file_json = json.load(f)
            else:
                with open(os.path.join(path_to_custom_minecraft_recipes, json_file), 'r') as f:
                    file_json = json.load(f)
            ingredient = file_json["ingredient"]

            if isinstance(ingredient, list):
                for ing in ingredient:
                    if ing["item"] == self.item:
                        ingredient.remove(ing)
                        break
            else:
                if "item" in ingredient.keys():
                    ingredient["item"] = "minecraft:bedrock"
                elif "tag" in ingredient.keys():
                    items = get_items_from_tag(ingredient["tag"])
                    ingredient = []
                    for item in items:
                        if item != self.item:
                            ingredient.append({"item": item})
            file_json["ingredient"] = ingredient

            with open(os.path.join(path_to_minecraft_recipes, json_file), 'w') as f:
                f.write(json.dumps(file_json, indent=4))

            # Parse new recipe, replacing vanilla one
            if get_nbt_tag_length(self.nbt) > 0:
                ingredient = {"item": self.item, "count": 1}
                file_json["ingredient"] = ingredient
                result = {"item": file_json["result"], "count": 1}
                file_json["result"] = result

                new_recipe = Recipe(file_json, os.sep + self.parent.name + '_minecraft.json')
                new_recipe.parse()




class Ingredient():
    count = 'count'
    item = 'item'
    nbt = 'nbt'
    tag = 'tag'

    def __init__(self, ingredient_json):
        self.items = self.get_items(ingredient_json)
        self.count = ingredient_json[Ingredient.count]
        self.nbt = get_nbt(ingredient_json)

    def get_items(self, ingredient_json):
        items = []
        keys = ingredient_json.keys()

        if Ingredient.item in keys:
            items.append(ingredient_json[Ingredient.item])
        if Ingredient.tag in keys:
            items.extend(get_items_from_tag(ingredient_json[Ingredient.tag]))

        return items


class Result():
    count = Ingredient.count
    item = Ingredient.item
    nbt = Ingredient.nbt

    def __init__(self, result_json):
        self.item = result_json[Result.item]
        self.count = result_json[Result.count]
        self.nbt = get_nbt(result_json)


class ItemTag():
    replace = 'replace'
    values = 'values'


def get_nbt(container):
    if Ingredient.nbt in container.keys():
        return container[Ingredient.nbt]
    return None

def get_nbt_tag_length(nbt_string):
    if nbt_string is None:
        return 0

    stack = []
    length = 0
    nbt_string = nbt_string[1:-1]

    for char in nbt_string:
        if stack == []:
            if char == ':':
                length += 1
            if char == '{' or char == '[' or char == '"' or char == '\'':
                stack.append(char)
        elif stack != []:
            if (char == '{' or char == '[' or char == '"' or char == '\'') and stack[-1] != '"' and stack[-1] != '\'':
                stack.append(char)
            if (char == '"' and stack[-1] == '"') or (char == '\'' and stack[-1] == '\''):
                stack.pop()
            if char == '}' or char == ']':
                stack.pop()

    return length


def get_used_ids():
    path_to_recipes = os.path.join(data_path, 'data', namespace, 'functions', 'recipes')
    path_furnace = os.path.join(path_to_recipes, 'furnace')
    path_blasting_furnace = os.path.join(path_to_recipes, 'blasting_furnace')
    path_smoker = os.path.join(path_to_recipes, 'smoker')
    used_ids = []

    files_furnace = [(f, path_furnace) for f in os.listdir(path_furnace) if os.path.isfile(os.path.join(path_furnace, f))]
    # files_blasting_furnace = [f for f in os.listdir(path_blasting_furnace) if os.path.isfile(os.path.join(path_blasting_furnace, f))]
    # files_smoker = [f for f in os.listdir(path_smoker) if os.path.isfile(os.path.join(path_smoker, f))]
    files = files_furnace

    for recipe_file, path in files:
        used_ids.append(get_recipe_id_from_file_path(os.path.join(path, recipe_file)))

    return used_ids


def get_recipe_id_from_file_path(path):
    with open(path, 'r') as f:
        for line in f:
            if "#nbtsmelt.recipe.id" in line:
                return int(line.strip().split()[-1])
    return None


def get_items_from_tag(tag):
    items = []
    namespace, item_tag = tag.split(':')

    if tag in tags_dict.keys():
        tag_items = tags_dict[tag]
        for item in tag_items:
            if item.startswith('#'):
                items.extend(get_items_from_tag(item[1:]))
            else:
                items.append(item)
    else:
        if '/' in item_tag:
            tag_path = item_tag.split('/')
        else:
            tag_path = [item_tag]

        path_to_tag = data_path + os.sep + 'data' + os.sep + namespace + os.sep + 'tags' + os.sep + 'items' + os.sep + os.sep.join(tag_path) + '.json'

        with open(path_to_tag, 'r') as f:
            tag_items = json.load(f)[ItemTag.values]

            for item in tag_items:
                if item.startswith('#'):
                    items.extend(get_items_from_tag(item[1:]))
                else:
                    items.append(item)
    return items






def main(args):
    global verbose
    global recursive
    global data_path
    global namespace
    global used_ids

    data_path = args.data_path
    parse_path = args.path
    excludes = args.exclude
    includes = args.include + [parse_path]
    namespace = args.namespace
    no_replace = args.no_replace
    verbose = args.verbose
    recursive = args.recursive

    used_ids = get_used_ids()

    validate_data_path(data_path, namespace)

    include_files = get_include_files(includes, excludes)
    if include_files == []:
        sys.exit("ERROR: no files to include! Please check if your paths are valid.")

    for path in include_files:
        with open(path, 'r') as f:
            try:
                file_json = json.load(f)
            except json.decoder.JSONDecodeError as e:
                if verbose:
                    print("WARN: invalid JSON in file '{}': {}".format(path, e))
                print("INFO: Skipping invalid file '{}'...".format(path))
                continue

            if not validate_json(path, file_json):
                print("INTO: Skipping invalid file '{}'...".format(path))
                continue
            else:
                if verbose:
                    print("INFO: Validated file '{}'".format(path))

                recipe = Recipe(file_json, path)
                exists = recipe_exists(recipe, path, namespace)
                if no_replace and exists:
                    print("INFO: Skipping duplicate recipe file '{}'...".format(path))
                    continue

                recipe.parse()


def recipe_exists(recipe, file_path, namespace):
    file_name = file_path.split(os.sep)[-1].split('.')[0]
    path_to_namespace = data_path + os.sep + namespace + os.sep
    block = type_to_block[recipe.type]

    file_exists = os.path.exists(path_to_namespace + 'recipes' + os.sep + file_name + '_exp.json')\
        or os.path.exists(path_to_namespace + 'predicates' + os.sep + 'recipes' + os.sep + file_name)\
        or os.path.exists(path_to_namespace + 'functions' + os.sep + 'recipes' + os.sep + block + os.sep + file_name + '.mcfunction')\
        or os.path.exists(path_to_namespace + 'functions' + os.sep + 'smelting' + os.sep + block + os.sep + 'get_recipe' + os.sep + 'found_recipe' + os.sep + file_name + '.mcfunction')

    length_paths = []
    for ingredient in recipe.ingredients:
        for item in ingredient.items:
            id_length = str(len(item))
            length_path = path_to_namespace + 'functions' + os.sep + 'smelting' + os.sep + block + os.sep + 'get_recipe' + os.sep + 'check_recipe_' + id_length + '.mcfunction'
            length_paths.append(length_path)

    command = f"execute if predicate nbtsmelt:recipes/{file_name}/input if predicate nbtsmelt:recipes/{file_name}/output run function nbtsmelt:smelting/furnace/get_recipe/found_recipe/{file_name}"
    found_command = False

    for length_path in length_paths:
        try:
            f = open(length_path, 'r')
        except FileNotFoundError:
            continue

        for line in f:
            if line == command:
                found_command = True

    return file_exists or found_command


def validate_json(file_path, file_json):
    keys = file_json.keys()

    # Check if keys exist
    if Recipe.type not in keys:
        if verbose:
            print("WARN: '{}' field not specified in file '{}'".format(Recipe.type, file_path))
        return False
    elif Recipe.ingredient not in keys:
        if verbose:
            print("WARN: '{}' field not specified in file '{}'".format(Recipe.ingredient, file_path))
        return False
    elif Recipe.result not in keys:
        if verbose:
            print("WARN: '{}' field not specified in file '{}'".format(Recipe.result, file_path))
        return False
    elif Recipe.experience not in keys:
        if verbose:
            print("WARN: '{}' field not specified in file '{}'".format(Recipe.experience, file_path))
        return False
    elif Recipe.cookingtime not in keys and verbose:
        print("INFO: '{}' not specified in file '{}'. Will be set to default.".format(Recipe.cookingtime, file_path))

    # Check if type is valid
    tp = file_json[Recipe.type]
    if not validate_type(tp):
        if verbose:
            print("WARN: '{}' field value '{}' is not valid in file '{}'. Must be one of the following: {}.".format(Recipe.type, tp, file_path, ', '.join(supported_types)))
        return False

    # Validate data types.
    ingredient = file_json[Recipe.ingredient]
    if not isinstance(ingredient, dict) and not isinstance(ingredient, list):
        if verbose:
            print("WARN: '{}' must be dict or list, not {} in file '{}'".format(Recipe.ingredient, type(ingredient).__name__, file_path))
        return False

    result = file_json[Recipe.result]
    if not isinstance(result, dict):
        if verbose:
            print("WARN: '{}' must be dict, not {} in file '{}'".format(Recipe.result, type(result).__name__, file_path))
        return False

    experience = file_json[Recipe.experience]
    if not isinstance(experience, int) and not isinstance(experience, float):
        if verbose:
            print("WARN: '{}' must be int or float, not {} in file '{}'".format(Recipe.experience, type(experience).__name__, file_path))
        return False
    elif experience < 0:
        if verbose:
            print("WARN: '{}' cannot be smaller than 0 in file '{}'.".format(Recipe.experience, file_path))
        return False

    if Recipe.cookingtime in keys:
        cookingtime = file_json[Recipe.cookingtime]
        if not isinstance(cookingtime, int):
            if verbose:
                print("WARN: '{}' must be int, not {} in file '{}'".format(Recipe.cookingtime, type(cookingtime).__name__, file_path))
            return False
        elif cookingtime < 1:
            if verbose:
                print("WARN: '{}' cannot be smaller than 1 in file '{}'.".format(Recipe.cookingtime, file_path))
            return False
        elif cookingtime > 2147483647:
            if verbose:
                print("WARN: '{}' cannot be larger than 2147483647 in file '{}'.".format(Recipe.cookingtime, file_path))
            return False

    if not validate_ingredient(ingredient, file_path):
        return False

    if not validate_result(result, file_path):
        return False

    return True


def validate_type(recipe_type):
    if recipe_type not in supported_types:
        return False
    return True


def validate_ingredient(ingredient, file_path):
    if isinstance(ingredient, list):
        for item in ingredient:
            validate_ingredient(item, file_path)
    else:
        keys = ingredient.keys()

        if Ingredient.item not in keys and Ingredient.tag not in keys:
            if verbose:
                print("WARN: '{}' or '{}' field not specified in file '{}'".format(Ingredient.item, Ingredient.tag, file_path))
            return False
        elif Ingredient.item in keys and Ingredient.tag in keys:
            if verbose:
                print("WARN: '{}' and '{}' fields are mutually exclusive in file '{}'".format(Ingredient.item, Ingredient.tag, file_path))
            return False
        elif Ingredient.count not in keys:
            if verbose:
                print("WARN: '{}' field not specified in file '{}'".format(Ingredient.count, file_path))
            return False

        if Ingredient.item in keys:
            item = ingredient[Ingredient.item]
            if item not in items_list:
                if verbose:
                    print("WARN: '{}' is not a valid item in file '{}'. Is it namespaced correctly?".format(item, file_path))
                return False
            max_stack_size = max_stack_sizes[item]

        if Ingredient.tag in keys:
            tag = ingredient[Ingredient.tag]
            max_stack_size = validate_item_tag(tag)
            if not max_stack_size:
                return False

        count = ingredient[Ingredient.count]
        if not isinstance(count, int):
            if verbose:
                print("WARN: '{}' must be int, not {} in file '{}'".format(Ingredient.count, type(count).__name__, file_path))
            return False
        if count < 1:
            if verbose:
                print("WARN: '{}' cannot be smaller than 1 in file '{}'.".format(Ingredient.count, file_path))
            return False
        elif count > max_stack_size:
            if verbose:
                print("WARN: '{}' cannot be larger than the maximum stack size {} in file '{}'.".format(Ingredient.count, max_stack_size, file_path))
            return False

        # TODO: VALIDATE NBT

    return True


def validate_result(result, file_path):
    keys = result.keys()

    if Result.item not in keys:
        if verbose:
            print("WARN: '{}' field not specified in file '{}'".format(Result.item, file_path))
        return False
    elif Result.count not in keys:
        if verbose:
            print("WARN: '{}' field not specified in file '{}'".format(Result.count, file_path))
        return False

    item = result[Result.item]
    if item not in items_list:
        if verbose:
            print("WARN: '{}' is not a valid item in file '{}'. Is it namespaced correctly?".format(item, file_path))
        return False

    count = result[Ingredient.count]
    max_stack_size = max_stack_sizes[item]
    if not isinstance(count, int):
        if verbose:
            print("WARN: '{}' must be int, not {} in file '{}'".format(Result.count, type(count).__name__, file_path))
        return False
    if count < 1:
        if verbose:
            print("WARN: '{}' cannot be smaller than 1 in file '{}'.".format(Result.count, file_path))
        return False
    elif count > max_stack_size:
        if verbose:
            print("WARN: '{}' cannot be larger than the maximum stack size {} in file '{}'.".format(Result.count, max_stack_size, file_path))
        return False

    # TODO: validate NBT
    return True


def validate_item_tag(tag, tag_stack=[]):
    max_stack_size = 0
    tag_stack.append(tag)

    try:
        namespace, item_tag = tag.split(':')
    except ValueError:
        if verbose:
            print("WARN: tag '{}' is invalid: no namespace recognised.".format(tag))
        return False

    if tag not in tags_dict.keys():
        if '/' in item_tag:
            tag_path = item_tag.split('/')
        else:
            tag_path = [item_tag]

        path_to_tag = data_path + os.sep + 'data' + os.sep + namespace + os.sep + 'tags' + os.sep + 'items' + os.sep + os.sep.join(tag_path) + '.json'

        if not os.path.exists(path_to_tag):
            if verbose:
                print("WARN: tag '{}' is invalid: tag does not exist.".format(tag))
            return False

        with open(path_to_tag, 'r') as f:
            try:
                tag_json = json.load(f)
            except json.decoder.JSONDecodeError as e:
                if verbose:
                    print("WARN: tag '{}' is invalid: tag file '{}' contains invalid JSON.".format(tag, path_to_tag))
                return False
            if 'values' in tag_json.keys():
                values = tag_json['values']
                if not isinstance(values, list):
                    if verbose:
                        print("WARN: tag '{}' is invalid: 'values' must be list, not {} in file '{}'".format(tag, type(values).__name__, path_to_tag))
                    return False

                for value in values:
                    if value.startswith('#'):
                        new_tag = value[1:]
                        if new_tag == tag:
                            if verbose:
                                print("WARN: tag '{}' is invalid: tag cannot reference itself in file '{}'".format(tag, path_to_tag))
                            return False
                        elif new_tag in tag_stack:
                            if verbose:
                                print("WARN: tag '{}' is invalid: tag cannot indirectly reference itself with '{}' in file '{}'".format(tag, new_tag, path_to_tag))
                            return False
                        max_stack = validate_item_tag(value[1:])
                        tag_stack.pop()
                        if not max_stack:
                            return False
                        max_stack_size = max_stack if max_stack_size == 0 else max_stack_size
                        if max_stack != max_stack_size:
                            if verbose:
                                print("WARN: tag '{}' is invalid: all items must have the same maximum stack size in file '{}'".format(tag, path_to_tag))
                            return False
                    elif value not in items_list:
                        if verbose:
                            print("WARN: tag '{}' is invalid: invalid item '{}' in file '{}'".format(tag, value, path_to_tag))
                        return False
                    else:
                        max_stack = max_stack_sizes[value]
                        max_stack_size = max_stack if max_stack_size == 0 else max_stack_size
                        if max_stack != max_stack_size:
                            if verbose:
                                print("WARN: tag '{}' is invalid: all items must have the same maximum stack size in file '{}'".format(tag, path_to_tag))
                            return False
    else:
        max_stack_size = get_tag_max_stack_size(tag)

    return max_stack_size


def get_tag_max_stack_size(tag):
    first_value = tags_dict[tag][0]

    if first_value.startswith('#'):
        return get_tag_max_stack_size(first_value[1:])
    else:
        return max_stack_sizes[first_value]


def validate_data_path(data_path, namespace):
    path_to_data = data_path + os.sep + "data"
    path_to_namespace = path_to_data + os.sep + namespace

    if not os.path.isdir(data_path):
        sys.exit("ERROR: data_path must be a directory.")
    elif not os.path.exists(path_to_data):
        sys.exit("ERROR: no 'data' folder found in path '{}'.".format(data_path + os.sep))
    elif not os.path.exists(path_to_namespace):
        sys.exit("ERROR: no namespace '{}' found in path '{}'.".format(namespace, path_to_data + os.sep))


def get_include_files(includes, excludes):
    include_files = get_files(includes)
    if include_files == []:
        sys.exit("ERROR: no files to include! Please check if your paths are valid.")

    exclude_files = get_files(excludes)

    return [f for f in include_files if f not in exclude_files]


def get_files(paths):
    files = []

    for path in paths:
        if os.path.isdir(path):
            new_files = get_files_from_dir(path)
        elif os.path.isfile(path):
            new_files = [path]
        else:
            new_files = []
            print("Skipping bad path '{}'...".format(path))

        for f in new_files:
            if f not in files and f.endswith('.json'):
                files.append(f)

    return files


def get_files_from_dir(directory):
    if not recursive:
        return glob.glob(directory + "/*.json")
    else:
        return glob.glob(directory + "/**/*.json", recursive=True)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Relative path to the directory or file to parse. More directories/files can be included with --include.")
    parser.add_argument("data_path", help="Relative path to the parent folder of the 'data' folder of the datapack.")
    parser.add_argument("-ns", "--namespace", help="Namespace that contains the NBT smelting modules. Defaults to 'nbtsmelt'.", default="nbtsmelt")
    parser.add_argument("-nr", "--no-replace", help="Does not parse recipes that already exist.", action="store_true", default=False)
    parser.add_argument("-v", "--verbose", help="Increases output verbosity.", action="store_true", default=False)
    parser.add_argument("-r", "--recursive", help="Parses directories recursively.", action="store_true", default=False)
    parser.add_argument("-e", "--exclude", help="Excludes a file or a directory from parsing. Should be a relative path to this file/directory. Can be specified multiple times to exclude multiple files/directories.", action="append", default=[])
    parser.add_argument("-i", "--include", help="Includes a file or a directory for parsing. Should be a relative path to this file/directory. Can be specified multiple times to include multiple files/directories.", action="append", default=[])
    args = parser.parse_args()
    main(args)