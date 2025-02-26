from pygame.sprite import groupcollide, spritecollideany

from units.class_Explosion import Explosion

from classes.class_SpriteGroups import SpriteGroups

sprite_groups = SpriteGroups()

def player_guard_collision(self):
    if (spritecollideany(self, sprite_groups.player_guard_group) and self.owner not in sprite_groups.player_group) or (spritecollideany(self, sprite_groups.player_group) and self.owner not in sprite_groups.player_group):
        explosion = Explosion(
            dir_path='images/explosions/rocket1_expl',
            speed_frame=.01,
            scale_value=(.5, .5),
            loops=1,
            obj=self,
            angle=self.angle
        )


def enemies_guard_collision(self):
    if (spritecollideany(self, sprite_groups.enemies_guard_group) and self.owner not in sprite_groups.enemies_group) or (spritecollideany(self, sprite_groups.enemies_group) and self.owner not in sprite_groups.enemies_group):
        explosion = Explosion(
            dir_path='images/explosions/pulsar',
            speed_frame=.01,
            scale_value=(.25, .25),
            loops=1,
            obj=self,
            angle=self.angle
        )

def shots_collision():
    object_collision = groupcollide(
        sprite_groups.player_shot_group,
        sprite_groups.enemies_shot_group,
        True,
        True
    )

    if object_collision:
        hits = list(object_collision.values())[0]
        explosion = Explosion(
            dir_path='images/explosions/rocket1_expl',
            speed_frame=.01,
            scale_value=(.5, .5),
            loops=1,
            obj=hits[0],
            angle=hits[0].angle
        )

def distance_collision(obj):
    if obj in sprite_groups.player_shot_group:
        explosion = Explosion(
            dir_path='images/explosions/pulsar',
            speed_frame=.01,
            scale_value=(.25, .25),
            loops=1,
            obj=obj,
            angle=obj.angle
        )

    if obj in sprite_groups.enemies_shot_group:
        explosion = Explosion(
            dir_path='images/explosions/rocket1_expl',
            speed_frame=.01,
            scale_value=(.5, .5),
            loops=1,
            obj=obj,
            angle=obj.angle
        )