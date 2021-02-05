from mcpi.minecraft import Minecraft
mc = Minecraft.create()

Patricia=[]
Stephanie=[]
Doris=[]
for i in range(1,4):
    Patricia.append('???')
for i in range(1,4):
    Stephanie.append('!!!')
for i in range(1,4): 
    Doris.append('^_^')
x,y,z = mc.player.getPos()
mc.setSign(x,y,z,63,2,str(Patricia),str(Stephanie),str(Doris))