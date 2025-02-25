from pygame.sprite import groupcollide
from config.create_Objects import screen

from icecream import ic

from classes.class_SpriteGroups import SpriteGroups

sprite_groups = SpriteGroups()

def enemies_collision():
    object_collide = groupcollide(
        sprite_groups.enemies_group,
        sprite_groups.player_shot_group,
        dokilla=False,
        dokillb=True
        )