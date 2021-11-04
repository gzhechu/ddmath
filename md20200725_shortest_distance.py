#!/usr/bin/env python3

from manimlib import *

# manim ddmath/md20200725_shortest_distance.py ShortestDistance -r1280,720 -pm
# manim ddmath/md20200725_shortest_distance.py ShortestDistance -r640,360 -pl


class ShortestDistance(Scene):
    CONFIG = {
        "color": WHITE,
        "A": np.array([-5, 4, 0]),
        "B": np.array([5, 8, 0]),
        "P": np.array([-4, 1, 0]),
        "A1": np.array([-5, -2, 0]),
        "A2": np.array([-5, -5, 0]),
        "river_width": 2,
        "river_length": 20,
        "txt": 7
    }

    def construct(self):
        # origin = Dot()
        # [txtO] = [TexMobject(X) for X in ["O"]]
        # txtO.next_to(origin, DR, buff=0.1)
        # self.play(FadeIn(origin), FadeIn(txtO))

        # ptH = self.A*RIGHT + self.B*UP
        # hLine = DashedLine(self.A, ptH)

        river = Rectangle(height=self.river_width, width=self.river_length)
        river.set_fill(color=BLUE, opacity=0.3)
        self.play(FadeIn(river))
        self.wait(3)

        [txtA, txtB, txtP, txtA1] = [
            TexMobject(X).scale(1.5) for X in ["A", "B", "P", "A'"]]
        [ptA, ptB, ptP, ptA1, ptA2] = [Dot(X)
                                       for X in [self.A, self.B,  self.P, self.A1, self.A2]]

        txtA.next_to(ptA, UP, buff=0.5)
        txtB.next_to(ptB, UP, buff=0.5)
        txtP.next_to(ptP, DOWN, buff=0.5)
        txtA1.next_to(ptA1, DOWN, buff=0.5)

        self.play(FadeIn(ptA), FadeIn(ptB), FadeIn(txtA), FadeIn(txtB))

        self.wait(3)

        line1 = DashedLine(ptA, ptP)
        line2 = DashedLine(ptP, ptB)
        g1 = VGroup(ptP, txtP, line1, line2)
        self.play(FadeIn(ptP), FadeIn(txtP))
        self.play(ShowCreation(line1))
        self.play(ShowCreation(line2))
        self.wait(3)

        def update1(group, alpha):
            ptP = Dot(self.P*UP + (self.P + alpha * 8)*RIGHT)
            txtP = TexMobject("P").scale(1.5)
            txtP.next_to(ptP, DOWN, buff=0.5)
            line1 = DashedLine(ptA, ptP)
            line2 = DashedLine(ptB, ptP)
            ng = VGroup(ptP, txtP, line1, line2)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(g1, update1),
                  run_time=6, rate_func=there_and_back)
        self.wait(3)

        lineH = DashedLine(ptA, ptA1)
        self.play(ShowCreation(lineH))
        self.play(FadeIn(ptA1), FadeIn(txtA1))
        self.wait(3)

        lineAB = DashedLine(ptA1, ptB)
        self.play(ShowCreation(lineAB))
        self.wait(3)

        def update2(group, alpha):
            ptP = Dot(self.P*UP + (self.P + alpha * 2)*RIGHT)
            txtP = TexMobject("P").scale(1.5)
            txtP.next_to(ptP, DOWN, buff=0.5)
            line1 = DashedLine(ptA, ptP)
            line2 = DashedLine(ptB, ptP)
            ng = VGroup(ptP, txtP, line1, line2)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(g1, update2),
                  run_time=6, rate_func=smooth)
        self.remove(lineAB, lineH, txtA1, ptA1)
        self.wait(3)

        bridge = Rectangle(height=2, width=2)
        bridge.set_fill(color=YELLOW, opacity=0.5)
        bridge.shift(LEFT*1.2)

        txtA1.next_to(ptA2, DOWN, buff=0.5)
        lineAB2 = DashedLine(ptA2, ptB)
        self.remove(ptA, ptA1, ptP, txtA, txtP,  line1, line2)
        self.wait(3)
        ga1 = VGroup(txtA, ptA)
        ga2 = VGroup(txtA1, ptA2)
        trans1 = ReplacementTransform(ga1, ga2)
        self.play(trans1)

        self.play(FadeIn(lineAB2))
        self.play(FadeIn(bridge))
        self.wait(3)
