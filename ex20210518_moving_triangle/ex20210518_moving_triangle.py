#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# develop and render undder manim version 0.5.0
#

"""
manim ex20210518_moving_triangle.py MovingTriangle -r1280,720 -pqm
manim ex20210518_moving_triangle.py MovingTriangle -r640,360 -pql

ffmpeg -i MovingTriangle.mp4 -i MovingTriangle.m4a SquareParallelRelease.mp4 -y
"""

from manim import *


class MovingTriangle(MovingCameraScene):
    """
这题可难了
    """

    def construct(self):
        unit_size = 0.3
        o = ORIGIN
        a = [30 * unit_size, 0, 0]
        b = [0, 7 * unit_size, 0]
        c = [24 * unit_size, 7 * unit_size, 0]
        d = c
        e = o
        f = np.asarray(c) * 0.6
        center = [15 * unit_size, 0, 0]

        ptO = Dot(o)
        ptA = Dot(a)
        ptB = Dot(b)
        ptC = Dot(c)
        ptD = Dot(d)
        ptE = Dot(e)
        ptF = Dot(f)

        [txtO, txtA, txtB, txtC, txtD, txtE, txtF, txtG, txtH] = [
            Tex(X) for X in ["O", "A", "B", "C", "D", "E", "F", "G", "H"]]

        [txt1, txt2, txt3, txt4, txt5, txt6] = [
            Tex(X) for X in ["1", "2", "3", "4", "5", "6"]]

        txtO.next_to(ptO, DL)
        txtA.next_to(ptA, DR)
        txtB.next_to(ptB, UL)
        txtC.next_to(ptC, UR)
        txtD.next_to(ptD, UP)
        txtE.next_to(ptE, DR)
        txtF.next_to(ptF, DR)

        ptTxts = [txtA, txtB, txtC]
        vgTxts = VGroup(*ptTxts)
        vgPt = VGroup(ptA, ptB, ptC)

        axes = Axes(axis_config={"include_tip": True, "include_ticks": False},
                    x_min=-2, x_max=33, y_min=-2, y_max=13,
                    y_axis_config={"unit_size": unit_size, },
                    x_axis_config={"unit_size": unit_size, }
                    )
        self.add(axes, txtO)
        self.play(self.camera.frame.animate.move_to(Dot(center)))
        self.wait()

        # 显示顶点
        self.play(FadeIn(vgPt))
        self.play(FadeIn(vgTxts))
        self.wait()

        lOC = Line(ORIGIN, c)
        lBC = Line(b, c)
        lDE = Line(d, e)

        self.play(Create(lBC))
        self.play(Write(lOC))
        self.wait()

        g1 = VGroup(ptD, ptE, txtD, txtE, lDE)

        def update1(group, alpha):
            speed_base = 10 * unit_size
            d1 = d + speed_base * LEFT * 2 * alpha
            e1 = e + speed_base * RIGHT * 3 * alpha
            lDE1 = Line(d1, e1)

            ptD1 = Dot(d1)
            ptE1 = Dot(e1)
            txtD.next_to(ptD1, UP)
            txtE.next_to(ptE1, DOWN)
            ng = VGroup(ptD1, ptE1, txtD, txtE, lDE1)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(g1, update1), FadeIn(ptF.copy()),
                  FadeIn(txtF.copy()), run_time=4, rate_func=there_and_back)
        self.remove(lDE)
        self.wait()

        def update2(group, alpha):
            speed_base = 4.5 * unit_size
            d1 = d + speed_base * LEFT * 2 * alpha
            e1 = e + speed_base * RIGHT * 3 * alpha
            lDE1 = Line(d1, e1)
            ptD1 = Dot(d1)
            ptE1 = Dot(e1)
            txtD.next_to(ptD1, UP)
            txtE.next_to(ptE1, DOWN)
            ng = VGroup(ptD1, ptE1, txtD, txtE, lDE1)
            group.become(ng)
            return group

        self.add(ptF, txtF)
        self.play(UpdateFromAlphaFunc(g1, update2),
                  run_time=2, rate_func=smooth)
        self.wait()

        d1 = d + 4.5 * unit_size * LEFT * 2
        e1 = e + 4.5 * unit_size * RIGHT * 3
        tri1 = Polygon(c, d1, f, color=BLUE, fill_opacity=0.3)
        tri2 = Polygon(o, e1, f, color=RED, fill_opacity=0.3)
        poly1 = Polygon(o, b, d1, f, color=WHITE, fill_opacity=0.3)
        self.play(Create(tri1), Create(tri2))
        self.play(Create(poly1))
        self.wait(5)
