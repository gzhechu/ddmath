#!/usr/bin/env python3

from manimlib.imports import *

# manim ddmath/md20200614_equal_height.py TriangleEqualHeight -r1280,720 -pm
# manim ddmath/md20200614_equal_height.py EqualHeightEx01 -r1280,720 -pm


class TriangleEqualHeight(Scene):
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
        t3.next_to(t2, RIGHT, buff=0.5)
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
        g0 = VGroup(txtA, txtH)
        trans1 = TransformFromCopy(g0, t1)
        self.play(trans1)

        ind1 = Indicate(txtA, color=YELLOW, scale_factor=1.5)
        ind2 = Indicate(txtH, color=YELLOW, scale_factor=1.5)

        self.play(ind1)
        self.play(ind1)
        self.play(ind2)
        self.play(ind2)

        self.wait(1)
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


class EqualHeightEx01(Scene):
    CONFIG = {
        "color": WHITE,
        "A": np.array([1, 4, 0]),
        "B": np.array([-4, -2, 0]),
        "C": np.array([5, -2, 0]),
        "D": np.array([-1, -2, 0]),
        "E": np.array([2, -2, 0]),
        "F": np.array([-1.5, 1, 0]),
        "txt": 7
    }

    def construct(self):
        # origin = Dot()
        # [txtO] = [TexMobject(X) for X in ["O"]]
        # txtO.next_to(origin, DR, buff=0.1)
        # self.play(FadeIn(origin), FadeIn(txtO))

        def indicate(obj, duration=1):
            ind = Indicate(obj, color=RED, scale_factor=1)
            self.play(ind, run_time=duration)

        t1 = TextMobject("AF=FB").scale(1.5)
        t2 = TextMobject("BD=DE=EC").scale(1.5)
        t3 = TexMobject("S\\bigtriangleup ABC=").scale(1.5)
        t4 = TexMobject("?").scale(1.5)
        t5 = TexMobject("36").scale(1.5)
        t1.move_to(self.txt * UP)
        t2.next_to(t1, DOWN, buff=0.5)
        t3.move_to(self.txt * UP)
        t4.next_to(t3, RIGHT)
        t5.next_to(t3, RIGHT)

        [ts6a, ts6b, ts12a, ts12b] = [
            TextMobject(X) for X in ["6", "6", "12", "12"]]

        [txtA, txtB, txtC, txtD, txtE, txtF] = [
            TextMobject(X) for X in ["A", "B", "C", "D", "E", "F"]]
        [dotD, dotE, dotF] = [
            Dot(X) for X in [self.D, self.E, self.F]]

        txtA.next_to(self.A, UP)
        txtB.next_to(self.B, DL)
        txtC.next_to(self.C, DR)
        txtD.next_to(self.D, DOWN)
        txtE.next_to(self.E, DOWN)
        txtF.next_to(self.F, UL)

        lAF = Line(self.A, self.F, color=RED, stroke_width=15)
        lBF = Line(self.B, self.F, color=RED, stroke_width=15)
        lAE = DashedLine(self.A, self.E, color=RED)

        lBD = Line(self.B, self.D, color=RED, stroke_width=15)
        lDE = Line(self.D, self.E, color=RED, stroke_width=15)
        lEC = Line(self.E, self.C, color=RED, stroke_width=15)
        lBE = Line(self.B, self.E, color=RED, stroke_width=15)

        ts6a.next_to(self.D, UR, buff=0.8)
        ts6b.next_to(self.D, UL, buff=0.8)
        ts12a.next_to(self.F, RIGHT, buff=1.5)
        ts12b.next_to(self.E, UR, buff=1)

        triangle = Polygon(self.A, self.B, self.C,
                           color=WHITE, fill_opacity=0.3)

        tri1 = Polygon(self.D, self.E, self.F,
                       color=BLUE, fill_opacity=0.3)
        tri2 = Polygon(self.B, self.D, self.F,
                       color=BLUE, fill_opacity=0.3)
        tri3 = Polygon(self.B, self.E, self.F,
                       color=GREEN, fill_opacity=0.3)
        tri4 = Polygon(self.A, self.E, self.F,
                       color=GREEN, fill_opacity=0.3)
        tri5 = Polygon(self.A, self.B, self.E,
                       color=RED, fill_opacity=0.3)
        tri6 = Polygon(self.A, self.C, self.E,
                       color=RED, fill_opacity=0.3)
        self.add(triangle, txtA, txtB, txtC)
        self.wait(6)

        self.play(Write(txtF), FadeIn(dotF), Write(t1))
        self.play(GrowFromCenter(lAF), GrowFromCenter(lBF))
        self.wait(1)
        self.remove(lAF, lBF)
        self.wait(1)

        self.play(Write(txtD), Write(txtE), FadeIn(
            dotD), FadeIn(dotE), Write(t2))
        self.play(GrowFromCenter(lBD), GrowFromCenter(
            lDE), GrowFromCenter(lEC))
        self.wait(1)
        self.remove(lBD, lDE, lEC)

        self.play(GrowFromCenter(tri1), Write(ts6a), FadeOut(t1), FadeOut(t2))
        self.wait(1)

        ind1 = Indicate(triangle, color=YELLOW, scale_factor=1)
        self.play(ind1)
        self.play(ind1)

        tg = VGroup(t3, t4)
        trans1 = TransformFromCopy(triangle, tg)
        self.play(trans1)
        self.wait(9)

        self.play(ShowCreation(lAE))
        self.wait(1)

        self.play(GrowFromCenter(lBD), GrowFromCenter(lDE))
        self.wait(1)
        self.remove(lBD, lDE)

        ind1 = Indicate(tri1, color=YELLOW, scale_factor=1)
        ind2 = Indicate(tri2, color=YELLOW, scale_factor=1)
        self.play(ind2, run_time=0.5)
        self.play(ind2, run_time=0.5)
        self.play(ind1, run_time=0.5)
        self.play(ind1, run_time=0.5)
        self.wait(1)
        self.play(Write(ts6b))
        self.remove(tri2)

        self.play(GrowFromCenter(lAF), GrowFromCenter(lBF))
        self.wait(1)
        self.remove(lAF, lBF)

        ind1 = Indicate(tri3, color=YELLOW, scale_factor=1)
        ind2 = Indicate(tri4, color=YELLOW, scale_factor=1)
        self.play(ind1, run_time=0.5)
        self.play(ind1, run_time=0.5)
        self.play(ind2, run_time=0.5)
        self.play(ind2, run_time=0.5)
        self.wait(1)
        self.play(Write(ts12a))
        self.remove(tri3, tri4)

        self.play(GrowFromCenter(lBE), GrowFromCenter(lEC))
        self.wait(1)
        self.remove(lBE, lEC)
        self.wait(1)

        ind1 = Indicate(tri5, color=YELLOW, scale_factor=1)
        ind2 = Indicate(tri6, color=YELLOW, scale_factor=1)
        self.play(ind1, run_time=0.5)
        self.play(ind1, run_time=0.5)
        self.wait(1)
        self.play(ind2, run_time=0.5)
        self.play(ind2, run_time=0.5)
        self.wait(1)
        self.play(Write(ts12b))
        self.wait(1)
        self.play(FadeOut(tri5), FadeOut(tri6))

        tg = VGroup(ts6a.copy(), ts6b, ts12a, ts12b)
        trans2 = Transform(tg, t5)
        self.play(FadeOut(t4), trans2)
        self.wait(5)
