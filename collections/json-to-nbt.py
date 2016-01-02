import json

from nbt import *

# Read json file

# Export as NBT

nbtfile = nbt.NBTFile()

nbtfile.name = "Schematic"

nbtfile.tags.append(nbt.TAG_Short(name="Width", value=2))
nbtfile.tags.append(nbt.TAG_Short(name="Length", value=2))
nbtfile.tags.append(nbt.TAG_Short(name="Height", value=2))
nbtfile.tags.append(nbt.TAG_String(name="Materials", value="Alpha"))

blocks = nbt.TAG_Byte_Array(name="Blocks")
blocks.value = bytearray([3,3,6,3,3,7,3,3])
nbtfile.tags.append(blocks)

data = nbt.TAG_Byte_Array(name="Data")
data.value = bytearray([0,0,0,0,0,0,0,0])
nbtfile.tags.append(data)

entities = nbt.TAG_List(name="Entities", type=nbt.TAG_Compound)
nbtfile.tags.append(entities)

tile_entities = nbt.TAG_List(name="TileEntities", type=nbt.TAG_Compound)
nbtfile.tags.append(tile_entities)

print(nbtfile.pretty_tree())
nbtfile.write_file("test.schematic")
