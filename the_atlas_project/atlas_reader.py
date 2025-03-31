import json
from pyray import *

class AtlasReader:
    def __init__(self, atlasJSON) -> None:
        with open(atlasJSON, "r") as file:
            self.atlasData = json.load(file)

        self.texture = load_texture(self.atlasData["atlas"])

    def draw_sprite(self, sprite_name, posx, posy, scalex=1.0, scaley=1.0):
        if not sprite_name in self.atlasData["entries"]:
            raise KeyError(f"Error: Sprite {sprite_name} not found in atlas properties.")

        sprite = self.atlasData["entries"][sprite_name]
        source_rect = Rectangle(sprite["x"], sprite["y"], sprite["w"], sprite["h"])
        dest_rect = Rectangle(posx, posy, sprite["w"] * scalex, sprite["h"] * scaley)
        draw_texture_pro(self.texture, source_rect, dest_rect, Vector2(0, 0), 0.0, WHITE)

    def unload(self):
        unload_texture(self.texture)
