from ursina import *


class Textures:
    @staticmethod
    def create_texture(texture: str):
        if texture == "grass":
            return load_texture("assets/Grass_Block_TEX.png")
        elif texture == "stone":
            return load_texture('assets/stone_block.png')
        elif texture == "brick":
            return load_texture('assets/brick_block.png')
        elif texture == "dirt":
            return load_texture('assets/dirt_block.png')
        elif texture == "sky":
            return load_texture('assets/sky_block.png')
        elif texture == "arm":
            return load_texture('assets/arm_block.png')
        else:
            raise ValueError(texture)
# if __name__ == '__main__':
#     Textures.create_texture("grass")
