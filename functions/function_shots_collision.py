from pygame.sprite import groupcollide

from units.class_Explosion import Explosion

from classes.class_SpriteGroups import SpriteGroups

sprite_groups = SpriteGroups()

def player_collision():
    object_collision = groupcollide(
        sprite_groups.player_guard_group,
        sprite_groups.enemies_shot_group,
        False,
        False
    ) or groupcollide(
        sprite_groups.player_group,
        sprite_groups.enemies_shot_group,
        False,
        False
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
        

def enemies_collision():
    object_collision = groupcollide(
        sprite_groups.enemies_guard_group,
        sprite_groups.player_shot_group,
        False,
        False
    ) or groupcollide(
        sprite_groups.enemies_group,
        sprite_groups.player_shot_group,
        False,
        False
    )

    if object_collision:
        hits = list(object_collision.values())[0]
        explosion = Explosion(
            dir_path='images/explosions/pulsar',
            speed_frame=.01,
            scale_value=(.25, .25),
            loops=1,
            obj=hits[0],
            angle=hits[0].angle
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