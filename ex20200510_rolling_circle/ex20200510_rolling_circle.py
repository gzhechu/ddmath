#!/usr/bin/env python3

from manim import *
import math

# manim ex20200510_rolling_circle.py RollingCircle1 -r1280,720 -pqm
# manim ex20200510_rolling_circle.py RollingCircle2 -r1280,720 -pqm

# ffmpeg -i RollingCircle1.mp4 -i v1.aac output1.mp4
# ffmpeg -i RollingCircle2.mp4 -i v2.aac output2.mp4

class RollingCircle1(Scene):
    def __init__(self, **kwargs):
        self.color = WHITE
        self.r1 = 4.5/2
        self.r2 = 4.5/3
        self.rr = 4.5
        super().__init__(**kwargs)

    def construct(self):
        origin = Dot()
        self.add(origin)
        [txtO] = [MathTex(X) for X in ["O"]]
        txtO.next_to(origin, DR, buff=0.1)
        self.play(Write(txtO))
        self.wait(1)

        o2 = Dot()
        circler = Circle(radius=self.rr, color=self.color)

        circle1 = Circle(radius=self.r1, color=self.color,
                         fill_color=YELLOW, fill_opacity=0.5)
        arrow1 = Arrow(circle1.get_center(), UP*self.r1)
        g1 = VGroup(circle1, o2, arrow1)
        g1.generate_target()
        g1.target.shift(UP*self.r1)

        t1 = MathTex("r_1:r_2=2:1}").scale(1.5)
        t1.shift(UP*self.rr*2+RIGHT*(self.rr-1))

        self.play(ShowCreation(circler))
        self.wait(1)
        self.play(FadeIn(g1))
        self.wait(1)
        rarrow = Line(ORIGIN, self.rr*UP)
        self.play(ShowCreation(rarrow))
        self.play(ReplacementTransform(rarrow, t1))
        self.wait(1)
        self.play(MoveToTarget(g1))
        self.wait(1)

        def update1(group, alpha):
            # print(alpha)
            angle = math.radians(360 * alpha)
            circle = Circle(radius=self.r1, color=self.color,
                            fill_color=YELLOW, fill_opacity=0.5)
            circle.shift(UP*self.r1)

            circle.rotate(angle=angle, about_point=ORIGIN)
            dx = circle.get_center()
            arrow = Arrow(dx, dx+UP*self.r1)
            angle = math.radians(-360 * alpha * (self.rr-self.r1)/self.r1)
            arrow.rotate(angle=angle, about_point=dx)

            dot = Dot(dx)
            new_group = VGroup(circle, dot, arrow)
            group.become(new_group)
            return group

        self.play(UpdateFromAlphaFunc(g1, update1),
                  run_time=10, rate_func=double_smooth)
        self.wait(3)

        g1.generate_target()
        g1.target.shift(UP*(self.rr))
        g1.target.rotate(math.radians(180))
        trans1 = MoveToTarget(g1)
        # trans2 = Rotate(g1, angle=math.radians(180))
        self.play(trans1)
        self.wait(3)

        def update2(group, alpha):
            angle = math.radians(-360 * alpha)
            circle = Circle(radius=self.r1, color=self.color,
                            fill_color=YELLOW, fill_opacity=0.5)
            circle.shift(UP*(self.r1+self.rr))

            circle.rotate(angle=angle, about_point=ORIGIN)
            dx = circle.get_center()
            arrow = Arrow(dx, dx + DOWN*self.r1)
            angle = math.radians(-360 * alpha * (self.rr+self.r1)/self.r1)
            arrow.rotate(angle=angle, about_point=dx)

            dot = Dot(dx)
            new_group = VGroup(circle, dot, arrow)
            group.become(new_group)
            return group

        self.play(UpdateFromAlphaFunc(g1, update2),
                  run_time=10, rate_func=double_smooth)
        self.wait(2)

        t2 = MathTex("r_1:r_2=3:1}").scale(1.5)
        t2.shift(UP*self.rr*2+RIGHT*(self.rr-1))

        circle2 = Circle(radius=self.r2, color=self.color,
                         fill_color=BLUE, fill_opacity=0.5)
        dx = circler.get_center()
        arrow2 = Arrow(dx, dx+UP*self.r2)
        dot = Dot()
        g2 = VGroup(circle2, dot, arrow2)
        g2.shift(UP*(self.rr-self.r2))
        trans1 = Transform(g1, g2)
        trans2 = Transform(t1, t2)
        self.play(trans1, trans2)
        self.wait(3)
        self.remove(g1)

        def update3(group, alpha):
            angle = math.radians(360 * alpha)
            circle = Circle(radius=self.r2, color=self.color,
                            fill_color=BLUE, fill_opacity=0.5)
            circle.shift(UP*(self.rr-self.r2))

            circle.rotate(angle=angle, about_point=ORIGIN)
            dx = circle.get_center()
            arrow = Arrow(dx, dx + UP*self.r2)
            angle = math.radians(-360 * alpha * (self.rr-self.r2)/self.r2)
            arrow.rotate(angle=angle, about_point=dx)

            dot = Dot(dx)
            new_group = VGroup(circle, dot, arrow)
            group.become(new_group)
            return group

        self.play(UpdateFromAlphaFunc(g1, update3),
                  run_time=9, rate_func=double_smooth)
        self.wait(5)


