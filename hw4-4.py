from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from random import randrange
answer=randrange(0,16)
myID=mc.getPlayerEntityId("Reyna")
while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        hit=hits[0]
        block=mc.getBlockWithData(hit.pos)
        data=block.data
        if data>answer:
            mc.postToChat('You are rone')
            hit=hits[0]
            block=mc.getBlockWithData(hit.pos)
            data=block.data
            if data>answer:
                mc.postToChat('You are rone')
                
                