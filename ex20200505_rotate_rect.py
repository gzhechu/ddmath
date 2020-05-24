#!/usr/bin/env python3

from manimlib.imports import *

# manim ddmath/ex20200505_rotate_rect.py RotateRect -r1280,720 -pm


class RotateRect(Scene):
    CONFIG = {
        "color": WHITE,
        "w": 4*1.6,
        "h": 3*1.6,
        "r": 5*1.6,
        "txt": 7,
    }

    def construct(self):
        t1 = TextMobject("AB=8,BC=6").set_color(WHITE).scale(1.5)
        t1.move_to(UP*(self.txt))
        t2 = TextMobject("围绕A点旋转90度").set_color(WHITE).scale(1.5)
        t2.move_to(UP*(self.txt))
        t3 = TextMobject("BC走到B'C'划过区域的面积").set_color(WHITE) .scale(1.5)
        t3.move_to(UP*(self.txt))
        t4 = TextMobject("用动画来模拟一下").set_color(WHITE).scale(1.5)
        t4.move_to(UP*(self.txt))

        rect1 = Rectangle(height=self.h, width=self.w)
        self.play(ShowCreation(rect1))
        self.wait(1)
        [ptA, ptB, ptC, ptD] = [rect1.get_corner(X) for X in [DR, DL, UL, UR]]
        [txtA, txtB, txtC, txtD] = [
            TextMobject(X) for X in ["A", "B", "C", "D"]]
        txtA.next_to(ptA, DOWN, buff=0.2)
        txtB.next_to(ptB, DL, buff=0.2)
        txtC.next_to(ptC, UL, buff=0.2)
        txtD.next_to(ptD, UL, buff=0.2)
        self.play(Write(txtA), Write(txtB), Write(txtC), Write(txtD))
        self.wait(1)

        line1 = Line(ptB, ptA, color=RED)
        num1 = TextMobject("8")
        num1.next_to(line1, DOWN, buff=0.2)
        line2 = Line(ptB, ptC, color=RED)
        num2 = TextMobject("6")
        num2.next_to(line2, LEFT, buff=0.2)
        self.play(Write(num1), Write(num2), Write(t1))

        g1 = VGroup(rect1, txtA, txtB, txtC, txtD,
                    num1, num2)
        g1.generate_target()
        g1.target.shift(LEFT*(self.h/2))
        trans1 = MoveToTarget(g1)
        self.play(trans1)
        self.wait(1)
        [ptA, ptB, ptC, ptD] = [rect1.get_corner(X) for X in [DR, DL, UL, UR]]

        rect2 = rect1.copy()
        angle = math.radians(-90)

        trans2 = ReplacementTransform(t1, t2)
        trans3 = ReplacementTransform(t2, t3)
        trans4 = ReplacementTransform(t3, t4)

        rotate1 = Rotate(rect2, angle=angle,
                         about_point=ptA)
        self.remove(g1)
        self.add(txtA)
        self.play(rotate1, trans2)
        [txtB1, txtC1, txtD1] = [TextMobject(X) for X in ["B'", "C'", "D'"]]
        [ptB1, ptC1, ptD1] = [rect2.get_corner(X) for X in [UL, UR, DR]]
        txtB1.next_to(ptB1, DR, buff=0.2)
        txtC1.next_to(ptC1, DR, buff=0.2)
        txtD1.next_to(ptD1, DR, buff=0.2)
        self.add(txtB1, txtC1, txtD1)
        self.wait(2)
        self.play(trans3)
        self.wait(3)

        # [ptA, ptB, ptC, ptD] = [rect1.get_corner(X) for X in [DR, DL, UL, UR]]
        # self.play(FadeIn(g1))
        g2 = VGroup(rect2, txtB1, txtC1, txtD1)
        self.play(ReplacementTransform(g2, g1))
        # self.add(g1)
        self.play(trans4)
        line1 = Line(ptB, ptC, color=RED)
        self.play(ShowCreation(line1))
        self.wait(3)

        # # self.remove(rect2, txtB1, txtC1, txtD1)
        # self.play(FadeOut(rect2), FadeOut(txtB1),
        #           FadeOut(txtC1), FadeOut(txtD1))
        # self.wait(1)

        line2 = line1.copy()
        line2.rotate(angle=angle, about_point=ptA)

        olst = []
        l = line1.copy()
        # r = rect1.copy()

        txtB1 = txtB.copy()
        txtC1 = txtC.copy()
        txtD1 = txtD.copy()
        self.add(txtB1, txtC1, txtD1)
        g = VGroup(rect2, txtB1, txtC1, txtD1)
        for i in range(1, 19):
            a1 = math.radians(-5)
            animation = Rotate(g, angle=a1,
                               about_point=ptA)
            self.play(animation, run_time=0.05)

            l = l.copy()
            l.rotate(a1, about_point=ptA)
            self.add(l)
            olst.append(l)

        self.remove(txtB1, txtC1, txtD1)
        self.add(line2)

        [txtB1, txtC1, txtD1] = [TextMobject(X) for X in ["B'", "C'", "D'"]]
        [ptB1, ptC1, ptD1] = [rect2.get_corner(X) for X in [UL, UR, DR]]
        txtB1.next_to(ptB1, DR, buff=0.1)
        txtC1.next_to(ptC1, DR, buff=0.1)
        txtD1.next_to(ptD1, DR, buff=0.1)
        self.add(txtB1, txtC1, txtD1)

        self.wait(1)

        arc1 = Arc(radius=self.w, arc_center=ptA,
                   color=RED, start_angle=np.deg2rad(180), angle=angle)
        arc2 = Arc(radius=self.r, arc_center=ptA,
                   color=RED, start_angle=np.deg2rad((np.arcsin(4/5)*180)/np.pi+90), angle=angle)
        self.play(ShowCreation(arc2))
        self.play(ShowCreation(arc1))
        self.wait(2)

        for o in olst:
            self.remove(o)
        self.wait(2)
        self.play(FadeOut(t4))

        line3 = DashedLine(rect1.get_corner(
            UL), rect1.get_corner(DR), color=BLUE)
        line4 = DashedLine(rect2.get_corner(
            UR), rect2.get_corner(DL), color=BLUE)
        self.play(ShowCreation(line3))
        self.play(ShowCreation(line4))
        self.wait(2)

        sector1 = Sector(arc_center=ptA, outer_radius=self.r, angle=TAU / 4,
                         start_angle=np.deg2rad((np.arcsin(4/5)*180)/np.pi),
                         color=BLUE, fill_opacity=0.5)
        self.play(ShowCreation(sector1))
        self.wait(1)

        triangle1 = Polygon(ptA, ptB, ptC, fill_color=BLUE, fill_opacity=0.5)
        self.play(ShowCreation(triangle1))
        self.wait(2)

        sector2 = Sector(arc_center=ptA, outer_radius=self.w, angle=TAU / 4,
                         start_angle=np.deg2rad(90),
                         color=BLACK, fill_opacity=0.8)
        self.play(ShowCreation(sector2))
        self.wait(1)

        triangle2 = Polygon(
            ptA, ptB1, ptC1, fill_color=BLACK, fill_opacity=0.8)
        self.play(ShowCreation(triangle2))
        self.wait(5)

        for o in [sector1, sector2, triangle1, triangle2, line3, line4]:
            self.remove(o)
        self.wait(3)

        for o in [line1, line2, arc1, arc2]:
            self.remove(o)
        self.wait(1)

        line1 = Line(ptC, ptD, color=RED)
        self.play(ShowCreation(line1))
        line2 = line1.copy()
        line2.rotate(angle=angle,
                     about_point=ptA)
        self.play(ShowCreation(line2))
        rotate1 = Rotate(line1, angle=angle,
                         about_point=ptA)
        self.play(rotate1)
        self.wait(5)


class Test(Scene):
    def construct(self):
        sector1 = Sector(outer_radius=5, color=RED, angle=TAU / 4,
                         start_angle=np.deg2rad((np.arcsin(4/5)*180)/np.pi),
                         fill_opacity=0.5).shift(DOWN*2.5)
        self.play(ShowCreation(sector1))
        self.wait(2)
