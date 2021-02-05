from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    hits=mc.events.pollProjectileHits()
    if len(hits)> 0:
        hit=hits[0]
        x,y,z =hit.pos.x,hit.pos.y,hit.pos.z
        mc.setBlocks(x,y,z,x+50,y+50,z+50,0)
