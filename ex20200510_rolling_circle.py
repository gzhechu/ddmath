#!/usr/bin/env python3

from manimlib.imports import *

# manim ddmath/ex20200510_rolling_circle.py RollingCircle -pm
# manim ddmath/ex20200510_rolling_circle.py RollingCircle -pm -r1280,720


class RollingCircle(Scene):
    CONFIG = {
        "color": WHITE,
        "r1": 2,
        "r2": 4,
    }

    def construct(self):
        origin = Dot(radius=0.06)
        self.add(origin)
        [txtO] = [TexMobject(X) for X in ["O"]]
        txtO.next_to(origin, DR, buff=0.1)
        self.play(Write(txtO))
        self.wait(1)

        o2 = Dot()
        circle1 = Circle(radius=self.r1, color=self.color,
                         fill_color=YELLOW, fill_opacity=0.5)
        circle2 = Circle(radius=self.r2, color=self.color)
        arrow1 = Arrow(circle1.get_center(), UP*self.r1)

        g1 = VGroup(circle1, o2, arrow1)
        g1.generate_target()
        g1.target.shift(UP*self.r1)

        self.play(FadeIn(circle2))
        self.wait(2)
        self.play(FadeIn(g1))
        self.play(MoveToTarget(g1))
        self.wait(3)

        def update1(group, alpha):
            # print(alpha)
            angle = math.radians(360 * alpha)
            circle = Circle(radius=self.r1, color=self.color,
                            fill_color=YELLOW, fill_opacity=0.5)
            circle.shift(UP*self.r1)

            circle.rotate(angle=angle, about_point=ORIGIN)
            dx = circle.get_center()
            arrow = Arrow(dx, dx+UP*self.r1)
            angle = math.radians(-360 * alpha)
            arrow.rotate(angle=angle, about_point=dx)

            o2 = Dot(circle.get_center())
            new_group = VGroup(circle, o2, arrow)
            group.become(new_group)
            return group

        self.play(UpdateFromAlphaFunc(g1, update1),
                  run_time=10, rate_func=double_smooth)
        self.wait(3)

        circle3 = Circle(radius=self.r1, color=self.color,
                         fill_color=BLUE, fill_opacity=0.5)
        dx = circle3.get_center()
        arrow2 = Arrow(dx,
                       dx+DOWN*self.r1)
        o3 = Dot()
        g2 = VGroup(circle3, o3, arrow2)
        g2.shift(UP*(self.r1 + self.r2))
        trans1 = Transform(g1, g2)
        self.play(trans1)
        self.wait(3)
        self.remove(g1)

        def update2(group, alpha):
            # print(alpha)
            angle = math.radians(-360 * alpha)
            circle = Circle(radius=self.r1, color=self.color,
                            fill_color=BLUE, fill_opacity=0.5)
            circle.shift(UP*(self.r1+self.r2))

            circle.rotate(angle=angle, about_point=ORIGIN)
            dx = circle.get_center()
            arrow = Arrow(dx,
                          dx + DOWN*self.r1)
            angle = math.radians(-360 * alpha * 3)
            arrow.rotate(angle=angle, about_point=dx)

            o2 = Dot(circle.get_center())
            new_group = VGroup(circle, o2, arrow)
            group.become(new_group)
            return group

        self.play(UpdateFromAlphaFunc(g1, update2),
                  run_time=10, rate_func=double_smooth)
        self.wait(6)


class Test(Scene):
    def construct(self):
        square = Square()
        square.generate_target()
        square.target.shift(2*UP)
        # anno = TextMobject("Move to target")
        # anno.shift(2 * DOWN)
        self.add(square)
        self.play(MoveToTarget(square))
