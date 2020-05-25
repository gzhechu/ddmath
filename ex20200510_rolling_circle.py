#!/usr/bin/env python3

from manimlib.imports import *
# from addons import Measurement
# import addons

# manim ddmath/ex20200510_rolling_circle.py RollingCircle1 -r1280,720 -pm
# manim ddmath/ex20200510_rolling_circle.py RollingCircle1 -r1280,720 -pm


class Measurement(VGroup):
    CONFIG = {
        "color": RED_B,
        "buff": 0.3,
        "laterales": 0.3,
        "invert": False,
        "dashed_segment_length": 0.09,
        "dashed": False,
        "con_flechas": True,
        "ang_flechas": 30*DEGREES,
        "tam_flechas": 0.2,
        "stroke": 2.4
    }

    def __init__(self, objeto, **kwargs):
        VGroup.__init__(self, **kwargs)
        if self.dashed == True:
            medicion = DashedLine(ORIGIN, objeto.get_length(
            )*RIGHT, dashed_segment_length=self.dashed_segment_length).set_color(self.color)
        else:
            medicion = Line(ORIGIN, objeto.get_length()*RIGHT)

        medicion.set_stroke(None, self.stroke)

        pre_medicion = Line(ORIGIN, self.laterales *
                            RIGHT).rotate(PI/2).set_stroke(None, self.stroke)
        pos_medicion = pre_medicion.copy()

        pre_medicion.move_to(medicion.get_start())
        pos_medicion.move_to(medicion.get_end())

        angulo = objeto.get_angle()
        matriz_rotacion = rotation_matrix(PI/2, OUT)
        vector_unitario = objeto.get_unit_vector()
        direction = np.matmul(matriz_rotacion, vector_unitario)
        self.direction = direction

        self.add(medicion, pre_medicion, pos_medicion)
        self.rotate(angulo)
        self.move_to(objeto)

        if self.invert == True:
            self.shift(-direction*self.buff)
        else:
            self.shift(direction*self.buff)
        self.set_color(self.color)
        self.tip_point_index = -np.argmin(self.get_all_points()[-1, :])

    def add_tips(self):
        line_reference = Line(self[0][0].get_start(), self[0][-1].get_end())
        vector_unitario = line_reference.get_unit_vector()

        punto_final1 = self[0][-1].get_end()
        punto_inicial1 = punto_final1-vector_unitario*self.tam_flechas

        punto_inicial2 = self[0][0].get_start()
        punto_final2 = punto_inicial2+vector_unitario*self.tam_flechas

        lin1_1 = Line(punto_inicial1, punto_final1).set_color(
            self[0].get_color()).set_stroke(None, self.stroke)
        lin1_2 = lin1_1.copy()
        lin2_1 = Line(punto_inicial2, punto_final2).set_color(
            self[0].get_color()).set_stroke(None, self.stroke)
        lin2_2 = lin2_1.copy()

        lin1_1.rotate(self.ang_flechas, about_point=punto_final1,
                      about_edge=punto_final1)
        lin1_2.rotate(-self.ang_flechas, about_point=punto_final1,
                      about_edge=punto_final1)

        lin2_1.rotate(self.ang_flechas, about_point=punto_inicial2,
                      about_edge=punto_inicial2)
        lin2_2.rotate(-self.ang_flechas, about_point=punto_inicial2,
                      about_edge=punto_inicial2)

        return self.add(lin1_1, lin1_2, lin2_1, lin2_2)

    def add_tex(self, texto, scale=1, buff=0.1, **moreargs):
        line_reference = Line(self[0][0].get_start(), self[0][-1].get_end())
        texto = TexMobject(texto, **moreargs)
        width = texto.get_height()/2
        texto.rotate(line_reference.get_angle()).scale(scale).move_to(self)
        texto.shift(self.direction*(buff+1)*width)
        return self.add(texto)

    def add_text(self, text, scale=1, buff=0.1, **moreargs):
        line_reference = Line(self[0][0].get_start(), self[0][-1].get_end())
        texto = TextMobject(text, **moreargs)
        width = texto.get_height()/2
        texto.rotate(line_reference.get_angle()).scale(scale).move_to(self)
        texto.shift(self.direction*(buff+1)*width)
        return self.add(texto)

    def add_size(self, texto, scale=1, buff=0.1, **moreargs):
        line_reference = Line(self[0][0].get_start(), self[0][-1].get_end())
        texto = TextMobject(texto, **moreargs)
        width = texto.get_height()/2
        texto.rotate(line_reference.get_angle())
        texto.shift(self.direction*(buff+1)*width)
        return self.add(texto)

    def add_letter(self, texto, scale=1, buff=0.1, **moreargs):
        line_reference = Line(self[0][0].get_start(), self[0][-1].get_end())
        texto = TexMobject(texto, **moreargs).scale(scale).move_to(self)
        width = texto.get_height()/2
        texto.shift(self.direction*(buff+1)*width)
        return self.add(texto)

    def get_text(self, text, scale=1, buff=0.1, invert_dir=False, invert_texto=False, elim_rot=False, **moreargs):
        line_reference = Line(self[0][0].get_start(), self[0][-1].get_end())
        texto = TextMobject(text, **moreargs)
        width = texto.get_height()/2
        if invert_texto:
            inv = PI
        else:
            inv = 0
        if elim_rot:
            texto.scale(scale).move_to(self)
        else:
            texto.rotate(line_reference.get_angle()
                         ).scale(scale).move_to(self)
            texto.rotate(inv)
        if invert_dir:
            inv = -1
        else:
            inv = 1
        texto.shift(self.direction*(buff+1)*width*inv)
        return texto

    def get_tex(self, tex, scale=1, buff=0.1, invert_dir=False, invert_texto=False, elim_rot=False, **moreargs):
        line_reference = Line(self[0][0].get_start(), self[0][-1].get_end())
        texto = TexMobject(texto, **moreargs)
        width = texto.get_height()/2
        if invert_texto:
            inv = PI
        else:
            inv = 0
        if elim_rot:
            texto.scale(scale).move_to(self)
        else:
            texto.rotate(line_reference.get_angle()
                         ).scale(scale).move_to(self)
            texto.rotate(inv)
        if invert_dir:
            inv = -1
        else:
            inv = 1
        texto.shift(self.direction*(buff+1)*width)
        return texto


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

        t1 = TexMobject("r_1:r_2=2:1}").scale(1.5)
        t1.shift(UP*self.rr*2+RIGHT*(self.rr-1))

        self.play(ShowCreation(circler))
        self.wait(1)
        self.play(FadeIn(g1))
        self.wait(1)
        rline = Line(ORIGIN, self.r2*UP)
        self.play(ReplacementTransform(rline, t1))
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
        self.wait(2)

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
        self.wait(3)

        t2 = TexMobject("r_1:r_2=3:1}").scale(1.5)
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
        self.wait(5)


