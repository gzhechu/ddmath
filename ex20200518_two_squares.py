#!/usr/bin/env python3

from manimlib.imports import *

# manim ex20200518_two_squares.py Diff2Square -pm -r1280,720
# manim ex20200518_two_squares.py Sum2Square -pm -r1280,720


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


class Diff2Square(Scene):
    CONFIG = {
        "a": 7,
        "b": 2,
        "top": 6,
    }

    def construct(self):
        # origin = Dot()
        # self.play(FadeIn(origin), FadeIn(txtO))
        # self.wait(1)

        t1 = TexMobject("\\Huge a^2 - b^2")
        t2 = TexMobject("\\Huge a^2 - b^2 = (a+b)*(a-b)")
        t1.move_to(UP*(self.a))
        t2.next_to(t1, DOWN, buff=0.5)

        # self.add(t1, t2)

        [txtA, txtB] = [TexMobject(X) for X in ["a", "b"]]

        lA = Line(LEFT * self.a / 2, RIGHT * self.a / 2, color=BLUE)
        lA.move_to(UP*self.top)
        txtA.next_to(lA, LEFT, buff=0.5)
        self.play(ShowCreation(lA), ShowCreation(txtA))

        lB = Line(LEFT * self.b/2, RIGHT * self.b/2, color=YELLOW)
        lB.move_to(UP*(self.top-1)+LEFT*(self.a-self.b)/2)
        txtB.next_to(lB, LEFT, buff=0.5)
        self.play(ShowCreation(lB), ShowCreation(txtB))
        self.wait(1)

        lgA = VGroup(lA, txtA)
        lgB = VGroup(lB, txtB)

        [txtAs, txtBs] = [TexMobject(X) for X in ["a^2", "b^2"]]
        sA = Square(side_length=self.a, color=BLUE, fill_opacity=0.3)
        gA = VGroup(sA, txtAs)

        sB = Square(side_length=self.b, color=YELLOW,  fill_opacity=0.3)
        gB = VGroup(sB, txtBs)
        gB.move_to(UP*(self.a))
        # self.play(ShowCreation(sA), ShowCreation(txtAs))
        self.play(ReplacementTransform(lgA, gA))
        self.wait(1)
        # self.play(ShowCreation(sB), ShowCreation(txtBs))
        self.play(ReplacementTransform(lgB, gB))
        self.wait(1)

        gB.generate_target()
        gB.target.move_to(UP*(self.a-self.b)/2+LEFT*(self.a-self.b)/2)
        trans1 = MoveToTarget(gB)
        self.play(trans1)
        self.wait(1)

        [ptAa, ptAb, ptAc, ptAd] = [sA.get_corner(X)for X in [UL, UR, DL, DR]]
        [ptBa, ptBb, ptBc, ptBd] = [sB.get_corner(X)for X in [UL, UR, DL, DR]]

        pX = Polygon(ptBb, ptAb, ptAd, ptAc, ptBc, ptBd)

        meA1 = Measurement(Line(ptAc, ptAd), invert=True, dashed=True,
                           buff=0.5).add_tips().add_tex("a", buff=-3, color=WHITE)
        meB1 = Measurement(Line(ptAa, ptBc), invert=True, dashed=True,
                           buff=0.5).add_tips().add_tex("b", buff=-3, color=WHITE)
        meAB1 = Measurement(Line(ptBc, ptAc), invert=True, dashed=True,
                            buff=0.5).add_tips().add_tex("a-b", buff=-3, color=WHITE)
        meB2 = Measurement(Line(ptBa, ptBb), invert=True, dashed=True,
                           buff=-0.5).add_tips().add_tex("b", buff=3, color=WHITE)
        meAB2 = Measurement(Line(ptBb, ptAb), invert=True, dashed=True,
                            buff=-0.5).add_tips().add_tex("a-b", buff=3, color=WHITE)
        mg = VGroup(meA1, meB1, meAB1, meB2, meAB2)
        self.play(*[GrowFromCenter(obj)for obj in [*mg]])
        self.wait(1)

        sg = VGroup(txtAs, txtBs)
        trans1 = ReplacementTransform(sg, t1)
        self.play(FadeIn(pX), FadeOut(sA), FadeOut(sB), trans1)
        self.wait(2)

        ptR = ptAd + UP*(self.a-self.b)
        rAB1 = Rectangle(height=self.b, width=self.a-self.b,
                         color=BLUE,  fill_opacity=0.3)
        rAB1.move_to(UP*(self.a-self.b)/2+RIGHT*(self.b)/2)
        rAB2 = Rectangle(height=self.a-self.b, width=self.a,
                         color=BLUE,  fill_opacity=0.3)
        rAB2.move_to(DOWN*(self.b)/2)

        self.play(FadeIn(rAB1), FadeIn(rAB2))
        self.remove(pX)
        self.wait(1)
        trans1 = Rotate(rAB1, about_point=ptR, angle=math.radians(-90))

        self.play(trans1, FadeOut(meB1), FadeOut(meB2), FadeOut(meAB2))
        rAB1.generate_target()
        rAB1.target.shift(DOWN*(self.a-self.b))
        trans1 = MoveToTarget(rAB1)
        self.play(trans1)
        self.wait(1)

        vg = VGroup(meA1, meAB1, rAB1, rAB2)
        vg.generate_target()
        vg.target.shift(LEFT*(self.b)/2)
        self.play(MoveToTarget(vg))

        ptABb = rAB1.get_corner(UR)
        ptABc = rAB1.get_corner(DL)
        ptABd = rAB1.get_corner(DR)
        meAB2 = Measurement(Line(ptABb, ptABd), invert=True, dashed=True,
                            buff=-0.5).add_tips().add_tex("a-b", buff=3, color=WHITE)
        meB2 = Measurement(Line(ptABc, ptABd), invert=True, dashed=True,
                           buff=0.5).add_tips().add_tex("b", buff=-3, color=WHITE)
        mg = VGroup(meAB2, meB2)
        self.play(Write(t2), *[GrowFromCenter(obj) for obj in [*mg]])
        self.wait(1)

        self.wait(5)


