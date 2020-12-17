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
        ball_radius = 0.3
        a = 1
        alpha = 1
        def func(x): return 2*np.exp(-2*(x-a*alpha)**2)
        def ball_function_path(x): return 2 * \
            np.exp(-2*(x-a*alpha)**2)+ball_radius

        func_graph = FunctionGraph(func)
        ball_path = FunctionGraph(ball_function_path)
        ball = Dot(radius=ball_radius)
        ball.move_to(ball_path.points[0])

        self.play(ShowCreation(func_graph), GrowFromCenter(ball))
        self.play(
            MoveAlongPath(ball, ball_path),
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
                            Rectangle(height=0.5, width=0.5,
                                      color=PALETTE[j*7+i], fill_opacity=1)
                            for i in range(8)]
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


class Cuboid(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70*DEGREES, theta=30*DEGREES)
        p = Prism(dimensions=[5, 3, 6], stroke_width=2, fill_opacity=0.5)
        self.add(p)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(6)
        self.stop_ambient_camera_rotation()


class SurfacesAnimation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        cylinder = ParametricSurface(
            lambda u, v: np.array([
                np.cos(TAU * v),
                np.sin(TAU * v),
                2 * (1 - u)
            ]),
            resolution=(6, 32)).fade(0.5)  # Resolution of the surfaces

        paraboloid = ParametricSurface(
            lambda u, v: np.array([
                np.cos(v) * u,
                np.sin(v) * u,
                u ** 2
            ]), v_max=TAU,
            checkerboard_colors=[PURPLE_D, PURPLE_E],
            resolution=(10, 32)).scale(2)

        para_hyp = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2-v**2
            ]), v_min=-2, v_max=2, u_min=-2, u_max=2, checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(15, 32)).scale(1)

        cone = ParametricSurface(
            lambda u, v: np.array([
                u * np.cos(v),
                u * np.sin(v),
                u
            ]), v_min=0, v_max=TAU, u_min=-2, u_max=2, checkerboard_colors=[GREEN_D, GREEN_E],
            resolution=(15, 32)).scale(1)

        hip_one_side = ParametricSurface(
            lambda u, v: np.array([
                np.cosh(u) * np.cos(v),
                np.cosh(u) * np.sin(v),
                np.sinh(u)
            ]), v_min=0, v_max=TAU, u_min=-2, u_max=2, checkerboard_colors=[YELLOW_D, YELLOW_E],
            resolution=(15, 32))

        ellipsoid = ParametricSurface(
            lambda u, v: np.array([
                1 * np.cos(u) * np.cos(v),
                2 * np.cos(u) * np.sin(v),
                0.5 * np.sin(u)
            ]), v_min=0, v_max=TAU, u_min=-PI/2, u_max=PI/2, checkerboard_colors=[TEAL_D, TEAL_E],
            resolution=(15, 32)).scale(2)

        sphere = ParametricSurface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]), v_min=0, v_max=TAU, u_min=-PI/2, u_max=PI/2, checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)

        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)

        self.add(axes)
        self.play(Write(sphere))
        self.wait()
        self.play(ReplacementTransform(sphere, ellipsoid))
        self.wait()
        self.play(ReplacementTransform(ellipsoid, cone))
        self.wait()
        self.play(ReplacementTransform(cone, hip_one_side))
        self.wait()
        self.play(ReplacementTransform(hip_one_side, para_hyp))
        self.wait()
        self.play(ReplacementTransform(para_hyp, paraboloid))
        self.wait()
        self.play(ReplacementTransform(paraboloid, cylinder))
        self.wait()
        self.play(FadeOut(cylinder))
        self.wait(3)
