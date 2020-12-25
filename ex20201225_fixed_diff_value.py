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
        "show_stretch_area": False,
        "show_label": True,
        "show_measurement": False,
        "show_measurement_x": False,
    }

    def __init__(self, **kwargs):
        digest_config(self, kwargs)
        self.fixed_width = self.width - self.a
        if self.fixed_width < 0:
            raise Exception("Illegal width parameter")
        if self.a + self.b * 3 != self.height:
            raise Exception("Illegal height parameter")
        Rectangle.__init__(self, **kwargs)

        l = Line(self.get_center()-RIGHT*self.width / 2,
                 self.get_center()+RIGHT*self.width/2)
        self.add(l)

        # left down
        l = Line(self.get_center(), DOWN*self.a)
        l.shift(LEFT*(self.width/2 - self.b*4))
        self.add(l)
        for i in range(3):
            l = Line(self.get_center()+UP*self.a/2,
                     self.get_center()+DOWN*self.a/2)
            l.shift(DOWN*(self.height/2 - self.a/2),
                    LEFT*(self.width/2 - self.b*(i+1)))
            self.add(l)

        # top right
        l = Line(self.get_center(), UP*self.a)
        l.shift(RIGHT*(self.width/2 - self.a))
        self.add(l)
        for i in range(2):
            l = Line(self.get_center()+LEFT*self.a/2,
                     self.get_center()+RIGHT*self.a/2)
            l.shift(UP*(self.height/2 - self.b*(i+1)),
                    RIGHT*(self.width-self.a)/2)
            self.add(l)

        # top left
        self.R1 = Rectangle(height=self.b*3, width=self.width-self.a,
                            fill_color=BLACK, fill_opacity=0.5, stroke_opacity=0)
        self.txtS1 = TexMobject("S_{1}")
        self.g1 = VGroup(self.R1, self.txtS1)
        self.g1.shift(LEFT*(self.a)/2, UP*(self.height-self.b*3)/2)
        self.add(self.g1)

        # right down
        self.R4 = Rectangle(height=self.a, width=self.width-self.b*4,
                            fill_color=BLACK, fill_opacity=0.5, stroke_opacity=0)
        self.txtS2 = TexMobject("S_{2}")
        self.g2 = VGroup(self.R4, self.txtS2)
        self.g2.shift(RIGHT*(self.b*2), DOWN*(self.b*3)/2)
        self.add(self.g2)

        self.R2 = Rectangle(height=3*self.b, width=self.a,
                            fill_color=BLUE, fill_opacity=0.5, stroke_opacity=0)
        self.R2.shift(RIGHT*(self.width-self.a)/2, UP*(self.height-self.b*3)/2)
        self.add(self.R2)

        self.R3 = Rectangle(height=self.a, width=self.b*4,
                            fill_color=BLUE, fill_opacity=0.5, stroke_opacity=0)
        self.R3.shift(LEFT*(self.width-self.b*4)/2,
                      DOWN*(self.height-self.a)/2)
        self.add(self.R3)

        if self.show_label:
            self.add_label()

        self.add_measurement()

        # gray zone
        self.r5 = Rectangle(height=self.b*3, width=self.stretch_width,
                            fill_color=WHITE, fill_opacity=0.6, stroke_opacity=0)
        self.r5.shift(RIGHT*((self.width)/2-self.a - self.stretch_width/2),
                      UP*(self.height-self.b*3)/2)
        self.r6 = Rectangle(height=self.a, width=self.stretch_width,
                            fill_color=WHITE, fill_opacity=0.6, stroke_opacity=0)
        self.r6.shift(RIGHT*((self.width)/2 - self.stretch_width/2),
                      DOWN*(self.height-self.a)/2)

        if self.show_stretch_area:
            self.add(self.r5)
            self.add(self.r6)

    def add_label(self):
        [ptA, ptB, ptC, ptD] = [self.get_corner(X)for X in [UL, DL, DR, UR]]
        self.txts = [txtA, txtB, txtC, txtD] = [
            TextMobject(X) for X in ["A", "B", "C", "D"]]
        txtA.next_to(ptA, UL)
        txtB.next_to(ptB, DL)
        txtC.next_to(ptC, DR)
        txtD.next_to(ptD, UR)
        self.add(*self.txts)

    def add_measurement(self, show=None):
        ptB = self.get_center() + LEFT * self.width/2 + DOWN * self.height/2
        ptA1 = ptB + UP * self.a
        ptC1 = ptB + RIGHT * self.b * 4

        ptD = self.get_center() + RIGHT * self.width/2 + UP * self.height/2
        ptA2 = ptD + LEFT * self.a
        ptC2 = ptD + DOWN * self.b * 3

        meAa = Measurement(Line(ptB, ptA1), invert=True, dashed=True,
                           buff=-0.5).add_tips().add_tex("a", buff=3, color=WHITE)
        meAb = Measurement(Line(ptB, ptC1), invert=True, dashed=True,
                           buff=0.5).add_tips().add_tex("4b", buff=-3, color=WHITE)
        meBa = Measurement(Line(ptA2, ptD), invert=True, dashed=True,
                           buff=-0.5).add_tips().add_tex("a", buff=3, color=WHITE)
        meBb = Measurement(Line(ptD, ptC2), invert=True, dashed=True,
                           buff=-0.5).add_tips().add_tex("3b", buff=2, color=WHITE)
        self.measurement = [meAa, meAb, meBa, meBb]
        if show is not None:
            self.show_measurement = show
        if self.show_measurement:
            self.add(*self.measurement)

    def add_measurement_x(self, show=None):
        ptD = self.get_center() + RIGHT * self.width/2 + UP * self.height/2
        ptX1a = ptD + LEFT * (self.a + self.stretch_width)
        ptX1b = ptD + LEFT * (self.a)

        ptC = self.get_center() + RIGHT * self.width/2 + DOWN * self.height/2
        ptX2a = ptC + LEFT * (self.stretch_width)

        meX1 = Measurement(Line(ptX1a, ptX1b), invert=True, dashed=True,
                           buff=-0.5).add_tips().add_tex("x1", buff=2, color=WHITE)
        meX2 = Measurement(Line(ptX2a, ptC), invert=True, dashed=True,
                           buff=0.5).add_tips().add_tex("x2", buff=-3, color=WHITE)
        self.measurement_x = [meX1, meX2]
        if show is not None:
            self.show_measurement_x = show
        if self.show_measurement_x:
            self.add(*self.measurement_x)