class Sum2Square(Scene):
    CONFIG = {
        "a": 5,
        "b": 2,
        "top": 6,
    }

    def construct(self):
        # origin = Dot()
        # self.play(FadeIn(origin), FadeIn(txtO))
        # self.wait(1)

        t1 = TexMobject("a^2+b^2").set_color(BLUE).scale(2)
        t2 = TexMobject("a^2+b^2=(a+b)^2-2ab").set_color(BLUE).scale(2)
        t1.move_to(UP*(self.top+1))
        t2.next_to(t1, DOWN, buff=0.5)

        # self.add(t1, t2)

        [txtA, txtB] = [TexMobject(X) for X in ["a", "b"]]

        lA = Line(LEFT * self.a / 2, RIGHT * self.a / 2, color=BLUE)
        lA.move_to(UP*self.top)
        txtA.next_to(lA, LEFT, buff=0.5)
        self.play(ShowCreation(lA), ShowCreation(txtA))

        lB = Line(LEFT * self.b/2, RIGHT * self.b/2, color=YELLOW)
        lB.move_to(UP*(self.top-1)+LEFT*(self.a-self.b)/2)
        txtB.next_to(lB, LEFT, buff=0.5)
        self.play(ShowCreation(lB), ShowCreation(txtB))
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
        gB.target.move_to(UP*(self.a-self.b)/2+RIGHT*(self.a+self.b)/2)
        trans1 = MoveToTarget(gB)
        self.play(trans1)
        self.wait(1)

        vg = VGroup(gA, gB)
        vg.generate_target()
        vg.target.shift(LEFT*(self.b)/2)
        self.play(MoveToTarget(vg))

        [ptAa, ptAb, ptAc, ptAd] = [sA.get_corner(X)for X in [UL, UR, DL, DR]]
        [ptBa, ptBb, ptBc, ptBd] = [sB.get_corner(X)for X in [UL, UR, DL, DR]]

        pX = Polygon(ptAa, ptBb, ptBd, ptBc, ptAd, ptAc)

        meA1 = Measurement(Line(ptAa, ptAb), invert=True, dashed=True,
                           buff=-0.5).add_tips().add_tex("a", buff=3, color=WHITE)
        meA2 = Measurement(Line(ptAa, ptAc), invert=True, dashed=True,
                           buff=0.5).add_tips().add_tex("a", buff=-4, color=WHITE)
        meB1 = Measurement(Line(ptBa, ptBb), invert=True, dashed=True,
                           buff=-0.5).add_tips().add_tex("b", buff=2, color=WHITE)
        meB2 = Measurement(Line(ptBb, ptBd), invert=True, dashed=True,
                           buff=-0.5).add_tips().add_tex("b", buff=2, color=WHITE)
        mg = VGroup(meA1, meA2, meB1, meB2)
        self.play(*[GrowFromCenter(obj)for obj in [*mg]])
        self.wait(1)

        sg = VGroup(txtAs, txtBs)
        trans1 = ReplacementTransform(sg, t1)
        self.play(FadeIn(pX), FadeOut(sA), FadeOut(sB), trans1)
        self.wait(2)

        l1 = Line(ptAa, ptBb)
        arc1 = Arc(radius=0)
        g1 = VGroup(l1, arc1)

        def update1(group, alpha):
            r = self.a + self.b
            angle = math.radians(90 * alpha)
            arc1 = Arc(radius=r, arc_center=ptAa,
                       start_angle=np.deg2rad(0), angle=-angle)
            l1 = Line(ptAa, ptBb)
            l1.rotate(angle=-angle, about_point=ptAa)
            ng = VGroup(l1, arc1)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(g1, update1),
                  run_time=2, rate_func=smooth)
        self.wait(1)
        self.play(FadeOut(arc1))
        self.wait(1)

        sC = Square(side_length=self.a+self.b)
        sC.move_to(DOWN*(self.b)/2)
        self.play(ShowCreation(sC), FadeOut(l1))
        self.wait(1)
        [ptCc, ptCd] = [sC.get_corner(X)for X in [DL, DR]]

        rAB1 = Rectangle(height=self.b, width=self.a,
                         color=BLUE,  fill_opacity=0.3)
        rAB1.move_to(DOWN*(self.a+self.b)/2+LEFT*(self.b)/2)
        rAB2 = Rectangle(height=self.a, width=self.b,
                         color=BLUE,  fill_opacity=0.3)
        rAB2.move_to(RIGHT*(self.a)/2+DOWN*(self.b))
        self.play(FadeIn(rAB1), FadeIn(rAB2), FadeOut(sC))
        self.wait(1)
        ptX = rAB1.get_corner(DR)

        meA3 = Measurement(Line(ptCc, ptX), invert=True, dashed=True,
                           buff=0.5).add_tips().add_tex("a", buff=-4, color=WHITE)
        meA4 = Measurement(Line(ptBd, ptCd), invert=True, dashed=True,
                           buff=-0.5).add_tips().add_tex("a", buff=3, color=WHITE)
        meB3 = Measurement(Line(ptAc, ptCc), invert=True, dashed=True,
                           buff=0.5).add_tips().add_tex("b", buff=-3, color=WHITE)
        meB4 = Measurement(Line(ptX, ptCd), invert=True, dashed=True,
                           buff=0.5).add_tips().add_tex("b", buff=-3, color=WHITE)
        mg = VGroup(meA3, meA4, meB3, meB4)
        self.play(Write(t2), *[GrowFromCenter(obj) for obj in [*mg]])
        self.wait(1)

        self.wait(5)


