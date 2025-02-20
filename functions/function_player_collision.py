from pygame.sprite import spritecollide
from config.create_Objects import screen
from units.class_Explosion import Explosion


def check_collision(obj):
    if len(obj.sprite_groups.enemies_shot_group):
        hits = spritecollide(
            obj, obj.sprite_groups.enemies_shot_group, dokill=False, collided=None
        )
        if hits:
            for hit in hits:
                if hit:
                    obj.expl_enemies_rocket = Explosion(
                        dir_path="images/Explosions/explosion_rocket1",
                        speed_frame=.05,
                        obj_rect=hit.rect,
                        loops=1
                    )
                    hit.kill()

                if hasattr(obj, "shield"):
                    if obj.shield.guard_level > 0:
                        obj.shield.decrease_level
                    else:
                        delattr(obj, "shield")
