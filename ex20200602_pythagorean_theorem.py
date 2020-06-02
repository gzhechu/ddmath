#!/usr/bin/env python3

from manimlib.imports import *

# manim ddmath/ex20200602_pythagorean_theorem.py ProofOne -r1280,720 -pm


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


class ProofOne(Scene):
    CONFIG = {
        "a": 5,
        "b": 2,
        "top": 6,
    }

    def construct(self):
        # origin = Dot()
        # self.play(FadeIn(origin), FadeIn(txtO))
        # self.wait(1)

        # t1 = TexMobject("a^2+b^2").scale(2)
        # t2 = TexMobject("+2\\times ab").scale(2)
        # t3 = TexMobject("=(a+b)^2").scale(2)
        # t1.move_to(UP*(self.top))

        # self.add(t1, t2)

        [txtA, txtB] = [TexMobject(X) for X in ["a", "b"]]

        lA = Line(LEFT * self.a / 2, RIGHT * self.a / 2, color=BLUE)
        lA.move_to(UP*self.top)
        txtA.next_to(lA, LEFT, buff=0.5)
        lB = Line(LEFT * self.b/2, RIGHT * self.b/2, color=YELLOW)
        lB.move_to(UP*(self.top-1)+LEFT*(self.a-self.b)/2)
        txtB.next_to(lB, LEFT, buff=0.5)
        self.play(ShowCreation(lB), ShowCreation(txtB),
                  ShowCreation(lA), ShowCreation(txtA))
        self.wait(1)

        lgA = VGroup(lA, txtA)
        lgB = VGroup(lB, txtB)

        [txtAs, txtBs] = [TexMobject(X) for X in ["a^2", "b^2"]]
        sA = Square(side_length=self.a, color=BLUE, fill_opacity=0.3)
        gA = VGroup(sA, txtAs)

        sB = Square(side_length=self.b, color=YELLOW,  fill_opacity=0.3)
        gB = VGroup(sB, txtBs)
        gB.move_to(UP*(self.top))
        self.play(ReplacementTransform(lgA, gA))
        self.wait(1)
        self.play(ReplacementTransform(lgB, gB))
        self.wait(1)

        # move square b
        gB.generate_target()
        gB.target.move_to(DOWN*(self.a+self.b)/2+RIGHT*(self.a+self.b)/2)
        move1 = MoveToTarget(gB)
        self.play(move1)
        vg = VGroup(gA, gB)
        vg.generate_target()
        vg.target.shift(LEFT*(self.b)/2)
        self.play(MoveToTarget(vg))
        self.wait(1)

        sC = Square(side_length=self.a+self.b)
        sC.move_to(DOWN*(self.b)/2)
        self.play(ShowCreation(sC), run_time=3)
        self.wait(1)

        [ptAa, ptAb, ptAc, ptAd] = [sA.get_corner(X)for X in [UL, UR, DL, DR]]
        [ptBa, ptBb, ptBc, ptBd] = [sB.get_corner(X)for X in [UL, UR, DL, DR]]
        [ptCa, ptCb, ptCc, ptCd] = [sC.get_corner(X)for X in [UL, UR, DL, DR]]
        ptRx = ptCb + DOWN * self.b

        meA1 = Measurement(Line(ptAa, ptAb), invert=True, dashed=True,
                           buff=-0.5).add_tips().add_tex("a", buff=3, color=WHITE)
        meA2 = Measurement(Line(ptAa, ptAc), invert=True, dashed=True,
                           buff=0.5).add_tips().add_tex("a", buff=-4, color=WHITE)
        meA3 = Measurement(Line(ptBd, ptCb), invert=True, dashed=True,
                           buff=0.5).add_tips().add_tex("a", buff=-4, color=WHITE)
        meA4 = Measurement(Line(ptCc, ptBc), invert=True, dashed=True,
                           buff=0.5).add_tips().add_tex("a", buff=-4, color=WHITE)
        meB1 = Measurement(Line(ptAb, ptCb), invert=True, dashed=True,
                           buff=-0.5).add_tips().add_tex("b", buff=2, color=WHITE)
        meB2 = Measurement(Line(ptAc, ptCc), invert=True, dashed=True,
                           buff=0.5).add_tips().add_tex("b", buff=-3, color=WHITE)
        meB3 = Measurement(Line(ptBd, ptBb), invert=True, dashed=True,
                           buff=0.5).add_tips().add_tex("b", buff=-3, color=WHITE)
        meB4 = Measurement(Line(ptBc, ptBd), invert=True, dashed=True,
                           buff=0.5).add_tips().add_tex("b", buff=-3, color=WHITE)
        mg = VGroup(meA1, meA2, meA3, meA4, meB1, meB2, meB3, meB4)
        self.play(*[GrowFromCenter(obj)for obj in [*mg]])
        self.wait(3)

        rAB1 = Rectangle(height=self.b, width=self.a,
                         color=WHITE,  fill_opacity=0.3)
        rAB1.move_to(DOWN*(self.a+self.b)/2+LEFT*(self.b)/2)
        rAB2 = Rectangle(height=self.a, width=self.b,
                         color=WHITE,  fill_opacity=0.3)
        rAB2.move_to(RIGHT*(self.a)/2)

        tR1 = Polygon(ptAc, ptAd, ptBc, color=BLUE, fill_opacity=0.3)
        tR2 = Polygon(ptAc, ptCc, ptBc, color=BLUE, fill_opacity=0.3)
        tR3 = Polygon(ptBa, ptAb, ptCb, color=BLUE, fill_opacity=0.3)
        tR4 = Polygon(ptBa, ptBb, ptCb, color=BLUE, fill_opacity=0.3)

        g1 = VGroup(tR1, tR2)
        g2 = VGroup(tR3, tR4)
        self.play(FadeIn(g1), FadeIn(g2), FadeOut(sA), FadeOut(sB))
        self.wait(1)

        ani1 = Rotate(tR1, angle=PI/2, about_point=ptAc)
        g2.generate_target()
        g2.target.shift(DOWN*(self.b))
        ani2 = MoveToTarget(g2)
        ani3 = Rotate(tR3, angle=-PI/2, about_point=ptRx)
        self.play(ani1, ani2)
        self.play(ani3)
        self.wait(2)

        # ani1 = Rotate(tR1, angle=-PI/2, about_point=ptAc)
        # g2.generate_target()
        # g2.target.shift(UP*(self.b))
        # ani2 = MoveToTarget(g2)
        # ani3 = Rotate(tR3, angle=PI/2, about_point=ptRx)
        # self.play(ani1, ani3)
        # self.play(ani2)
        # self.wait(1)
        # g2.generate_target()
        # g2.target.shift(UP*(self.b))
        # self.play(MoveToTarget(g2))
        self.wait(5)


class Test(Scene):
    def construct(self):
        pass
