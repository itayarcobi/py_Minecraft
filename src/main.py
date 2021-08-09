from ursina import *


class Test_cube(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model="quad",
            texture="white_cube",
            rotation=(45, 45, 45)
        )


class Test_button(Button):
    def __init__(self):
        super().__init__(
            parent=scene,
            model="cube",
            texture="brick",
            rotation=(45, 45, 45),
            highlight_color=color.red,
            pressed_color=color.lime
        )


def update():
    if held_keys['a']:
        t1.x -= 1 * time.dt
    if held_keys['d']:
        t1.x += 1 * time.dt


if __name__ == '__main__':
    app = Ursina()
    # t = Test_cube()
    t1 = Test_button()
    # cube = Entity(model="quad", color=color.orange, scale=(2, 5), position=(5, 1))

    app.run()
