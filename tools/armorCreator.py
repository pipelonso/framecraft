from ursina import *

class Voxel(Button):
    def __init__(self, position=(0,0,0), message = "", rotation = (0,0,0), scale = 1, parent=scene):
        super().__init__(parent=parent,
            position=position,
            model='plane',
            origin_y=.5,
            color=color.red,
            highlight_color=color.lime,
            message = message,
            rotation = rotation,
            scale = scale
        )


class armorCreator:

    right_leg_bone = None
    left_arm_bone = None

    def generate_grid(self):
        r = 8
        for i in range(1, r):
            t = i/r
            s = 5*i
            print(s)
            grid = Entity(model=Grid(s,s), scale=s, color=color.hsv(0,0,.8,lerp(.8,0,t)), rotation_x=90, y=i/1000)
            subgrid = duplicate(grid)
            subgrid.model = Grid(s*4, s*4)
            subgrid.color = color.hsv(0,0,.4,lerp(.8,0,t))

    def initEditor(self):

        app = Ursina(borderless=False)

        self.generate_grid()

        self.left_leg_bone = Entity(model='cube', position=(3, 0, 0), scale=0.5)
        self.right_arm_bone = Entity(model='cube', position=(-3, 0, 0), scale=0.5)


        player_model_path = "player/player.obj"

        #player = Entity(model=player_model_path, scale=(6.8, 6.8, 6.8), position=(0, 0, -1.2), texture = "player.png", )

        self.generate_left_leg()

        Sky(texture="sky_sunset")

        EditorCamera()
        app.run()

    def generate_left_leg(self):
        
        # Generate front
        for i in range(0, 12):
            cubo = Voxel(position=(0,i,3), message = "Puto el que lo lea", rotation=(90,0,0), scale=1, parent=self.left_leg_bone)
            cubo = Voxel(position=(1, i,3), message = "Puto el que lo lea", rotation=(90,0,0), scale=1, parent=self.left_leg_bone)
            cubo = Voxel(position=(2,i,3), message = "Puto el que lo lea", rotation=(90,0,0), scale=1, parent=self.left_leg_bone)
            cubo = Voxel(position=(3,i,3), message = "Puto el que lo lea", rotation=(90,0,0), scale=1, parent=self.left_leg_bone)
            

            cubo = Voxel(position=(0,i,-2), message = "Puto el que lo lea", rotation=(90,0,180), scale=1, parent=self.left_leg_bone)
            cubo = Voxel(position=(1, i,-2), message = "Puto el que lo lea", rotation=(90,180), scale=1, parent=self.left_leg_bone)
            cubo = Voxel(position=(2,i,-2), message = "Puto el que lo lea", rotation=(90,0,180), scale=1, parent=self.left_leg_bone)
            cubo = Voxel(position=(3,i,-2), message = "Puto el que lo lea", rotation=(90,0,180), scale=1, parent=self.left_leg_bone)

            cubo = Voxel(position=(-1,i, -1), message = "Puto el que lo lea", rotation=(90,0,270), scale=1, parent=self.left_leg_bone)
            cubo = Voxel(position=(-1, i,0), message = "Puto el que lo lea", rotation=(90,0,270), scale=1, parent=self.left_leg_bone)
            cubo = Voxel(position=(-1,i,1), message = "Puto el que lo lea", rotation=(90,0,270), scale=1, parent=self.left_leg_bone)
            cubo = Voxel(position=(-1,i,2), message = "Puto el que lo lea", rotation=(90,0,270), scale=1, parent=self.left_leg_bone)

            cubo = Voxel(position=(4,i, -1), message = "Puto el que lo lea", rotation=(90,0,90), scale=1, parent=self.left_leg_bone)
            cubo = Voxel(position=(4, i,0), message = "Puto el que lo lea", rotation=(90,0,90), scale=1, parent=self.left_leg_bone)
            cubo = Voxel(position=(4,i,1), message = "Puto el que lo lea", rotation=(90,0,90), scale=1, parent=self.left_leg_bone)
            cubo = Voxel(position=(4,i,2), message = "Puto el que lo lea", rotation=(90,0,90), scale=1, parent=self.left_leg_bone)

        cubo = Voxel(position=(0,12,2), message = "Puto el que lo lea", rotation=(0,0,0), scale=1, parent=self.left_leg_bone)
        cubo = Voxel(position=(1,12,2), message = "Puto el que lo lea", rotation=(0,0,0), scale=1, parent=self.left_leg_bone)
        cubo = Voxel(position=(2,12,2), message = "Puto el que lo lea", rotation=(0,0,0), scale=1, parent=self.left_leg_bone)
        cubo = Voxel(position=(3,12,2), message = "Puto el que lo lea", rotation=(0,0,0), scale=1, parent=self.left_leg_bone)

        cubo = Voxel(position=(0,12,1), message = "Puto el que lo lea", rotation=(0,0,0), scale=1, parent=self.left_leg_bone)
        cubo = Voxel(position=(1,12,1), message = "Puto el que lo lea", rotation=(0,0,0), scale=1, parent=self.left_leg_bone)
        cubo = Voxel(position=(2,12,1), message = "Puto el que lo lea", rotation=(0,0,0), scale=1, parent=self.left_leg_bone)
        cubo = Voxel(position=(3,12,1), message = "Puto el que lo lea", rotation=(0,0,0), scale=1, parent=self.left_leg_bone)

        cubo = Voxel(position=(0,12,0), message = "Puto el que lo lea", rotation=(0,0,0), scale=1, parent=self.left_leg_bone)
        cubo = Voxel(position=(1,12,0), message = "Puto el que lo lea", rotation=(0,0,0), scale=1, parent=self.left_leg_bone)
        cubo = Voxel(position=(2,12,0), message = "Puto el que lo lea", rotation=(0,0,0), scale=1, parent=self.left_leg_bone)
        cubo = Voxel(position=(3,12,0), message = "Puto el que lo lea", rotation=(0,0,0), scale=1, parent=self.left_leg_bone)

        cubo = Voxel(position=(0,12,-1), message = "Puto el que lo lea", rotation=(0,0,0), scale=1, parent=self.left_leg_bone)
        cubo = Voxel(position=(1,12,-1), message = "Puto el que lo lea", rotation=(0,0,0), scale=1, parent=self.left_leg_bone)
        cubo = Voxel(position=(2,12,-1), message = "Puto el que lo lea", rotation=(0,0,0), scale=1, parent=self.left_leg_bone)
        cubo = Voxel(position=(3,12,-1), message = "Puto el que lo lea", rotation=(0,0,0), scale=1, parent=self.left_leg_bone)


        cubo = Voxel(position=(0,-1,2), message = "Puto el que lo lea", rotation=(180,0,0), scale=1, parent=self.left_leg_bone)
        cubo = Voxel(position=(1,-1,2), message = "Puto el que lo lea", rotation=(180,0,0), scale=1, parent=self.left_leg_bone)
        cubo = Voxel(position=(2,-1,2), message = "Puto el que lo lea", rotation=(180,0,0), scale=1, parent=self.left_leg_bone)
        cubo = Voxel(position=(3,-1,2), message = "Puto el que lo lea", rotation=(180,0,0), scale=1, parent=self.left_leg_bone)

        cubo = Voxel(position=(0,-1,1), message = "Puto el que lo lea", rotation=(180,0,0), scale=1, parent=self.left_leg_bone)
        cubo = Voxel(position=(1,-1,1), message = "Puto el que lo lea", rotation=(180,0,0), scale=1, parent=self.left_leg_bone)
        cubo = Voxel(position=(2,-1,1), message = "Puto el que lo lea", rotation=(180,0,0), scale=1, parent=self.left_leg_bone)
        cubo = Voxel(position=(3,-1,1), message = "Puto el que lo lea", rotation=(180,0,0), scale=1, parent=self.left_leg_bone)

        cubo = Voxel(position=(0,-1,0), message = "Puto el que lo lea", rotation=(180,0,0), scale=1, parent=self.left_leg_bone)
        cubo = Voxel(position=(1,-1,0), message = "Puto el que lo lea", rotation=(180,0,0), scale=1, parent=self.left_leg_bone)
        cubo = Voxel(position=(2,-1,0), message = "Puto el que lo lea", rotation=(180,0,0), scale=1, parent=self.left_leg_bone)
        cubo = Voxel(position=(3,-1,0), message = "Puto el que lo lea", rotation=(180,0,0), scale=1, parent=self.left_leg_bone)

        cubo = Voxel(position=(0,-1,-1), message = "Puto el que lo lea", rotation=(180,0,0), scale=1, parent=self.left_leg_bone)
        cubo = Voxel(position=(1,-1,-1), message = "Puto el que lo lea", rotation=(180,0,0), scale=1, parent=self.left_leg_bone)
        cubo = Voxel(position=(2,-1,-1), message = "Puto el que lo lea", rotation=(180,0,0), scale=1, parent=self.left_leg_bone)
        cubo = Voxel(position=(3,-1,-1), message = "Puto el que lo lea", rotation=(180,0,0), scale=1, parent=self.left_leg_bone)




        cubo.on_click = Sequence(Func(self.sayHola, cubo))

        pass

    def sayHola(self, cubo):
            print(cubo.message)

    
editor = armorCreator()





editor.initEditor()