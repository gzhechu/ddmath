#!/usr/bin/env python3

from manimlib.imports import *

# manim ddmath/ex20200510_rolling_circle.py RollingCircle1 -pm
# manim ddmath/ex20200510_rolling_circle.py RollingCircle1 -pm -r1280,720


class RollingCircle1(Scene):
    CONFIG = {
        "color": WHITE,
        "r1": 2,
        "r2": 4/3,
        "rr": 4,
    }

    def construct(self):
        origin = Dot()
        self.add(origin)
        [txtO] = [TexMobject(X) for X in ["O"]]
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

        self.play(FadeIn(circler))
        self.wait(1)
        self.play(FadeIn(g1))
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

            o2 = Dot(circle.get_center())
            new_group = VGroup(circle, o2, arrow)
            group.become(new_group)
            return group

        self.play(UpdateFromAlphaFunc(g1, update1),
                  run_time=10, rate_func=double_smooth)
        self.wait(3)

        circle1 = Circle(radius=self.r1, color=self.color,
                         fill_color=YELLOW, fill_opacity=0.5)
        dx = circle1.get_center()
        arrow2 = Arrow(dx, dx+DOWN*self.r1)
        o3 = Dot()
        g2 = VGroup(circle1, o3, arrow2)
        g2.shift(UP*(self.r1 + self.rr))
        trans1 = Transform(g1, g2)
        self.play(trans1)
        self.wait(3)
        self.remove(g2)

        def update2(group, alpha):
            # print(alpha)
            angle = math.radians(-360 * alpha)
            circle = Circle(radius=self.r1, color=self.color,
                            fill_color=YELLOW, fill_opacity=0.5)
            circle.shift(UP*(self.r1+self.rr))

            circle.rotate(angle=angle, about_point=ORIGIN)
            dx = circle.get_center()
            arrow = Arrow(dx, dx + DOWN*self.r1)
            angle = math.radians(-360 * alpha * (self.rr+self.r1)/self.r1)
            arrow.rotate(angle=angle, about_point=dx)

            o2 = Dot(circle.get_center())
            new_group = VGroup(circle, o2, arrow)
            group.become(new_group)
            return group

        self.play(UpdateFromAlphaFunc(g1, update2),
                  run_time=10, rate_func=double_smooth)
        self.wait(2)

        circle2 = Circle(radius=self.r2, color=self.color,
                         fill_color=BLUE, fill_opacity=0.5)
        dx = circler.get_center()
        arrow2 = Arrow(dx, dx+DOWN*self.r2)
        o3 = Dot()
        g2 = VGroup(circle2, o3, arrow2)
        g2.shift(UP*(self.r2 + self.rr))
        trans1 = Transform(g1, g2)
        self.play(trans1)
        self.wait(3)
        self.remove(g2)

        def update3(group, alpha):
            # print(alpha)
            angle = math.radians(-360 * alpha)
            circle = Circle(radius=self.r2, color=self.color,
                            fill_color=BLUE, fill_opacity=0.5)
            circle.shift(UP*(self.r2+self.rr))

            circle.rotate(angle=angle, about_point=ORIGIN)
            dx = circle.get_center()
            arrow = Arrow(dx, dx + DOWN*self.r2)
            angle = math.radians(-360 * alpha * (self.r2+self.rr)/self.r2)
            arrow.rotate(angle=angle, about_point=dx)

            o2 = Dot(circle.get_center())
            new_group = VGroup(circle, o2, arrow)
            group.become(new_group)
            return group

        self.play(UpdateFromAlphaFunc(g1, update3),
                  run_time=10, rate_func=double_smooth)
        self.wait(6)


