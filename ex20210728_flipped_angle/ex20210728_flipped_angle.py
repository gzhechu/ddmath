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
        o = ORIGIN
        # self.a = [1.5, 7 , 0]
        # self.b = [-4, -1, 0]
        # self.c = [3.6, -1, 0]
        self.a = [1.5, 3 , 0]
        self.b = [-4, -3, 0]
        self.c = [3.6, -3, 0]
        self.e = self.d = self.a
        
        ptO = Dot(o)
        self.ptA = Dot(self.a)
        ptB = Dot(self.b)
        ptC = Dot(self.c)
        self.ptA1 = self.ptA.copy()

        lAB = Line(self.b, self.a)
        self.angAB = lAB.get_angle()
        lAC = Line(self.c, self.a)
        self.angAC = lAC.get_angle()

        self.yd = 3.5
        self.ye = 3.1
        self.d = self.a + DOWN * self.yd +  LEFT * (self.yd / np.tan(self.angAB))
        self.e = self.a + DOWN * self.ye +  LEFT * (self.ye / np.tan(self.angAC))
        self.ptD = Dot(self.d)
        self.ptE = Dot(self.e)
        self.lDE = Line(self.d, self.e)

        [lblO, lblA, self.lblA1, lblB, lblC, lblD, lblE] = [
            Tex(X) for X in ["O", "A", "A'", "B", "C", "D", "E" ]]

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
        self.triADE = Polygon(self.a, self.d, self.e, color=BLUE, fill_opacity=0.3)
        # 显示顶点
        self.play(FadeIn(triABC), FadeIn(self.ptA), FadeIn(ptB), FadeIn(ptC), FadeIn(self.lDE))
        self.play(FadeIn(lbsABC), FadeIn(self.lblD), FadeIn(self.lblE))
        self.wait()

        self.play(FadeIn(self.triADE), FadeIn(self.ptA1))

        self.vgRotate = VGroup(self.triADE, self.ptA1)
        # angDE = lDE.get_angle()
        # direction = [1, 1*np.tan(angDE), 0]
        # rotate1 = Rotate(self.vgRotate, angle=PI, axis=direction, about_point=self.d)
        # self.play(rotate1)
        self.flip()

        self.lblA1.next_to(self.ptA1, DOWN)
        self.play(FadeIn(self.lblA1))
        self.wait()

        def update1(group, alpha):
            mv1 = self.yd - 0.8 *alpha
            mv2 = self.ye + 1 *alpha
            self.d = self.a + DOWN * mv1 +  LEFT * (mv1 / np.tan(self.angAB))
            self.e = self.a + DOWN * mv2 +  LEFT * (mv2 / np.tan(self.angAC))

            ptD = Dot(self.d)
            ptE = Dot(self.e)
            lblD.next_to(ptD, LEFT)
            lblE.next_to(ptE, RIGHT)
            lDE = Line(self.d, self.e)
            self.triADE = Polygon(self.a, self.d, self.e, color=BLUE, fill_opacity=0.3)

            angDE = lDE.get_angle()
            direction = [1, 1*np.tan(angDE), 0]
            self.triADE.rotate(angle=PI, axis=direction,about_point=self.d)
            self.ptA1 = self.ptA.copy()
            self.ptA1.rotate(angle=PI, axis=direction,about_point=self.d)
            self.lblA1.next_to(self.ptA1, DOWN)

            ng = VGroup(ptD, ptE, lblD, lblE, lDE, self.triADE, self.ptA1, self.lblA1)
            group.become(ng)
            return group

        def update2(group, alpha):
            mv1 = self.yd - 0.2 *alpha
            mv2 = self.ye + 0.3 *alpha
            self.d = self.a + DOWN * mv1 +  LEFT * (mv1 / np.tan(self.angAB))
            self.e = self.a + DOWN * mv2 +  LEFT * (mv2 / np.tan(self.angAC))

            ptD = Dot(self.d)
            ptE = Dot(self.e)
            lblD.next_to(ptD, LEFT)
            lblE.next_to(ptE, RIGHT)
            lDE = Line(self.d, self.e)
            self.triADE = Polygon(self.a, self.d, self.e, color=BLUE, fill_opacity=0.3)

            angDE = lDE.get_angle()
            direction = [1, 1*np.tan(angDE), 0]
            self.triADE.rotate(angle=PI, axis=direction,about_point=self.d)
            self.ptA1 = self.ptA.copy()
            self.ptA1.rotate(angle=PI, axis=direction,about_point=self.d)
            self.lblA1.next_to(self.ptA1, DOWN)

            ng = VGroup(ptD, ptE, lblD, lblE, lDE, self.triADE, self.ptA1, self.lblA1)
            group.become(ng)
            return group


        self.wiggle()

        g1 = VGroup(self.ptD, self.ptE, lblD, lblE, self.lDE, self.triADE, self.ptA1, self.lblA1)
        self.play(UpdateFromAlphaFunc(g1, update1 ), run_time=4, rate_func=there_and_back)
        self.play(UpdateFromAlphaFunc(g1, update2 ), run_time=1, rate_func=smooth)
        self.wait()

        a1 = self.ptA1.get_center()
        lA1D = Line(a1, self.d)
        lA1E = Line(a1, self.e)
        angA1D = lA1D.get_angle()
        angA1E = lA1E.get_angle()

        secA = Sector(outer_radius=0.8, color=RED, fill_opacity=0.8,
                      start_angle=PI+self.angAB, angle=(self.angAC-self.angAB))
        sec1 = Sector(outer_radius=0.8, color=BLUE, fill_opacity=0.8,
                      start_angle=PI+self.angAB, angle=(angA1D-self.angAB))
        sec2 = Sector(outer_radius=0.8, color=YELLOW, fill_opacity=0.8,
                      start_angle=PI+angA1E, angle=(self.angAC-angA1E))
        secA.shift(self.a)
        sec1.shift(self.d)
        sec2.shift(self.e)
        self.vgSec = VGroup(secA, sec1, sec2)
        self.play(FadeIn(self.vgSec))

        lineAA1 = DashedLine(self.a, a1)
        self.play(FadeIn(lineAA1))

        self.wait(3)
        self.embed()

    def flip(self):
        lDE = Line(self.d, self.e)
        angDE = lDE.get_angle()
        direction = [1, 1*np.tan(angDE), 0]
        rotate1 = Rotate(self.vgRotate, angle=PI, axis=direction, about_point=self.d)
        self.play(rotate1)

    def wiggle(self):
        def update1(group, alpha):
            cd = self.ptD.get_center()
            ce = self.ptE.get_center()
            mv1 = self.yd - 0.8 *alpha
            mv2 = self.ye + 1 *alpha
            self.d = cd + DOWN * mv1 +  LEFT * (mv1 / np.tan(self.angAB))
            self.e = ce + DOWN * mv2 +  LEFT * (mv2 / np.tan(self.angAC))

            ptD = Dot(self.d)
            ptE = Dot(self.e)
            self.lblD.next_to(ptD, LEFT)
            self.lblE.next_to(ptE, RIGHT)
            lDE = Line(self.d, self.e)
            triADE = Polygon(self.a, self.d, self.e, color=BLUE, fill_opacity=0.3)

            angDE = lDE.get_angle()
            direction = [1, 1*np.tan(angDE), 0]
            triADE.rotate(angle=PI, axis=direction,about_point=self.d)
            ptA1 = self.ptA.copy()
            ptA1.rotate(angle=PI, axis=direction,about_point=self.d)
            self.lblA1.next_to(self.ptA1, DOWN)

            ng = VGroup(ptD, ptE, lDE, triADE, ptA1)
            group.become(ng)
            return group

        # def update2(group, alpha):
        #     mv1 = self.yd - 0.2 *alpha
        #     mv2 = self.ye + 0.3 *alpha
        #     self.d = self.a + DOWN * mv1 +  LEFT * (mv1 / np.tan(self.angAB))
        #     self.e = self.a + DOWN * mv2 +  LEFT * (mv2 / np.tan(self.angAC))

        #     ptD = Dot(self.d)
        #     ptE = Dot(self.e)
        #     self.lblD.next_to(ptD, LEFT)
        #     self.lblE.next_to(ptE, RIGHT)
        #     lDE = Line(self.d, self.e)
        #     self.triADE = Polygon(self.a, self.d, self.e, color=BLUE, fill_opacity=0.3)

        #     angDE = lDE.get_angle()
        #     direction = [1, 1*np.tan(angDE), 0]
        #     self.triADE.rotate(angle=PI, axis=direction,about_point=self.d)
        #     self.ptA1 = self.ptA.copy()
        #     self.ptA1.rotate(angle=PI, axis=direction,about_point=self.d)
        #     self.lblA1.next_to(self.ptA1, DOWN)

        #     ng = VGroup(ptD, ptE, lDE, self.triADE, self.ptA1)
        #     group.become(ng)
        #     return group

        g1 = VGroup(self.ptD, self.ptE, self.lDE, self.triADE, self.ptA1)
        self.play(UpdateFromAlphaFunc(g1, update1 ), run_time=4, rate_func=there_and_back)
        # self.play(UpdateFromAlphaFunc(g1, update2 ), run_time=1, rate_func=smooth)
