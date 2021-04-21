#!/usr/bin/env python3

from manim import *

# manim md20200620_half_of_size.py HalfSize -r1280,720 -pqm


class HalfSize(Scene):
    CONFIG = {
        "color": WHITE,
        "A": np.array([2, 4, 0]),
        "B": np.array([-4.5, -2, 0]),
        "C": np.array([5, -2, 0]),
        "txt": 7
    }

    def construct(self):
        origin = Dot()
        [txtO] = [TexMobject(X) for X in ["O"]]
        txtO.next_to(origin, DR, buff=0.1)
        self.play(FadeIn(origin), FadeIn(txtO))
        self.wait()