class RollingCircle2(Scene):
    CONFIG = {
        "color": WHITE,
        "r1": 4/3,
        "r2": 4,
        "r3": 0.7,
        "r4": 2.1,
    }

    def construct(self):
        origin = Dot()
        [txtO] = [TexMobject(X) for X in ["O"]]
        txtO.next_to(origin, DR, buff=0.1)
        # self.add(origin, txtO)
        self.play(FadeIn(origin), FadeIn(txtO))
        self.wait(1)

        circle1 = Circle(radius=self.r1, color=self.color,
                         fill_color=BLUE, fill_opacity=0.5)
        circle2 = Circle(radius=self.r2, color=self.color)
        arrow = Arrow(UP*self.r1, DOWN*self.r1)

        g1 = VGroup(circle1, arrow)
        g1.shift(UP*(self.r1+self.r2))
        # self.add(circle2, g1)
        self.play(FadeIn(circle2), FadeIn(g1))
        self.wait(1)

        t1 = TexMobject("r1:r2 = 1:3")
        t1.shift(UP*self.r2*2+RIGHT*self.r2)
        self.play(Write(t1))

        def update1(group, alpha):
            # print(alpha)
            angle = math.radians(-360 * alpha)
            circle = Circle(radius=self.r1, color=self.color,
                            fill_color=BLUE, fill_opacity=0.5)
            circle.shift(UP*(self.r1+self.r2))

            circle.rotate(angle=angle, about_point=ORIGIN)
            dx = circle.get_center()
            arrow = Arrow(dx+UP*self.r1, dx + DOWN*self.r1)
            angle = math.radians(-360 * alpha * (self.r1+self.r2)/self.r1)
            arrow.rotate(angle=angle, about_point=dx)

            new_group = VGroup(circle, arrow)
            group.become(new_group)
            return group

        self.play(UpdateFromAlphaFunc(g1, update1),
                  run_time=10, rate_func=double_smooth)
        self.wait(1)

        circle3 = Circle(radius=self.r3, color=self.color,
                         fill_color=BLUE, fill_opacity=0.5)
        circle4 = Circle(radius=self.r4, color=self.color)
        arrow = Arrow(UP*self.r3, DOWN*self.r3)
        g2 = VGroup(circle3, arrow)
        g2.shift(UP*(self.r3+self.r4))

        trans1 = Transform(g1, g2)
        trans2 = Transform(circle2, circle4)
        self.play(trans1, trans2)
        self.wait(3)

        circle5 = Circle(radius=self.r3+self.r4, color=BLUE,
                         fill_color=BLUE, fill_opacity=0)
        circle5.rotate(angle=math.radians(90))
        self.play(ShowCreation(circle5))
        self.wait(3)

        llen = (self.r3 + self.r4) * PI

        circle6 = Circle(radius=self.r3, color=self.color,
                         fill_color=BLUE, fill_opacity=0.5)
        arrow = Arrow(RIGHT*self.r3, LEFT*self.r3)
        g3 = VGroup(circle6, arrow)
        g3.shift(UP*llen)

        line1 = Line(DOWN*llen, UP*llen)
        line1.shift(LEFT*self.r3)
        trans1 = Transform(circle5, line1)
        trans2 = Transform(g2, g3)
        self.play(FadeOut(txtO), FadeOut(origin),
                  FadeOut(circle2))
        self.wait(1)
        self.remove(g1)
        self.play(trans1, trans2)
        self.wait(1)

        def update2(group, alpha):
            # print(alpha)
            llen = (self.r3 + self.r4) * PI * 2
            angle = math.radians(-360 * alpha)
            circle = Circle(radius=self.r3, color=self.color,
                            fill_color=BLUE, fill_opacity=0.5)
            circle.shift(UP*llen/2 + DOWN*llen*alpha)

            dx = circle.get_center()
            arrow = Arrow(dx + RIGHT*self.r3, dx + LEFT*self.r3)
            angle = math.radians(-360 * alpha * (self.r3+self.r4)/self.r3)
            ags = int((360 * alpha * (self.r3+self.r4)/self.r3) % 360)
            ta = TexMobject("angle={:d}".format(ags))
            ta.shift(UP*self.r2*2+LEFT*self.r2)
            # print(ags)

            arrow.rotate(angle=angle, about_point=dx)

            new_group = VGroup(circle, arrow, ta)
            group.become(new_group)
            return group

        self.remove(g2)
        self.play(UpdateFromAlphaFunc(g1, update2),
                  run_time=10, rate_func=double_smooth)
        self.wait(6)

