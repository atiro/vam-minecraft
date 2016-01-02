import json

from nbt import *

# Read json file

# Export as NBT

with open('bed-of-ware.json', 'r') as json_f:
    schematic_j = json.load(json_f)

    for object in schematic_j["schematics"]:
        nbtfile = nbt.NBTFile()
        nbtfile.name = "Schematic"

        width = object["width"]
        nbtfile.tags.append(nbt.TAG_Short(name="Width", value=width))

        height = object["height"]
        nbtfile.tags.append(nbt.TAG_Short(name="Height", value=height))

        length = object["length"]
        nbtfile.tags.append(nbt.TAG_Short(name="Length", value=length))

        materials = object["materials"]
        nbtfile.tags.append(nbt.TAG_String(name="Materials", value=materials))

        blocks = nbt.TAG_Byte_Array(name="Blocks")
        blocks_data = object["blocks"]
        blocks.value = bytearray(blocks_data)
        nbtfile.tags.append(blocks)

        data = nbt.TAG_Byte_Array(name="Data")
        data_data = object["data"]
        data.value = bytearray(data_data)
        nbtfile.tags.append(data)

        entities = nbt.TAG_List(name="Entities", type=nbt.TAG_Compound)
        nbtfile.tags.append(entities)

        tile_entities = nbt.TAG_List(
            name="TileEntities", type=nbt.TAG_Compound)

        nbtfile.tags.append(tile_entities)

        print(nbtfile.pretty_tree())
        nbtfile.write_file("test2.schematic")