class Test(Scene):
    def construct(self):
        # textHuge = TextMobject("{\\Huge Huge Text 012.\\#!?} Text")
        textHuge = TextMobject("\\Huge (a+b)*(a-b)")
        texthuge = TextMobject("{\\huge huge Text 012.\\#!?} Text")
        textLARGE = TextMobject("{\\LARGE LARGE Text 012.\\#!?} Text")
        textLarge = TextMobject("{\\Large Large Text 012.\\#!?} Text")
        textlarge = TextMobject("{\\large large Text 012.\\#!?} Text")
        textNormal = TextMobject("{\\normalsize normal Text 012.\\#!?} Text")
        textsmall = TextMobject("{\\small small Text 012.\\#!?} Texto normal")
        textfootnotesize = TextMobject(
            "{\\footnotesize footnotesize Text 012.\\#!?} Text")
        textscriptsize = TextMobject(
            "{\\scriptsize scriptsize Text 012.\\#!?} Text")
        texttiny = TextMobject("{\\tiny tiny Texto 012.\\#!?} Text normal")
        textHuge.to_edge(UP)
        texthuge.next_to(textHuge, DOWN, buff=0.1)
        textLARGE.next_to(texthuge, DOWN, buff=0.1)
        textLarge.next_to(textLARGE, DOWN, buff=0.1)
        textlarge.next_to(textLarge, DOWN, buff=0.1)
        textNormal.next_to(textlarge, DOWN, buff=0.1)
        textsmall.next_to(textNormal, DOWN, buff=0.1)
        textfootnotesize.next_to(textsmall, DOWN, buff=0.1)
        textscriptsize.next_to(textfootnotesize, DOWN, buff=0.1)
        texttiny.next_to(textscriptsize, DOWN, buff=0.1)
        self.add(textHuge, texthuge, textLARGE, textLarge, textlarge,
                 textNormal, textsmall, textfootnotesize, textscriptsize, texttiny)
        self.wait(3)
