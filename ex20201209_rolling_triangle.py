#!/usr/bin/env python3

from manimlib.for_3b1b_videos.pi_creature_animations import Blink
from manimlib.imports import *
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))


# manim ddmath/ex20201209_rolling_triangle.py RollingTriangle1 -r1280,720 -pm
# manim ddmath/ex20201209_rolling_triangle.py RollingTriangle1 -r640,360 -pl

"""
ffmpeg -i RollingTriangle1.mp4 -i voice.m4a output.mp4
"""


class RollingTriangle1(Scene):
    """
00 各位好，这是女儿今天花了比较长时间做的一道题
04 说：点O是直线AB上一个点
06 直角三角形MON在直线AB上
08 直角边ON与AO重叠，
10 射线OC在角MON内部，且角AOC的角度为80度
15 问：若三角形MON以每秒5度的速度顺时针旋转一周
26 多长时间后，角MOC等于角MOB？
30 这道题的坑就在于它有两个解，
32 孩子就卡在了第二个解上。
34 想象一下三角形旋转的情况，
38 线段MO与OB及OC可以在两种情况下构成相等的两个角
38 来我们重放一下
38 这是第一种情况，这是第二种
44 看明白这两种情况后，
50 就很容易算出结果了
52 过程就不详细解释，
53 结合已知条件仔细算一下，
55 你算出来了么？
57 好了 下次再见！
    """
    CONFIG = {
        "color": WHITE,
        "o": [0, 0, 0],
        "a": [-5, 0, 0],
        "b": [5, 0, 0],
        "c": [5, 0, 0],  # need rotate
        "n": [-3, 0, 0],
        "m": [0, 4, 0],
        "txt": 9,
    }

    def construct(self):
        tx1 = TexMobject("\\angle MON=90^\\circ").scale(1.5)
        tx1b = TexMobject(",\\angle AOC=80^\\circ").scale(1.5)
        tx2 = TexMobject("\\omega=5^\\circ/s").scale(1.5)
        tx1.move_to(self.txt * UP)
        tx1b.next_to(tx1, RIGHT)
        tx2.next_to(tx1, DOWN, buff=0.5)

        lAB = Line(self.a, self.b)
        lOC = Line(self.o, self.c, color=YELLOW)
        lOM1 = Line(self.o, self.m)
        lOM2 = Line(self.o, self.m)

        [ptA, ptB, ptC, ptO, ptM, ptN] = [
            Dot(X) for X in [self.a, self.b, self.c, self.o, self.m, self.n]]
        [txtA, txtB, txtC, txtM, txtN, txtO, txtM1, txtM2] = [
            TextMobject(X) for X in ["A", "B", "C", "M", "N", "O", "M'", "M\""]]
        triangle = Polygon(self.m, self.o, self.n, color=WHITE)

        txtA.next_to(ptA, DOWN, buff=0.5)
        txtB.next_to(ptB, DOWN, buff=0.5)
        txtO.next_to(ptO, DOWN, buff=0.5)
        txtM.next_to(ptM, UP, buff=0.5)
        txtN.next_to(ptN, DOWN, buff=0.5)

        # view line AB
        self.play(FadeIn(lAB), FadeIn(txtA), FadeIn(txtB))
        self.wait(3)
        self.play(FadeIn(ptO), FadeIn(txtO))
        self.wait(1)
        self.play(FadeIn(triangle), FadeIn(txtM), FadeIn(txtN))
        self.wait(1)
        trans1 = TransformFromCopy(triangle, tx1)
        self.play(trans1)
        self.wait(2)

        # draw line OC
        angC = Sector(arc_center=ORIGIN, outer_radius=0.6, color=YELLOW, fill_opacity=0.8,
                      start_angle=PI, angle=math.radians(-80))
        txtA80 = TexMobject("80^\\circ")
        txtA80.next_to(ptO, UL, buff=0.6)
        gOC = VGroup(lOC, ptC)
        gOC.rotate(angle=math.radians(100), about_point=ORIGIN)
        txtC.next_to(ptC, UP, buff=0.5)
        self.play(ShowCreation(lOC))
        self.play(FadeIn(txtC))
        self.play(FadeIn(txtA80), FadeIn(angC))
        trans1 = TransformFromCopy(angC, tx1b)
        self.play(trans1)

        sg1 = VGroup(tx1, tx1b)
        sg1.generate_target()
        sg1.target.shift(LEFT*sg1.get_center())
        move1 = MoveToTarget(sg1)
        self.play(move1)
        self.wait(1)

        ptM1 = ptB.copy()
        ptM2 = ptB.copy()
        lOM1 = Line(self.o, self.b, color=RED)
        lOM2 = Line(self.o, self.b, color=RED)
        gM1 = VGroup(lOM1, ptM1)
        gM2 = VGroup(lOM2, ptM2)
        gM1.rotate(angle=math.radians(50), about_point=ORIGIN)
        gM2.rotate(angle=math.radians(-130), about_point=ORIGIN)
        txtM1.next_to(ptM1, RIGHT, buff=0.5)
        txtM2.next_to(ptM2, LEFT, buff=0.5)

        g1 = VGroup(triangle)

        def update1(group, alpha):
            angle = math.radians(-360 * alpha)
            # print(alpha)
            triangle = Polygon(self.m, self.o, self.n, color=WHITE)
            triangle.rotate(angle=angle, about_point=ORIGIN)
            new_group = VGroup(triangle)
            group.become(new_group)
            return group

        def update2(group, alpha):
            angle = math.radians(-360 * alpha)
            # print(alpha)
            triangle = Polygon(self.m, self.o, self.n, color=WHITE)
            triangle.rotate(angle=angle, about_point=ORIGIN)
            lOM = Line(self.o, [0, 5, 0], color=RED)
            lOM.rotate(angle=angle, about_point=ORIGIN)
            new_group = VGroup(triangle, lOM)
            group.become(new_group)
            return group


        def updateA(group, alpha):
            angle = math.radians(-40 * alpha)
            # print(alpha)
            triangle = Polygon(self.m, self.o, self.n, color=WHITE)
            triangle.rotate(angle=angle, about_point=ORIGIN)
            new_group = VGroup(triangle)
            group.become(new_group)
            return group

        def updateB(group, alpha):
            angle = math.radians((-180 * alpha) - 40)
            # print(alpha)
            triangle = Polygon(self.m, self.o, self.n, color=WHITE)
            triangle.rotate(angle=angle, about_point=ORIGIN)
            new_group = VGroup(triangle)
            group.become(new_group)
            return group

        def updateC(group, alpha):
            angle = math.radians((-140 * alpha) - 220)
            # print(alpha)
            triangle = Polygon(self.m, self.o, self.n, color=WHITE)
            triangle.rotate(angle=angle, about_point=ORIGIN)
            new_group = VGroup(triangle)
            group.become(new_group)
            return group

        self.play(FadeIn(tx2))
        self.remove(txtM, txtN)
        self.play(UpdateFromAlphaFunc(g1, update1),
                  run_time=9, rate_func=smooth)
        self.add(txtM, txtN)
        self.wait(3)

        # rolling again
        self.remove(txtM, txtN)
        lOM = Line(self.o, self.m, color=RED)
        g2 = VGroup(triangle, lOM)
        self.play(UpdateFromAlphaFunc(g2, update2),
                  run_time=5, rate_func=smooth)
        self.add(txtM, txtN)
        self.remove(lOM)
        self.wait(2)

        # rolling step by step, with explain.
        self.remove(txtM, txtN)
        self.play(UpdateFromAlphaFunc(g1, updateA),
                  run_time=1.5, rate_func=linear)
        self.play(ShowCreation(lOM1), FadeIn(txtM1))
        angA1 = Sector(arc_center=ORIGIN, outer_radius=0.9, color=BLUE, fill_opacity=0.8,
                       start_angle=0, angle=math.radians(50))
        angA2 = Sector(arc_center=ORIGIN, outer_radius=0.9, color=GREEN, fill_opacity=0.8,
                       start_angle=math.radians(50), angle=math.radians(50))
        # self.play(FadeIn(angA1), FadeIn(angA2))
        # self.wait()
        ind1 = Indicate(angA1, color=BLUE,
                        running_start=double_smooth, scale_factor=1.2)
        ind2 = Indicate(angA2, color=GREEN,
                        running_start=double_smooth, scale_factor=1.2)
        self.play(ind1, run_time=0.5)
        self.play(ind2, run_time=0.5)

        self.play(UpdateFromAlphaFunc(g1, updateB),
                  run_time=3, rate_func=linear)
        self.play(ShowCreation(lOM2), FadeIn(txtM2))
        angB1 = Sector(arc_center=ORIGIN, outer_radius=0.9, color=ORANGE, fill_opacity=0.3,
                       start_angle=0, angle=math.radians(-130))
        angB2 = Sector(arc_center=ORIGIN, outer_radius=0.9, color=RED, fill_opacity=0.3,
                       start_angle=math.radians(100), angle=math.radians(130))
        # self.play(FadeIn(angB1), FadeIn(angB2))
        # self.wait()

        ind1 = Indicate(angB1, color=RED,
                        running_start=double_smooth, scale_factor=1.2)
        ind2 = Indicate(angB2, color=ORANGE,
                        running_start=double_smooth, scale_factor=1.2)
        self.play(ind1, run_time=1)
        self.play(ind2, run_time=1)

        self.play(UpdateFromAlphaFunc(g1, updateC),
                  run_time=5, rate_func=rush_from)
        self.add(txtM, txtN)

        self.wait(7)
