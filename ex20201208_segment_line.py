#!/usr/bin/env python3

from manimlib.imports import *
from random import shuffle, randrange
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from utils import Measurement

# manim ddmath/ex20201208_segment_line.py SegLine1 -r1280,720 -pm
# manim ddmath/ex20201208_segment_line.py SegLine1 -r640,360 -pl

"""
ffmpeg -i voice.m4a -acodec copy v.aac -y
ffmpeg -i bg.m4a -acodec copy b.aac -y
cat b.aac v.aac >> sound.aac -y
ffmpeg -i sound.aac -acodec copy -bsf:a aac_adtstoasc sound.m4a -y
ffmpeg -i SegLine1.mp4 -i sound.m4a output.mp4
"""


class SegLine1(Scene):
    CONFIG = {
        "color": WHITE,
        "a": [-3*1.5, 1, 0],
        "b": [-1*1.5, 1, 0],
        "c": [-0*1.5, 1, 0],
        "d": [3*1.5, 1, 0],
        "e": [-1.5*1.5, 1, 0],
        "f": [1*1.5, 1, 0],
        "txt": 9,
    }

    def construct(self):
        lAD = Line(self.a, self.d)
        lAC = Line(self.a, self.c, stroke_width=10, color=YELLOW)
        lBD = Line(self.b, self.d, stroke_width=10, color=RED)
        lEF = Line(self.e, self.f, stroke_width=10, color=YELLOW)
        lBC = Line(self.b, self.c, stroke_width=10, color=BLUE)

        tx1 = TexMobject("BC=\\frac{1}{3}AC")
        tx1.move_to(self.txt * UP)
        tx1b = TexMobject("=\\frac{1}{4}BD")
        tx1b.next_to(tx1, RIGHT)
        tx2 = TexMobject("AE=EC")
        tx2.next_to(tx1, DOWN, buff=0.5)
        tx2b = TexMobject(", BF=FD")
        tx2b.next_to(tx2, RIGHT)
        tx3 = TexMobject("EF=5")
        tx3.next_to(tx2, DOWN, buff=0.5)

        [ptA, ptB, ptC, ptD, ptE, ptF] = [
            Dot(X) for X in [self.a, self.b, self.c, self.d, self.e, self.f]]
        [txtA, txtB, txtC, txtD, txtE, txtF] = [
            TextMobject(X) for X in ["A", "B", "C", "D", "E", "F"]]

        txtA.next_to(ptA, DOWN, buff=0.6)
        txtB.next_to(ptB, DOWN, buff=0.6)
        txtC.next_to(ptC, DOWN, buff=0.6)
        txtD.next_to(ptD, DOWN, buff=0.6)
        txtE.next_to(ptE, DOWN, buff=0.6)
        txtF.next_to(ptF, DOWN, buff=0.6)

        self.play(FadeIn(lAD), FadeIn(ptA), FadeIn(
            ptD), FadeIn(txtA), FadeIn(txtD))
        self.wait(2)

        self.play(FadeIn(ptB), FadeIn(ptC), FadeIn(txtB), FadeIn(txtC))
        self.wait(2)

        self.play(GrowFromCenter(lBC))
        self.wait(1)

        gE = VGroup(ptE, txtE)
        gE.set_color(YELLOW)
        self.play(GrowFromCenter(lAC))
        self.wait(1)
        self.play(FadeIn(gE))
        ind1 = Indicate(gE, color=YELLOW,
                        running_start=double_smooth, scale_factor=1.2)
        self.play(ind1, FadeIn(tx1), FadeIn(tx2))
        self.remove(lAC)
        gE.set_color(YELLOW)
        ptA.set_color(YELLOW)
        ptC.set_color(YELLOW)
        self.wait(2)

        sg1 = VGroup(tx1, tx1b)
        sg1.generate_target()
        sg1.target.shift(LEFT*sg1.get_center())
        move1 = MoveToTarget(sg1)
        self.play(move1)
        self.wait()

        sg2 = VGroup(tx2, tx2b)
        sg2.generate_target()
        sg2.target.shift(LEFT*sg2.get_center())
        move2 = MoveToTarget(sg2)
        self.play(move2)

        gF = VGroup(ptF, txtF)
        self.play(GrowFromCenter(lBD))
        self.wait(1)
        self.play(FadeIn(gF))
        ind1 = Indicate(gF, color=RED,
                        running_start=double_smooth, scale_factor=1.2)
        self.play(ind1)
        self.remove(lBD)
        gF.set_color(RED)
        ptB.set_color(RED)
        ptD.set_color(RED)
        self.wait(2)

        # 显示 EF 长度
        meEF = Measurement(lEF, invert=True, dashed=True,
                           buff=-0.5).add_tips().add_tex("5", buff=0.6, color=WHITE)
        self.play(GrowFromCenter(meEF), FadeIn(tx3))
        self.wait(1)

        meAD = Measurement(lAD, invert=True, dashed=True,
                           buff=-1.2).add_tips().add_tex("?", buff=0.6, color=WHITE)
        self.play(GrowFromCenter(meAD))

        self.wait(5)
