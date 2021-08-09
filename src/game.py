from ursina import Ursina

from player import Player
from voxel import Voxel, Sky
from world import World




class Game:

    def __init__(self):
        self.app = Ursina()
        self.world = World()
        self.player = Player()
        self.sky = Sky()
        self.app.run()


if __name__ == '__main__':
    g = Game()
