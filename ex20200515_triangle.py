#!/usr/bin/env python3

from manimlib.imports import *

# manim ddmath/ex20200515_triangle.py Triangle -pm
# manim ddmath/ex20200515_triangle.py Triangle -pm -r1280,720


class Triangle(Scene):
    CONFIG = {
        "color": WHITE,
        "A": np.array([-1.5, 2, 0]),
        "B": np.array([-3, -2, 0]),
        "C": np.array([4.5, -2, 0]),
    }

    def construct(self):
        # origin = Dot()
        # [txtO] = [TexMobject(X) for X in ["O"]]
        # txtO.next_to(origin, DR, buff=0.1)
        # self.play(FadeIn(origin), FadeIn(txtO))

        [txtA, txtB, txtC] = [TexMobject(X) for X in ["A", "B", "C"]]
        # [txtA1, txtB1, txtC1] = [TexMobject(X) for X in ["a", "b", "c"]]

        triangle = Polygon(self.A, self.B, self.C)
        self.play(ShowCreation(triangle))
        self.wait(1)
        txtA.next_to(self.A, UP, buff=0.36)
        txtB.next_to(self.B, DL, buff=0.36)
        txtC.next_to(self.C, DR, buff=0.36)
        self.play(Write(txtA), Write(txtB), Write(txtC))
        self.wait(3)

        eq1 = TexMobject("\\angle ABC=\\angle EAB").scale(1.2)
        eq2 = TexMobject("\\angle ACB=\\angle FAC").scale(1.2)
        eq3 = TexMobject("\\angle EAB+\\angle FAC+\\angle BAC=180").scale(1.2)
        eq4 = TexMobject("\\angle ABC+\\angle ACB+\\angle BAC=180").scale(1.2)
        eq1.shift(UP*self.A*4)
        eq2.next_to(eq1, DOWN, buff=0.5)
        eq3.next_to(eq2, DOWN, buff=0.5)
        eq4.next_to(eq3, DOWN, buff=0.5)

        ptE = self.A + 3*LEFT
        ptF = self.A + 7*RIGHT
        [txtE, txtF] = [TexMobject(X) for X in ["E", "F"]]
        txtE.next_to(ptE, UP, buff=0.2)
        txtF.next_to(ptF, UP, buff=0.2)
        line = DashedLine(ptE, ptF)
        self.play(ShowCreation(line), Write(txtE), Write(txtF))
        self.wait(2)

        angle = math.radians(180)

        t1 = triangle.copy()
        t1.set_color(color=YELLOW)
        t1.set_opacity(opacity=0.2)
        rotate1 = Rotate(t1, angle=-angle, about_point=self.A)
        self.play(rotate1)
        self.wait(1)
        t1.generate_target()
        t1.target.shift(LEFT*(np.abs(self.B-self.A)) +
                        DOWN*(np.abs(self.A-self.B)))
        trans1 = MoveToTarget(t1)

        l = Line(self.A, self.B)
        a1 = l.get_angle()
        arc1 = Arc(arc_center=self.A, radius=1, color=YELLOW,
                   start_angle=np.deg2rad(180), angle=np.deg2rad(180 + np.rad2deg(a1)))
        arc2 = Arc(arc_center=self.B, radius=1, color=YELLOW,
                   start_angle=np.deg2rad(0), angle=np.deg2rad(180 + np.rad2deg(a1)))

        self.play(trans1)
        self.play(ShowCreation(arc1), ShowCreation(arc2), Write(eq1))
        self.wait(1)

        t2 = triangle.copy()
        t2.set_color(color=RED)
        t2.set_opacity(opacity=0.2)
        rotate2 = Rotate(t2, angle=angle, about_point=self.A)
        self.play(rotate2)
        self.wait(1)
        t2.generate_target()
        t2.target.shift(RIGHT*(np.abs(self.C-self.A)) +
                        DOWN*(np.abs(self.A-self.B)))
        trans2 = MoveToTarget(t2)

        l = Line(self.A, self.C)
        a2 = l.get_angle()
        arc1 = Arc(arc_center=self.A, radius=1, color=RED,
                   start_angle=np.deg2rad(0), angle=np.deg2rad(np.rad2deg(a2)))
        arc2 = Arc(arc_center=self.C, radius=1, color=RED,
                   start_angle=np.deg2rad(180), angle=np.deg2rad(np.rad2deg(a2)))

        arc3 = Arc(arc_center=self.A, radius=0.9, color=RED,
                   start_angle=np.deg2rad(0), angle=np.deg2rad(np.rad2deg(a2)))
        arc4 = Arc(arc_center=self.C, radius=0.9, color=RED,
                   start_angle=np.deg2rad(180), angle=np.deg2rad(np.rad2deg(a2)))

        self.play(trans2)
        self.play(ShowCreation(arc1), ShowCreation(arc2),
                  ShowCreation(arc3), ShowCreation(arc4), Write(eq2))
        self.wait(1)

        arcx = Arc(arc_center=self.A, radius=1.1, color=BLUE,
                   start_angle=np.deg2rad(180), angle=np.deg2rad(180))
        self.play(ShowCreation(arcx), Write(eq3))
        self.wait(2)

        t1.generate_target()
        t1.target.rotate(angle=angle)
        t1.target.shift(RIGHT*(np.abs(self.C-self.A)))
        trans1 = MoveToTarget(t1)
        self.play(trans1)
        self.wait(1)
        self.play(FadeOut(t1), FadeOut(eq1))
        self.wait(1)

        t2.generate_target()
        t2.target.rotate(angle=angle)
        t2.target.shift(LEFT*(np.abs(self.B-self.A)))
        trans2 = MoveToTarget(t2)
        self.play(trans2)
        self.wait(1)
        self.play(FadeOut(t2), FadeOut(eq2))

        trans = Transform(eq3, eq4)
        self.play(trans, FadeOut(arcx))

        self.wait(5)
