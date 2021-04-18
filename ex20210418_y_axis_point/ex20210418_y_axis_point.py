#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# 2021-01-09
# develop and render undder manim version 0.4.0
#

"""
manim ex20210418_y_axis_point.py PointOnAxis -r1280,720 -p --quality m
manim ex20210418_y_axis_point.py PointOnAxis -r640,360 -p --quality l

ffmpeg -i PointOnAxis.mp4 -i PointOnAxis.m4a PointOnAxisRelease.mp4 -y
"""

from manim import *


class PointOnAxis(Scene):
    """
00 这是一道坐标系的几何题
02 说平面直角坐标系中
03 有ABC三个点
04 他们的坐标已知如图
05 并且连接成一个三角形
05 问：在Y轴上是否存在一个点P
06 使三角形APC的面积与三角形ABC面积相等
07 其实这题小学知识就能解
07 暂停想一想……
08 现在开始解题：标出AC在Y轴上的交点D
09 三角形APC可以分解为红、蓝色两个小三角形
10 蓝色三角形面积可用底边PD与蓝色高算出
11 同理红色三角形面积用PD与红色高算出
12 而两个高的长度相加等于AB的长
13 也就是三角形ABC的一条直角边的长度
14 根据等底等高面积相等原理
15 可以推理出如果要三角形APC与ABC面积相等
16 只需满足PD的长度等于BC长度
16 此时P点对应的位置就本题的答案
18 具体过程不详细计算，注意有两个答案哦
19 你学会了么？
19 好了，下次再见
    """

    def construct(self):
        ptOrigin = Dot(ORIGIN)
        a = [-2, 0, 0]
        b = [2, 0, 0]
        c = [2, 2, 0]
        d = [0, 1, 0]
        e = [0, 2, 0]
        p = d

        ptA = Dot(a)
        ptB = Dot(b)
        ptC = Dot(c)
        ptD = Dot(d)
        ptP = Dot(d)

        triangleABC = Polygon(a, c, b, color=WHITE)
        [txtO, txtA, txtB, txtC, txtD, txtP, txtP1] = [
            Tex(X).scale(0.6) for X in ["O", "A", "B", "C", "D", "P", "P'"]]
        [lblA, lblB, lblC, lblD, lblP1, lblP] = [
            Tex(X).scale(0.6) for X in ["(-2,0)", "(2,0)", "(2,2)", "(1,0)", "(0,3)", "(0,-1)"]]

        txtA.next_to(ptA, DL)
        txtB.next_to(ptB, DR)
        txtC.next_to(ptC, UR)
        txtD.next_to(ptD, DR)
        txtP.next_to(ptP, LEFT)
        vgTxt = VGroup(txtA, txtB, txtC)

        lblA.next_to(ptA, DOWN)
        lblB.next_to(ptB, DOWN)
        lblC.next_to(ptC, UR)
        lblD.next_to(ptD, UL)
        vgLbl = VGroup(lblA, lblB, lblC)
        vgPt = VGroup(ptOrigin, txtO, ptA, ptB, ptC)

        numberPlane = NumberPlane(
            axis_config={"include_tip": True, "include_ticks": True},)
        txtO.next_to(ptOrigin, DR)

        self.play(Write(numberPlane))
        self.play(AnimationGroup(FadeIn(vgPt), FadeIn(vgTxt), lag_ratio=0.5))
        self.wait(1)
        self.play(AnimationGroup(FadeOut(vgTxt), FadeIn(vgLbl), lag_ratio=0.5))
        self.wait(1)
        # self.play(AnimationGroup(Write(triangleABC),  FadeOut(vgLbl),
        #                          FadeIn(vgTxt), lag_ratio=0.5))
        self.play(Write(triangleABC), FadeOut(vgLbl),
                  FadeIn(vgTxt), run_time=2)

        # 画出 P 点
        self.play(FadeIn(ptP), Indicate(txtP, scale_factor=1.5))
        triangle = Polygon(a, c, p, color=WHITE)
        g1 = VGroup(triangle, ptP, txtP)

        def update1(group, alpha):
            p = [0, 1 + 2 * alpha, 0]
            ptP = Dot(p)
            txtP = Tex("P").scale(0.6).next_to(ptP, LEFT)
            triangle = Polygon(a, c, p,
                               color=WHITE, fill_opacity=0.2)
            ng = VGroup(triangle, ptP, txtP)
            group.become(ng)
            return group

        def update2(group, alpha):
            p = [0, 3 - 4 * alpha, 0]
            ptP = Dot(p)
            txtP = Tex("P").scale(0.6).next_to(ptP, LEFT)
            triangle = Polygon(a, c, p,
                               color=WHITE, fill_opacity=0.2)
            ng = VGroup(triangle, ptP, txtP)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(g1, update1),
                  run_time=1, rate_func=smooth)
        self.wait(0.5)

        # 出题
        self.play(Indicate(triangle), run_time=1)
        self.wait(0.5)
        self.play(Indicate(triangleABC), run_time=1)
        self.wait(2)

        # 解答
        self.play(UpdateFromAlphaFunc(g1, update2),
                  run_time=5, rate_func=there_and_back)
        self.wait(1)
        p = [0, 3, 0]
        self.play(FadeIn(ptD), Indicate(txtD, scale_factor=1.5))
        self.wait(1)
        t1 = Polygon(a, p, d, color=RED,  fill_opacity=0.5)
        t2 = Polygon(c, p, d, color=BLUE, fill_opacity=0.5)
        self.play(FadeIn(t1), FadeIn(t2))
        # self.play(Indicate(t2))
        self.play(FadeOut(t1), FadeOut(t2))
        self.wait(1)

        lPD = DashedLine(p, d, stroke_width=10, color=WHITE)
        lCE = DashedLine(c, e, stroke_width=10, color=BLUE)
        lAO = DashedLine(a, ORIGIN, stroke_width=10, color=RED)
        # 第一个小三角形
        self.play(FadeIn(t2))
        self.wait(0.5)
        self.play(GrowFromCenter(lPD), FadeOut(t2))
        self.play(ShowCreation(lCE))
        self.wait(1)

        # 第二个小三角形
        self.play(FadeIn(t1))
        self.wait(0.5)
        self.play(WiggleOutThenIn(lPD), FadeOut(t1))
        self.play(ShowCreation(lAO))
        self.wait(1)

        # 共同的底边
        lCE.generate_target()
        lCE.target.shift(DOWN*2)
        move1 = MoveToTarget(lCE)
        self.play(move1)
        self.wait(1)
        self.play(WiggleOutThenIn(lAO), WiggleOutThenIn(lCE))
        self.play(FadeOut(lPD), FadeOut(lCE), FadeOut(lAO))
        self.wait(2)

        # 标记三角形
        self.play(Indicate(triangle), run_time=1)
        self.play(Indicate(triangleABC), run_time=1)

        # 平行移动底边
        self.play(WiggleOutThenIn(lPD))
        self.wait(0.5)
        lPD.generate_target()
        lPD.target.shift([2, -1, 0])
        move1 = MoveToTarget(lPD)
        self.play(move1)

        lPD.generate_target()
        lPD.target.shift([-2, 1, 0])
        move1 = MoveToTarget(lPD)
        self.play(move1)
        # self.wait(1)
        self.play(FadeOut(lPD))

        # 复制第一个点
        ptP1 = ptP.copy()
        txtP1.next_to(ptP1, LEFT)
        triangle1 = triangle.copy()
        triangle1.set_fill(color=BLUE, opacity=0.3)
        self.add(triangle1, ptP1, txtP1)
        self.wait(2)

        # 移动到第二个点
        txtP.next_to(ptP, LEFT)
        g1 = VGroup(triangle, ptP, txtP)
        self.play(UpdateFromAlphaFunc(g1, update2),
                  run_time=2, rate_func=smooth)

        self.play(FadeOut(triangle1))
        self.play(FadeOut(triangle))

        lblP.next_to(ptP, RIGHT)
        lblP1.next_to(ptP1, RIGHT)
        self.play(FadeIn(lblP), FadeIn(lblP1))
        self.wait(1)
