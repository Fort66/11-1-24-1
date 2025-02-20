from classes.class_Animator import Animator

class Explosion(Animator):
    def __init__(
        self, dir_path=None, speed_frame=0.05, obj_rect=None, guard_level=None, loops=-1
    ):
        super().__init__(
            dir_path,
            speed_frame,
            obj_rect,
            loops
        )