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
        "show_measurement_stretch": False,
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

        # gray zone
        self.R7 = Rectangle(height=self.b*3, width=self.width-self.a-self.stretch_width,
                            fill_color=BLACK, fill_opacity=0.5, stroke_opacity=0)
        self.R7.shift(LEFT*(self.a+self.stretch_width)/2,
                      UP*(self.height-self.b*3)/2)
        self.R8 = Rectangle(height=self.a, width=self.width - self.b*4 - self.stretch_width,
                            fill_color=BLACK, fill_opacity=0.5, stroke_opacity=0)
        self.R8.shift(RIGHT*((self.b*2 - self.stretch_width/2)),
                      DOWN*(self.a)/2)
        self.add(self.R7)
        self.add(self.R8)

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
        self.g2.shift(RIGHT*(self.b*2), DOWN*(self.a)/2)
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
        self.add_measurement_x()

        # gray zone
        self.R5 = Rectangle(height=self.b*3, width=self.stretch_width,
                            fill_color=WHITE, fill_opacity=0.6, stroke_opacity=0)
        self.R5.shift(RIGHT*((self.width)/2-self.a - self.stretch_width/2),
                      UP*(self.height-self.b*3)/2)
        self.R6 = Rectangle(height=self.a, width=self.stretch_width,
                            fill_color=WHITE, fill_opacity=0.6, stroke_opacity=0)
        self.R6.shift(RIGHT*((self.width)/2 - self.stretch_width/2),
                      DOWN*(self.height-self.a)/2)
        if self.show_stretch_area:
            self.add(self.R5)
            self.add(self.R6)

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
        ptB = self.get_center() + LEFT * self.width/2 + DOWN * self.height/2
        ptC = self.get_center() + RIGHT * self.width/2 + DOWN * self.height/2

        meX = Measurement(Line(ptB, ptC), invert=True, dashed=True,
                          buff=1.2).add_tips().add_tex("x", buff=-2.5, color=WHITE)
        self.measurement_x = [meX]
        if show is not None:
            self.show_measurement_x = show
        if self.show_measurement_x:
            self.add(*self.measurement_x)

    def add_measurement_stretch(self, show=None):
        ptD = self.get_center() + RIGHT * self.width/2 + UP * self.height/2
        ptX1a = ptD + LEFT * (self.a + self.stretch_width)
        ptX1b = ptD + LEFT * (self.a)

        ptC = self.get_center() + RIGHT * self.width/2 + DOWN * self.height/2
        ptX2a = ptC + LEFT * (self.stretch_width)

        meX1 = Measurement(Line(ptX1a, ptX1b), invert=True, dashed=True,
                           buff=-0.5).add_tips().add_tex("x1", buff=2, color=WHITE)
        meX2 = Measurement(Line(ptX2a, ptC), invert=True, dashed=True,
                           buff=0.5).add_tips().add_tex("x2", buff=-3, color=WHITE)
        self.measurement_stretch = [meX1, meX2]
        if show is not None:
            self.show_measurement_stretch = show
        if self.show_measurement_stretch:
            self.add(*self.measurement_stretch)


