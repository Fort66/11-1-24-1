from pygame.sprite import spritecollide
from config.create_Objects import screen


def check_collision(obj):
    if len(obj.sprite_groups.enemies_shot_group):
        hits = spritecollide(
            obj, obj.sprite_groups.enemies_shot_group, dokill=False, collided=None
        )
        if hits:
            for hit in hits:
                hit.kill()

                if hasattr(obj, "shield"):
                    if obj.shield.guard_level > 0:
                        obj.shield.decrease_level
                    else:
                        delattr(obj, "shield")
