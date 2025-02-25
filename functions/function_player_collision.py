from pygame.sprite import groupcollide
from config.create_Objects import screen
from units.class_Explosion import Explosion


from classes.class_SpriteGroups import SpriteGroups

sprite_groups = SpriteGroups()

def player_collision():
    object_collide = groupcollide(
        sprite_groups.player_group,
        sprite_groups.enemies_shot_group,
        dokilla=False,
        dokillb=True
        )