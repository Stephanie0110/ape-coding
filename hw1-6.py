from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x,y,z=mc.player.getPos()
mc.setBlocks(x,y,z,22)
