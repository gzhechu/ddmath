#!/usr/bin/env python3

# import numpy as np
from manim import *
import math

"""
manimce ex20220628_two_squares.py Diff2Square -pqm -r720,1280
manimce ex20220628_two_squares.py Diff2Square -p
"""


class Diff2Square(Scene):
    def construct(self):
        self.a = 4.5
        self.b = 2.5
        self.top = 2

        lA = Line(LEFT * self.a / 2, RIGHT * self.a / 2, color=BLUE)
        lA.move_to(DOWN*self.a / 2)
        bA = Brace(lA)
        bAtext = bA.get_text("a")

        lB = Line(LEFT * self.b/2, RIGHT * self.b/2, color=YELLOW)
        lB.move_to(LEFT*(self.a - self.b)/2 + UP * (self.a-2*self.b)/2)
        bB = Brace(lB)
        angle = math.radians(90)
        # bB.rotate(angle=angle)
        # bB.move_to(LEFT*1)
        bBtext = bB.get_text("b")
        # self.add(lB, bB, bBtext)

        [txtAs, txtBs] = [Text(X, color=WHITE) for X in ["大", "小"]]
        # txtBs = MarkupText(f'小<span fgcolor="{YELLOW}">b</span>', color=RED )
        sA = Square(side_length=self.a, color=BLUE, fill_opacity=0.3)
        gA = VGroup(sA, txtAs)

        sB = Square(side_length=self.b, color=YELLOW,  fill_opacity=0.3)
        gB = VGroup(sB, txtBs)
        gB.move_to(UP*(self.a))
        gB.move_to(UP*(self.a-self.b)/2+LEFT*(self.a-self.b)/2)
        # self.play(FadeIn(sA), FadeIn(txtAs))
        self.play(FadeIn(gA))
        self.wait(1)
        # self.play(FadeIn(sB), FadeIn(txtBs))
        txtAs.generate_target()
        txtAs.target.shift(DOWN*1 + RIGHT * 1)
        trans1 = MoveToTarget(txtAs)

        self.play(FadeIn(gB), trans1)
        self.wait(1)

        self.play(FadeIn(bA), FadeIn(bAtext))
        self.wait(1)

        bC = bB.copy()
        bC.rotate(angle=angle, about_point=sB.get_center())
        self.play(FadeIn(bB), FadeIn(bC))

        self.wait(1)
        bC.generate_target()
        bC.target.shift(RIGHT * (self.a-self.b))
        trans1 = MoveToTarget(bC)
        self.play(trans1)
        self.wait(1)

        [ptAa, ptAb, ptAc, ptAd] = [sA.get_corner(X)for X in [UL, UR, DL, DR]]
        [ptBa, ptBb, ptBc, ptBd] = [sB.get_corner(X)for X in [UL, UR, DL, DR]]

        pX = Polygon(ptBb, ptAb, ptAd, ptAc, ptBc, ptBd)

        sg = VGroup(txtAs, txtBs)
        self.play(FadeIn(pX), FadeOut(sA), FadeOut(sg))
        self.wait(2)

        ptR = ptAd + UP*(self.a-self.b)
        rAB1 = Rectangle(height=self.b, width=self.a-self.b,
                         color=BLUE,  fill_opacity=0.3)
        rAB1.move_to(UP*(self.a-self.b)/2+RIGHT*(self.b)/2)
        rAB2 = Rectangle(height=self.a-self.b, width=self.a,
                         color=BLUE,  fill_opacity=0.3)
        rAB2.move_to(DOWN*(self.b)/2)

        gABC = VGroup(rAB1, bC)
        self.play(FadeIn(rAB1), FadeIn(rAB2))
        self.remove(pX)
        self.wait(1)
        trans1 = Rotate(gABC, about_point=ptR, angle=math.radians(-90))
        self.play(trans1)

        gABC.generate_target()
        gABC.target.shift(DOWN*(self.a-self.b))
        trans1 = MoveToTarget(gABC)

        self.play(trans1, FadeOut(bB))
        bCtext = bC.get_text("b")
        self.play(FadeIn(bCtext))
        self.wait(1)

        vg = VGroup(rAB2, sB, bA, bAtext, gABC, bC, bCtext)
        vg.generate_target()
        vg.target.shift(LEFT*vg.get_center())
        self.play(MoveToTarget(vg))

        self.wait(5)
