#!/usr/bin/env python3

from manimlib.imports import *

# manimlib ex20200515_interior_angle.py Triangle -r1280,720 -pm


class Triangle(Scene):
    CONFIG = {
        "color": WHITE,
        "A": np.array([1.5, 4, 0]),
        "B": np.array([-4.5, -2, 0]),
        "C": np.array([5, -2, 0]),
        "txt": 7
    }

    def construct(self):
        # origin = Dot()
        # [txtO] = [TexMobject(X) for X in ["O"]]
        # txtO.next_to(origin, DR, buff=0.1)
        # self.play(FadeIn(origin), FadeIn(txtO))

        [txtA, txtB, txtC] = [TexMobject(X) for X in ["A", "B", "C"]]

        triangle = Polygon(self.A, self.B, self.C, color=WHITE)
        self.play(ShowCreation(triangle))
        self.wait(1)
        txtA.next_to(self.A, UP, buff=0.5)
        txtB.next_to(self.B, DL, buff=0.3)
        txtC.next_to(self.C, DR, buff=0.3)
        self.play(Write(txtA), Write(txtB), Write(txtC))
        self.wait(2)

        self.parallelLine()
        self.flipAngle()

    def parallelLine(self):

        [alpha, beta, gamma] = [TexMobject(X)
                                for X in ["a", "b", "c"]]
        [alpha1, beta1, gamma1] = [TexMobject(X)
                                   for X in ["a'", "b'", "c'"]]
        eq1 = TexMobject("\\angle b=\\angle b'").scale(2)
        eq2 = TexMobject("\\angle c=\\angle c'").scale(2)
        eq3 = TexMobject(
            "\\angle a+\\angle b'+\\angle c'=180^\\circ").scale(2)
        eq4 = TexMobject(
            "\\angle a+\\angle b+\\angle c=180^\\circ").scale(2)
        eq1.move_to(UP*self.txt)
        eq2.move_to(UP*self.txt)
        eq3.move_to(UP*self.txt)
        eq4.move_to(UP*self.txt)

        ptE = self.A*UP - self.B*LEFT
        ptF = self.A*UP + self.C*RIGHT
        parallelLine = DashedLine(ptE, ptF)
        self.play(ShowCreation(parallelLine))
        self.wait(1)

        l = Line(self.A, self.B)
        a1 = l.get_angle()
        l = Line(self.A, self.C)
        a2 = l.get_angle()

        self.angA = Sector(arc_center=self.A, outer_radius=1.2, color=BLUE, fill_opacity=0.8,
                           start_angle=a1, angle=(a2-a1))
        alpha.next_to(self.angA, DOWN, buff=0.1)
        self.play(ShowCreation(self.angA), FadeIn(alpha))
        self.wait(1)

        angA1 = Sector(arc_center=self.A, outer_radius=1.2, color=YELLOW, fill_opacity=0.8,
                       start_angle=PI, angle=PI + a1)
        self.angB = Sector(arc_center=self.B, outer_radius=1.2, color=YELLOW, fill_opacity=0.8,
                           start_angle=0, angle=PI + a1)

        beta.next_to(self.angB, RIGHT, buff=0.1)
        beta1.next_to(angA1, LEFT, buff=0.1)
        self.play(ShowCreation(self.angB), FadeIn(beta))
        self.wait(1)
        self.play(TransformFromCopy(self.angB, angA1),
                  FadeIn(beta1), Write(eq1))
        self.wait(2)

        angA2 = Sector(arc_center=self.A, outer_radius=1.2, color=RED, fill_opacity=0.8,
                       start_angle=0, angle=a2)
        self.angC = Sector(arc_center=self.C, outer_radius=1.2, color=RED, fill_opacity=0.8,
                           start_angle=PI, angle=a2)

        gamma.next_to(self.angC, LEFT, buff=0.1)
        gamma1.next_to(angA2, RIGHT, buff=0.1)
        self.play(ShowCreation(self.angC), FadeIn(gamma))
        self.wait(1)
        self.play(TransformFromCopy(self.angC, angA2), FadeIn(
            gamma1), ReplacementTransform(eq1, eq2))
        self.wait(2)

        self.play(FadeOut(beta),
                  FadeOut(gamma), FadeOut(self.angB), FadeOut(self.angC))
        self.wait(1)

        self.remove(eq2)
        gl = VGroup(beta1, gamma1, alpha.copy())
        self.remove(alpha)
        self.play(ReplacementTransform(gl, eq3))
        self.wait(3)

        trans = ReplacementTransform(eq3, eq4)
        self.play(trans, FadeIn(alpha), FadeIn(beta), FadeIn(gamma), ReplacementTransform(
            angA1, self.angB), ReplacementTransform(angA2, self.angC),)
        self.wait(3)
        self.play(FadeOut(parallelLine), FadeOut(eq4))
        self.wait(2)

    def flipAngle(self):
        [alpha1, beta1, gamma1] = [TexMobject(X)
                                   for X in [" a'", " b'", " c'"]]
        eq1 = TexMobject("\\angle a=\\angle a'").scale(2)
        eq2 = TexMobject("\\angle b=\\angle b'").scale(2)
        eq3 = TexMobject("\\angle c=\\angle c'").scale(2)
        eq4 = TexMobject(
            "\\angle a'+\\angle b'+\\angle c'=180^\\circ").scale(2)
        eq5 = TexMobject(
            "\\angle a+\\angle b+\\angle c=180^\\circ").scale(2)
        eq1.move_to(UP*self.txt)
        eq2.move_to(UP*self.txt)
        eq3.move_to(UP*self.txt)
        eq4.move_to(UP*self.txt)
        eq5.move_to(UP*self.txt)

        ptA = self.A*RIGHT + self.B*UP
        # self.add(Dot(ptA))

        ptE = (self.A+self.B)/2
        ptF = (self.A+self.C)/2

        ptB1 = self.B*UP - ptE*LEFT
        ptC1 = self.C*UP + ptF*RIGHT

        t1 = Polygon(self.A, ptE, ptF, color=BLUE,
                     stroke_opacity=0, fill_opacity=0.3)
        self.play(ShowCreation(t1, run_time=2))
        g1 = VGroup(t1, self.angA)
        rotate1 = Rotate(g1, angle=PI, axis=RIGHT, about_point=ptE, run_time=2)

        self.play(rotate1, Write(eq1))
        alpha1.next_to(self.angA, UP, buff=0.1)
        self.add(alpha1)
        self.wait(1)

        t2 = Polygon(self.B, ptB1, ptE, color=YELLOW,
                     stroke_opacity=0, fill_opacity=0.3)
        self.play(ShowCreation(t2, run_time=2))
        g2 = VGroup(t2, self.angB)
        rotate2 = Rotate(g2, angle=PI, axis=UP, about_point=ptE, run_time=2)

        self.play(rotate2, ReplacementTransform(eq1, eq2))
        beta1.next_to(self.angB, LEFT, buff=0.1)
        self.add(beta1)
        self.wait(1)

        t3 = Polygon(self.C, ptC1, ptF, color=RED,
                     stroke_opacity=0, fill_opacity=0.3)
        self.play(ShowCreation(t3, run_time=2))
        g3 = VGroup(t3, self.angC)
        rotate3 = Rotate(g3, angle=PI, axis=UP, about_point=ptF, run_time=2)

        self.play(rotate3, ReplacementTransform(eq2, eq3))
        gamma1.next_to(self.angC, RIGHT, buff=0.1)
        self.add(gamma1)
        self.wait(1)

        self.remove(eq3)
        gl = VGroup(alpha1, beta1, gamma1)
        self.play(ReplacementTransform(gl, eq4))
        self.wait(3)

        rotate1 = Rotate(g1, angle=PI, axis=RIGHT, about_point=ptE, run_time=2)
        rotate2 = Rotate(g2, angle=PI, axis=UP, about_point=ptE, run_time=2)
        rotate3 = Rotate(g3, angle=PI, axis=UP, about_point=ptF, run_time=2)
        self.play(rotate1, rotate2, rotate3, ReplacementTransform(eq4, eq5))
        self.remove(t1, t2, t3)
        self.wait(5)
