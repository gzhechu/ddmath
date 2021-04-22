#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# develop and render undder manim version 0.5.0
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
            Tex(X) for X in ["O", "A", "B", "C", "D"]]
        [lblA, lblB, lblC, lblD] = [
            Tex(X) for X in ["(1,-1)", "(-1,1)", "(-1,1)", "(1,1)"]]

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
                      color=WHITE, start_angle=np.deg2rad((-n + 1)*90), angle=np.deg2rad(-90))
            direction = [RIGHT, DOWN, LEFT, UP]
            pt = Dot(center + direction[idx] * radius)
            txt = "A_{}".format(n)
            lbl = MathTex(txt)
            lbl.next_to(pt, DR)
            return arc, pt, lbl

        a1, p1, t1 = get_arc(1)
        a2, p2, t2 = get_arc(2)
        a3, p3, t3 = get_arc(3)
        a4, p4, t4 = get_arc(4)

        self.play(Create(a1), FadeIn(p1), Indicate(t1, scale_factor=1.6))
        self.wait()
        self.play(Create(a2), FadeIn(p2), Indicate(t2, scale_factor=2.5),
                  self.camera.frame.animate.set(width=12))
        self.wait()

        self.play(Create(a3, rate_func=linear),
                  FadeIn(p3), Indicate(t3, scale_factor=3))
        self.wait()
        self.play(Create(a4, rate_func=linear),
                  FadeIn(p4), Indicate(t4), reset_camera)
        self.wait()

        # 标明字母
        self.play(AnimationGroup(*[Indicate(X, scale_factor=1.6)
                                   for X in [txtB, txtC, txtD, txtA]], lag_ratio=0.1))

        self.remove(a1, a2, a3, a4)

        # 先放大，同时画
        draw_list = []
        for i in range(1, 9):
            a, p, t = get_arc(i)
            draw_arc = AnimationGroup(Create(a, rate_func=linear),
                                      FadeIn(p), Indicate(t, scale_factor=2+i*0.5), lag_ratio=0)
            draw_list.append(draw_arc)
        draw_arc = AnimationGroup(*draw_list, lag_ratio=1.0)
        zoom_out = self.camera.frame.animate.set(width=config.frame_width*2)
        self.play(draw_arc, zoom_out, run_time=4)

        # 再恢复，同时继续画
        draw_list = []
        for i in range(9, 11):
            a, p, t = get_arc(i)
            draw_arc = AnimationGroup(Create(a, rate_func=linear),
                                      FadeIn(p), Indicate(t, scale_factor=4), lag_ratio=0)
            draw_list.append(draw_arc)
        draw_arc = AnimationGroup(*draw_list, lag_ratio=1.0)
        self.play(draw_arc, reset_camera, run_time=2)

        self.wait(5)
