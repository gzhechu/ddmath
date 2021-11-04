#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
manimce th20211104_exponents_basic.py TestGLResolution -r720,1280 -pqm

manimce th20211104_exponents_basic.py ExponentsLaw -r720,1280 -pqm
manimce th20211104_exponents_basic.py ExponentsLaw -r360,640 -pqm

ffmpeg -i FlipAngle.mp4 -i FlipAngle.m4a FlipAngleRelease.mp4 -y
"""

# from manimlib import *
from manim import *


class TestGLResolution(Scene):
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

        txt = MathTex("Hello A_1")
        txt.move_to(UP * 7)
        self.play(Create(txt))

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
        self.play(FadeIn(vgPt), Write(square))
        self.play(AnimationGroup(*[FadeIn(X) for X in ptTxts], lag_ratio=0.1))
        self.wait(10)


equations = [
    ["a^m", "=", "a \cdot a \cdot {\dots} \cdot a"],
    ["a^1", "=", "a"],
    ["a^m \cdot a^n", "=", "a^{m+n}"],
    ["(a^m)^n", "=", "a^{m \cdot n}"],
    ["\\frac{a^m}{a^n}", "=", "a^{m-n}"],
    ["a^0", "=", "1"],
    ["a^{-n}", "=", "\\frac{1}{a^n}"],
    ["(a \cdot b)^m", "=", "a^m \cdot b^m}"],
    ["(\\frac{a}{b})^m", "=", "\\frac{a^m}{b^m}"]
]

selected_framebox = None
menu = None


class ExponentsLaw(Scene):
    # def __init__(self, **kwargs):
    #     pass

    def construct(self):
        menu = self.draw_menu(selected=5)
        for x in range(len(equations)):
            self.select_menu_item(menu, x)
        self.select_menu_item(menu)
        self.wait(3)

    def introduction(self):
        pass

    def draw_menu(self, selected=None, lag_ratio=0.1, run_time=2):
        # menu = [MathTex(*x).set_color(random_color()) for x in equations]
        menu = [MathTex(*x).set_color_by_tex_to_color_map(
            {"a": BLUE, "b": TEAL, "m": GREEN}) for x in equations]

        # menu = []
        # for x in equations:
        #     eq = MathTex(*x).set_color(random_color())
        #     # for l in eq:
        #     #     l.set_color(random_color())
        #     menu.append(eq)

        menu[0].move_to(UP * 6)
        for n in range(1, len(menu)):
            menu[n].next_to(menu[n-1], DOWN, buff=0.8)
        animations = [FadeIn(o)for o in menu]
        if selected is not None:
            global selected_framebox
            selected_framebox = SurroundingRectangle(
                menu[selected], buff=.3)
            animations.append(Create(selected_framebox))
        self.play(AnimationGroup(
            *animations, lag_ratio=lag_ratio, run_time=run_time))
        return menu

    def select_menu_item(self, menu, idx=None, run_time=1):
        global selected_framebox
        framebox = None
        if idx is None:
            self.play(FadeOut(selected_framebox), run_time=run_time)
        else:
            framebox = SurroundingRectangle(menu[idx], buff=.3)
            self.play(ReplacementTransform(
                selected_framebox, framebox), run_time=run_time)
        selected_framebox = framebox