class RollingCircle3(Scene):
    CONFIG = {
        "color": WHITE,
        "r1": 4/3,
        "r2": 4,
    }

    def construct(self):
        origin = Dot()
        [txtO] = [TexMobject(X) for X in ["O"]]
        txtO.next_to(origin, DR, buff=0.1)
        self.play(FadeIn(origin), FadeIn(txtO))
        self.wait(1)

        circle1 = Circle(radius=self.r1, color=self.color,
                         fill_color=BLUE, fill_opacity=0.5)
        circle2 = Circle(radius=self.r2, color=self.color)
        arrow = Arrow(circle1.get_center(), UP*self.r1)
        dot1 = Dot()

        g1 = VGroup(circle1, arrow, dot1)
        g1.shift(UP*(self.r2-self.r1))
        self.play(FadeIn(circle2), FadeIn(g1))
        self.wait(1)

        t1 = TexMobject("{\\LARGE r1:r2 = 1:3}")
        t1.shift(UP*self.r2*2+RIGHT*self.r2)
        self.play(Write(t1))

        def update1(group, alpha):
            # print(alpha)
            angle = math.radians(360 * alpha)
            circle = Circle(radius=self.r1, color=self.color,
                            fill_color=BLUE, fill_opacity=0.5)
            circle.shift(UP*(self.r2-self.r1))

            circle.rotate(angle=angle, about_point=ORIGIN)
            dx = circle.get_center()
            arrow = Arrow(dx, dx + UP*self.r1)
            dot1 = Dot(dx)
            angle = math.radians(-360 * alpha * (self.r2-self.r1)/self.r1)
            arrow.rotate(angle=angle, about_point=dx)

            new_group = VGroup(circle, arrow, dot1)
            group.become(new_group)
            return group

        self.play(UpdateFromAlphaFunc(g1, update1),
                  run_time=10, rate_func=double_smooth)
        self.wait(1)

        circle5 = Circle(radius=self.r2-self.r1, color=BLUE,
                         fill_color=BLUE, fill_opacity=0)
        circle5.rotate(angle=math.radians(90))
        self.play(ShowCreation(circle5))
        self.wait(3)

        llen = (self.r2 - self.r1) * PI

        circle6 = Circle(radius=self.r1, color=self.color,
                         fill_color=BLUE, fill_opacity=0.5)
        dot1 = Dot(circle6.get_center())
        arrow = Arrow(circle6.get_center(), LEFT*self.r1)
        g3 = VGroup(circle6, arrow, dot1)
        g3.shift(UP*llen)

        line1 = Line(DOWN*llen, UP*llen)
        line1.shift(LEFT*self.r1)
        trans1 = Transform(circle5, line1)
        trans2 = Transform(g1, g3)

        self.play(FadeOut(txtO), FadeOut(origin),
                  FadeOut(circle2))
        self.wait(1)
        self.remove(g1)
        self.play(trans1, trans2)
        self.wait(1)

        def update2(group, alpha):
            # print(alpha)
            llen = (self.r2 - self.r1) * PI * 2
            angle = math.radians(-360 * alpha)
            circle = Circle(radius=self.r1, color=self.color,
                            fill_color=BLUE, fill_opacity=0.5)
            circle.shift(UP*llen/2 + DOWN*llen*alpha)

            dx = circle.get_center()
            arrow = Arrow(dx, dx + LEFT*self.r1)
            dot1 = Dot(dx)
            angle = math.radians(-360 * alpha * (self.r2-self.r1)/self.r1)
            agr = int((360 * alpha * (self.r2-self.r1)/self.r1) % 360)
            agc = "{:.1f}".format((360 * alpha * (self.r2-self.r1)/self.r1) / 360)
            # agr = 0
            # agc = "0"
            # print(agr)
            ta = TexMobject("angle={:d}".format(agr))
            tb = TexMobject("round={:s}".format(agc))
            ta.shift(UP*self.r2*2+LEFT*self.r2)
            tb.next_to(ta,DOWN)

            arrow.rotate(angle=angle, about_point=dx)

            new_group = VGroup(circle, arrow, dot1, ta, tb)
            group.become(new_group)
            return group

        # self.remove(g2)
        self.play(UpdateFromAlphaFunc(g1, update2),
                  run_time=10, rate_func=double_smooth)
        self.wait(6)


class Test(Scene):
    def construct(self):
        textHuge = TextMobject("{\\Huge Huge Text 012}")
        texthuge = TextMobject("{\\huge huge Text 012.\\#!?} Text")
        textLARGE = TextMobject("{\\LARGE LARGE Text 012.\\#!?} Text")
        textLarge = TextMobject("{\\Large Large Text 012.\\#!?} Text")
        textlarge = TextMobject("{\\large large Text 012.\\#!?} Text")
        textNormal = TextMobject("{\\normalsize normal Text 012.\\#!?} Text")
        textsmall = TextMobject("{\\small small Text 012.\\#!?} Texto normal")
        textfootnotesize = TextMobject("{\\footnotesize footnotesize Text 012.\\#!?} Text")
        textscriptsize = TextMobject("{\\scriptsize scriptsize Text 012.\\#!?} Text")
        texttiny = TextMobject("{\\tiny tiny Texto 012.\\#!?} Text normal")
        textHuge.to_edge(UP)
        texthuge.next_to(textHuge,DOWN,buff=0.1)
        textLARGE.next_to(texthuge,DOWN,buff=0.1)
        textLarge.next_to(textLARGE,DOWN,buff=0.1)
        textlarge.next_to(textLarge,DOWN,buff=0.1)
        textNormal.next_to(textlarge,DOWN,buff=0.1)
        textsmall.next_to(textNormal,DOWN,buff=0.1)
        textfootnotesize.next_to(textsmall,DOWN,buff=0.1)
        textscriptsize.next_to(textfootnotesize,DOWN,buff=0.1)
        texttiny.next_to(textscriptsize,DOWN,buff=0.1)
        self.add(textHuge,texthuge,textLARGE,textLarge,textlarge,textNormal,textsmall,textfootnotesize,textscriptsize,texttiny)
        self.wait(3)
