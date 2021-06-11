#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# develop and render undder manim version 0.5.0
#

"""
manim ex20210611_moving_midpoint.py MovingMidpoint -r1280,720 -pqm
manim ex20210611_moving_midpoint.py MovingMidpoint -r640,360 -pql

ffmpeg -i MovingMidpoint.mp4 -i MovingMidpoint.m4a SquareParallelRelease.mp4 -y
"""

from manim import *


class MovingMidpoint(MovingCameraScene):
    """
这题可难了，是一道中考题。
    """

    def construct(self):
        unit_size = 0.9
        o = ORIGIN
        a = [0, 8 * unit_size, 0]
        b = [0, 0, 0]
        c = [0, 4 * unit_size, 0]
        d = c
        e = o
        f = np.asarray(c) * 0.6
        center = [4 * unit_size, 0, 0]

        ptO = Dot(o)
        ptA = Dot(a)
        ptB = Dot(b)
        ptC = Dot(c)
        ptD = Dot(d)
        ptE = Dot(e)
        ptF = Dot(f)

        [txtO, txtA, txtB, txtC, txtD, txtE, txtF, txtG, txtH] = [
            Tex(X) for X in ["O", "A", "B", "C", "D", "E", "F", "G", "H"]]

        [lblA, lblB, lblC] = [Tex(X) for X in ["(0,8)", "(0,0)", "(0,4)"]]

        txtO.next_to(ptO, DL)
        txtA.next_to(ptA, LEFT)
        txtB.next_to(ptB, DR)
        txtC.next_to(ptC, LEFT)
        txtD.next_to(ptD, UP)
        txtE.next_to(ptE, DR)
        txtF.next_to(ptF, DR)

        lblA.next_to(ptA, RIGHT)
        lblB.next_to(ptB, UR)
        lblC.next_to(ptC, RIGHT)

        ptTxts = [txtA, txtB, txtC]
        vgTxts = VGroup(*ptTxts)
        vgPt = VGroup(ptA, ptB, ptC)
        vgLbls = VGroup(lblA, lblB, lblC)

        axes = Axes(axis_config={"include_tip": True, "include_ticks": True},
                    x_min=-2, x_max=10, y_min=-2, y_max=11,
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
        self.play(FadeIn(vgLbls))
        self.wait()

        lAB = Line(a, b)
        self.play(Create(lAB))
        self.remove(vgLbls)
        arc = Arc(radius=4, arc_center=o,
                  color=RED, start_angle=np.deg2rad(90), angle=0)

        g1 = VGroup(lAB, arc, ptA, ptB, ptC, txtA, txtB, txtC)

        def update1(group, alpha):
            speed_base = 8 * unit_size
            a1 = a + speed_base * DOWN * alpha
            angle =
            b1 = b + speed_base * RIGHT * alpha
            lAB1 = Line(a1, b1)
            arc = Arc(radius=4*unit_size, arc_center=o,
                      color=RED, start_angle=np.deg2rad(90), angle=-alpha * np.deg2rad(90))
            ptA1 = Dot(a1)
            ptB1 = Dot(b1)
            ptC1 = Dot(o)
            txtA.next_to(ptA1, LEFT)
            txtB.next_to(ptB1, DR)

            ng = VGroup(lAB1, arc, ptA1, ptB1, ptC1, txtA, txtB, txtC)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(g1, update1),
                  run_time=4, rate_func=linear)
        self.wait(5)
        return

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
        self.wait(3)

        d1 = d + 4.5 * unit_size * LEFT * 2
        e1 = e + 4.5 * unit_size * RIGHT * 3
        tri1 = Polygon(c, d1, f, color=BLUE, fill_opacity=0.3)
        tri2 = Polygon(o, e1, f, color=RED, fill_opacity=0.3)
        poly1 = Polygon(o, b, d1, f, color=WHITE, fill_opacity=0.3)
        self.play(Create(tri1), Create(tri2))
        self.wait()

        vgTriangle = VGroup(tri1, tri2)
        self.play(TransformFromCopy(vgTriangle, tx3))
        self.wait()

        # self.play(Create(poly1))
        self.wait(5)
