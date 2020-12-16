#!/usr/bin/env python3

from manimlib.imports import *

# manim ddmath/test.py Test -pm
# manim ddmath/ex20200510_rolling_circle.py RollingCircle1 -pm -r1280,720


class AnimationGrowFromEdge(Scene):
    def construct(self):
        for label, edge in zip(
            ["LEFT", "RIGHT", "UP", "DOWN"], [LEFT, RIGHT, UP, DOWN]):
            anno = TextMobject(f"Grow from {label} edge")
            anno.shift(2 * DOWN)
            self.add(anno)
            square = Square()
            self.play(GrowFromEdge(square, edge))
            self.remove(anno, square)


class RollingBall(Scene):
    def construct(self):
        ball_radius=0.3
        a=1
        alpha=1
        func=lambda x: 2*np.exp(-2*(x-a*alpha)**2)
        ball_function_path=lambda x: 2*np.exp(-2*(x-a*alpha)**2)+ball_radius

        func_graph=FunctionGraph(func)
        ball_path=FunctionGraph(ball_function_path)
        ball=Dot(radius=ball_radius)
        ball.move_to(ball_path.points[0])

        self.play(ShowCreation(func_graph),GrowFromCenter(ball))
        self.play(
            MoveAlongPath(ball,ball_path),
            run_time=5,
            rate_func=linear
        )
        self.wait()

class AllColor(Scene):
    def construct(self):
        self.add(
            VGroup(
                *[
                    VGroup(
                        *[
                            # Text(list(COLOR_MAP.keys())[j*7+i]).set_color(PALETTE[j*7+i]).scale(0.6)
                            Rectangle(height=0.5, width=0.5, color=PALETTE[j*7+i], fill_opacity=1)
                            for i in range(8)                        ]
                    ).arrange_submobjects(RIGHT)
                    for j in range(7)
                ]
            ).arrange_submobjects(DOWN)
        )
        self.wait(5)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
        self.wait(5)