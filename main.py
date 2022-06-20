from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import time
app = Ursina()
window.title="Minecraft Transform - Anyone can"
grasstexture=load_texture('minecraft/grass_text.png')
stonetexture=load_texture('minecraft/Stone_block.png')
woodtexture=load_texture('minecraft/Wood_block_texture.png')
concretetexture=load_texture('minecraft/concreteblock.png')
skytexture=load_texture('minecraft/Sky.png')
leaftexture=load_texture('minecraft/Leaf_block.png')
doortexture=load_texture('minecraft/door.png')
flowertexture=load_texture('minecraft/flower.jpg')
watertexture=load_texture('minecraft/wattexture.png')
glasstexture=load_texture('minecraft/panetextureblue.png')
hand=load_texture('minecraft/minecraftpickaxe.png')
ladder=load_texture('minecraft/ladder.png')
# woodtexture=load_texture('minecraft/Wood_block_texture.png')
lavatexture=load_texture('minecraft/Lava_block.png')
portaltexture=load_texture('minecraft/portaltexture.png')
leaftexture=load_texture('minecraft/Leaf_block.png')
Nethracktexture=load_texture('minecraft/Netherrack.png')
diamondtexture=load_texture('minecraft/Diamond_block.png')
lighttexture=load_texture('minecraft/lighttexture.png')
crafttabletexture=load_texture('minecraft/minecraftcrafttable.png')
lighttexture=load_texture('minecraft/lighttexture.png')
rainbowtexture=load_texture('minecraft/rainbow.png')
obsidiantexture=load_texture('minecraft/obsidiantexture.png')
stairtexture=load_texture('minecraft/stair.png')
zombieparts=load_texture('minecraft/zombieparts.png')
alexparts=load_texture('minecraft/alexparts.png')
steveparts=load_texture('minecraft/steveparts.png')
piston=load_texture('minecraft/pistontexture.png')
text=Text(text="Grass Block", x=-0.12, y=-.4, scale=2)
text.text="1234567"
block_choice=1
mode="portal"
nb=[]
pb=[]
bc2=1
doorp=[]
doorp2=[]
no=Vec3(0, 0, 0)
no2=0
no3=0
def togglemode():
    global mode
    if mode=="portal":
        for i in range(len(pb)):
            pb[i].disable()
        for i in range(len(nb)):
            nb[i].enable()
        mode="normal"
    elif mode=="normal":
        for i in range(len(nb)):
            nb[i].disable()
        for i in range(len(pb)):
            pb[i].enable()
        mode="portal"
        
def update():
    global block_choice
    global bc2
    if held_keys["1"]:
        block_choice=bc2+1
    if held_keys["-"]:
        bc2=0
    if held_keys["["]:
        bc2=20
    if held_keys["]"]:
        bc2=30
    if held_keys["="]:
        bc2=10
    if held_keys["\\"]:
        bc2=40
    if held_keys["2"]:
        block_choice=bc2+2
    if held_keys["3"]:
        block_choice=bc2+3
    if held_keys["4"]:
        block_choice=bc2+4
    if held_keys["5"]:
        block_choice=bc2+5
    if held_keys["6"]:
        block_choice=bc2+6
    if held_keys["7"]:
        block_choice=bc2+7
    if held_keys["8"]:
        block_choice=bc2+8
    if held_keys["9"]:
        block_choice=bc2+9
    if held_keys["0"]:
        block_choice=bc2+0
    if held_keys["f"]:
        for i in range(len(doorp)):
            destroy(doorp[i])
    if held_keys["g"]:
        for i in range(len(doorp2)):
            destroy(doorp2[i])
    if held_keys["i"]:
        player.position+=Vec3(0, 0.3, 0)
        player.land()
    
    # if held_keys[","]:
    #     no3=0
    # if held_keys["."]:
    #     no3=90
    # if held_keys["down arrow"]:
    #     no=Vec3(0, -0.5, 0)
    # if held_keys["up arrow"]:
    #     no=Vec3(0, 0, 0)
    # if held_keys["left arrow"]:
    #     no2=0
    # if held_keys["right arrow"]:
    #     no2=90
    # if player.air_time>0.2:
        # exit()
