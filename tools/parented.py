from ursina import *

class Voxel(Button):
    def __init__(self, position=(0, 0, 0), message="", rotation=(0, 0, 0), scale=1, parent=scene):
        super().__init__(
            parent=parent,
            position=position,
            model='plane',
            origin_y=.5,
            color=color.red,
            highlight_color=color.lime,
            rotation=rotation,
            scale=scale
        )
        self.message = message

class ArmorCreator:
    def __init__(self):
        self.right_arm_bone = None
        self.left_arm_bone = None
        self.body_bone = None
        self.left_leg_bone = None
        self.right_leg_bone = None

    def initEditor(self):
        app = Ursina(borderless=False)

        self.createGrid()

        self.body_bone = Entity(model='cube', position=(0, 2, 0))
        self.left_arm_bone = Entity(model='cube', position=(3, 2, 0))
        self.right_arm_bone = Entity(model='cube', position=(-3, 2, 0))
        self.left_leg_bone = Entity(model='cube', position=(1, -2, 0))
        self.right_leg_bone = Entity(model='cube', position=(-1, -2, 0))

        self.createArmorPart(self.body_bone, "body")
        self.createArmorPart(self.left_arm_bone, "left_arm")
        self.createArmorPart(self.right_arm_bone, "right_arm")
        self.createArmorPart(self.left_leg_bone, "left_leg")
        self.createArmorPart(self.right_leg_bone, "right_leg")

        Sky(texture="sky_sunset")
        EditorCamera()
        app.run()

    def createGrid(self):
        r = 8
        for i in range(1, r):
            t = i / r
            s = 5 * i
            grid = Entity(model=Grid(s, s), scale=s, color=color.hsv(0, 0, .8, lerp(.8, 0, t)), rotation_x=90, y=i / 1000)
            subgrid = duplicate(grid)
            subgrid.model = Grid(s * 4, s * 4)
            subgrid.color = color.hsv(0, 0, .4, lerp(.8, 0, t))

    def createArmorPart(self, bone, part_name):
        if part_name == "body":
            positions = [
                (0, 1, 0), (0, -1, 0),  # Front and Back
                (0.5, 0, 0), (-0.5, 0, 0),  # Sides
                (0, 0, 0.5), (0, 0, -0.5)  # Top and Bottom
            ]
        elif part_name in ["left_arm", "right_arm"]:
            positions = [
                (0, 0.5, 0), (0, -0.5, 0),  # Front and Back
                (0.25, 0, 0), (-0.25, 0, 0),  # Sides
                (0, 0, 0.25), (0, 0, -0.25)  # Top and Bottom
            ]
        elif part_name in ["left_leg", "right_leg"]:
            positions = [
                (0, 0.5, 0), (0, -0.5, 0),  # Front and Back
                (0.25, 0, 0), (-0.25, 0, 0),  # Sides
                (0, 0, 0.25), (0, 0, -0.25)  # Top and Bottom
            ]

        for pos in positions:
            Voxel(position=pos, parent=bone)

    def sayHola(self, cubo):
        print(cubo.message)

def update():
    editor.left_arm_bone.x += time.dt
    editor.right_arm_bone.x -= time.dt

editor = ArmorCreator()
editor.initEditor()
