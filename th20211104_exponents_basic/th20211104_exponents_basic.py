#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
manimce th20211104_exponents_basic.py TestGLResolution -r720,1280 -pqm

manimce th20211104_exponents_basic.py ExponentsLaw -r720,1280 -pqm
manimce th20211104_exponents_basic.py ExponentsLaw -r360,640 -pqm

ffmpeg -i FlipAngle.mp4 -i FlipAngle.m4a FlipAngleRelease.mp4 -y
"""

from manim import *

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
colors = ["#ade7d9", "#c1e0b3", "#94d5e4", "#ecdbba", "#b4cda8",
          "#e4f0d6", "#a1a1a1", "#ffc297", "#fbe3cb", "#e8a3de"]
selected_framebox = None
menu = None


class ExponentsLaw(Scene):
    # def __init__(self, **kwargs):
    #     pass

    def init_menu(self):
        global menu
        menu = []
        for i, x in enumerate(equations):
            c = colors[i]
            eq = MathTex(*x).set_color(c)
            # for l in eq:
            #     l.set_color(random_color())
            menu.append(eq)
        menu[0].move_to(UP * 6)
        for n in range(1, len(menu)):
            menu[n].next_to(menu[n-1], DOWN, buff=0.8)

    def construct(self):
        global menu
        self.init_menu()
        self.introduction()
        self.select_menu_item(menu, idx=0)
        self.wait()
        self.clear()
        self.draw_menu(selected=0)
        self.select_menu_item(menu, 1)
        # for x in range(len(equations)):
        #     self.select_menu_item(menu, x)
        self.select_menu_item(menu)

        self.wait(3)
        self.simple_equation()  # 一次幂
        menu = self.draw_menu(selected=1)
        self.wait(3)

    def introduction(self):
        """
        幂运算，是初等代数的重要概念，
        表达式如图，
        读作a的m次方或者a的m次幂，
        其中，a称为底数，而m称为指数，
        通常指数写成上标，放在底数的右上角。
        若m为正整数，可以把看它作乘方的结果，等同于数字a自乘m次。
        大家好，今天就来讲一讲幂运算，
        并用动图的方式，讲解幂运算的几个基本法则。
        如：同底数幂的乘法，幂的乘方与积的乘方、同底数幂的除法等等。

        """
        scale_ratio = 1.5
        eq1 = MathTex("a^", "m").scale(scale_ratio).set_color(colors[0])
        eq2 = MathTex("=").scale(scale_ratio).set_color(colors[1])
        eq3 = MathTex("a \cdot a \cdot {\dots} \cdot a").scale(
            scale_ratio).set_color(colors[2])
        eq2.next_to(eq1, RIGHT)
        eq3.next_to(eq2, RIGHT)

        self.play(Create(eq1), run_time=2)
        self.wait()
        self.play(Indicate(eq1[0]), scale_factor=2)
        self.play(Indicate(eq1[1]), scale_factor=2)
        self.wait(3)
        vg1 = VGroup(eq1, eq2, eq3)
        vg1.generate_target()
        vg1.target.shift(LEFT*vg1.get_center())
        move1 = MoveToTarget(vg1)
        # self.play(move1)
        self.play(FadeIn(eq2), TransformFromCopy(eq1[0], eq3), move1)
        self.wait(2)
        b1 = Brace(eq3).set_color(colors[3])
        b1t = b1.get_tex("m").set_color(colors[4])
        vg2 = VGroup(b1, b1t)
        self.play(FadeIn(b1), TransformFromCopy(eq1[1], b1t))
        self.wait(2)
        self.play(Indicate(b1t), scale_factor=2)
        self.play(ApplyWave(eq3))
        self.wait(2)

        # draw main memu
        global menu
        animations = [FadeIn(o) for o in menu]
        self.play(AnimationGroup(*animations, lag_ratio=0.1, run_time=2),
                  Transform(vg1, menu[0]), FadeOut(vg2))

    def simple_equation(self):
        """
        一次幂的运算是最简单的幂运算了
        底数a的1次方，就是a的一次幂，等于a本身
        用前面学到的幂运算公式可以得到
        1乘以1个a，就这么简单
        在此专门列出，就是要
        """
        m = menu[1].copy().scale(1.5)
        m.move_to(UP * 6)
        t = TransformFromCopy(menu[1], m)
        self.play(FadeOut(*menu), FadeOut(selected_framebox), t)
        self.wait(1)
        self.clear()
        self.wait(3)

    def draw_menu(self, selected=None, lag_ratio=0.1, run_time=2):
        global menu
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
            if selected_framebox is None:
                self.play(Create(framebox), run_time=run_time)
            else:
                self.play(ReplacementTransform(
                    selected_framebox, framebox), run_time=run_time)
        selected_framebox = framebox
