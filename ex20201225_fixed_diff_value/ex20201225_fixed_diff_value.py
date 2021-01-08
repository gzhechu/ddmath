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
# ffmpeg -i FixedDiffValue1.mp4 -i v1.m4a FixedDiffValue1R.mp4

# manim ddmath/ex20201225_fixed_diff_value.py FixedDiffValue2 -r1280,720 -pm
# manim ddmath/ex20201225_fixed_diff_value.py FixedDiffValue2 -r640,360 -pl
# ffmpeg -i FixedDiffValue2.mp4 -i v1.m4a FixedDiffValue2R.mp4

_DEBUG_ = False


class FixedDiffRect(Rectangle):
    # 长方体
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
        "show_all": False
    }

    def __init__(self, **kwargs):
        digest_config(self, kwargs)
        if self.show_all:
            self.show_measurement = True
            # self.show_measurement_x = True
            self.show_measurement_stretch = True
            self.show_stretch_area = True

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
                            fill_color=WHITE, fill_opacity=0.3, stroke_opacity=0)
        self.R5.shift(RIGHT*((self.width)/2-self.a - self.stretch_width/2),
                      UP*(self.height-self.b*3)/2)
        self.R6 = Rectangle(height=self.a, width=self.stretch_width,
                            fill_color=WHITE, fill_opacity=0.3, stroke_opacity=0)
        self.R6.shift(RIGHT*((self.width)/2 - self.stretch_width/2),
                      DOWN*(self.height-self.a)/2)
        if self.show_stretch_area:
            self.add(self.R5)
            self.add(self.R6)

        self.stretch_label = [txtC1, txtC2] = [
            TexMobject(X) for X in ["C_{1}", "C_{2}"]]
        self.txtC1 = txtC1
        self.txtC2 = txtC2
        self.txtC1.move_to(self.R5.get_center())
        self.txtC2.move_to(self.R6.get_center())

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
                           buff=-0.5).add_tips().add_tex("x", buff=2, color=WHITE)
        meX2 = Measurement(Line(ptX2a, ptC), invert=True, dashed=True,
                           buff=0.5).add_tips().add_tex("x", buff=-3, color=WHITE)
        self.measurement_stretch = [meX1, meX2]
        if show is not None:
            self.show_measurement_stretch = show
        if self.show_measurement_stretch:
            self.add(*self.measurement_stretch)


