from mcpi.minecraft import Minecraft
mc = Minecraft.create()
def plantTree(X,Y,Z):
    mc.setBlocks(x+1,y+2,z,x+3,y+5,z+2,18)
    mc.setBlocks(x+2,y,z+1,x+2,y+4,z+1,17)
for i in range(10):
    for i in range(10):
        x,y,z=mc.player.getPos()
        plantTree(x,y,z)
