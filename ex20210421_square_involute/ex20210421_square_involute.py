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
在平面直角坐标系中有一个正方形
四个顶点的坐标如图
如果以B点为圆心，AB为半径画圆弧AA1
然后以C点为圆心，A1C为半径画圆弧A1A2
继续以D点为圆心，A2D为半径画圆弧A2A3
以此类推绘制的曲线叫做“正方形的渐开线”
问：当曲线持续绘制下去，到点A18时的坐标是什么？
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
        vgPt = VGroup(ptOrigin, ptA, ptB, ptC, ptD)

        # 正方形 及坐标网格
        square = Square()
        grid = NumberPlane(
            axis_config={"include_tip": True, "include_ticks": True},)
        axes = Axes(axis_config={"include_tip": True, "include_ticks": True})

        # self.add(axes)
        self.play(Write(axes), Write(txtO))
        self.play(FadeIn(vgPt), Create(square))
        # self.play(AnimationGroup(*[FadeIn(X) for X in ptTxts], lag_ratio=0.1))
        # self.wait(1)
        # 保存镜头状态
        self.camera.frame.save_state()
        reset_camera = Restore(self.camera.frame)
        # 拉近镜头 # 隐藏网格
        self.play(self.camera.frame.animate.set(width=9),
                  *[FadeIn(X) for X in ptLbls],
                  run_time=1)
        self.wait(0.5)
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

        a1, p1, lb1 = get_arc(1)
        a2, p2, lb2 = get_arc(2)
        a3, p3, lb3 = get_arc(3)
        a4, p4, lb4 = get_arc(4)

        l1 = DashedLine(vertex[1], vertex[0], stroke_width=10, color=RED)
        self.play(Write(l1), run_time=0.25)
        self.play(Create(a1), FadeIn(p1), FadeOut(l1))
        self.play(Indicate(a1), Indicate(txtA, scale_factor=1.6),
                  Indicate(lb1, scale_factor=1.6))
        self.wait(2)

        zoom_camera = self.camera.frame.animate.set(width=12)
        l2 = DashedLine(vertex[2], p1, stroke_width=10, color=RED)
        self.play(Write(l2), run_time=0.25)
        self.play(Create(a2), FadeIn(p2), FadeOut(l2), zoom_camera)
        self.play(Indicate(a2), Indicate(lb1, scale_factor=2),
                  Indicate(lb2, scale_factor=2))
        self.wait(2)

        l3 = DashedLine(vertex[3], p2, stroke_width=10,  color=RED)
        self.play(Write(l3), run_time=0.25)
        self.play(Create(a3),  FadeIn(p3), FadeOut(l3))
        self.play(Indicate(a3), Indicate(lb2, scale_factor=2),
                  Indicate(lb3, scale_factor=2))
        self.wait(2)

        l4 = DashedLine(vertex[0], p3, stroke_width=10, color=RED)
        self.play(Write(l4), run_time=0.25)
        self.play(Create(a4), FadeIn(p4), FadeOut(l4), reset_camera)
        self.play(Indicate(a4), Indicate(lb3, scale_factor=3),
                  Indicate(lb4, scale_factor=3))
        self.wait(2)

        # self.remove(a1, a2, a3, a4)
        # 先放大，同时画
        draw_list = []
        for i in range(5, 9):
            a, p, t = get_arc(i)
            draw_arc = AnimationGroup(Create(a, rate_func=linear),
                                      FadeIn(p), Indicate(t, scale_factor=2+i*0.5), lag_ratio=0)
            draw_list.append(draw_arc)
        draw_arc = AnimationGroup(*draw_list, lag_ratio=1.0)
        zoom_camera = self.camera.frame.animate.set(width=config.frame_width*2)
        self.play(draw_arc, zoom_camera, run_time=2)

        # 再恢复，同时继续画
        draw_list = []
        for i in range(9, 11):
            a, p, t = get_arc(i)
            draw_arc = AnimationGroup(Create(a, rate_func=linear),
                                      FadeIn(p), Indicate(t, scale_factor=4), lag_ratio=0)
            draw_list.append(draw_arc)
        draw_arc = AnimationGroup(*draw_list, lag_ratio=1.0)

        # 标明字母
        show_alist = AnimationGroup(*[Indicate(X, scale_factor=3)
                                      for X in [lb1, lb2, lb3, lb4]], lag_ratio=0.25)
        zoom_camera = self.camera.frame.animate.set(width=15)
        self.play(draw_arc, show_alist, zoom_camera, run_time=2)

        top = 9
        rect = Rectangle(width=12.0, height=3.0, color=BLACK,
                         fill_opacity=1, stroke_width=0)
        rect.move_to(UP * top)
        self.add(rect)
        rect = Rectangle(width=12.0, height=3.0, color=BLUE,
                         fill_opacity=0.6, stroke_width=0)
        rect.move_to(UP * top)
        # self.play(FadeIn(rect))

        txtQ1 = MathTex("A_{18}").scale(2.5)
        txtQ2 = Tex("=").scale(2.5)
        txtQ3 = Tex("(?, ?)").scale(2.5)
        txtQ4 = Tex("(-37,1)").scale(2.5)
        txtQ1.move_to(UP * top)
        txtQ2.next_to(txtQ1, RIGHT, buff=0.2)
        txtQ3.next_to(txtQ2, RIGHT, buff=0.2)

        self.play(FadeIn(rect), Write(txtQ1))
        self.play(FadeIn(txtQ2), FadeIn(txtQ3))

        sg1 = VGroup(txtQ1, txtQ2, txtQ3)
        sg1.generate_target()
        sg1.target.shift(LEFT*sg1.get_center())
        move1 = MoveToTarget(sg1)
        self.play(move1)

        txtQ4.next_to(txtQ2, RIGHT, buff=0.2)
        trans1 = ReplacementTransform(txtQ3, txtQ4)
        # self.play(trans1)

        self.wait(3)