class FixedDiffValue1(Scene):
    """
00 这是一个长方形
03 它的长宽之比为a比b
05 如图小长方形不重叠地放在大长方形ABCD中
06 未被覆盖的阴影部分为
07 S1和S2
09 当CD边向右平移时
11 S1与S2的面积差始终保持不变
07 问a与b的数量关系如何？
09 呃…… 七年级会有这种变量变化但表达式恒等的题
11 想一想 变量变化…… 但是表达式值恒等……
12 对，所以，列出等式关系
13 说不定此题就有解
27 马上
28 设BC的长度为变量x
30 则S1面积为(x-a)*3b
33 S2面积为(x-4b)*a
37 计算面积之差
38 逐步化简……
39 就像这样
40 最终得到面积之差为
42 (3b-a)*x+ab
47 注意看
20 题目说无论x如何变化，算式的结果都不变
21 要符合这个情况的，只能是与x相乘的数为0
53 也就是3b-a=0 再化简
23 结果就出来了……
24 明白了么？
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
        tx1 = TexMobject("S_{1}-S_{2}").scale(1.5)
        tx1a = TexMobject("=S_{\\delta}").scale(1.5)
        tx1.move_to(UP*self.txt)
        tx1a.next_to(tx1, RIGHT)

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
        self.play(Write(meAa), Write(meAb))
        self.wait()

        def to_corner(mobject):
            mobject.scale(0.5)
            mobject.move_to(UP*(self.sample)+LEFT*(self.rect_x))
            return mobject

        fdr = FixedDiffRect(height=self.sh*self.unit, width=self.sw*self.unit,
                            a=self.a*self.unit, b=self.b*self.unit,
                            stretch_width=self.stretch_width*self.unit)
        self.play(Write(fdr), ApplyFunction(to_corner, gRA), run_time=2)
        self.wait(1)

        # indicate S1 and S2
        self.play(Indicate(fdr.R1))
        self.play(Indicate(fdr.R4))

        fdr.generate_target()
        fdr.target.shift(RIGHT*(self.sw*self.unit/2 - self.rect_x))
        shift1 = MoveToTarget(fdr)
        self.play(shift1)

        def update1(group, alpha):
            stretch = 1.2 * self.unit * alpha
            fdr = FixedDiffRect(height=self.sh*self.unit, width=self.sw*self.unit + stretch,
                                a=self.a*self.unit, b=self.b*self.unit,
                                stretch_width=stretch, show_measurement=False)
            fdr.shift(RIGHT*((self.sw*self.unit + stretch)/2 - self.rect_x))

            ng = VGroup(fdr)
            group.become(ng)
            return group

        g1 = VGroup(fdr)
        self.play(UpdateFromAlphaFunc(g1, update1),
                  run_time=1, rate_func=smooth)

        self.play(TransformFromCopy(VGroup(fdr.txtS1, fdr.txtS2), tx1))
        self.play(FadeIn(tx1a))

        vt1x = VGroup(tx1, tx1a)
        vt1x.generate_target()
        vt1x.target.shift(LEFT*vt1x.get_center())
        move1 = MoveToTarget(vt1x)
        self.play(move1, run_time=0.5)
        self.wait(1)

        # 更新一下对象
        self.remove(fdr)
        stretch = 1.2 * self.unit
        fdr = FixedDiffRect(height=self.sh*self.unit, width=self.sw*self.unit + stretch,
                            a=self.a*self.unit, b=self.b*self.unit,
                            stretch_width=stretch, show_measurement=False)
        fdr.shift(RIGHT*((self.sw*self.unit + stretch)/2 - self.rect_x))
        self.add(fdr)

        def update2(group, alpha):
            stretch = 1.2 * self.unit * (1-alpha)
            fdr = FixedDiffRect(height=self.sh*self.unit, width=self.sw*self.unit + stretch,
                                a=self.a*self.unit, b=self.b*self.unit,
                                stretch_width=stretch, show_measurement=False)
            fdr.shift(RIGHT*((self.sw*self.unit + stretch)/2 - self.rect_x))

            ng = VGroup(fdr)
            group.become(ng)
            return group

        # 慢速拖动一遍
        g1 = VGroup(fdr)
        if _DEBUG_:
            self.play(Write(g1), run_time=5)
        else:
            self.play(UpdateFromAlphaFunc(g1, update2),
                      run_time=5, rate_func=there_and_back)

        self.wait(1)

        def update3(group, alpha):
            stretch = 1.2 * self.unit * (1-alpha)
            fdr = FixedDiffRect(height=self.sh*self.unit, width=self.sw*self.unit + stretch,
                                a=self.a*self.unit, b=self.b*self.unit,
                                stretch_width=stretch, show_measurement=True, show_measurement_x=True)
            fdr.shift(RIGHT*((self.sw*self.unit + stretch)/2 - self.rect_x))

            ng = VGroup(fdr)
            group.become(ng)
            return group

        # 再慢速拖动一遍
        g1 = VGroup(fdr)
        if _DEBUG_:
            self.play(Write(g1), run_time=5)
        else:
            self.play(UpdateFromAlphaFunc(g1, update2),
                      run_time=5, rate_func=there_and_back)
        self.wait(1)

        # 加标签
        fdr.add_measurement(True)
        fdr.add_measurement_x(True)
        self.play(*[Write(o) for o in fdr.measurement],
                  *[Write(o) for o in fdr.measurement_x])
        self.play(Indicate(fdr.measurement_x[0]))
        self.wait(1)

        # # 替换一下
        # stretch = 1.2 * self.unit
        # fdr = FixedDiffRect(height=self.sh*self.unit, width=self.sw*self.unit + stretch,
        #                     a=self.a*self.unit, b=self.b*self.unit,
        #                     stretch_width=stretch, show_measurement=True)
        # fdr.shift(RIGHT*((self.sw*self.unit + stretch)/2 - self.rect_x))
        # self.remove(g1)
        # self.add(fdr)

        tx2 = TexMobject("S_{1}").scale(1.5)
        tx2a = TexMobject("=(x-a)\\times 3b").scale(1.5)
        tx3 = TexMobject("S_{2}").scale(1.5)
        tx3a = TexMobject("=(x-4b)\\times a").scale(1.5)

        tx2.next_to(tx1, DOWN, buff=0.6)
        tx3.next_to(tx2, DOWN, buff=0.6)

        # 显示 S1
        tx2a.next_to(tx2, RIGHT)
        self.play(TransformFromCopy(fdr.txtS1, tx2))
        self.play(TransformFromCopy(fdr.txtS1, tx2a))
        vt2x = VGroup(tx2, tx2a)
        vt2x.generate_target()
        vt2x.target.shift(LEFT*vt2x.get_center())
        move2 = MoveToTarget(vt2x)
        self.play(move2, run_time=0.5)

        # 显示 S2
        tx3a.next_to(tx3, RIGHT)
        self.play(TransformFromCopy(fdr.txtS2, tx3))
        self.play(TransformFromCopy(fdr.txtS2, tx3a))
        vt3x = VGroup(tx3, tx3a)
        vt3x.generate_target()
        vt3x.target.shift(LEFT*vt3x.get_center())
        move3 = MoveToTarget(vt3x)
        self.play(move3, run_time=0.5)
        self.wait(1)

        # 显示差
        tx1a = TexMobject("S_{\\delta}=S_{1}-S_{2}").scale(1.5)
        tx2 = TexMobject("S_{\\delta}").scale(1.5)
        tx2a = TexMobject("=S_{1}-S_{2}").scale(1.5)
        tx2b = TexMobject("=(x-a)\\times 3b-(x-4b)\\times a").scale(1.5)
        tx2c = TexMobject("=3bx-3ab-xa+4ab").scale(1.5)
        tx2d = TexMobject("=", "(3b-a)", "\\times x+ab").scale(1.5)
        tx2e = TexMobject("=", "(3b-a)",
                          "\\times", "x", "+ab").scale(1.5)
        tx2e.set_color_by_tex("(3b-a)", BLUE)
        tx2e.set_color_by_tex("x", RED)

        tx3 = TexMobject("3b-a=0").scale(1.5)
        tx3a = TexMobject("3b=a").scale(1.5)

        # step 1
        tx2.next_to(vt1x, DOWN, buff=0.6)
        tx3.next_to(tx2, DOWN, buff=0.6)
        tx3a.next_to(tx2, DOWN, buff=0.6)
        tx1a.move_to(vt1x.get_center())
        self.remove(vt1x)
        self.play(ReplacementTransform(VGroup(vt2x, vt3x), tx1a))

        self.play(FadeIn(tx2))
        # step 1
        tx2a.next_to(tx2, RIGHT)
        vt2x = VGroup(tx2, tx2a)
        vt2x.generate_target()
        vt2x.target.shift(LEFT*vt2x.get_center())
        move1 = MoveToTarget(vt2x)
        self.play(move1, run_time=0.5)

        # step 2
        tx2b.next_to(tx2, RIGHT)
        self.play(ReplacementTransform(tx2a, tx2b))
        vt2x = VGroup(tx2, tx2b)
        vt2x.generate_target()
        vt2x.target.shift(LEFT*vt2x.get_center())
        move1 = MoveToTarget(vt2x)
        self.play(move1, run_time=0.5)

        # step 3
        tx2c.next_to(tx2, RIGHT)
        self.play(ReplacementTransform(tx2b, tx2c))
        vt2x = VGroup(tx2, tx2c)
        vt2x.generate_target()
        vt2x.target.shift(LEFT*vt2x.get_center())
        move1 = MoveToTarget(vt2x)
        self.play(move1, run_time=0.5)

        # step 4
        tx2d.next_to(tx2, RIGHT)
        self.play(ReplacementTransform(tx2c, tx2d))
        vt2x = VGroup(tx2, tx2d)
        vt2x.generate_target()
        vt2x.target.shift(LEFT*vt2x.get_center())
        move1 = MoveToTarget(vt2x)
        self.play(move1, run_time=0.5)
        # self.wait(1)

        g1 = VGroup(fdr)
        if _DEBUG_:
            self.play(Write(g1), run_time=5)
        else:
            self.play(UpdateFromAlphaFunc(g1, update3),
                      run_time=5, rate_func=there_and_back)
        # self.wait(1)
        self.play(WiggleOutThenIn(fdr.measurement_x[0], run_time=3))

        # mark 3b-a
        tx2e.move_to(tx2d.get_center())
        vt2x = VGroup(tx2, tx2e)
        self.play(Indicate(vt2x))
        self.play(FadeInFrom(tx3, UP))
        self.wait(3)
        self.play(ReplacementTransform(tx3, tx3a))
        self.wait(2)


class FixedDiffValue2(Scene):
    """
