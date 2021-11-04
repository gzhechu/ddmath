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

from manim import *
import numpy as np


class FlippedAngle(Scene):
    def construct(self):
        self.init()
        self.wait()
        self.wiggle()
        self.wait()
        self.draw_angle()
        self.wait()
        triADE = self.triADE.copy()
        triADE.set_color(color=WHITE)
        triADE.set_fill(opacity=0)
        self.play(FadeOut(self.vgSecs),
                  ReplacementTransform(self.triADE, triADE))
        self.wait()

        # 绘制辅助线
        self.calc_auxiliary()
        self.play(FadeIn(self.lA1A))
        self.wait()
        self.play(FadeIn(self.vgSec34))
        self.wait()
        self.play(FadeIn(self.vgSec56))
        self.wait()
        ind1 = Indicate(self.vgSec1, scale_factor=1.1)
        ind34 = Indicate(self.vgSec34, scale_factor=1.02)
        ind2 = Indicate(self.vgSec2, scale_factor=1.1)
        ind56 = Indicate(self.vgSec56, scale_factor=1.02)
        self.play(ind1, run_time=0.5)
        self.play(ind1, run_time=0.5)
        self.wait()
        self.play(ind34, run_time=0.5)
        self.play(ind34, run_time=0.5)
        self.wait()
        self.play(ind2, run_time=0.5)
        self.play(ind2, run_time=0.5)
        self.wait()
        self.play(ind56, run_time=0.5)
        self.play(ind56, run_time=0.5)
        self.wait()

        self.embed()

    def init(self):
        self.clear()
        self.camera.background_color = "#101010"
        # self.a = [1.5, 3, 0]
        # self.b = [-4, -3, 0]
        # self.c = [3.6, -3, 0]
        self.a = [1.5, 7, 0]
        self.b = [-4, -1, 0]
        self.c = [3.6, -1, 0]
        self.e = self.d = self.a
        self.d_dist_y = 3.2
        self.e_dist_y = 3.3

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
                  FadeIn(ptB), FadeIn(ptC))
        self.play(FadeIn(lbsABC))
        self.wait()
        self.play(FadeIn(self.lDE), FadeIn(self.lblD), FadeIn(self.lblE),
                  FadeIn(self.ptD), FadeIn(self.ptE))
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

        [lblOne, lblTwo] = [Tex(X) for X in ["1", "2"]]

        self.secA = Sector(outer_radius=0.8, color=YELLOW, fill_opacity=0.8,
                           start_angle=PI+self.angAB, angle=(self.angAC-self.angAB))
        sec1 = Sector(outer_radius=0.8, color=BLUE, fill_opacity=0.8,
                      start_angle=PI+self.angAB, angle=(angA1D-self.angAB))
        sec2 = Sector(outer_radius=0.8, color=RED, fill_opacity=0.8,
                      start_angle=PI+angA1E, angle=(self.angAC-angA1E))
        self.secA.shift(self.a)
        sec1.shift(self.d)
        sec2.shift(self.e)
        lblOne.next_to(sec1, DOWN)
        lblTwo.next_to(sec2, DOWN)
        self.vgSec1= VGroup(sec1, lblOne)
        self.vgSec2= VGroup(sec2, lblTwo)
        self.vgSecs = VGroup(self.secA, self.vgSec1, self.vgSec2)
        self.play(FadeIn(self.vgSecs))

    def calc_auxiliary(self):
        try:
            if self.lA1A:
                pass
        except:
            self.lA1A = DashedLine(self.a1, self.a)

        lA1D = Line(self.a1, self.d)
        lA1E = Line(self.a1, self.e)
        angA1D = lA1D.get_angle()
        angA1E = lA1E.get_angle()

        angA1A = self.lA1A.get_angle()
        sec3 = Sector(outer_radius=0.8, color=BLUE, fill_opacity=0.6,
                      start_angle=PI+self.angAB, angle=(angA1A-self.angAB))
        sec4 = Sector(outer_radius=0.8, color=BLUE, fill_opacity=0.6,
                      start_angle=angA1A, angle=(angA1D-angA1A))
        sec5 = Sector(outer_radius=0.8, color=RED, fill_opacity=0.8,
                      start_angle=PI+angA1A, angle=(self.angAC-angA1A))
        sec6 = Sector(outer_radius=0.8, color=RED, fill_opacity=0.8,
                      start_angle=angA1E, angle=(angA1A-angA1E))
        sec3.shift(self.a)
        sec5.shift(self.a)
        sec4.shift(self.a1)
        sec6.shift(self.a1)
        self.vgSec34 = VGroup(sec3, sec4)
        self.vgSec56 = VGroup(sec5, sec6)

    def flip(self):
        lDE = Line(self.d, self.e)
        angDE = lDE.get_angle()
        direction = [1, 1*np.tan(angDE), 0]
        rotate1 = Rotate(self.vgRotate, angle=PI,
                         axis=direction, about_point=self.d)
        self.play(rotate1)

    def wiggle(self):
        def update1(group, alpha):
            mv1 = -0.5 * alpha
            mv2 = 0.8 * alpha
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
            mv1 = - 0.1 * alpha
            mv2 = 0.1 * alpha
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
