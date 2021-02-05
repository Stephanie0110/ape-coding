from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setBlocks(x,y,z,x+10,y+20,z+10,95)
mc.setBlocks(x+1,y+1,z+1,x+9,y+19,z+9,0)
mc.setBlocks(x+3,y+1,z,x+3,y+2,z,0)
mc.setBlocks(x+1,y+6,z+1,x+9,y+6,z+9,95)