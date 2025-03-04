from pygame.sprite import groupcollide

from classes.class_SpriteGroups import SpriteGroups
from units.class_Explosion import Explosion

sprite_groups = SpriteGroups()

def player_collision():
    object_collide = groupcollide(
        sprite_groups.player_group,
        sprite_groups.enemies_shot_group,
        dokilla=False,
        dokillb=True
        )
    if object_collide:
        lot_hits = len(list(object_collide.values())[0])
        hits = list(object_collide.keys())[0]

        if hits.hp > 0:
            hits.decrease_hp(lot_hits)

        if hits.hp <= 0:
            explosion = Explosion(
                dir_path='images/explosions/ship1_expl',
                speed_frame=.12,
                scale_value=(.75, .75),
                loops=1,
                obj=hits,
                angle=hits.angle
            )
            if not explosion:
                hits.kill()
            