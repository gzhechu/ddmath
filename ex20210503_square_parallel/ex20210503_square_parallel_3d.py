#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# develop and render undder manim version 0.5.0
#

"""
manim ex20210503_square_parallel_3d.py SquareParallel -r1280,720 -pqm
manim ex20210503_square_parallel_3d.py SquareParallel -r640,360 -pql

ffmpeg -i SquareParallel.mp4 -i SquareParallel.m4a SquareParallel3DRelease.mp4 -y
"""

from manim import *


class SquareParallel(ThreeDScene):
    """
这是一道平行线应用题
说长方形ABCD的底边CD上有一个点F
连接AF构成三角形ADF
延AF边翻转三角形
形成一个新三角形AEF
新三角形的边AE刚好与对角线BD平行
已知角1为28度
问：角2是多少度？
好了先暂停一下
想一想不要看答案
然后……我开始解题
从翻转的蓝色三角形可知：
角3与角4相等、角5是一个直角
又因为AE平行于BD
所以角6也是一个直角
还有个条件是长方形上下两边平行
所以角2等于角3
那么，求角2的度数就很简单了。
其实解这道题的关键点，
是要把所有已知的条件全部用到
你试一试……能解出来了么？
    """

    def construct(self):
        width = 4.0
        height = np.tan(np.deg2rad(28)) * width

        a = [-width, height, 0]
        b = [width, height, 0]
        c = [width, -height, 0]
        d = [-width, -height, 0]

        ptA = Dot(a)
        ptB = Dot(b)
        ptC = Dot(c)
        ptD = Dot(d)

        [txtA, txtB, txtC, txtD, txtE, txtF, txtG, txtH] = [
            Tex(X) for X in ["A", "B", "C", "D", "E", "F", "G", "H"]]

        [txt1, txt2, txt3, txt4, txt5, txt6] = [
            Tex(X) for X in ["1", "2", "3", "4", "5", "6"]]

        txtA.next_to(ptA, UL)
        txtB.next_to(ptB, UR)
        txtC.next_to(ptC, DR)
        txtD.next_to(ptD, DL)

        ptTxts = [txtA, txtB, txtC, txtD]
        vgTxts = VGroup(*ptTxts)

        vgPt = VGroup(ptA, ptB, ptC, ptD)

        # self.set_camera_orientation(phi=60 * DEGREES, theta=-60*DEGREES)

        axes = ThreeDAxes()

        # 正方形 及坐标网格
        rect = Rectangle(height=height*2.0,
                         width=width*2.0)
        self.play(FadeIn(vgPt), Create(rect))
        # 显示顶点
        self.play(FadeIn(vgTxts))
        self.move_camera(phi=30 * DEGREES, theta=-100*DEGREES, run_time=1)
        self.play(FadeIn(axes))
        self.begin_ambient_camera_rotation(rate=0.1)

        lBD = DashedLine(b, d)
        lAE = Line([2*height, 0, 0], [0, 0, 0])
        lAE.rotate_about_origin(angle=np.deg2rad(28))
        lAE.shift(height * UP + LEFT * width)
        e = lAE.get_start()
        # print(e)
        ptE = Dot(e)
        txtE.next_to(ptE, UP)

        lAF = Line([0, 0, 0], [2.0 * height/np.sin(np.deg2rad(31)), 0, 0])
        lAF.rotate_about_origin(angle=np.deg2rad(-31))
        lAF.shift(height * UP + LEFT * width)
        f = lAF.get_end()
        # print(f)
        ptF = Dot(f)
        txtF.next_to(ptF, DR)

        lEF = Line(e, f)

        self.play(Indicate(txtF, scale_factor=2), FadeIn(ptF))
        self.play(Write(lAF))

        tADF = Polygon(a, d, f, color=BLUE, fill_opacity=0.2)
        self.play(Write(tADF))
        # self.wait(1)
        self.move_camera(phi=70 * DEGREES, theta=-95*DEGREES, run_time=1)

        direction = [-1/np.tan(np.deg2rad(31)), 1, 0]
        rotate1 = Rotate(tADF, angle=PI, axis=direction, about_point=a)
        self.play(FadeIn(lEF), FadeIn(lAE), FadeIn(ptE),
                  FadeIn(txtE), rotate1, run_time=2)
        self.move_camera(phi=30 * DEGREES, run_time=1)
        self.wait()

        lAE1 = lAE.copy()
        lAE1.generate_target()
        lAE1.target.shift(DOWN*height+RIGHT*width)

        self.play(Write(lBD), run_time=1)
        self.play(MoveToTarget(lAE1), rate_func=there_and_back, run_time=3)

        ang1 = Sector(outer_radius=1, color=BLUE, fill_opacity=0.5,
                      angle=np.deg2rad(28))
        ang1.shift(d)
        txt1.next_to(ang1, RIGHT)

        ang2 = Sector(outer_radius=1, color=RED, fill_opacity=0.5,
                      angle=np.deg2rad(-31))
        ang2.shift(a)
        txt2.next_to(ang2, RIGHT)

        ang3 = Sector(outer_radius=1, color=YELLOW, fill_opacity=0.5,
                      start_angle=np.deg2rad(180), angle=np.deg2rad(-31))
        ang3.shift(f)
        txt3.next_to(ang3, LEFT)

        ang4 = Sector(outer_radius=1, color=GREEN, fill_opacity=0.5,
                      start_angle=np.deg2rad(149), angle=np.deg2rad(-31))
        ang4.shift(f)
        txt4.next_to(ang4, UL)

        ang5 = RightAngle(lEF, lAE, other_angle=False)
        ang6 = RightAngle(lEF, lBD, other_angle=True)
        txt5.next_to(ang5, DOWN)
        txt6.next_to(ang6, DOWN)

        t1 = MathTex("\\angle 1 = 28^\\circ").scale(2)
        t2 = MathTex("\\angle 2 = ?").scale(2)
        t3 = MathTex("\\angle 1 + \\angle 3 + \\angle 4 = 90^\\circ").scale(2)
        t1.move_to(UP * 8.6)
        t2.next_to(t1, DOWN, buff=0.5)
        t3.next_to(t2, DOWN, buff=0.5)

        self.play(Indicate(ang1), Indicate(txt1), scale_factor=2)
        self.add_fixed_in_frame_mobjects(t1)        
        self.play(Write(t1))
        self.play(Indicate(ang2), Indicate(txt2), scale_factor=2)
        self.add_fixed_in_frame_mobjects(t2)
        self.play(Write(t2))
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=30 * DEGREES, theta=-60*DEGREES, run_time=2)
        self.wait(3)

        rotate2 = Rotate(tADF, angle=-PI, axis=direction, about_point=a)
        self.play(rotate2, rate_func=there_and_back, run_time=3)

        self.begin_ambient_camera_rotation(rate=0.1)

        self.play(Indicate(ang3), Indicate(txt3), scale_factor=2, run_time=0.5)
        self.play(Indicate(ang4), Indicate(txt4), scale_factor=2, run_time=0.5)
        self.wait(0.5)
        self.play(Indicate(ang5), Indicate(txt5), scale_factor=2)
        self.wait(0.5)

        self.play(ApplyWave(lAE))
        self.play(ApplyWave(lBD))

        self.play(Indicate(ang6), Indicate(txt6), scale_factor=2)
        self.move_camera(phi=15 * DEGREES, theta=-110*DEGREES, run_time=2)
        self.stop_ambient_camera_rotation()
        self.wait(2)

        self.play(Indicate(ang2), Indicate(txt2), scale_factor=2)
        self.play(Indicate(ang3), Indicate(txt3), scale_factor=2)

        self.move_camera(phi=0 * DEGREES, theta=-90*DEGREES, run_time=1)
        self.play(FadeOut(axes))
        
        self.add_fixed_in_frame_mobjects(t3)
        self.play(Write(t3))
        self.wait(5)
