from classes.class_Animator import Animator


class Guardian(Animator):
    def __init__(
                self,
                dir_path=None,
                speed_frame=.05,
                obj_rect=None,
                angle=0
                ):
        super().__init__(
                        dir_path,
                        speed_frame,
                        obj_rect,
                        angle
                        )

