import os
import json

path = os.path.join("minecraft", "recipes")
for root, dirs, files in os.walk(path):
    for f in files:
        with open(os.path.join(root, f), 'r') as fl:
            file_json = json.load(fl)
        if not (file_json["type"] == "minecraft:smelting" or file_json["type"] == "minecraft:blasting" or file_json["type"] == "minecraft:smoking"):
            os.remove(os.path.join(root, f))
            print("Removed file '{}'".format(f))
