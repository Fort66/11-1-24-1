from pygame.sprite import groupcollide

from classes.class_SpriteGroups import SpriteGroups

sprite_groups = SpriteGroups()

def enemies_collision():
    object_collide = groupcollide(
        sprite_groups.enemies_group,
        sprite_groups.player_shot_group,
        dokilla=False,
        dokillb=True
        )
    if object_collide:
        lot_hits = len(list(object_collide.values())[0])
        hits = list(object_collide.keys())[0]

        if hits.hp > 0:
            hits.decrease_hp(lot_hits)

        if hits.hp <= 0:
            hits.kill()