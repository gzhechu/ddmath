#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# develop and render undder manim version 0.5.0
#

"""
manim ex20210611_moving_ladder.py MovingLadder -r1280,720 -pqm
manim ex20210611_moving_ladder.py MovingLadder -r640,360 -pql

ffmpeg -i MovingLadder.mp4 -i MovingLadder.m4a MovingLadderRelease.mp4 -y
"""

from typing_extensions import runtime
from manim import *


class MovingLadder(MovingCameraScene):
    """
据说这曾经是一道中考的动点大题
但用到的知识却不是很难
如图靠墙竖直摆放着一个梯子AB高度是8
假设梯子会滑落到地板
问滑落过程中梯子中点C走过弧线的长度是多少？
其实肉眼观察就猜出来
这个弧线是四分之一个圆
但是，数学是严谨的
不能仅靠感觉来答题而必须用公式证明
具体到这道题，我们需要证明这个弧线是圆的一部分
并且求出圆的半径即可
来我们把梯子扶到一个比较便于分析的状态
连接OC
如果我们能证明梯子滑落到任何角度时OC的长度永远等于OC‘
也就证明了弧线CC’是圆弧
那么就得到了我们的答案
具体怎么做呢？
有两种方法：
第一，直角三角形斜边上的中线长度等于斜边的一半，这是可以直接套用的性质。所以OC等于AB的一半也就是4。
第二，如果没有学过这个知识点，则过C点做OB的平行线CD，证明三角形ADC和三角形ODC全等，也能得到OC的等于4。
所以，你能算出来弧线的长度了么？

    """

    def construct(self):
        unit_size = 0.9
        o = ORIGIN
        a = [0, 8 * unit_size, 0]
        b = [0, 0, 0]
        c = [0, 4 * unit_size, 0]
        d = c
        center = [3.6 * unit_size, 0, 0]

        ptO = Dot(o)
        ptA = Dot(a)
        ptB = Dot(b)
        ptC = Dot(c)
        ptD = Dot(d)
        ptA1 = Dot(a)
        ptC1 = Dot(c)

        [txtO, txtA, txtB, txtC, txtD, txtA1, txtC1] = [
            Tex(X) for X in ["O", "A", "B", "C", "D", "A'", "C'"]]

        [lblA, lblB, lblC] = [Tex(X) for X in ["(0,8)", "(0,0)", "(0,4)"]]

        txtO.next_to(ptO, DR)
        txtA.next_to(ptA, LEFT)
        txtB.next_to(ptB, DL)
        txtC.next_to(ptC, UR)
        txtD.next_to(ptD, LEFT)
        txtA1.next_to(ptA1, LEFT)
        txtC1.next_to(ptC1, LEFT)

        lblA.next_to(ptA, RIGHT)
        lblB.next_to(ptB, UR)
        lblC.next_to(ptC, RIGHT)

        vgLbls = VGroup(lblA, lblB, lblC)

        axes = Axes(axis_config={"include_tip": True, "include_ticks": True},
                    x_min=-2, x_max=10, y_min=-2, y_max=11,
                    y_axis_config={"unit_size": unit_size, },
                    x_axis_config={"unit_size": unit_size, }
                    )
        self.add(axes, ptO, txtO)
        self.play(self.camera.frame.animate.move_to(Dot(center)))
        self.wait()

        # 显示顶点
        self.play(FadeIn(ptA), FadeIn(ptB))
        self.play(FadeIn(txtA), FadeIn(txtB))
        self.wait()
        lAB = Line(a, b, stroke_width=6, color=BLUE)
        self.play(Create(lAB))
        self.wait()

        self.play(FadeIn(lblA), FadeIn(ptA), FadeIn(ptA1), FadeIn(ptC1))

        arcCC = Arc(radius=4*unit_size, arc_center=o,
                    color=RED, start_angle=np.deg2rad(90), angle=0)

        g1 = VGroup(lAB, arcCC, ptA, ptB, ptC, txtA, txtB, txtC)

        def update1(group, alpha):
            l = 8 * unit_size
            down = l * alpha
            y = l - down

            angle = np.arccos(y/l)
            x = np.sin(angle) * l

            a1 = a + DOWN * down
            b1 = b + RIGHT * x
            lAB1 = Line(a1, b1, stroke_width=6, color=BLUE)
            arcCC = Arc(radius=4*unit_size, arc_center=o,
                        color=RED, start_angle=np.deg2rad(90), angle=0)
            ptA1 = Dot(a1)
            ptB1 = Dot(b1)
            ptC1 = Dot([0, 4 * unit_size, 0])
            ptC1.rotate(angle=-angle, about_point=o)

            txtA.next_to(ptA1, UL)
            txtB.next_to(ptB1, DOWN)
            txtC.next_to(ptC1, UR)

            ng = VGroup(lAB1, arcCC, ptA1, ptB1, ptC1, txtA, txtB, txtC)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(g1, update1), FadeIn(txtA1), FadeIn(txtC1),
                  run_time=2, rate_func=smooth)
        self.wait(1)

        def update2(group, alpha):
            l = 8 * unit_size
            down = l * (1-alpha)
            y = l - down

            angle = np.arccos(y/l)
            x = np.sin(angle) * l

            a1 = a + DOWN * down
            b1 = b + RIGHT * x
            lAB1 = Line(a1, b1, stroke_width=6, color=BLUE)
            arcCC = Arc(radius=4*unit_size, arc_center=o,
                        color=RED, start_angle=np.deg2rad(90), angle=0)
            ptA1 = Dot(a1)
            ptB1 = Dot(b1)
            ptC1 = Dot([0, 4 * unit_size, 0])
            ptC1.rotate(angle=-angle, about_point=o)

            txtA.next_to(ptA1, UL)
            txtB.next_to(ptB1, DOWN)
            txtC.next_to(ptC1, UR)

            ng = VGroup(lAB1, arcCC, ptA1, ptB1, ptC1, txtA, txtB, txtC)
            group.become(ng)
            return group

        # 梯子回退
        self.play(UpdateFromAlphaFunc(g1, update2), FadeOut(txtA1), FadeOut(txtC1), FadeIn(vgLbls),
                  run_time=1, rate_func=smooth)
        self.wait()
        self.play(FadeOut(vgLbls))

        def update3(group, alpha):
            l = 8 * unit_size
            down = l * alpha
            y = l - down

            angle = np.arccos(y/l)
            x = np.sin(angle) * l

            a1 = a + DOWN * down
            b1 = b + RIGHT * x
            lAB1 = Line(a1, b1, stroke_width=6, color=BLUE)
            arcCC = Arc(radius=4*unit_size, arc_center=o,
                        color=RED, start_angle=np.deg2rad(90), angle=-angle)
            ptA1 = Dot(a1)
            ptB1 = Dot(b1)
            ptC1 = Dot([0, 4 * unit_size, 0])
            ptC1.rotate(angle=-angle, about_point=o)

            txtA.next_to(ptA1, UL)
            txtB.next_to(ptB1, DOWN)
            txtC.next_to(ptC1, UR)

            ng = VGroup(lAB1, arcCC, ptA1, ptB1, ptC1, txtA, txtB, txtC)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(g1, update3), FadeIn(txtA1), FadeIn(txtC1),
                  run_time=6, rate_func=smooth)
        self.wait(3)
        circle = Circle(radius=4*unit_size, color=YELLOW)
        self.play(Create(circle), run_time=2)
        self.play(FadeOut(circle), run_time=1)
        self.wait(2)

        def update4(group, alpha):
            l = 8 * unit_size
            down = (1.6 + 6.4 * (1-alpha)) * unit_size
            y = l - down

            angle = np.arccos(y/l)
            x = np.sin(angle) * l

            a1 = a + DOWN * down
            b1 = b + RIGHT * x
            lAB1 = Line(a1, b1, stroke_width=6, color=BLUE)
            arcCC = Arc(radius=4*unit_size, arc_center=o,
                        color=RED, start_angle=np.deg2rad(90), angle=-angle)
            ptA1 = Dot(a1)
            ptB1 = Dot(b1)
            ptC1 = Dot([0, 4 * unit_size, 0])
            ptC1.rotate(angle=-angle, about_point=o)

            txtA.next_to(ptA1, UL)
            txtB.next_to(ptB1, DOWN)
            txtC.next_to(ptC1, UR)

            ng = VGroup(lAB1, arcCC, ptA1, ptB1, ptC1, txtA, txtB, txtC)
            group.become(ng)
            return group

        # 扶起来
        self.play(UpdateFromAlphaFunc(g1, update4),
                  run_time=1, rate_func=smooth)
        self.wait(1)
        lOC = Line(ptO, ptC)
        self.play(Create(lOC))
        self.wait(1)

        def update5(group, alpha):
            l = 8 * unit_size
            down = (1.6 + 3.0 * (alpha)) * unit_size
            y = l - down

            angle = np.arccos(y/l)
            x = np.sin(angle) * l

            a1 = a + DOWN * down
            b1 = b + RIGHT * x
            lAB1 = Line(a1, b1, stroke_width=6, color=BLUE)
            arcCC = Arc(radius=4*unit_size, arc_center=o,
                        color=RED, start_angle=np.deg2rad(90), angle=-angle)
            ptA1 = Dot(a1)
            ptB1 = Dot(b1)
            ptC1 = Dot([0, 4 * unit_size, 0])
            ptC1.rotate(angle=-angle, about_point=o)
            lOC1 = Line(ptO, ptC1, color=YELLOW)

            txtA.next_to(ptA1, UL)
            txtB.next_to(ptB1, DOWN)
            txtC.next_to(ptC1, UR)

            ng = VGroup(lAB1, arcCC, ptA1, ptB1, ptC1, txtA, txtB, txtC, lOC1)
            group.become(ng)
            return group

        g2 = VGroup(lAB, arcCC, ptA, ptB, ptC, txtA, txtB, txtC, lOC)
        self.play(UpdateFromAlphaFunc(g2, update5),
                  run_time=2, rate_func=there_and_back)
        lOC1 = Line(ptO, ptC1, color=RED,  stroke_width=10)
        self.play(WiggleOutThenIn(lOC), run_time=1.5)
        self.play(WiggleOutThenIn(lOC1), run_time=1.5)
        self.play(Indicate(arcCC, scale_factor=2), run_time=2)
        self.play(FadeOut(lOC1))
        self.wait(2)

        tABO = Polygon(o, ptA.get_center(), ptB.get_center(),
                       color=BLUE, fill_opacity=0.2)
        self.play(FadeIn(tABO))
        self.play(WiggleOutThenIn(lOC), run_time=1)
        self.play(WiggleOutThenIn(lAB), run_time=1)
        self.play(FadeOut(tABO))
        self.wait(1)
        self.play(UpdateFromAlphaFunc(g2, update5),
                  run_time=2, rate_func=there_and_back)
        self.wait(3)

        d = [0, ptC.get_y(), 0]
        ptD = Dot(d)
        lDC = Line(ptD, ptC)
        lAC = Line(ptA, ptC)
        txtD.next_to(ptD, LEFT)

        self.play(Create(lDC), FadeIn(ptD), FadeIn(txtD))

        tCAD = Polygon(ptC.get_center(), ptA.get_center(), ptD.get_center(),
                       color=RED, fill_opacity=0.2)
        tCOD = Polygon(ptC.get_center(), ptO.get_center(), ptD.get_center(),
                       color=YELLOW, fill_opacity=0.2)

        self.play(FadeIn(tCAD))
        self.play(FadeIn(tCOD), FadeOut(tCAD))
        self.play(FadeOut(tCOD))

        self.play(WiggleOutThenIn(lAC), WiggleOutThenIn(lOC), run_time=2)
        self.wait(2)
