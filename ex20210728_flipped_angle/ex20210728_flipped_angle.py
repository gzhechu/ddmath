#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# develop and render undder manim version 0.5.0
#

"""
manimce ex20210728_flipped_angle.py FlippedAngle -r1280,720 -pqm
manimce ex20210728_flipped_angle.py FlippedAngle -r640,360 -pql

ffmpeg -i FlippedAngle.mp4 -i FlippedAngle.m4a FlippedAngleRelease.mp4 -y
"""

from manimlib import *
import numpy as np


class FlippedAngle(Scene):
    def construct(self):
        self.init()
        self.wait()
        self.wiggle()
        self.wait()
        self.draw_angle()
        self.wait()

        lineAA1 = DashedLine(self.a, self.a1)
        self.play(FadeIn(lineAA1))
        self.wait()
        self.embed()

    def init(self):
        self.clear()
        self.camera.background_color = GREY
        # self.a = [1.5, 7 , 0]
        # self.b = [-4, -1, 0]
        # self.c = [3.6, -1, 0]
        self.a = [1.5, 3, 0]
        self.b = [-4, -3, 0]
        self.c = [3.6, -3, 0]
        self.e = self.d = self.a
        self.d_dist_y = 3.2
        self.e_dist_y = 3.6

        self.ptA = Dot(self.a)
        ptB = Dot(self.b)
        ptC = Dot(self.c)
        self.ptA1 = self.ptA.copy()

        lAB = Line(self.b, self.a)
        self.angAB = lAB.get_angle()
        lAC = Line(self.c, self.a)
        self.angAC = lAC.get_angle()

        self.d = self.a + DOWN * self.d_dist_y + \
            LEFT * (self.d_dist_y / np.tan(self.angAB))
        self.e = self.a + DOWN * self.e_dist_y + \
            LEFT * (self.e_dist_y / np.tan(self.angAC))
        self.ptD = Dot(self.d)
        self.ptE = Dot(self.e)
        self.lDE = Line(self.d, self.e)

        [lblO, lblA, self.lblA1, lblB, lblC, lblD, lblE] = [
            Tex(X) for X in ["O", "A", "A'", "B", "C", "D", "E"]]

        lblA.next_to(self.ptA, UP)
        lblB.next_to(ptB, DL)
        lblC.next_to(ptC, DR)
        lblD.next_to(self.ptD, LEFT)
        lblE.next_to(self.ptE, RIGHT)
        self.lblE = lblE
        self.lblD = lblD
        self.lblA1 = self.lblA1
        lbsABC = VGroup(lblA, lblB, lblC)
        triABC = Polygon(self.a, self.b, self.c, color=WHITE)
        self.triADE = Polygon(self.a, self.d, self.e,
                              color=BLUE, fill_opacity=0.3)
        # 显示顶点
        self.play(FadeIn(triABC), FadeIn(self.ptA),
                  FadeIn(ptB), FadeIn(ptC), FadeIn(self.lDE))
        self.play(FadeIn(lbsABC), FadeIn(self.lblD), FadeIn(
            self.lblE), FadeIn(self.ptD), FadeIn(self.ptE))
        self.wait()

        self.play(FadeIn(self.triADE), FadeIn(self.ptA1))

        self.vgRotate = VGroup(self.triADE, self.ptA1)
        self.flip()

        self.lblA1.next_to(self.ptA1, DOWN)
        self.play(FadeIn(self.lblA1))

    def draw_angle(self):
        self.a1 = self.ptA1.get_center()
        lA1D = Line(self.a1, self.d)
        lA1E = Line(self.a1, self.e)
        angA1D = lA1D.get_angle()
        angA1E = lA1E.get_angle()

        self.secA = Sector(outer_radius=0.8, color=RED, fill_opacity=0.8,
                           start_angle=PI+self.angAB, angle=(self.angAC-self.angAB))
        self.sec1 = Sector(outer_radius=0.8, color=BLUE, fill_opacity=0.8,
                           start_angle=PI+self.angAB, angle=(angA1D-self.angAB))
        self.sec2 = Sector(outer_radius=0.8, color=YELLOW, fill_opacity=0.8,
                           start_angle=PI+angA1E, angle=(self.angAC-angA1E))
        self.secA.shift(self.a)
        self.sec1.shift(self.d)
        self.sec2.shift(self.e)
        self.vgSecs = VGroup(self.secA, self.sec1, self.sec2)
        self.play(FadeIn(self.vgSecs))

    def flip(self):
        lDE = Line(self.d, self.e)
        angDE = lDE.get_angle()
        direction = [1, 1*np.tan(angDE), 0]
        rotate1 = Rotate(self.vgRotate, angle=PI,
                         axis=direction, about_point=self.d)
        self.play(rotate1)

    def wiggle(self):
        def update1(group, alpha):
            mv1 = -0.8 * alpha
            mv2 = 1 * alpha
            d = self.d + DOWN * mv1 + LEFT * (mv1 / np.tan(self.angAB))
            e = self.e + DOWN * mv2 + LEFT * (mv2 / np.tan(self.angAC))

            ptD = Dot(d)
            ptE = Dot(e)
            self.lblD.next_to(ptD, LEFT)
            self.lblE.next_to(ptE, RIGHT)
            lDE = Line(d, e)
            triADE = Polygon(self.a, d, e, color=BLUE, fill_opacity=0.3)

            angDE = lDE.get_angle()
            direction = [1, 1*np.tan(angDE), 0]
            triADE.rotate(angle=PI, axis=direction, about_point=d)
            ptA1 = self.ptA.copy()
            ptA1.rotate(angle=PI, axis=direction, about_point=d)
            self.lblA1.next_to(ptA1, DOWN)

            ng = VGroup(ptD, ptE, self.lblD, self.lblE,
                        lDE, triADE, ptA1, self.lblA1)
            group.become(ng)
            return group

        def update2(group, alpha):
            mv1 = - 0.2 * alpha
            mv2 = 0.3 * alpha
            d = self.d + DOWN * mv1 + LEFT * (mv1 / np.tan(self.angAB))
            e = self.e + DOWN * mv2 + LEFT * (mv2 / np.tan(self.angAC))

            ptD = Dot(d)
            ptE = Dot(e)
            self.lblD.next_to(ptD, LEFT)
            self.lblE.next_to(ptE, RIGHT)
            lDE = Line(d, e)
            triADE = Polygon(self.a, d, e, color=BLUE, fill_opacity=0.3)

            angDE = lDE.get_angle()
            direction = [1, 1*np.tan(angDE), 0]
            triADE.rotate(angle=PI, axis=direction, about_point=d)
            ptA1 = self.ptA.copy()
            ptA1.rotate(angle=PI, axis=direction, about_point=d)
            self.lblA1.next_to(ptA1, DOWN)

            ng = VGroup(ptD, ptE, self.lblD, self.lblE,
                        lDE, triADE, ptA1, self.lblA1)
            group.become(ng)
            return group

        self.d = self.ptD.get_center()
        self.e = self.ptE.get_center()
        g1 = VGroup(self.ptD, self.ptE, self.lblD, self.lblE,
                    self.lDE, self.triADE, self.ptA1, self.lblA1)
        self.play(UpdateFromAlphaFunc(g1, update1),
                  run_time=4, rate_func=there_and_back)
        self.play(UpdateFromAlphaFunc(g1, update2),
                  run_time=1, rate_func=smooth)
        self.d = self.ptD.get_center()
        self.e = self.ptE.get_center()