class FixedDiffValue1(Scene):
    CONFIG = {
        "color": WHITE,
        "unit": 0.9,
        "a": 3,
        "b": 1,
        "sw": 6.6,
        "sh": 6,
        "stretch_width": 0,
        "sample": 10,
        "txt": 9,
        "rect_x": 3.5,
    }

    def construct(self):
        RectSample = Rectangle(height=self.b*self.unit, width=self.a*self.unit,
                               fill_color=BLUE, fill_opacity=0.5)
        [ptAa, ptAb, ptAc, ptAd] = [RectSample.get_corner(X) for X in [
            UL, DL, UR,  DR]]

        meAa = Measurement(Line(ptAa, ptAc), invert=True, dashed=True,
                           buff=-0.5).add_tips().add_tex("a", buff=3, color=WHITE)
        meAb = Measurement(Line(ptAa, ptAb), invert=False, dashed=True,
                           buff=-0.5).add_tips().add_tex("b", buff=-3, color=WHITE)
        gRA = VGroup(RectSample, meAa, meAb)
        self.play(Write(RectSample))
        self.wait(1)
        self.play(Write(meAa), Write(meAb))
        self.wait()

        def custom_method(mobject):
            mobject.scale(0.5)
            mobject.shift(UP*(self.sample)+LEFT*(self.rect_x))
            return mobject

        self.play(ApplyFunction(custom_method, gRA))

        fdr = FixedDiffRect(height=self.sh*self.unit, width=self.sw*self.unit,
                            a=self.a*self.unit, b=self.b*self.unit,
                            stretch_width=self.stretch_width*self.unit)
        self.play(Write(fdr), run_time=2)
        self.wait(3)

        fdr.add_measurement(True)
        self.play(*[Write(o)for o in fdr.measurement])
        self.wait()

        self.play(Indicate(fdr.R1))
        self.play(Indicate(fdr.R4))
        self.wait(3)

        fdr.generate_target()
        fdr.target.shift(RIGHT*(self.sw*self.unit/2 - self.rect_x))
        shift1 = MoveToTarget(fdr)
        self.play(shift1)

        g1 = VGroup(fdr)

        def update1(group, alpha):
            stretch = 1.2 * self.unit * alpha
            fdr = FixedDiffRect(height=self.sh*self.unit, width=self.sw*self.unit + stretch,
                                a=self.a*self.unit, b=self.b*self.unit,
                                stretch_width=stretch, show_measurement=True)
            fdr.shift(RIGHT*((self.sw*self.unit + stretch)/2 - self.rect_x))

            ng = VGroup(fdr)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(g1, update1),
                  run_time=5, rate_func=there_and_back)
        self.wait(1)

        def update2(group, alpha):
            stretch = 1.2 * self.unit * alpha
            fdr = FixedDiffRect(height=self.sh*self.unit, width=self.sw*self.unit + stretch,
                                a=self.a*self.unit, b=self.b*self.unit,
                                stretch_width=stretch, show_measurement=True, show_stretch_area=True)
            fdr.shift(RIGHT*((self.sw*self.unit + stretch)/2 - self.rect_x))

            ng = VGroup(fdr)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(g1, update2),
                  run_time=5, rate_func=smooth)
        self.wait(1)

        # 替换一下
        stretch = 1.2 * self.unit
        fdr = FixedDiffRect(height=self.sh*self.unit, width=self.sw*self.unit + stretch,
                            a=self.a*self.unit, b=self.b*self.unit,
                            stretch_width=stretch, show_measurement=True, show_stretch_area=True)
        fdr.shift(RIGHT*((self.sw*self.unit + stretch)/2 - self.rect_x))
        self.remove(g1)
        self.add(fdr)

        self.play(Indicate(fdr.R1))
        self.play(Indicate(fdr.R2))
        self.play(Indicate(fdr.R3))
        self.play(Indicate(fdr.R4))
        self.play(Indicate(fdr.r5))
        self.play(Indicate(fdr.r6))

        fdr.add_measurement_x(True)
        self.play(*[Write(o)for o in fdr.measurement_x])

        tx1 = TexMobject("S_{\\delta}").scale(1.5)
        tx1a = TexMobject("=S_{1}+S_{2}").scale(1.5)
        tx1.move_to(UP*self.txt)
        tx1a.next_to(tx1, RIGHT)
        self.play(FadeIn(tx1))
        self.play(TransformFromCopy(VGroup(fdr.txtS1, fdr.txtS2), tx1a))

        vt1x = VGroup(tx1, tx1a)
        vt1x.generate_target()
        vt1x.target.shift(LEFT*vt1x.get_center())
        move1 = MoveToTarget(vt1x)
        self.play(move1, run_time=0.5)



        self.wait(6)
