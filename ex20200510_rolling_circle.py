#!/usr/bin/env python3

from manimlib.imports import *

# manim ddmath/ex20200510_rolling_circle.py RollingCircle -pm
# manim ddmath/ex20200510_rolling_circle.py RollingCircle -pm -r1280,720


class RollingCircle1(Scene):
    CONFIG = {
        "color": WHITE,
        "r1": 2,
        "r2": 4/3,
        "rr": 4,
    }

    def construct(self):
        origin = Dot(radius=0.06)
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
        origin = Dot(radius=0.06)
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
            ags = int(360 * alpha * (self.r3+self.r4)/self.r3)
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


class Test(Scene):
    def construct(self):
        square = Square()
        anno = TextMobject("Uncreate")
        anno.shift(2*DOWN)
        self.add(anno)
        self.add(square)
        self.play(Uncreate(square))