class RollingCircle2(Scene):
    def __init__(self, **kwargs):
        self.color = WHITE
        self.r1 = 4.5/3
        self.r2 = 4.5
        self.txt = 3
        super().__init__(**kwargs)

    def construct(self):
        origin = Dot()
        [txtO] = [MathTex(X) for X in ["O"]]
        txtO.next_to(origin, DR, buff=0.1)

        circle_r = Circle(radius=self.r2, color=self.color)
        circle1 = Circle(radius=self.r1, color=self.color,
                         fill_color=BLUE, fill_opacity=0.5)
        arrow1 = Arrow(circle1.get_center(), UP*self.r1)
        dot1 = Dot()
        arc1 = Arc(radius=self.r2-self.r1,
                   color=BLUE, start_angle=np.deg2rad(90), angle=0)
        g1 = VGroup(dot1, circle1, arrow1, arc1)
        g1.shift(UP*(self.r2-self.r1))

        t1 = MathTex("r_1:r_2=3:1}").scale(1.5)
        t1.shift(UP*self.r2*2+RIGHT*(self.r2-1))

        t2 = MathTex("r_3=r_1-r_2").scale(1.5)
        t2.next_to(t1, DOWN, buff=0.5)

        tx3 = MathTex("r_3:r_2=2:1").scale(1.5)
        tx3.next_to(t1, DOWN, buff=0.5)

        self.play(FadeIn(circle_r), FadeIn(g1), FadeIn(origin), FadeIn(txtO))
        self.play(Write(t1))
        self.wait(3)

        def update1(group, alpha):
            angle = math.radians(360 * alpha)
            arc = Arc(radius=self.r2-self.r1,
                      color=BLUE, start_angle=np.deg2rad(90), angle=angle)
            circle = Circle(radius=self.r1, color=self.color,
                            fill_color=BLUE, fill_opacity=0.5)
            circle.shift(UP*(self.r2-self.r1))

            circle.rotate(angle=angle, about_point=ORIGIN)
            dx = circle.get_center()
            arrow = Arrow(dx, dx + UP*self.r1)
            dot = Dot(dx)
            angle = math.radians(-360 * alpha * (self.r2-self.r1)/self.r1)
            arrow.rotate(angle=angle, about_point=dx)

            ng = VGroup(dot, circle, arrow, arc)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(g1, update1),
                  run_time=8, rate_func=double_smooth)
        self.wait(1)
        radline = Line(ORIGIN, UP*(self.r2-self.r1), color=WHITE)
        self.play(ShowCreation(radline))
        trans1 = ReplacementTransform(radline, t2)
        self.play(trans1)
        self.wait(1)
        trans2 = ReplacementTransform(t2, tx3)
        self.play(trans2)
        self.wait(1)

        llen = (self.r2 - self.r1) * PI
        g1 = VGroup(circle1, arrow1, dot1)
        g1.generate_target()
        g1.target.shift(UP*llen - (self.r2-self.r1) + RIGHT*self.r1*2)
        trans1 = MoveToTarget(g1)

        track_line = Line(UP*llen, DOWN*llen,)
        trans2 = Transform(arc1, track_line)

        self.play(FadeOut(txtO), FadeOut(origin), FadeOut(circle_r))
        self.wait(1)
        self.play(trans1, trans2)
        self.wait(1)
        track_line.generate_target()
        track_line.target.shift(LEFT*self.r1)
        self.remove(arc1)
        trans1 = MoveToTarget(track_line)
        trans2 = Rotate(g1, angle=math.radians(90),
                        about_point=circle1.get_center())
        self.play(trans1, trans2)
        self.wait(3)

        def update2(group, alpha):
            angle = math.radians(-360 * alpha)
            circle = Circle(radius=self.r1, color=self.color,
                            fill_color=BLUE, fill_opacity=0.5)
            circle.shift(UP*llen + DOWN*llen*alpha*2)
            # line = DashedLine(UP*llen, UP*llen + DOWN*llen*alpha*2, color=BLUE)

            dx = circle.get_center()
            arrow = Arrow(dx, dx + LEFT*self.r1)
            dot = Dot(dx)
            angle = math.radians(-360 * alpha * (self.r2-self.r1)/self.r1)
            agr = int((360 * alpha * (self.r2-self.r1)/self.r1) % 360)
            agc = "{:.1f}".format((360*alpha*(self.r2-self.r1)/self.r1)/360)
            # agr = 0
            # agc = "0"
            # print(agr)
            ta = MathTex("angle={:d}".format(
                agr), alignment="\\raggedright").scale(1.5)
            tb = MathTex("round={:s}".format(
                agc), alignment="\\raggedright").scale(1.5)
            ta.shift(UP*self.r2*2+LEFT*self.r2)
            tb.next_to(ta, DOWN, buff=0.5)

            arrow.rotate(angle=angle, about_point=dx)

            ng = VGroup(circle, arrow, dot, ta, tb)
            # ng = VGroup(circle, arrow, dot)
            group.become(ng)
            return group

        ta = MathTex("angle=0", alignment="\\raggedright").scale(1.5)
        tb = MathTex("round=0", alignment="\\raggedright").scale(1.5)
        g1 = VGroup(circle1, arrow1, dot1, ta, tb)
        self.play(UpdateFromAlphaFunc(g1, update2),
                  run_time=5, rate_func=double_smooth)
        self.wait(2)

        g1 = VGroup(circle1, arrow1, dot1)

        equl = MathTex("=").scale(2)
        equl.move_to(UP*(self.txt))
        rnd = MathTex("round").scale(2)
        rnd.next_to(equl, LEFT)
        t2 = MathTex("s=2\\times\\pi\\times r_3").scale(2)
        t2.move_to(UP*(self.txt+1))
        t3 = MathTex("c=2\\times\\pi\\times r_2").scale(2)
        t3.move_to(UP*(self.txt-1))
        t4r = MathTex("\\frac{s}{c}").scale(2)
        t4r.next_to(equl, RIGHT)
        t4 = VGroup(rnd, equl, t4r)

        t5r = MathTex(
            "\\frac{2\\times\\pi\\times r_3}{2\\times\\pi\\times r_2}").scale(2)
        t5r.next_to(equl, RIGHT)
        t6r = MathTex("\\frac{r_3}{r_2}").scale(2)
        t6r.next_to(equl, RIGHT)
        t7r = MathTex("2").scale(2)
        t7r.next_to(equl, RIGHT)

        self.play(ReplacementTransform(track_line, t2))
        self.wait(1)
        self.play(ReplacementTransform(g1, t3))
        self.wait(2)
        g2 = VGroup(t2, t3)

        circle1 = Circle(radius=self.r1, color=self.color,
                         fill_color=BLUE, fill_opacity=0.5)
        arrow1 = Arrow(circle1.get_center(), UP*self.r1)
        dot1 = Dot()
        arc1 = Circle(radius=self.r2-self.r1, color=BLUE)
        arc1.move_to(DOWN*(self.r2-self.r1))
        g3 = VGroup(circle1, arrow1, dot1, arc1)
        g3.move_to(DOWN*3)

        self.play(ReplacementTransform(g2, t4), FadeIn(g3))
        self.wait(2)
        self.play(ReplacementTransform(t4r, t5r))
        self.wait(3)

        arrow2 = Arrow(ORIGIN, UP*(self.r2-self.r1))
        arrow2.move_to(arc1.get_center()+UP*(self.r2-self.r1)/2)

        trans1 = Indicate(arrow1, run_time=1, scale_factor=3)
        trans2 = Indicate(arrow2, run_time=1, scale_factor=2)
        trans3 = ShowPassingFlashAround(tx3, run_time=5)

        self.play(ReplacementTransform(t5r, t6r))
        self.wait(1)
        self.play(trans2)
        self.play(trans1)
        self.wait(1)

        self.play(ReplacementTransform(t6r, t7r), trans3)

        self.wait(2)


class Test(Scene):
    CONFIG = {
        "color": WHITE,
        "r1": 4.5/3,
        "r2": 4.5,
        "txt": 6
    }
    def construct(self):

        t1 = MathTex("r_1:r_2=3:1}").scale(1.5)
        t1.shift(UP*self.r2*2+RIGHT*(self.r2-1))

        t2 = MathTex("\\bigodot_1   r_1").scale(1.5)
        t2.move_to(UP*(self.txt))

        t3 = MathTex("\\bigcirc_2   r_2").scale(1.5)
        t3.next_to(t2, DOWN, buff=0.2)

        self.play(Write(t2), Write(t3))
        self.play(Write(t1))
        self.wait(3)
