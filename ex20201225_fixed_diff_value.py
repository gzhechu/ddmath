#!/usr/bin/env python3

from manimlib.imports import *
from random import shuffle, randrange

try:
    import sys
    sys.path.append(os.path.dirname(os.path.realpath(__file__)))
    from utils import Measurement
except:
    pass

# manim ddmath/ex20201225_fixed_diff_value.py FixedDiffValue1 -r1280,720 -pm
# manim ddmath/ex20201225_fixed_diff_value.py FixedDiffValue1 -r640,360 -pl
# ffmpeg -i FixedDiffValue1.mp4 -i sound.m4a FixedDiffValue1R.mp4


# 长方体
class FixedDiffRect(Rectangle):
    CONFIG = {
        "a": 3.0,
        "b": 1.0,
        "fixed_width": 0,
        "stretch_width": 1,
        "show_stretch_area": False
    }

    def __init__(self, **kwargs):
        digest_config(self, kwargs)
        self.fixed_width = self.width - self.a
        if self.fixed_width < 0:
            raise Exception("Illegal width parameter")
        if self.a + self.b * 3 != self.height:
            raise Exception("Illegal height parameter")
        Rectangle.__init__(self, **kwargs)

        l = Line(ORIGIN-RIGHT*self.width/2, ORIGIN+RIGHT*self.width/2)
        self.add(l)

        # left down
        l = Line(ORIGIN, DOWN*self.a)
        l.shift(LEFT*(self.width/2 - self.b*4))
        self.add(l)
        for i in range(3):
            l = Line(ORIGIN+UP*self.a/2, ORIGIN+DOWN*self.a/2)
            l.shift(DOWN*(self.height/2 - self.a/2),
                    LEFT*(self.width/2 - self.b*(i+1)))
            self.add(l)
        self.r3 = Rectangle(height=self.a, width=self.b*4,
                         fill_color=BLUE, fill_opacity=0.5, stroke_opacity=0)
        self.r3.shift(LEFT*(self.width-self.b*4)/2, DOWN*(self.height-self.a)/2)
        self.add(self.r3)

        # top right
        l = Line(ORIGIN, UP*self.a)
        l.shift(RIGHT*(self.width/2 - self.a))
        self.add(l)
        for i in range(2):
            l = Line(ORIGIN+LEFT*self.a/2, ORIGIN+RIGHT*self.a/2)
            l.shift(UP*(self.height/2 - self.b*(i+1)),
                    RIGHT*(self.width-self.a)/2)
            self.add(l)
        self.r2 = Rectangle(height=3*self.b, width=self.a,
                         fill_color=BLUE, fill_opacity=0.5, stroke_opacity=0)
        self.r2.shift(RIGHT*(self.width-self.a)/2, UP*(self.height-self.b*3)/2)
        self.add(self.r2)

        # top left
        self.r1 = Rectangle(height=self.b*3, width=self.width-self.a,
                            fill_color=BLACK, fill_opacity=0.5, stroke_opacity=0)
        self.r1.shift(LEFT*(self.a)/2, UP*(self.height-self.b*3)/2)
        self.add(self.r1)

        # right down
        self.r4 = Rectangle(height=self.a, width=self.width-self.b*4,
                            fill_color=BLACK, fill_opacity=0.5, stroke_opacity=0)
        self.r4.shift(RIGHT*(self.b*2), DOWN*(self.b*3)/2)
        self.add(self.r4)

        if self.show_stretch_area:
            self.r5 = Rectangle(height=self.b*3, width=self.stretch_width,
                                fill_color=WHITE, fill_opacity=0.6, stroke_opacity=0)
            self.r5.shift(RIGHT*((self.width)/2-self.a - self.stretch_width/2),
                          UP*(self.height-self.b*3)/2)
            self.add(self.r5)
            self.r6 = Rectangle(height=self.a, width=self.stretch_width,
                                fill_color=WHITE, fill_opacity=0.6, stroke_opacity=0)
            self.r6.shift(RIGHT*((self.width)/2 - self.stretch_width/2),
                          DOWN*(self.height-self.a)/2)
            self.add(self.r6)


class FixedDiffValue1(Scene):
    CONFIG = {
        "color": WHITE,
        "unit": 0.9,
        "a": 3,
        "b": 1,
        "sw": 6.5,
        "sh": 6,
        "stretch_width": 0,
        "sample": 10,
        "txt": 7,
        "rect_x": 3.5,
    }

    def construct(self):
        RectA = Rectangle(height=self.b*self.unit, width=self.a*self.unit, fill_color=BLUE,
                         fill_opacity=0.5)
        [ptAa, ptAb, ptAc, ptAd] = [RectA.get_corner(X)for X in [UL, UR, DL, DR]]

        meAa = Measurement(Line(ptAa, ptAc), invert=True, dashed=True,
                           buff=0.5).add_tips().add_tex("a", buff=-3, color=WHITE)
        meAb = Measurement(Line(ptAa, ptAb), invert=True, dashed=True,
                           buff=-0.5).add_tips().add_tex("b", buff=0, color=WHITE)
        gRA = VGroup(RectA, meAa, meAb)
        self.play(ShowCreation(RectA))
        self.wait(1)
        self.play(Write(meAa), Write(meAb))
        self.wait()



        def custom_method(mobject):
            # mobject.set_color(RED)
            mobject.scale(0.5)
            mobject.shift(UP*(self.sample)+LEFT*(self.rect_x))
            return mobject

        # gRA.generate_target()
        # gRA.target.shift(UP*(self.sample)+LEFT*(self.rect_x))
        # shift1 = MoveToTarget(gRA)
        # self.play(shift1, run_time=0.5)
        # self.play(ScaleInPlace(gRA, 0.5), run_time=0.5)

        self.play(ApplyFunction(custom_method, gRA))



        fdr = FixedDiffRect(height=self.sh*self.unit, width=self.sw*self.unit,
                            a=self.a*self.unit, b=self.b*self.unit,
                            stretch_width=self.stretch_width*self.unit)
        self.play(Write(fdr), run_time=2)
        self.wait(3)

        fdr.generate_target()
        fdr.target.shift(RIGHT*(self.sw*self.unit/2 - self.rect_x))
        shift1 = MoveToTarget(fdr)
        self.play(shift1)

        g1 = VGroup(fdr)

        def update1(group, alpha):
            stretch = 2 * self.unit * alpha
            fdr = FixedDiffRect(height=self.sh*self.unit, width=self.sw*self.unit + stretch,
                                a=self.a*self.unit, b=self.b*self.unit,
                                stretch_width=stretch)
            fdr.shift(RIGHT*((self.sw*self.unit + stretch)/2 - self.rect_x))

            ng = VGroup(fdr)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(g1, update1),
                  run_time=8, rate_func=there_and_back)
        self.wait(1)


        def update2(group, alpha):
            stretch = 2 * self.unit * alpha
            fdr = FixedDiffRect(height=self.sh*self.unit, width=self.sw*self.unit + stretch,
                                a=self.a*self.unit, b=self.b*self.unit,
                                stretch_width=stretch, show_stretch_area=True)
            fdr.shift(RIGHT*((self.sw*self.unit + stretch)/2 - self.rect_x))

            ng = VGroup(fdr)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(g1, update2),
                  run_time=8, rate_func=there_and_back)
        self.wait(1)

        self.play(Indicate(fdr.r1))
        self.wait(6)
