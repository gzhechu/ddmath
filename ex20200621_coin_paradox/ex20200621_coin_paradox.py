#!/usr/bin/env python3

from manim import *
import math

# manim ex20200621_coin_paradox.py CoinParadox -r1280,720 -pqm


class CoinParadox(Scene):
    def construct(self):
        self.r = 1.2
        self.txt = 8
        self.equation = 4
        self.left = 4.5
        self.right = 3.5

        [txYi, txYuan] = [TextMobject(X).scale(1.5) for X in ["One", "Yuan"]]
        txYuan.next_to(txYi, DOWN)
        txtYY = VGroup(txYi, txYuan)
        txtYY.shift(DOWN*txtYY.get_center())

        circle0 = Circle(radius=self.r, color=WHITE,
                         fill_color=YELLOW, fill_opacity=0.5)
        circle0 = VGroup(circle0, txtYY)

        circle1 = Circle(radius=self.r, color=WHITE,
                         fill_color=BLUE, fill_opacity=0.5)
        arrow1 = txtYY.copy()
        dot1 = Dot()
        arc1 = Arc(radius=self.r*2, color=BLUE,
                   start_angle=np.deg2rad(90), angle=0)

        g0 = VGroup(circle1, arrow1)
        g0.shift(UP*(self.r*2))

        t1 = TextMobject("Coin: r").scale(1.5)
        t1.move_to(UP*self.txt+RIGHT*self.right)

        t2 = TextMobject("Path: R").scale(1.5)
        t2.next_to(t1, DOWN, buff=0.5)

        t3 = TextMobject("R = 2 × r").scale(1.5)
        t3.next_to(t2, DOWN, buff=0.5)

        # self.play(FadeIn(circle0), FadeIn(g0), FadeIn(origin), FadeIn(txtO))
        self.add(circle0, g0,  txtYY)
        self.play(Write(t1))
        self.wait(1)

        def update0(group, alpha):
            angle = math.radians(360 * alpha)
            circle = Circle(radius=self.r, color=WHITE,
                            fill_color=BLUE, fill_opacity=0.5)
            circle.shift(UP*(self.r*2))

            circle.rotate(angle=-angle, about_point=ORIGIN)
            dx = circle.get_center()
            # arrow = Arrow(dx, dx + UP*self.r)
            arrow = txtYY.copy()
            angle = math.radians(-360 * alpha * (self.r)/self.r*2)
            arrow.rotate(angle=angle)
            arrow.move_to(dx)

            ng = VGroup(circle, arrow)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(g0, update0),
                  run_time=8, rate_func=double_smooth)
        self.wait(1)

        g1 = VGroup(circle1, arrow1, arc1)
        g1.shift(UP*(self.r*2))

        def update1(group, alpha):
            angle = math.radians(360 * alpha)
            arc = Arc(radius=self.r*2, color=BLUE,
                      start_angle=np.deg2rad(90), angle=-angle)
            circle = Circle(radius=self.r, color=WHITE,
                            fill_color=BLUE, fill_opacity=0.5)
            circle.shift(UP*(self.r*2))

            circle.rotate(angle=-angle, about_point=ORIGIN)
            dx = circle.get_center()
            # arrow = Arrow(dx, dx + UP*self.r)
            arrow = txtYY.copy()

            angle = math.radians(-360 * alpha * (self.r)/self.r*2)
            # arrow.rotate(angle=angle, about_point=dx)
            arrow.rotate(angle=angle)
            arrow.move_to(dx)

            ng = VGroup(circle, arrow, arc)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(g1, update1),
                  run_time=6, rate_func=double_smooth)
        self.wait(1)

        radline = Line(ORIGIN, UP*(self.r*2), color=WHITE)
        self.play(ShowCreation(radline))
        trans1 = ReplacementTransform(radline, t2)
        self.play(trans1)
        self.wait(1)
        self.play(Write(t3))
        self.wait(1)

        self.play(FadeOut(circle0))
        self.remove(txtYY)
        self.wait(1)

        llen = self.r * PI * 2
        g1 = VGroup(circle1, arrow1)
        g1.generate_target()
        g1.target.shift(UP*(llen - self.r*2))
        trans1 = MoveToTarget(g1)
        track_line = Line(UP*llen, DOWN*llen,)
        trans2 = Transform(arc1, track_line)
        self.play(trans1, trans2)
        self.wait(1)

        track_line.generate_target()
        track_line.target.shift(LEFT*self.r)
        self.remove(arc1)
        trans1 = MoveToTarget(track_line)
        trans2 = Rotate(g1, angle=math.radians(90),
                        about_point=circle1.get_center())
        self.play(trans1, trans2)
        self.wait(3)

        def update2(group, alpha):
            angle = math.radians(-360 * alpha)
            circle = Circle(radius=self.r, color=WHITE,
                            fill_color=BLUE, fill_opacity=0.5)
            circle.shift(UP*llen + DOWN*llen*alpha*2)
            line = DashedLine(UP*llen, UP*llen + DOWN*llen*alpha*2, color=BLUE)

            dx = circle.get_center()
            arrow = Arrow(dx, dx + LEFT*self.r)
            arrow = txtYY.copy()

            angle = math.radians(-360 * alpha * 2) + PI/2
            agr = int(alpha * 2)
            agc = "{:.1f}".format(alpha*2)
            agr = 0
            agc = "0"
            # print(agr)
            ta = TextMobject("angle={:d}".format(agr)).scale(1.5)
            tb = TextMobject("round={:s}".format(agc)).scale(1.5)
            ta.shift(UP*self.txt+LEFT*self.left)
            tb.next_to(ta, DOWN, buff=0.5)

            # arrow.rotate(angle=angle, about_point=dx)
            arrow.rotate(angle=angle)
            arrow.move_to(dx)

            ng = VGroup(circle, arrow, ta, tb, line)
            # ng = VGroup(circle, arrow, dot)
            group.become(ng)
            return group

        ta = TexMobject("angle=0").scale(1.5)
        tb = TexMobject("round=0").scale(1.5)
        line = DashedLine(color=BLUE)
        g1 = VGroup(circle1, arrow1, ta, tb, line)

        self.play(UpdateFromAlphaFunc(g1, update2),
                  run_time=8, rate_func=double_smooth)
        self.wait(3)

        g2 = VGroup(circle1, arrow1)

        rnd = TexMobject("round").scale(1.5)
        rnd.move_to(self.equation*UP)

        equl = TexMobject("=").scale(1.5)
        equl.next_to(rnd, RIGHT)

        t2 = TexMobject("S=2\\pi R").scale(1.5)
        t2.move_to(UP*(self.txt-4))
        t3 = TexMobject("C=2\\pi r").scale(1.5)
        t3.next_to(t2, DOWN, buff=0.5)

        t4r = TexMobject("\\frac{S}{C}").scale(1.5)
        t4r.next_to(equl, RIGHT)
        t4 = VGroup(rnd, equl, t4r)

        t5r = TexMobject(
            "\\frac{2\\pi R}{2\\pi\\ r}").scale(1.5)
        t6r = TexMobject("\\frac{R}{r}").scale(1.5)
        t7r = TexMobject("2").scale(1.5)

        self.remove(line)
        self.play(ReplacementTransform(track_line, t2))
        self.wait(1)
        self.play(ReplacementTransform(g2, t3))
        self.wait(2)
        g2 = VGroup(t2, t3)

        circle1 = Circle(radius=self.r, color=WHITE,
                         fill_color=BLUE, fill_opacity=0.5)
        arrow1 = Arrow(circle1.get_center(), UP*self.r)
        # dot1 = Dot()
        arc1 = Circle(radius=self.r*2, color=BLUE)
        arc1.move_to(DOWN*(self.r*2))
        g3 = VGroup(circle1, arrow1, dot1, arc1)

        arrow2 = Arrow(ORIGIN, UP*(self.r*2))
        arrow2.move_to(arc1.get_center()+UP*(self.r*2)/2)

        ind1 = Indicate(arrow1, run_time=1, scale_factor=3)
        ind2 = Indicate(arrow2, run_time=1, scale_factor=2)

        self.play(ReplacementTransform(g2, t4), FadeIn(g3))
        t4.generate_target()
        t4.target.shift(LEFT*t4.get_center())
        move1 = MoveToTarget(t4)
        self.play(move1)
        self.wait(1)
        # self.play()
        # self.play(ind1)

        t5r.next_to(equl, RIGHT)
        self.play(ReplacementTransform(t4r, t5r), ind2)
        self.wait(1)

        t6r.next_to(equl, RIGHT)
        self.play(ReplacementTransform(t5r, t6r), ind1)
        self.wait(1)

        t7r.next_to(equl, RIGHT)
        self.play(ReplacementTransform(t6r, t7r))

        self.wait(4)
