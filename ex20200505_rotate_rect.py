#!/usr/bin/env python3

from manimlib.imports import *


class RotateRect(Scene):
    def construct(self):
        textT = TextMobject("Question:")
        textT.to_edge(UP)
        self.play(Write(textT))

        rect1 = Rectangle(height=3, width=4)
        self.play(ShowCreation(rect1))
        self.wait(1)

        self.play(rect1.to_edge, DOWN, {"buff": 1})
        rect2 = rect1.copy()
        angle = math.radians(-90)

        ptA = rect1.get_corner(DR)

        rotate1 = Rotate(rect2, angle=angle,
                         about_point=ptA)
        self.play(rotate1)
        self.wait(0.1)

        group = VGroup(rect1, rect2)
        gwidth = group.get_width()
        self.play(group.to_edge, LEFT, {"buff": (14.2-gwidth)/2})
        ptA = rect1.get_corner(DR)
        ptB = rect1.get_corner(DL)
        ptC = rect1.get_corner(UL)
        ptD = rect1.get_corner(UR)
        self.wait(1)
        rect2.fade_to(color=BLACK, alpha=0)
        self.remove(rect2)
        self.wait(1)

        line1 = Line(ptB, ptA, color=RED)
        txt4 = TexMobject("8")
        txt4.next_to(line1, DOWN, buff=0.1)
        self.play(Write(txt4))

        line1 = Line(ptB, ptC, color=RED)
        txt3 = TexMobject("6")
        txt3.next_to(line1, LEFT, buff=0.1)
        self.play(Write(txt3))

        txtA = TexMobject("A")
        txtB = TexMobject("B")
        txtC = TexMobject("C")
        txtD = TexMobject("D")

        txtB1 = TexMobject("B'")
        txtC1 = TexMobject("C'")
        txtD1 = TexMobject("D'")

        txtA.next_to(ptA, DOWN, buff=0.1)
        txtB.next_to(ptB, DL, buff=0.1)
        txtC.next_to(ptC, UL, buff=0.1)
        txtD.next_to(ptD, UL, buff=0.1)
        self.add(txtA)
        self.add(txtB)
        self.add(txtC)
        self.add(txtD)
        self.wait(1)

        self.play(ShowCreation(line1))
        self.wait(1)

        line2 = line1.copy()
        line2.rotate(angle=angle,
                     about_point=ptA)

        olst = []
        rlst = []
        l = line1.copy()
        r = rect1.copy()
        for i in range(1, 19):
            a1 = math.radians(-5)
            # a2 = math.radians(-10*i)

            # r = r.copy()
            animation = Rotate(r, angle=a1,
                               about_point=ptA)
            self.play(animation, run_time=0.05)
            # rlst.append(r)

            l = l.copy()
            l.rotate(a1, about_point=ptA)
            self.add(l)
            olst.append(l)

            # arc1 = Arc(radius=4, arc_center=ptA,
            #            color=RED, start_angle=np.deg2rad(180), angle=a2)
            # arc2 = Arc(radius=5, arc_center=ptA,
            #            color=RED, start_angle=np.deg2rad((np.arcsin(4/5)*180)/np.pi+90), angle=a2)
            # self.add(arc1)
            # self.add(arc2)
            # olst.append(arc1)
            # olst.append(arc2)

        self.add(rect2)
        self.add(line2)

        self.wait(1)
        for r in rlst:
            r.fade_to(color=BLACK, alpha=0)
            self.remove(r)
            self.wait(0.08)

        ptB1 = rect2.get_corner(UL)
        ptC1 = rect2.get_corner(UR)
        ptD1 = rect2.get_corner(DR)
        txtB1.next_to(ptB1, DR, buff=0.1)
        txtC1.next_to(ptC1, DR, buff=0.1)
        txtD1.next_to(ptD1, DR, buff=0.1)
        self.add(txtB1)
        self.add(txtC1)
        self.add(txtD1)

        arc1 = Arc(radius=4, arc_center=ptA,
                   color=RED, start_angle=np.deg2rad(180), angle=angle)
        arc2 = Arc(radius=5, arc_center=ptA,
                   color=RED, start_angle=np.deg2rad((np.arcsin(4/5)*180)/np.pi+90), angle=angle)
        self.play(ShowCreation(arc2))
        self.play(ShowCreation(arc1))

        textQ = TextMobject("What is the size of red area?")
        textQ.next_to(textT, DOWN, buff=0.1)
        self.play(Write(textQ))

        # self.wait(1)
        # for o in olst:
        #     o.fade_to(color=BLACK, alpha=0)
        #     self.remove(o)

        # group = VGroup(line1, line2, arc1, arc2)
        # group.set_color(color=BLUE)
        # group.set_fill(BLUE, opacity=0.5)

        self.wait(6)

        # line3 = DashedLine(rect1.get_corner(
        #     UL), rect1.get_corner(DR), color=YELLOW)
        # line4 = DashedLine(rect2.get_corner(
        #     UR), rect2.get_corner(DL), color=YELLOW)
        # self.play(ShowCreation(line3))
        # self.play(ShowCreation(line4))
        # self.wait(5)
