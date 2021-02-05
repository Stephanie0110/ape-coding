from mcpi.minecraft import Minecraft
mc = Minecraft.create()
for i in range(50):
    x,y,z=mc.player.getPos()
    z=z-i
    mc.setBlock(x,y-1,z,57)