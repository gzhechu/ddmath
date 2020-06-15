#!/usr/bin/env python3

from manimlib.imports import *

# manim ddmath/md20200614_equal_height.py Triangle -r1280,720 -pm


class Triangle(Scene):
    CONFIG = {
        "color": WHITE,
        "A": np.array([2, 4, 0]),
        "B": np.array([-4.5, -2, 0]),
        "C": np.array([5, -2, 0]),
        "txt": 7
    }

    def construct(self):
        # origin = Dot()
        # [txtO] = [TexMobject(X) for X in ["O"]]
        # txtO.next_to(origin, DR, buff=0.1)
        # self.play(FadeIn(origin), FadeIn(txtO))

        [txtS1, txtS2] = [TexMobject(X) for X in ["S_1", "S_2"]]
        t1 = TexMobject("S=\\frac{1}{2}\\times a\\times h").scale(2)
        t1.move_to(self.txt * UP)
        t2 = TexMobject("\\frac{S_1}{S_2}=").scale(2)
        t2.move_to(self.txt * UP)
        t3 = TexMobject(
            "\\frac{\\frac{1}{2}\\times a\\times h}{\\frac{1}{2}\\times b\\times h}").scale(2)
        t3.next_to(t2, RIGHT, buff=0)
        t4 = TexMobject(
            "\\frac{a}{b}").scale(2)

        [txtA, txtB, txtH] = [
            TexMobject(X).scale(1.5) for X in ["a", "b", "h"]]

        triangle = Polygon(self.A, self.B, self.C,
                           color=WHITE, fill_opacity=0.3)
        self.play(ShowCreation(triangle))
        self.wait(3)

        bcLine = Line(self.B, self.C)
        txtA.next_to(bcLine, DOWN, buff=0.5)

        ptH = self.A*RIGHT + self.B*UP
        hLine = DashedLine(self.A, ptH)

        txtH.next_to(hLine, RIGHT, buff=0.5)
        self.play(ShowCreation(hLine), Write(txtH), Write(txtA))
        self.wait(1)

        ind1 = Indicate(txtA, color=YELLOW, scale_factor=1.5)
        ind2 = Indicate(txtH, color=YELLOW, scale_factor=1.5)

        self.play(ind1)
        self.play(ind1)
        self.play(ind2)
        self.play(ind2)

        g0 = VGroup(txtA, txtH)
        trans1 = TransformFromCopy(g0, t1)
        self.play(trans1)

        self.wait(3)
        ptE = self.A*UP - self.B*LEFT
        ptF = self.A*UP + self.C*RIGHT
        pLine = DashedLine(ptE, ptF)
        self.play(ShowCreation(pLine))

        g1 = VGroup(triangle, hLine, txtH)

        def update1(group, alpha):
            ptA = (self.A*RIGHT+2*RIGHT) * (1-alpha) + self.A*UP - 2*RIGHT
            ptH = ptA*RIGHT + self.B*UP
            hLine = DashedLine(ptA, ptH)
            txtH.next_to(hLine, RIGHT, buff=0.5)
            triangle = Polygon(ptA, self.B, self.C,
                               color=WHITE, fill_opacity=0.3)
            ng = VGroup(triangle, hLine, txtH)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(g1, update1),
                  run_time=6, rate_func=there_and_back)
        self.wait(3)

        ptD = self.B + 3*RIGHT
        dotD = Dot(ptD)
        triB = Polygon(self.A, self.B, ptD, color=WHITE,
                       fill_color=BLUE, fill_opacity=0.3,)
        triC = Polygon(self.A, self.C, ptD, color=WHITE,
                       fill_color=YELLOW, fill_opacity=0.3,)
        txtS1.move_to(triB.get_center()-UP*1.5)
        txtS2.move_to(triC.get_center()-UP*1.5)
        self.play(ShowCreation(dotD), FadeOut(t1))
        self.play(ShowCreation(triB), Write(txtS1))
        self.play(ShowCreation(triC), Write(txtS2))
        self.remove(triangle)

        lBD = Line(self.B, ptD)
        lDC = Line(self.C, ptD)
        txtAx = txtA.copy()
        txtAx.next_to(lBD, DOWN, buff=0.5)
        txtB.next_to(lDC, DOWN, buff=0.5)
        txtA.generate_target()
        txtA.target.move_to(txtAx.get_center())
        self.play(MoveToTarget(txtA), Write(txtB))
        self.wait(1)

        g2 = VGroup(triangle, triB, triC, hLine,
                    txtA, txtH, txtS1, txtS2)

        def update2(group, alpha):
            ptA = (self.A*RIGHT+2*RIGHT) * (1-alpha) + self.A*UP - 2*RIGHT
            ptH = ptA*RIGHT + self.B*UP
            hLine = DashedLine(ptA, ptH)
            txtH.next_to(hLine, RIGHT, buff=0.5)
            triangle = Polygon(ptA, self.B, self.C, color=WHITE)

            triB = Polygon(ptA, self.B, ptD, color=WHITE,
                           fill_color=BLUE, fill_opacity=0.3,)
            triC = Polygon(ptA, self.C, ptD, color=WHITE,
                           fill_color=YELLOW, fill_opacity=0.3,)
            txtS1.move_to(triB.get_center()-UP*1.5)
            txtS2.move_to(triC.get_center()-UP*1.5)
            ng = VGroup(triangle, triB, triC, hLine,
                        txtA, txtH, txtS1, txtS2)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(g2, update2),
                  run_time=6, rate_func=there_and_back)
        self.wait(1)

        sg1 = VGroup(t2, t3)
        sg1.shift(LEFT*sg1.get_center())
        gs = VGroup(txtS1, txtS2)
        trans1 = TransformFromCopy(gs, sg1)
        self.play(FadeOut(pLine), trans1)
        self.wait(5)

        t4.next_to(t2, RIGHT, buff=0.5)
        self.play(ReplacementTransform(t3, t4), FadeOut(hLine), FadeOut(txtH))
        sg2 = VGroup(t2, t4)
        sg2.generate_target()
        sg2.target.shift(LEFT*sg2.get_center())
        move1 = MoveToTarget(sg2)
        self.play(move1)
        self.wait(2)

        g3 = VGroup(triB, triC, dotD, txtS1, txtS2, txtA, txtB)

        def update3(group, alpha):
            ptD = self.B + 3*RIGHT + 5*RIGHT*alpha
            dotD = Dot(ptD)
            triB = Polygon(self.A, self.B, ptD, color=WHITE,
                           fill_color=BLUE, fill_opacity=0.3,)
            triC = Polygon(self.A, self.C, ptD, color=WHITE,
                           fill_color=YELLOW, fill_opacity=0.3,)

            lBD = Line(self.B, ptD)
            lDC = Line(self.C, ptD)
            txtA.next_to(lBD, DOWN, buff=0.5)
            txtB.next_to(lDC, DOWN, buff=0.5)

            txtS1.move_to(triB.get_center()-UP*1.5)
            txtS2.move_to(triC.get_center()-UP*1.5)

            ng = VGroup(triB, triC, dotD, txtS1, txtS2, txtA, txtB)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(g3, update3),
                  run_time=6, rate_func=there_and_back)

        self.play(UpdateFromAlphaFunc(g3, update3),
                  run_time=6, rate_func=there_and_back)
        self.wait(3)
