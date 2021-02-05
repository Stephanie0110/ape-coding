from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

Position=mc.player.getTilePos()
x=Position.x
y=Position.y
z=Position.z

time.sleep(10)
mc.player.getTilePos(x,y,z)