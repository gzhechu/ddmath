#!/usr/bin/env python3

from manimlib.imports import *

# manim ddmath/ex20200510_rolling_circle.py RollingCircle1 -pm
# manim ddmath/ex20200510_rolling_circle.py RollingCircle1 -pm -r1280,720


class RollingCircle1(Scene):
    CONFIG = {
        "color": WHITE,
        "r1": 4.5/2,
        "r2": 4.5/3,
        "rr": 4.5,
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

        t1 = TexMobject("R_1:R_2=2:1}").scale(1.5)
        t1.shift(UP*self.rr*2+RIGHT*(self.rr-1))

        self.play(FadeIn(circler), Write(t1))
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

        t2 = TexMobject("R_1:R_2=3:1}").scale(1.5)
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
                  run_time=10, rate_func=double_smooth)
        self.wait(6)


class RollingCircle2(Scene):
    CONFIG = {
        "color": WHITE,
        "r1": 4.5/3,
        "r2": 4.5,
    }

    def construct(self):
        origin = Dot()
        [txtO] = [TexMobject(X) for X in ["O"]]
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

        t1 = TexMobject("R_1:R_2=3:1}").scale(1.5)
        t1.shift(UP*self.r2*2+RIGHT*(self.r2-1))

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
                  run_time=10, rate_func=double_smooth)
        self.wait(1)

        llen = (self.r2 - self.r1) * PI
        g1 = VGroup(circle1, arrow1, dot1)
        g1.generate_target()
        g1.target.shift(UP*llen - (self.r2-self.r1) + RIGHT*self.r1*2)
        trans1 = MoveToTarget(g1)

        linex = Line(DOWN*llen, UP*llen)
        trans2 = Transform(arc1, linex)

        self.play(FadeOut(txtO), FadeOut(origin), FadeOut(circle_r))
        self.wait(1)
        self.play(trans1, trans2)
        self.wait(1)
        linex.generate_target()
        linex.target.shift(LEFT*self.r1)
        self.remove(arc1)
        trans1 = MoveToTarget(linex)
        trans2 = Rotate(g1, angle=math.radians(90),
                        about_point=circle1.get_center())
        self.play(trans1, trans2)
        self.wait(1)

        def update2(group, alpha):
            angle = math.radians(-360 * alpha)
            circle = Circle(radius=self.r1, color=self.color,
                            fill_color=BLUE, fill_opacity=0.5)
            circle.shift(UP*llen + DOWN*llen*alpha*2)
            line = DashedLine(UP*llen, UP*llen + DOWN*llen*alpha*2, color=BLUE)

            dx = circle.get_center()
            arrow = Arrow(dx, dx + LEFT*self.r1)
            dot1 = Dot(dx)
            angle = math.radians(-360 * alpha * (self.r2-self.r1)/self.r1)
            agr = int((360 * alpha * (self.r2-self.r1)/self.r1) % 360)
            agc = "{:.1f}".format((360*alpha*(self.r2-self.r1)/self.r1)/360)
            agr = 0
            agc = "0"
            # print(agr)
            ta = TextMobject("角度={:d}".format(
                agr), alignment="\\raggedright").scale(1.5)
            tb = TextMobject("圈数={:s}".format(
                agc), alignment="\\raggedright").scale(1.5)
            ta.shift(UP*self.r2*2+LEFT*self.r2)
            tb.next_to(ta, DOWN)

            arrow.rotate(angle=angle, about_point=dx)

            ng = VGroup(circle, arrow, dot1, ta, tb, line)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(g1, update2),
                  run_time=10, rate_func=double_smooth)
        self.wait(6)


class Test(Scene):
    def construct(self):
        a = VGroup()
        a.foo = Circle()
        a.bar = Rectangle()
        a.digest_mobject_attrs()
        a.print_family()
        print(id(a.foo), id(a.bar))
        self.add(a)
        self.wait()

        a.generate_target()
        a.target.remove(a.target.foo)
        a.target.print_family()
        print(id(a.target.foo), id(a.target.bar))

        self.play(MoveToTarget(a))
        self.wait()

        # textHuge = TextMobject("{\\Huge Huge Text 012}")
        # texthuge = TextMobject("{\\huge huge Text 012.\\#!?} Text")
        # textLARGE = TextMobject("{\\LARGE LARGE Text 012.\\#!?} Text")
        # textLarge = TextMobject("{\\Large Large Text 012.\\#!?} Text")
        # textlarge = TextMobject("{\\large large Text 012.\\#!?} Text")
        # textNormal = TextMobject("{\\normalsize normal Text 012.\\#!?} Text")
        # textsmall = TextMobject("{\\small small Text 012.\\#!?} Texto normal")
        # textfootnotesize = TextMobject(
        #     "{\\footnotesize footnotesize Text 012.\\#!?} Text")
        # textscriptsize = TextMobject(
        #     "{\\scriptsize scriptsize Text 012.\\#!?} Text")
        # texttiny = TextMobject("{\\tiny tiny Texto 012.\\#!?} Text normal")
        # textHuge.to_edge(UP)
        # texthuge.next_to(textHuge, DOWN, buff=0.1)
        # textLARGE.next_to(texthuge, DOWN, buff=0.1)
        # textLarge.next_to(textLARGE, DOWN, buff=0.1)
        # textlarge.next_to(textLarge, DOWN, buff=0.1)
        # textNormal.next_to(textlarge, DOWN, buff=0.1)
        # textsmall.next_to(textNormal, DOWN, buff=0.1)
        # textfootnotesize.next_to(textsmall, DOWN, buff=0.1)
        # textscriptsize.next_to(textfootnotesize, DOWN, buff=0.1)
        # texttiny.next_to(textscriptsize, DOWN, buff=0.1)
        # self.add(textHuge, texthuge, textLARGE, textLarge, textlarge,
        #          textNormal, textsmall, textfootnotesize, textscriptsize, texttiny)
        # self.wait(3)
