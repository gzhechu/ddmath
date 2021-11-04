#!/usr/bin/env python3

from manimlib import *
# from manim import *

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
                np.cos(v) * u, np.sin(v) * u,
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


class AnimationGroupExample(Scene):
    def construct(self):
        dots = VGroup(*[Dot() for _ in range(10)])
        dots.arrange(RIGHT, buff=0.8)
        self.add(dots)

        def dot_func(mob):
            mob.scale(3)
            mob.set_color(RED)
            return mob

        self.play(
            # Replace AnimationGroup with LaggedStart
            LaggedStart(
                *[
                    ApplyFunction(
                        dot_func,
                        dot,
                        rate_func=there_and_back
                    )
                    for dot in dots
                ]
            )
        )
        self.wait(2)


class AnimationGroupExampleFail(Scene):
    def construct(self):
        dots = VGroup(*[Dot() for _ in range(10)])
        dots.arrange(RIGHT, buff=0.8)
        self.add(dots)

        ag = AnimationGroup(*[Indicate(o, scale_factor=2)
                              for o in dots], lag_ratio=0.2)
        # for dot in dots:
        #     self.play(
        #         dot.scale,3,
        #         dot.set_color,RED,
        #         rate_func=there_and_back
        #     )
        self.play(ag, run_time=5)
        self.wait(2)


# try:
#     import sys
#     sys.path.append(os.path.dirname(os.path.realpath(__file__)))
#     from utils import Measurement
# except:
#     pass