00 接上一个视频
01 说大长方形ABCD中如图排列了7个小长方形
05 当侧边CD向右平移时
07 S1与S2的面积差始终保持不变
10 问小长方形长宽a与b的数值关系如何？
14 还是先标出辅助数据
08 这次试试用几何方法来解题
09 先平移CD边
21 不过平移之前，标记出初始的S1和S2
24 然后……
25 我们看到随着平移新增了两个灰色长方形C1和C2
29 题目说到S1与S2的面积差保持不变
14 那么拉伸后的面积就可以表示为
18 (S1+C1)和(S2+C2)
38 带入等式仔细看一下
19 两边都有S1-S2
20 则消去化简为0=C1-C2
21 也就是说新增的灰色长方形面积相等
22 突然变得很有趣对吧？
23 接着计算两个灰色长方形的面积
24 假设CD向右平移的距离为x
25 那么两个灰色长方形的宽也为x
26 他们的面积公式则可以列为
27 3b*x=a*x
28 看！
23 结果就出来了……
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
        tx1 = TexMobject("S_1-S_2").scale(1.5)
        tx1a = TexMobject("=S_\\delta").scale(1.5)
        tx1.move_to(UP*self.txt)
        tx1a.next_to(tx1, RIGHT)
        tx2 = TexMobject("S_\\delta").scale(1.5)
        tx2a1 = TexMobject("=(S_1+C_1)").scale(1.5)
        tx2a2 = TexMobject("-(S_2+C2)").scale(1.5)
        tx2b = TexMobject("=S_1+C_1-S_2-C2").scale(1.5)
        tx2.next_to(tx1, DOWN, buff=0.6)

        def update1(group, alpha):
            stretch = 1.2 * self.unit * alpha
            fdr = FixedDiffRect(height=self.sh*self.unit, width=self.sw*self.unit + stretch,
                                a=self.a*self.unit, b=self.b*self.unit,
                                stretch_width=stretch, show_measurement=False, )
            fdr.shift(RIGHT*((self.sw*self.unit + stretch)/2 - self.rect_x))
            ng = VGroup(fdr)
            group.become(ng)
            return group

        def update2(group, alpha):
            stretch = 1.2 * self.unit * alpha
            fdr = FixedDiffRect(height=self.sh*self.unit, width=self.sw*self.unit + stretch,
                                a=self.a*self.unit, b=self.b*self.unit,
                                stretch_width=stretch, show_all=True, )
            fdr.shift(RIGHT*((self.sw*self.unit + stretch)/2 - self.rect_x))
            ng = VGroup(fdr)
            group.become(ng)
            return group

        def update3(group, alpha):
            stretch = 1.2 * self.unit * (1-alpha)
            fdr = FixedDiffRect(height=self.sh*self.unit, width=self.sw*self.unit + stretch,
                                a=self.a*self.unit, b=self.b*self.unit,
                                stretch_width=stretch, show_all=True)
            fdr.shift(RIGHT*((self.sw*self.unit + stretch)/2 - self.rect_x))
            ng = VGroup(fdr)
            group.become(ng)
            return group

        RectSample = Rectangle(height=self.b*self.unit, width=self.a*self.unit,
                               fill_color=BLUE, fill_opacity=0.5)
        [ptAa, ptAb, ptAc, ptAd] = [RectSample.get_corner(X) for X in [
            UL, DL, UR,  DR]]

        meAa = Measurement(Line(ptAa, ptAc), invert=True, dashed=True,
                           buff=-0.5).add_tips().add_tex("a", buff=3, color=WHITE)
        meAb = Measurement(Line(ptAa, ptAb), invert=False, dashed=True,
                           buff=-0.5).add_tips().add_tex("b", buff=-3, color=WHITE)
        gRA = VGroup(RectSample, meAa, meAb)

        gRA.scale(0.5)
        gRA.move_to(ORIGIN+UP*(self.sample)+LEFT*(self.rect_x))

        fdr = FixedDiffRect(height=self.sh*self.unit, width=self.sw*self.unit,
                            a=self.a*self.unit, b=self.b*self.unit,
                            stretch_width=self.stretch_width*self.unit)
        fdr.shift(RIGHT*(self.sw*self.unit/2 - self.rect_x))
        self.play(Write(fdr), FadeIn(gRA), run_time=2)
        # self.wait(1)
        g1 = VGroup(fdr)

        if _DEBUG_:
            self.play(Write(g1), run_time=4)
        else:
            self.play(UpdateFromAlphaFunc(g1, update1),
                      run_time=4, rate_func=there_and_back)

        # indicate S1 and S2
        self.play(Indicate(fdr.R1))
        self.play(Indicate(fdr.R4))
        trans1 = TransformFromCopy(VGroup(fdr.txtS1, fdr.txtS2), tx1a)
        self.play(trans1, FadeIn(tx1))
        vt1x = VGroup(tx1, tx1a)
        vt1x.generate_target()
        vt1x.target.shift(LEFT*vt1x.get_center())
        move1 = MoveToTarget(vt1x)
        self.play(move1, run_time=1)

        def to_center(mobject):
            mobject.scale(2)
            mobject.move_to(ORIGIN + UP*(self.sample/1.6))
            return mobject

        def to_corner(mobject):
            mobject.scale(0.5)
            mobject.move_to(ORIGIN+UP*(self.sample)+LEFT*(self.rect_x))
            return mobject

        self.play(ApplyFunction(to_center, gRA))
        self.wait(1)
        self.play(ApplyFunction(to_corner, gRA))

        fdr.add_measurement(True)
        self.play(*[Write(o) for o in fdr.measurement])
        self.wait(2)

        self.play(ShowPassingFlashAround(fdr.R1), run_time=2)
        self.play(ShowPassingFlashAround(fdr.R4), run_time=2)

        g1 = VGroup(fdr)
        if _DEBUG_:
            self.play(Write(g1), run_time=3)
        else:
            self.play(UpdateFromAlphaFunc(g1, update2),
                      run_time=3, rate_func=smooth)

        # 更新一下对象，不知道为啥不更新会有问题
        self.remove(fdr)
        stretch = 1.2 * self.unit
        fdr = FixedDiffRect(height=self.sh*self.unit, width=self.sw*self.unit + stretch,
                            a=self.a*self.unit, b=self.b*self.unit,
                            stretch_width=stretch, show_all=True, )
        self.add(fdr)

        # 显示 C1，C2
        self.play(AnimationGroup(Write(fdr.txtC1),
                                 Write(fdr.txtC2), lag_ratio=0.5))
        self.wait(3)

        # 显示公式
        tx2a1.next_to(tx2, RIGHT)
        tx2a2.next_to(tx2a1, RIGHT)
        self.play(Write(tx2))
        self.play(TransformFromCopy(VGroup(fdr.txtS1, fdr.txtC1), tx2a1))
        self.play(TransformFromCopy(VGroup(fdr.txtS2, fdr.txtC2), tx2a2))

        vt2x = VGroup(tx2, tx2a1, tx2a2)
        vt2x.generate_target()
        vt2x.target.shift(LEFT*vt2x.get_center())
        move2 = MoveToTarget(vt2x)
        self.play(move2, run_time=0.5)

        # 消元公式
        tx1b = TexMobject("=", "S_1", "+C_1", "-S_2", "-C2").scale(1.5)
        tx1c = TexMobject("0").scale(1.5)
        tx1d = TexMobject("=C_1-C_2").scale(1.5)
        tx1e = TexMobject("C_1").scale(1.5)
        tx1f = TexMobject("=C_2").scale(1.5)

        tx1b.next_to(tx1, RIGHT)
        self.remove(tx1a)
        # tx1 = tx1l
        self.play(ReplacementTransform(vt2x, tx1b))
        vt1x = VGroup(tx1, tx1b)
        vt1x.generate_target()
        vt1x.target.shift(LEFT*vt1x.get_center())
        move1 = MoveToTarget(vt1x)
        self.play(move1, run_time=1)
        self.play(Indicate(vt1x))

        tx1.set_color_by_tex("S_1-S_2", BLUE)
        tx1b.set_color_by_tex("S_1", RED)
        tx1b.set_color_by_tex("-S_2", RED)
        # 显示颜色后停顿
        self.wait()

        tx1c.next_to(tx1b, LEFT)
        tx1d.next_to(tx1c, RIGHT)
        self.play(ReplacementTransform(tx1, tx1c),
                  ReplacementTransform(tx1b, tx1d))
        vt1x = VGroup(tx1c, tx1d)
        vt1x.generate_target()
        vt1x.target.shift(LEFT*vt1x.get_center())
        move1 = MoveToTarget(vt1x)
        self.play(move1, run_time=1)

        tx1e.next_to(tx1d, LEFT)
        tx1f.next_to(tx1e, RIGHT)
        self.play(ReplacementTransform(tx1c, tx1e),
                  ReplacementTransform(tx1d, tx1f))
        vt1x = VGroup(tx1e, tx1f)
        vt1x.generate_target()
        vt1x.target.shift(LEFT*vt1x.get_center())
        move1 = MoveToTarget(vt1x)
        self.play(move1, run_time=1)

        self.play(*[Indicate(o) for o in [fdr.R5, fdr.R6]])
        self.play(TransformFromCopy(fdr.R5, tx1e.copy()),
                  TransformFromCopy(fdr.R6, tx1f.copy()))

        # 更新一下对象，不知道为啥不更新会有问题
        self.remove(fdr.txtC1, fdr.txtC2)
        self.remove(fdr)
        stretch = 1.2 * self.unit
        fdr = FixedDiffRect(height=self.sh*self.unit, width=self.sw*self.unit + stretch,
                            a=self.a*self.unit, b=self.b*self.unit,
                            stretch_width=stretch, show_all=True, )
        self.add(fdr)
        g1 = VGroup(fdr)
        if _DEBUG_:
            self.play(Write(g1), run_time=4)
        else:
            self.play(UpdateFromAlphaFunc(g1, update3),
                      run_time=4, rate_func=there_and_back)
        self.add(fdr.txtC1, fdr.txtC2)

        # 加 x1, x2
        fdr.add_measurement_stretch(True)
        self.play(*[Write(o) for o in fdr.measurement_stretch])
        self.play(*[Indicate(o, rate_func=there_and_back, scale_factor=1.5, run_time=1)
                    for o in fdr.measurement_stretch])

        self.wait(1)

        tx2l1 = TexMobject("C_1=3b\\times x").scale(1.5)
        tx2r1 = TexMobject("=C_2=a\\times x").scale(1.5)
        tx2l2 = TexMobject("3b", "\\times x").scale(1.5)
        tx2r2 = TexMobject("=a", "\\times x").scale(1.5)
        tx2l3 = TexMobject("3b").scale(1.5)
        tx2r3 = TexMobject("=a").scale(1.5)

        tx2l1.next_to(vt1x, DOWN, buff=0.6)
        tx2r1.next_to(tx2l1, RIGHT)
        self.play(TransformFromCopy(fdr.R5, tx2l1))
        self.play(TransformFromCopy(fdr.R6, tx2r1))
        vt2x = VGroup(tx2l1, tx2r1)
        vt2x.generate_target()
        vt2x.target.shift(LEFT*vt2x.get_center())
        move2 = MoveToTarget(vt2x)
        self.play(move2, run_time=0.5)

        tx2l2.next_to(tx2r1, LEFT)
        tx2r2.next_to(tx2l2, RIGHT)
        self.play(ReplacementTransform(tx2l1, tx2l2))
        self.play(ReplacementTransform(tx2r1, tx2r2))
        vt2x = VGroup(tx2l2, tx2r2)
        vt2x.generate_target()
        vt2x.target.shift(LEFT*vt2x.get_center())
        move2 = MoveToTarget(vt2x)
        self.play(move2, run_time=0.5)
        tx2l2.set_color_by_tex("\\times x", BLUE)
        tx2r2.set_color_by_tex("\\times x", BLUE)
        self.wait()

        tx2l3.next_to(tx2r2, LEFT)
        tx2r3.next_to(tx2l3, RIGHT)
        self.play(ReplacementTransform(tx2l2, tx2l3),
                  ReplacementTransform(tx2r2, tx2r3))

        self.wait()
