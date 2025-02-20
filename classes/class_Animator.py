import pygame as pg
from pygame.image import load
from pygame.transform import scale, rotozoom, rotate, scale_by

from os import listdir
from time import time
import copy
import numpy as np

from icecream import ic


class Animator:
    def __init__(
        self,
        dir_path=None,
        speed_frame=0.05,
        obj_rect=None,
        loops=-1
    ):

        self.dir_path = dir_path
        self.speed_frame = speed_frame
        self.obj_rect = obj_rect[2:]

        self.frames = 0
        self.frame = 0
        self.frame_time = 0
        self.paused_time = 0
        self.loops = loops
        self.paused = False
        self.ended = False
        self.file_list = sorted(listdir(self.dir_path))
        self.__post_init__()

    def __post_init__(self):
        self.original_frames = np.array(
            [
                [
                    scale(
                        load(f"{self.dir_path}/{value}").convert_alpha(),
                        self.obj_rect,
                    ),
                    self.speed_frame,
                ]
                for value in self.file_list
            ]
        )
        self.frames = self.original_frames.copy()

    def animate(self, obj_rect):
        self.obj_rect = obj_rect[2:]

        if self.frame_time == 0:
            self.frame_time = time()

        if time() - self.frame_time >= self.frames[self.frame][1] and not self.paused:

            if self.loops == -1:
                self.frame = self.frame + 1 if self.frame < len(self.frames) - 1 else 0
                self.frame_time = time()
            else:

                if self.loops > 0:
                    self.frame = self.frame + 1 if self.frame < len(self.frames) - 1 else len(self.frames) - 1
                    self.frame_time = time()

                    if self.frame == len(self.frames) - 1:
                        self.loops -= 1

        if self.loops:
            self.frames = self.original_frames.copy()
            self.frames[self.frame][0] = scale(
                self.frames[self.frame][0], self.obj_rect
            )

        # if self.frame >= len(self.frames) - 1:
        #     self.loops[0] += 1