class RollingCircle2(Scene):
    CONFIG = {
        "color": WHITE,
        "r1": 4.5/3,
        "r2": 4.5,
        "txt": 6
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

        t1 = TexMobject("r_1:r_2=3:1}").scale(1.5)
        t1.shift(UP*self.r2*2+RIGHT*(self.r2-1))

        t2 = TexMobject("r_3=r_1-r_2").scale(1.5)
        t2.next_to(t1, DOWN, buff=0.5)

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
        radline = Line(ORIGIN, UP*(self.r2-self.r1), color=BLUE)
        self.play(ShowCreation(radline))
        trans1 = ReplacementTransform(radline, t2)
        self.play(trans1)
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

        meTrack = Measurement(track_line, invert=True, dashed=True, color=BLUE,
                              buff=1).add_tips().add_tex("2\\pi r_3", buff=-3, color=WHITE)
        self.play(GrowFromCenter(meTrack))

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
            # agr = int((360 * alpha * (self.r2-self.r1)/self.r1) % 360)
            # agc = "{:.1f}".format((360*alpha*(self.r2-self.r1)/self.r1)/360)
            # agr = 0
            # agc = "0"
            # print(agr)
            # ta = Text("angle={:d}".format(
            #     agr), font="Hack", alignment="\\raggedright").scale(1.2)
            # tb = Text("round={:s}".format(
            #     agc), font="Hack", alignment="\\raggedright").scale(1.2)
            # ta.shift(UP*self.r2*2+LEFT*self.r2)
            # tb.next_to(ta, DOWN)

            arrow.rotate(angle=angle, about_point=dx)

            # ng = VGroup(circle, arrow, dot1, ta, tb, line)
            ng = VGroup(circle, arrow, dot1, line)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(g1, update2),
                  run_time=10, rate_func=double_smooth)
        self.wait(3)

        # llen = self.r1 * PI
        # line2 = Line(LEFT*llen, RIGHT*llen)
        # trans1 = ReplacementTransform(track_line, line2)
        # circle2 = Circle(radius=self.r1/2, color=BLUE)
        # circle2.shift(LEFT*llen + UP*self.r1/2)
        # trans2 = ReplacementTransform(g1, circle2)

        # self.play(trans1, trans2)
        # self.wait(3)

        # line3 = DashedLine(LEFT*(llen), LEFT*(llen), color=BLUE)
        # g1 = VGroup(circle2, line2, line3)

        # def update3(group, alpha):
        #     # print(alpha)
        #     start_angle = (-720 * alpha - 90) % 360
        #     angle = -((start_angle + 90) % 360)
        #     # print(start_angle, angle)

        #     len = llen * 2 * alpha
        #     arc1 = Arc(radius=(self.r1)/2, arc_center=(UP*self.r1)/2 + LEFT*(RIGHT*llen-len),
        #                color=BLUE, start_angle=math.radians(start_angle), angle=math.radians(angle))
        #     line2 = Line(LEFT*(llen), LEFT*(llen-len), color=BLUE)
        #     line3 = Line(RIGHT*(llen), LEFT*(llen-len), color=WHITE)

        #     ng = VGroup(arc1, line2, line3)
        #     group.become(ng)
        #     return group

        # self.play(UpdateFromAlphaFunc(g1, update3),
        #           run_time=10, rate_func=double_smooth)

        t2 = TexMobject("r_3=r_1-r_2").scale(1.5)
        t2.move_to(UP*(self.txt))
        t3 = TexMobject("r_3=3\\times r_2-r_2").scale(1.5)
        t3.move_to(UP*(self.txt))
        t4 = TexMobject("r_3=2\\times r_2").scale(1.5)
        t4.move_to(UP*(self.txt))
        t4 = TexMobject("C_3=4\\times \\pi \\times r_2").scale(1.5)
        t4.move_to(UP*(self.txt))
        t5 = TexMobject("C_2=2\\times \\pi \\times r_2").scale(1.5)
        t5.move_to(UP*(self.txt))
        trans2 = ReplacementTransform(t2, t3)
        trans3 = ReplacementTransform(t3, t4)
        trans4 = ReplacementTransform(t4, t5)

        self.play(Write(t2))
        self.wait(1)
        self.play(trans2)
        self.wait(1)
        self.play(trans3)
        self.wait(1)
        self.play(trans4)
        self.wait(1)
        self.wait(6)


class Test(Scene):
    CONFIG = {
        "color": WHITE,
        "r1": 4.5/3,
        "r2": 4.5,
        "txt": 6
    }
    def construct(self):

        t1 = TexMobject("r_1:r_2=3:1}").scale(1.5)
        t1.shift(UP*self.r2*2+RIGHT*(self.r2-1))

        t2 = TexMobject("\\bigodot_1   r_1").scale(1.5)
        t2.move_to(UP*(self.txt))

        t3 = TexMobject("\\bigcirc_2   r_2").scale(1.5)
        t3.next_to(t2, DOWN, buff=0.2)

        self.play(Write(t2), Write(t3))
        self.play(Write(t1))
        self.wait(3)