class Dimensioning(VGroup):
    def __init__(self, start=LEFT, end=RIGHT, buff=-0.5,
                 dashed=False, stroke=2.4, color=WHITE, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.side = 0.3
        self.dashed = dashed
        self.buff = buff
        self.stroke = stroke
        self.color = color
        self.label_margin = 0.0
        self.arrow_angle = 18*DEGREES
        self.arrow_length = 0.25

        reference_line = Line(start, end)
        self.reference_line = reference_line

        if self.dashed:
            self.start_dim = DashedLine(reference_line.get_length() * LEFT/2,
                                        reference_line.get_length() * RIGHT/2, **kwargs)
        else:
            self.start_dim = Line(reference_line.get_length() * LEFT/2,
                                  reference_line.get_length() * RIGHT/2, **kwargs)
        self.end_dim = None
        pre_medicion = Line(ORIGIN, self.side *
                            RIGHT).rotate(PI/2).set_stroke(None, self.stroke)
        pos_medicion = pre_medicion.copy()
        pre_medicion.move_to(self.start_dim.get_start())
        pos_medicion.move_to(self.start_dim.get_end())

        self.start_dim.set_stroke(width=self.stroke).set_color(self.color)
        pre_medicion.set_stroke(width=self.stroke).set_color(self.color)
        pos_medicion.set_stroke(width=self.stroke).set_color(self.color)

        self.add(pre_medicion, self.start_dim, pos_medicion)
        angle = reference_line.get_angle()

        matrix_rotation = rotation_matrix(PI/2, OUT)
        vector_unitary = reference_line.get_unit_vector()
        direction = np.matmul(matrix_rotation, vector_unitary)
        self.direction = direction
        self.rotate(angle)
        self.move_to(reference_line)
        self.shift(direction*self.buff)

    def add_tex(self, text, invert=False, scale=1, margin=0.1, **kwargs):
        reference_line = self.reference_line
        texto = MathTex(text, **kwargs)
        if invert:
            texto.rotate(PI)

        self.label_margin = margin
        tex_margen = texto.get_width() / 2 + self.label_margin

        if self.dashed:
            start_dim = DashedLine(reference_line.get_length() * LEFT / 2,
                                   ORIGIN + LEFT * tex_margen, **kwargs)
            end_dim = DashedLine(ORIGIN + RIGHT * tex_margen,
                                 reference_line.get_length() * RIGHT / 2, **kwargs)
        else:
            start_dim = Line(reference_line.get_length() * LEFT/2,
                             ORIGIN + LEFT * tex_margen, **kwargs)
            end_dim = Line(ORIGIN + RIGHT * tex_margen,
                           reference_line.get_length() * RIGHT/2, **kwargs)
        self.remove(self.start_dim, self.end_dim)

        start_dim.set_stroke(width=self.stroke).set_color(self.color)
        end_dim.set_stroke(width=self.stroke).set_color(self.color)

        self.start_dim = start_dim
        self.end_dim = end_dim

        angle = reference_line.get_angle()
        vg = VGroup(self.start_dim, texto, self.end_dim)
        vg.rotate(angle)
        vg.move_to(reference_line)
        vg.shift(self.direction*self.buff)
        self.add(vg)

        return self

    def add_tips(self):
        single_vector = self.reference_line.get_unit_vector()

        point_final1 = self.reference_line.get_end()
        point_initial1 = point_final1-single_vector*self.arrow_length

        point_initial2 = self.reference_line.get_start()
        point_final2 = point_initial2+single_vector*self.arrow_length

        lin1_1 = Line(point_initial1, point_final1).set_color(
            self[0].get_color()).set_stroke(None, self.stroke)
        lin1_2 = lin1_1.copy()
        lin2_1 = Line(point_initial2, point_final2).set_color(
            self[0].get_color()).set_stroke(None, self.stroke)
        lin2_2 = lin2_1.copy()

        lin1_1.rotate(self.arrow_angle, about_point=point_final1,
                      about_edge=point_final1)
        lin1_2.rotate(-self.arrow_angle, about_point=point_final1,
                      about_edge=point_final1)

        lin2_1.rotate(self.arrow_angle, about_point=point_initial2,
                      about_edge=point_initial2)
        lin2_2.rotate(-self.arrow_angle, about_point=point_initial2,
                      about_edge=point_initial2)

        vg = VGroup(lin1_1, lin1_2, lin2_1, lin2_2)
        vg.shift(self.direction*self.buff)
        return self.add(vg)

    def add_letter(self, texto, scale=1, buff=0.1, **kwargs):
        line_reference = self.line_reference
        texto = TexMobject(texto, **kwargs).scale(scale).move_to(self)
        width = texto.get_height()/2
        # texto.shift(self.direction*(buff+1)*width)
        return self.add(texto)


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()                    # create a circle
        circle.set_fill(PINK, opacity=0.5)   # set color and transparency

        square = Square(4)                    # create a square
        square.rotate(-3 * TAU / 8)          # rotate a certain amount

        ptA = square.get_corner(UL)
        ptB = square.get_corner(UR)
        ptC = ORIGIN + RIGHT * 5

        # me = Measurement(Line(ptA, ptB), invert=True, dashed=True,
        #                  buff=-0.5).add_tips().add_tex("a", buff=3, color=WHITE)

        self.add(Dot(ptA), Dot(ptC), Dot(ORIGIN))
        # self.add(Line(ptB, ORIGIN))
        me = Dimensioning(ptA, ORIGIN, dashed=False, margin=-0.5)
        mf = Dimensioning(ORIGIN, ptB, color=RED).add_tips().add_tex(
            "abc", color=BLUE)
        mg = Dimensioning(ORIGIN, ptC).add_tips().add_tex("abcxyz", color=RED)

        # animate the creation of the square
        # self.play(ShowCreation(square))
        self.play(ShowCreation(me), run_time=3)
        self.play(Write(mf), run_time=3)
        self.play(ShowCreation(mg), run_time=3)
        self.wait(3)
        # interpolate the square into the circle
        # self.play(Transform(square, circle))
        # self.play(FadeOut(square))           # fade out animation

        self.wait(5)


class IsolateText(Scene):
    def construct(self):
        isolate_tex = ["x", "y", "3", "="]
        t1 = Tex("x+y=3", isolate=isolate_tex)
        t2 = Tex("x=3-y", isolate=isolate_tex)
        t3 = Tex("x=3-y", isolate=isolate_tex)
        t4 = Tex("x+y=3", isolate=isolate_tex)
        VGroup(t1, t2, t3, t4).scale(3)
        t1.shift(UP * 1)
        t2.shift(UP * 1)
        t2.align_to(t1, LEFT)
        t3.shift(DOWN * 1)
        t4.shift(DOWN * 1)
        t4.align_to(t3, LEFT)

        self.add(t1, t3)
        self.wait()
        self.play(TransformMatchingTex(t1, t2,
                                       key_map={"+": "-"}
                                       ),
                  TransformMatchingTex(t3, t4,
                                       #  key_map={"+": "-"}
                                       ),
                  run_time=5)
        self.wait(3)
