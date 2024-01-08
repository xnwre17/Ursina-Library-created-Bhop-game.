from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()
sky = Sky(texture='sky_sunset')

platform = Entity(model='plane', texture='grass', scale=500, collider='mesh', position=(0, -20, 0))
cube = Entity(model='cube', texture='white_cube', scale=(10, 1, 10), collider='box')

gun = Entity(model='cube', parent=camera, position=(.5,-.25,.25), scale=(.3,.2,1), origin_z=-.5, color=color.red, on_cooldown=False)

cube = Entity(model='cube', texture='white_cube', scale=(2, 1, 2), collider='box', position=(0, 0, 7))
cube = Entity(model='cube', texture='white_cube', scale=(2, 1, 2), collider='box', position=(0, 0, 11))
z = 11
x = 0

for i in range(30):
    bagit = random.randint(1, 3)
    if bagit == 1:
        x -= 4
    elif bagit == 2:
        z += 4
    elif bagit == 3:
        x += 4
    cube = Entity(model='cube', texture='white_cube', scale=(2, 1, 2), collider='box', position=(x, 0, z))

finish = Entity(model='cube', texture='white_cube', scale=(10, 1, 10), collider='box', position=(x+7, 0, z+7))
finish_x_araliq = range(int(finish.position.x)-5, int(finish.position.x)+5)
finish_z_araliq = range(int(finish.position.z)-5, int(finish.position.z)+5)
t = Text('Game Over', color=color.red, origin=(0, -3), scale=10)
t2 = Text('You Win', color=color.green, origin=(0, -3), scale=10)

person = FirstPersonController()
person.speed = 5

def input(key):
    if key == 'space':
        person.speed += 0.5

def update():
    if int(person.position.x) in finish_x_araliq and int(person.position.z) in finish_z_araliq and person.position.y > 0:
        t2.origin = (0, 0)
    elif person.position.y < 0:
        t.origin = (0, 0)
        t2.origin = (0, -3)
app.run()