class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=grasstexture, model="minecraft/block", scale=0.5, collide="box", rotation=Vec3(0, 0, 0)):
        super().__init__(
            collider=collide,
            parent=scene,
            position=position,
            model=model,
            origin_y=0.5,
            texture=texture,
            color=color.white,
            highlight_color=color.gray,
            pressed_color=color.green,
            scale=scale,
            rotation=rotation)
        if mode=="portal":
            pb.append(self)
        if mode=="normal":
            nb.append(self)
        # print(self.rotation)
    def input(self,key):
        if self.hovered:
            if key=="left mouse down":
                if block_choice==16:
                    voxel=Voxel(self.position+mouse.normal, grasstexture)
                if block_choice==13:
                    voxel=Voxel(self.position+mouse.normal, stonetexture)
                if block_choice==12:
                    voxel=Voxel(self.position+mouse.normal, woodtexture)
                if block_choice==14:
                    voxel=Voxel(self.position+mouse.normal+no, woodtexture, model="woodplank")
                if block_choice==15:
                    voxel=Voxel(self.position+mouse.normal, leaftexture)
                if block_choice==11:
                    voxel=Voxel(self.position+mouse.normal, concretetexture)
                if block_choice==17:
                    voxel=Voxel(self.position+mouse.normal+Vec3(0, 0.5, 0), doortexture, model="door", collide="mesh", rotation=Vec3(0, no3, 0))
                    doorp.append(voxel)
                if block_choice==18:
                    voxel=Voxel(self.position+mouse.normal, flowertexture, model="flower", scale=0.57)
                if block_choice==19:
                    voxel=Voxel(self.position+mouse.normal, scale=0.5, texture=watertexture, collide="mesh")
                    doorp2.append(voxel)
                if block_choice==20:
                    voxel=Voxel(self.position+mouse.normal, scale=0.5, texture=glasstexture, model="glass_pane", rotation=Vec3(0, no2, 0))
                if block_choice==1:
                    voxel=Voxel(self.position+mouse.normal, scale=0.5)
                if block_choice==2:
                    voxel=Voxel(self.position+mouse.normal, scale=0.5, texture=stonetexture)
                if block_choice==3:
                    voxel=Voxel(self.position+mouse.normal, scale=0.5, texture=woodtexture)
                if block_choice==4:
                    voxel=Voxel(self.position+mouse.normal, scale=0.5, texture=leaftexture)
                if block_choice==5:
                    voxel=Voxel(self.position+mouse.normal, scale=0.5, texture=lavatexture)
                if block_choice==6:
                    voxel=Voxel(self.position+mouse.normal, scale=0.5, texture=diamondtexture)
                if block_choice==7:
                    voxel=Voxel(self.position+mouse.normal, scale=0.5, texture=lighttexture, model="light")
                if block_choice==8:
                    voxel=Voxel(self.position+mouse.normal, scale=0.5, texture=crafttabletexture)
                if block_choice==9:
                    voxel=Voxel(self.position+mouse.normal, scale=0.5, texture=stairtexture, model="stair")
                if block_choice==10:
                    voxel=Voxel(self.position+mouse.normal, scale=0.5, texture=rainbowtexture)
                if block_choice==21:
                    voxel=Voxel(self.position+mouse.normal, scale=0.5, texture=zombieparts, model="person")
                if block_choice==22:
                    voxel=Voxel(self.position+mouse.normal+Vec3(0, 0.8, 0), scale=1, texture=zombieparts, model="person", collide="mesh")
                if block_choice==23:
                    voxel=Voxel(self.position+mouse.normal+Vec3(0, 0.8, 0), scale=1, texture=alexparts, model="person", collide="mesh")
                if block_choice==24:
                    voxel=Voxel(self.position+mouse.normal+Vec3(0, 0.8, 0), scale=1, texture=steveparts, model="person", collide="mesh")
                if block_choice==25:
                    voxel=Portal(self.position+mouse.normal)
                if block_choice==26:
                    voxel=Voxel(self.position+mouse.normal, texture=piston)
                if block_choice==27:
                    voxel=Voxel(self.position+mouse.normal, model="ladder", texture=ladder)
                if block_choice==28:
                    voxel=Voxel(self.position+mouse.normal, texture=obsidiantexture)
            if key=="right mouse down":
                # destroy(self)
                destroy(self)
                if self in pb:
                    pb.remove(self)
                elif self in nb:
                    nb.remove(self)
                # time.sleep(1)
                # self.enable()
class Portal(Button):
    def __init__(self, position=(0, 0, 0), texture=portaltexture, model="minecraft/block", scale=0.5, collide="box", rotation=Vec3(0, 0, 0)):
        super().__init__(
            collider=collide,
            parent=scene,
            position=position,
            model=model,
            origin_y=0.5,
            texture=texture,
            color=color.white,
            highlight_color=color.gray,
            pressed_color=color.green,
            scale=scale,
            rotation=rotation)
        if mode=="portal":
            pb.append(self)
        if mode=="normal":
            nb.append(self)
        # print(self.rotation)
    def input(self,key):
        if self.hovered:
            if key=="left mouse down":
                togglemode()
            if key=="right mouse down":
                # destroy(self)
                destroy(self)
                if self in pb:
                    pb.remove(self)
                elif self in nb:
                    nb.remove(self)
                # time.sleep(1)
                # self.enable()
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model="sphere",
            texture=skytexture,
            scale=100,
            double_sided=True,
            collider="mesh"
        )
class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model="axe",
            texture=hand,
            scale=0.4,
            # rotation=Vec3(-150, 10, -55),
            position=Vec2(0.5, -0.3),
        )
networl=[Nethracktexture, Nethracktexture, Nethracktexture,  Nethracktexture,  Nethracktexture,  Nethracktexture, lavatexture]
def makescene():
    for x in range(-13, 13):
        for y in range(-13, 13):
            voxel=Voxel(position=(x, 0, y))
            lon=random.randint(0, 6)
            togglemode()
            if lon==5:
                voxel=Voxel(position=(x, 0, y), texture=lavatexture, collide="mesh")
            else:
                voxel=Voxel(position=(x, 0, y), texture=Nethracktexture)
            togglemode()
player=FirstPersonController()
Sky()
hand=Hand()
makescene()
app.run()