class FixedDiffValue1(Scene):
    """
00 这是一个长方形
01 它的长宽之比为a比b
02 如图中小长方形不重叠地放在大长方形ABCD内
03 未被覆盖的阴影部分为S1和S
04 当CD边向右平移时
06 S1与S2的面积差始终保持不变
07 问a与b的数量关系如何？
09 呃…… 为什么七年级会有这种变量变化情况下表达式恒等的题
11 对…… 变量变化…… 恒等……
12 所以，列出等式关系
13 说不定此题就能有解
14 马上 设BC的长度为变量x
15 则S1面积为(x-a)*3b
16 S2面积为（x-4b）*a
17 面积之差为计算化简为
18 3bx-3ab-3ax+4ab即
19 (3b-a)*x+ab
20 注意看
20 题目说无论x如何变化，算式的结果都不变
21 要符合这个情况的，只能是与x相乘的数为0
22 也就是3b-a=0，a=3b
23 结果就出来了……
24 看明白了么？
"""

    CONFIG = {
        "color": WHITE,
        "unit": 0.9,
        "a": 3,
        "b": 1,
        "sw": 6.6,
        "sh": 6,
        "stretch_width": 0,
        "sample": 10,
        "txt": 8,
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

        def to_corner(mobject):
            mobject.scale(0.5)
            mobject.move_to(UP*(self.sample)+LEFT*(self.rect_x))
            return mobject

        self.play(ApplyFunction(to_corner, gRA))

        fdr = FixedDiffRect(height=self.sh*self.unit, width=self.sw*self.unit,
                            a=self.a*self.unit, b=self.b*self.unit,
                            stretch_width=self.stretch_width*self.unit)
        self.play(Write(fdr), run_time=2)
        self.wait(3)

        fdr.add_measurement(True)
        self.play(*[Write(o)for o in fdr.measurement])
        self.wait()

        # indicate S1 and S2
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
                  run_time=6, rate_func=there_and_back)
        self.wait(1)

        fdr.add_measurement_x(True)
        self.play(*[Write(o)for o in fdr.measurement_x])
        self.wait()

        def update2(group, alpha):
            stretch = 1.2 * self.unit * alpha
            fdr = FixedDiffRect(height=self.sh*self.unit, width=self.sw*self.unit + stretch,
                                a=self.a*self.unit, b=self.b*self.unit,
                                stretch_width=stretch, show_measurement=True)
            fdr.shift(RIGHT*((self.sw*self.unit + stretch)/2 - self.rect_x))

            ng = VGroup(fdr)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(g1, update1),
                  run_time=5, rate_func=smooth)
        self.wait(1)

        def update3(group, alpha):
            stretch = 1.2 * self.unit * (1-alpha)
            fdr = FixedDiffRect(height=self.sh*self.unit, width=self.sw*self.unit + stretch,
                                a=self.a*self.unit, b=self.b*self.unit,
                                stretch_width=stretch, show_measurement=True, show_stretch_area=True)
            fdr.shift(RIGHT*((self.sw*self.unit + stretch)/2 - self.rect_x))

            ng = VGroup(fdr)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(g1, update3),
                  run_time=6, rate_func=there_and_back)
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
        self.play(Indicate(fdr.R5))
        self.play(Indicate(fdr.R6))
        self.play(Indicate(fdr.R7))
        self.play(Indicate(fdr.R8))

        fdr.add_measurement_stretch(True)
        self.play(*[Write(o)for o in fdr.measurement_stretch])

        tx1 = TexMobject("S_{\\delta}").scale(1.5)
        tx1a = TexMobject("=S_{1}-S_{2}").scale(1.5)
        tx1b = TexMobject("=(x-a)\\times 3b-(x-4b)\\times a").scale(1.5)
        tx1c = TexMobject("=3bx-3ab-xa+4ab").scale(1.5)
        tx1d = TexMobject("=(3b-a)\\times x+ab").scale(1.5)

        tx2 = TexMobject("(3b-a)=0").scale(1.5)
        tx2a = TexMobject("3b=a").scale(1.5)

        tx1.move_to(UP*self.txt)
        tx1a.next_to(tx1, RIGHT)
        tx2.next_to(tx1, DOWN, buff=0.6)
        tx2a.next_to(tx1, DOWN, buff=0.6)
        self.play(FadeIn(tx1))
        self.play(TransformFromCopy(VGroup(fdr.txtS1, fdr.txtS2), tx1a))

        vt1x = VGroup(tx1, tx1a)
        vt1x.generate_target()
        vt1x.target.shift(LEFT*vt1x.get_center())
        move1 = MoveToTarget(vt1x)
        self.play(move1, run_time=0.5)

        # step 2
        tx1b.next_to(tx1, RIGHT)
        self.play(ReplacementTransform(tx1a, tx1b))

        vt1x = VGroup(tx1, tx1b)
        vt1x.generate_target()
        vt1x.target.shift(LEFT*vt1x.get_center())
        move1 = MoveToTarget(vt1x)
        self.play(move1, run_time=0.5)

        # step 3
        tx1c.next_to(tx1, RIGHT)
        self.play(ReplacementTransform(tx1b, tx1c))

        vt1x = VGroup(tx1, tx1c)
        vt1x.generate_target()
        vt1x.target.shift(LEFT*vt1x.get_center())
        move1 = MoveToTarget(vt1x)
        self.play(move1, run_time=0.5)

        # step 4
        tx1d.next_to(tx1, RIGHT)
        self.play(ReplacementTransform(tx1c, tx1d))

        vt1x = VGroup(tx1, tx1d)
        vt1x.generate_target()
        vt1x.target.shift(LEFT*vt1x.get_center())
        move1 = MoveToTarget(vt1x)
        self.play(move1, run_time=0.5)
        self.wait()

        self.play(Write(tx2))
        self.play(ReplacementTransform(tx2, tx2a))


        self.wait(6)
