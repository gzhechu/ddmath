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

from manim import *


class MovingLadder(MovingCameraScene):
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
        center = [3.6 * unit_size, 0, 0]

        ptO = Dot(o)
        ptA = Dot(a)
        ptB = Dot(b)
        ptC = Dot(c)
        ptD = Dot(d)

        [txtO, txtA, txtB, txtC, txtD, txtE, txtF, txtG, txtH] = [
            Tex(X) for X in ["O", "A", "B", "C", "D", "E", "F", "G", "H"]]

        [lblA, lblB, lblC] = [Tex(X) for X in ["(0,8)", "(0,0)", "(0,4)"]]

        txtO.next_to(ptO, DL)
        txtA.next_to(ptA, UL)
        txtB.next_to(ptB, DR)
        txtC.next_to(ptC, UR)
        txtD.next_to(ptD, UP)

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

        self.play(FadeIn(ptC), FadeIn(txtC))

        arc = Arc(radius=4, arc_center=o,
                  color=RED, start_angle=np.deg2rad(90), angle=0)

        g1 = VGroup(lAB, arc, ptA, ptB, ptC, txtA, txtB, txtC)

        def update1(group, alpha):
            l = 8 * unit_size
            down = l * alpha
            y = l - down

            angle = np.arccos(y/l)
            x = np.sin(angle) * l

            a1 = a + DOWN * down
            b1 = b + RIGHT * x
            lAB1 = Line(a1, b1, stroke_width=6, color=BLUE)
            arc = Arc(radius=4*unit_size, arc_center=o,
                      color=RED, start_angle=np.deg2rad(90), angle=0)
            ptA1 = Dot(a1)
            ptB1 = Dot(b1)
            ptC1 = Dot([0, 4 * unit_size, 0])
            ptC1.rotate(angle=-angle, about_point=o)

            txtA.next_to(ptA1, UL)
            txtB.next_to(ptB1, DR)
            txtC.next_to(ptC1, UR)

            ng = VGroup(lAB1, arc, ptA1, ptB1, ptC1, txtA, txtB, txtC)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(g1, update1),
                  run_time=2, rate_func=smooth)
        self.wait(2)

        def update2(group, alpha):
            l = 8 * unit_size
            down = l * (1-alpha)
            y = l - down

            angle = np.arccos(y/l)
            x = np.sin(angle) * l

            a1 = a + DOWN * down
            b1 = b + RIGHT * x
            lAB1 = Line(a1, b1, stroke_width=6, color=BLUE)
            arc = Arc(radius=4*unit_size, arc_center=o,
                      color=RED, start_angle=np.deg2rad(90), angle=0)
            ptA1 = Dot(a1)
            ptB1 = Dot(b1)
            ptC1 = Dot([0, 4 * unit_size, 0])
            ptC1.rotate(angle=-angle, about_point=o)

            txtA.next_to(ptA1, UL)
            txtB.next_to(ptB1, DR)
            txtC.next_to(ptC1, UR)

            ng = VGroup(lAB1, arc, ptA1, ptB1, ptC1, txtA, txtB, txtC)
            group.become(ng)
            return group

        # 梯子回退
        self.play(UpdateFromAlphaFunc(g1, update2),
                  run_time=1, rate_func=smooth)

        self.play(FadeIn(vgLbls))
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
            arc = Arc(radius=4*unit_size, arc_center=o,
                      color=RED, start_angle=np.deg2rad(90), angle=-angle)
            ptA1 = Dot(a1)
            ptB1 = Dot(b1)
            ptC1 = Dot([0, 4 * unit_size, 0])
            ptC1.rotate(angle=-angle, about_point=o)

            txtA.next_to(ptA1, UL)
            txtB.next_to(ptB1, DR)
            txtC.next_to(ptC1, UR)

            ng = VGroup(lAB1, arc, ptA1, ptB1, ptC1, txtA, txtB, txtC)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(g1, update3),
                  run_time=3, rate_func=smooth)
        self.wait(5)

        def update4(group, alpha):
            l = 8 * unit_size
            down = (1.6 + 6.4 * (1-alpha)) * unit_size
            y = l - down

            angle = np.arccos(y/l)
            x = np.sin(angle) * l

            a1 = a + DOWN * down
            b1 = b + RIGHT * x
            lAB1 = Line(a1, b1, stroke_width=6, color=BLUE)
            arc = Arc(radius=4*unit_size, arc_center=o,
                      color=RED, start_angle=np.deg2rad(90), angle=-angle)
            ptA1 = Dot(a1)
            ptB1 = Dot(b1)
            ptC1 = Dot([0, 4 * unit_size, 0])
            ptC1.rotate(angle=-angle, about_point=o)

            txtA.next_to(ptA1, UL)
            txtB.next_to(ptB1, DR)
            txtC.next_to(ptC1, UR)

            ng = VGroup(lAB1, arc, ptA1, ptB1, ptC1, txtA, txtB, txtC)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(g1, update4),
                  run_time=3, rate_func=smooth)
        self.wait(2)

        d = [0, ptC.get_y(), 0]
        ptD = Dot(d)
        lOC = Line(ptO, ptC)
        lDC = Line(ptD, ptC)
        lAC = Line(ptA, ptC)
        self.play(Create(lOC))
        self.play(Create(lDC), FadeIn(ptD))
        self.play(Create(lAC))

        self.wait(5)
