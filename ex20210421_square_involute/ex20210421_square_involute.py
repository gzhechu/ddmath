#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# 2021-01-09
# develop and render undder manim version 0.4.0
#

"""
manim ex20210421_square_involute.py SquareInvolute -r1280,720 -pqm
manim ex20210421_square_involute.py SquareInvolute -r640,360 -pql

ffmpeg -i SquareInvolute.mp4 -i SquareInvolute.m4a SquareInvoluteRelease.mp4 -y
"""

from manim import *


class SquareInvolute(MovingCameraScene):
    """
00 这道题里，我们会画一个正方形的渐开线
    """

    def construct(self):
        ptOrigin = Dot(ORIGIN)
        a = [1, -1, 0]
        b = [-1, -1, 0]
        c = [-1, 1, 0]
        d = [1, 1, 0]
        vertex = [a, b, c, d]

        ptA = Dot(a)
        ptB = Dot(b)
        ptC = Dot(c)
        ptD = Dot(d)

        [txtO, txtA, txtB, txtC, txtD] = [
            Tex(X).scale(0.8) for X in ["O", "A", "B", "C", "D"]]
        [lblA, lblB, lblC, lblD] = [
            Tex(X).scale(0.8) for X in ["(1,-1)", "(-1,1)", "(-1,1)", "(1,1)"]]

        txtA.next_to(ptA, DR)
        txtB.next_to(ptB, DL)
        txtC.next_to(ptC, UL)
        txtD.next_to(ptD, UR)
        txtO.next_to(ptOrigin, DR)
        ptTxts = [txtA, txtB, txtC, txtD]
        vgTxts = VGroup(*ptTxts)

        lblA.next_to(ptA, DR)
        lblB.next_to(ptB, DL)
        lblC.next_to(ptC, UL)
        lblD.next_to(ptD, UR)
        ptLbls = [lblA, lblB, lblC, lblD]
        vgLbls = VGroup(*ptLbls)
        vgPt = VGroup(ptOrigin, txtO, ptA, ptB, ptC, ptD)

        # 正方形 及坐标网格
        square = Square()
        grid = NumberPlane(
            axis_config={"include_tip": True, "include_ticks": True},)
        axes = Axes(axis_config={"include_tip": True, "include_ticks": True})

        self.play(Write(grid))
        self.play(FadeIn(vgPt), Create(square))
        # self.play(AnimationGroup(*[FadeIn(X) for X in ptTxts], lag_ratio=0.1))
        self.wait(1)
        # 保存镜头状态
        self.camera.frame.save_state()
        reset_camera = Restore(self.camera.frame)
        # 拉近镜头 # 隐藏网格
        self.add(axes)
        self.play(self.camera.frame.animate.set(width=9),
                  FadeOut(grid), *[FadeIn(X) for X in ptLbls],
                  run_time=2)
        self.wait(1)

        # 显示顶点
        trans1 = ReplacementTransform(vgLbls, vgTxts)
        self.play(trans1)
        self.wait()

        # 计算弧线的函数
        def get_arc(n):
            idx = n % 4
            radius = n * 2
            center = vertex[idx]
            arc = Arc(radius=radius, arc_center=center,
                      color=RED, start_angle=np.deg2rad((-n + 1)*90), angle=np.deg2rad(-90))
            return arc

        a1 = get_arc(1)
        a2 = get_arc(2)
        a3 = get_arc(3)
        a4 = get_arc(4)

        self.play(Create(a1))
        self.wait()
        self.play(Create(a2),
                  self.camera.frame.animate.set(width=12))
        self.wait()
        self.play(Create(a3, rate_func=linear))
        self.wait()

        self.play(Create(a4, rate_func=linear), reset_camera)
        self.wait()

        # 标明字母
        arc_list = [a1, a2, a3, a4]
        self.play(AnimationGroup(*[Indicate(X, scale_factor=1.6)
                                   for X in [txtB, txtC, txtD, txtA]], lag_ratio=0.1))
        self.play(AnimationGroup(*[Indicate(X, scale_factor=1.06)
                                   for X in arc_list], lag_ratio=0.3))

        # 先放大，同时画两个
        arc_list = []
        for i in range(5, 7):
            a = get_arc(i)
            arc_list.append(a)
        draw_arc = AnimationGroup(
            *[Create(X, rate_func=linear) for X in arc_list], lag_ratio=1.0)
        zoom_out = self.camera.frame.animate.set(width=config.frame_width*1.8)
        self.play(draw_arc, zoom_out, run_time=2)

        # 再恢复，同时继续画
        arc_list = []
        for i in range(7, 9):
            a = get_arc(i)
            arc_list.append(a)
        draw_arc = AnimationGroup(
            *[Create(X, rate_func=linear) for X in arc_list], lag_ratio=1.0)

        self.play(draw_arc, reset_camera)

        self.wait(5)
