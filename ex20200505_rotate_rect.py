#!/usr/bin/env python3

from manimlib.imports import *

# manim ex20200505_rotate_rect.py RotateRect -pm


class RotateRect(Scene):
    def construct(self):
        rect1 = Rectangle(height=3, width=4)
        self.play(ShowCreation(rect1))
        self.wait(1)
        self.play(rect1.to_edge, DOWN, {"buff": 2})

        [ptA, ptB, ptC, ptD] = [rect1.get_corner(X) for X in [DR, DL, UL, UR]]

        line1 = Line(ptB, ptA, color=RED)
        num1 = TexMobject("8")
        num1.next_to(line1, DOWN, buff=0.1)
        self.play(Write(num1))

        line2 = Line(ptB, ptC, color=RED)
        num2 = TexMobject("6")
        num2.next_to(line2, LEFT, buff=0.1)
        self.play(Write(num2))

        [txtA, txtB, txtC, txtD] = [
            TexMobject(X) for X in ["A", "B", "C", "D"]]

        txtA.next_to(ptA, DOWN, buff=0.1)
        txtB.next_to(ptB, DL, buff=0.1)
        txtC.next_to(ptC, UL, buff=0.1)
        txtD.next_to(ptD, UL, buff=0.1)

        self.add(txtA, txtB, txtC, txtD)
        self.wait(1)

        rect2 = rect1.copy()
        angle = math.radians(-90)

        rotate1 = Rotate(rect2, angle=angle,
                         about_point=ptA)
        self.play(rotate1)
        self.wait(1)

        [txtB1, txtC1, txtD1] = [TexMobject(X) for X in ["B'", "C'", "D'"]]
        [ptB1, ptC1, ptD1] = [rect2.get_corner(X) for X in [UL, UR, DR]]

        txtB1.next_to(ptB1, DR, buff=0.1)
        txtC1.next_to(ptC1, DR, buff=0.1)
        txtD1.next_to(ptD1, DR, buff=0.1)
        self.add(txtB1, txtC1, txtD1)

        group = VGroup(rect1, rect2, txtA, txtB, txtC,
                       txtD, num1, num2, txtB1, txtC1, txtD1)
        gwidth = group.get_width()
        self.play(group.to_edge, LEFT, {"buff": (14.2-gwidth)/2})

        [ptA, ptB, ptC, ptD] = [rect1.get_corner(X) for X in [DR, DL, UL, UR]]

        line1 = Line(ptB, ptC, color=RED)
        self.play(ShowCreation(line1))
        self.wait(3)

        self.remove(rect2, txtB1, txtC1, txtD1)
        self.wait(1)

        line2 = line1.copy()
        line2.rotate(angle=angle, about_point=ptA)

        olst = []
        l = line1.copy()
        r = rect1.copy()

        txtB1 = txtB.copy()
        txtC1 = txtC.copy()
        txtD1 = txtD.copy()
        self.add(txtB1, txtC1, txtD1)

        g = VGroup(r, txtB1, txtC1, txtD1)
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

        [txtB1, txtC1, txtD1] = [TexMobject(X) for X in ["B'", "C'", "D'"]]
        [ptB1, ptC1, ptD1] = [rect2.get_corner(X) for X in [UL, UR, DR]]
        txtB1.next_to(ptB1, DR, buff=0.1)
        txtC1.next_to(ptC1, DR, buff=0.1)
        txtD1.next_to(ptD1, DR, buff=0.1)
        self.add(txtB1, txtC1, txtD1)

        self.wait(1)

        arc1 = Arc(radius=4, arc_center=ptA,
                   color=RED, start_angle=np.deg2rad(180), angle=angle)
        arc2 = Arc(radius=5, arc_center=ptA,
                   color=RED, start_angle=np.deg2rad((np.arcsin(4/5)*180)/np.pi+90), angle=angle)
        self.play(ShowCreation(arc2))
        self.play(ShowCreation(arc1))
        self.wait(2)

        for o in olst:
            self.remove(o)
        self.wait(2)

        line3 = DashedLine(rect1.get_corner(
            UL), rect1.get_corner(DR), color=YELLOW)
        line4 = DashedLine(rect2.get_corner(
            UR), rect2.get_corner(DL), color=YELLOW)
        self.play(ShowCreation(line3))
        self.play(ShowCreation(line4))
        self.wait(2)

        sector1 = Sector(arc_center=ptA, outer_radius=5, angle=TAU / 4,
                         start_angle=np.deg2rad((np.arcsin(4/5)*180)/np.pi),
                         color=YELLOW, fill_opacity=0.5)
        self.play(ShowCreation(sector1))

        triangle1 = Polygon(ptA, ptB, ptC, fill_color=YELLOW, fill_opacity=0.5)
        self.play(ShowCreation(triangle1))
        self.wait(2)

        sector2 = Sector(arc_center=ptA, outer_radius=4, angle=TAU / 4,
                         start_angle=np.deg2rad(90),
                         color=BLACK, fill_opacity=0.8)
        self.play(ShowCreation(sector2))

        triangle2 = Polygon(
            ptA, ptB1, ptC1, fill_color=BLACK, fill_opacity=0.8)
        self.play(ShowCreation(triangle2))
        self.wait(2)

        for o in [sector1, sector2, triangle1, triangle2, line3, line4]:
            self.remove(o)
        self.wait(2)

        for o in [line1, line2, arc1, arc2]:
            self.remove(o)
        self.wait(2)

        line1 = Line(ptC, ptD, color=RED)
        self.play(ShowCreation(line1))
        self.wait(1)

        line2 = line1.copy()
        line2.rotate(angle=angle,
                     about_point=ptA)
        self.play(ShowCreation(line2))
        self.wait(2)

        self.remove(rect2)
        rect2 = rect1.copy()
        rotate1 = Rotate(rect2, angle=angle,
                         about_point=ptA)
        self.play(rotate1)
        self.wait(6)


class Test(Scene):
    def construct(self):
        sector1 = Sector(outer_radius=5, color=RED, angle=TAU / 4,
                         start_angle=np.deg2rad((np.arcsin(4/5)*180)/np.pi),
                         fill_opacity=0.5).shift(DOWN*2.5)
        self.play(ShowCreation(sector1))
        self.wait(2)
