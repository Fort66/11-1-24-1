from pygame.sprite import Sprite
from pygame.transform import rotozoom
from classes.class_Animator import Animator


class Guardian(Animator, Sprite):
    def __init__(
        self,
        dir_path=None,
        speed_frame=None,
        obj=None,
        guard_level=None,
        loops=None,
        pos=None,
        size=None,
        angle=None,
        scale_value=None
    ):
        super().__init__(
            dir_path=dir_path,
            speed_frame=speed_frame,
            loops=loops,
            size=size,
            scale_value=scale_value
        )

        self.guard_level = guard_level
        self.angle = angle
        # self.obj = obj

    @property
    def decrease_level(self):
        if self.guard_level > 0:
            self.guard_level -= 1



    def update(self):
        self.image_rotation = self.frames[self.frame][0]
        self.image_rotation = rotozoom(self.image_rotation, self.angle, 1)
        self.rect = self.image_rotation.get_rect(center=self.rect.center)
        
        super().animate(self, )