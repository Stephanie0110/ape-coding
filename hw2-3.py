from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setBlocks(x-10,y-10,z-10,x+10,y+10,z+10,1)
mc.setBlocks(x-9,y-9,z-9,x+9,y+9,z+9,0)