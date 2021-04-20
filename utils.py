#!/usr/bin/env python3

from manim import *


# 长方体
class Cuboid(VGroup):
    def __init__(self, x=3, y=4, z=5, has_top=True, **kwargs):
        self.x = x
        self.y = y
        self.z = z
        self.has_top = has_top
        super().__init__(**kwargs)

    def __str__(self):
        return str("class:{}, x:{}, y:{}, z:{}".format(self.name, self.x*10, self.y*10, self.z*10))

    def generate_points(self):
        for vect in IN, OUT:
            if not self.has_top and vect is OUT:
                continue
            face = Rectangle(
                height=self.y, width=self.x,
                shade_in_3d=True,
            )
            face.flip()
            face.shift(self.z * OUT / 2.0)
            face.apply_matrix(z_to_vector(vect))
            self.add(face)
        for vect in LEFT, RIGHT:
            face = Rectangle(
                height=self.y, width=self.z,
                shade_in_3d=True,
            )
            face.flip()
            face.shift(self.x * OUT / 2.0)
            face.apply_matrix(z_to_vector(vect))
            self.add(face)
        for vect in UP, DOWN:
            face = Rectangle(
                height=self.x, width=self.z,
                shade_in_3d=True,
            )
            face.flip()
            face.shift(self.y * OUT / 2.0)
            face.apply_matrix(z_to_vector(vect))
            self.add(face)


# 测量工具
class Measurement(VGroup):
    def __init__(self, objeto, color=RED, dashed=True, invert=False,
                 buff=0.3, stroke=2.4, **kwargs):
        self.color = color
        self.buff = buff
        self.laterales = 0.3
        self.invert = invert
        self.dashed_segment_length = 0.09
        self.dashed = dashed
        self.con_flechas = True
        self.ang_flechas = 30*DEGREES
        self.tam_flechas = 0.2
        self.stroke = stroke

        VGroup.__init__(self, **kwargs)
        if self.dashed == True:
            medicion = DashedLine(ORIGIN, objeto.get_length(
            )*RIGHT, dashed_segment_length=self.dashed_segment_length).set_color(self.color)
        else:
            medicion = Line(ORIGIN, objeto.get_length()*RIGHT)

        medicion.set_stroke(color=self.color, width=self.stroke)

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
        texto = TexMobject(tex, **moreargs)
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


class Test0(ThreeDScene):
    def construct(self):
        cbox = Cuboid()
        self.set_camera_orientation(phi=70 * DEGREES, theta=30*DEGREES)
        self.play(FadeIn(cbox))
        self.wait(5)


class Test1(Scene):
    def construct(self):
        text = TextMobject("Text or object")
        self.add(text)
        me = Measurement(Line(ORIGIN+5*LEFT, ORIGIN+5*RIGHT))
        #  .add_tips().add_text("measurement", buff=2, color=BLUE, scale=2)
        self.add(me)
        self.wait(5)


class Test2(Scene):
    def construct(self):
        text = TextMobject("Text or object")
        self.add(text)
        line = DashedLine(ORIGIN+5*LEFT, ORIGIN+5*RIGHT).set_color(RED)
        self.add(line)
        self.wait(5)
