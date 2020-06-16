#!/usr/bin/env python3

from manimlib.imports import *

# manim ddmath/ex20200602_pythagorean_theorem.py ProofOne -r1280,720 -pm
# manim ddmath/ex20200602_pythagorean_theorem.py ProofTwo -r1280,720 -pm


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

        title = TextMobject("Pythagoras Theorem").scale(2)
        title.move_to(UP*self.top)
        t1 = TexMobject("a^2+b^2").scale(2)
        t2 = TexMobject("c^2").scale(2)
        t3 = TexMobject("=c^2").scale(2)
        t5 = TexMobject("(a-b)^2").scale(1.2)
        equl = TexMobject("=").scale(2)
        t6 = TexMobject("(a-b)^2").scale(2)
        t7 = TexMobject("+\\frac{1}{2}ab\\times 4").scale(2)
        t8 = TexMobject("+2ab").scale(2)
        t9 = TexMobject("a^2+b^2-2ab").scale(2)
        t10 = TexMobject("a^2+b^2").scale(2)
        t1.move_to(UP*(self.top))
        t2.move_to(DOWN*self.b/2)
        t5.move_to(DOWN*self.b/2)
        t6.move_to(UP*self.top)
        t8.move_to(UP*self.top)
        t9.move_to(UP*self.top)
        t10.move_to(UP*self.top)

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

        [txtAs, txtBs] = [TexMobject(X).scale(1.5) for X in ["a^2", "b^2"]]
        sA = Square(side_length=self.a, color=BLUE, fill_opacity=0.3)
        gA = VGroup(sA, txtAs)

        sB = Square(side_length=self.b, color=YELLOW,  fill_opacity=0.3)
        gB = VGroup(sB, txtBs)
        gB.move_to(UP*(self.top))
        self.play(ReplacementTransform(lgA, gA), ReplacementTransform(lgB, gB))
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

        [ptAa, ptAb, ptAc, ptAd] = [sA.get_corner(X)for X in [UL, UR, DL, DR]]
        [ptBa, ptBb, ptBc, ptBd] = [sB.get_corner(X)for X in [UL, UR, DL, DR]]
        [ptCa, ptCb, ptCc, ptCd] = [sC.get_corner(X)for X in [UL, UR, DL, DR]]
        ptRx = ptCb + DOWN * self.b

        ptX1 = ptAa + RIGHT * self.b
        ptX2 = ptCb + DOWN * self.b
        ptX3 = ptAa + DOWN * self.b
        ptX4 = ptCc + RIGHT * self.b
        polyX1 = Polygon(ptX1, ptX2, ptBc, ptAc, color=BLUE,
                         stroke_opacity=0, fill_opacity=0.3)

        polyX2 = Polygon(ptX3, ptX4, ptBb, ptAb, color=BLUE,
                         stroke_opacity=0, fill_opacity=0.3)

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
        self.play(*[GrowFromCenter(obj)
                    for obj in [*mg]], ShowCreation(sC), run_time=1)
        self.wait(1)

        rAB1 = Rectangle(height=self.b, width=self.a,
                         color=WHITE,  fill_opacity=0.3)
        rAB1.move_to(DOWN*(self.a+self.b)/2+LEFT*(self.b)/2)
        rAB2 = Rectangle(height=self.a, width=self.b,
                         color=WHITE,  fill_opacity=0.3)
        rAB2.move_to(RIGHT*(self.a)/2)

        sg1 = VGroup(gA, gB, )
        trans1 = ReplacementTransform(sg1, t1)

        self.play(trans1, FadeIn(rAB1), FadeIn(rAB2))
        self.wait(1)

        tR1 = Polygon(ptAc, ptAd, ptBc, color=WHITE, fill_opacity=0.3)
        tR2 = Polygon(ptAc, ptCc, ptBc, color=WHITE, fill_opacity=0.3)
        tR3 = Polygon(ptBa, ptAb, ptCb, color=WHITE, fill_opacity=0.3)
        tR4 = Polygon(ptBa, ptBb, ptCb, color=WHITE, fill_opacity=0.3)

        g1 = VGroup(tR1, tR2)
        g2 = VGroup(tR3, tR4)
        self.play(FadeIn(g1), FadeIn(g2), FadeOut(rAB1), FadeOut(rAB2))
        self.wait(1)

        ani1 = Rotate(tR1, angle=PI/2, about_point=ptAc)
        g2.generate_target()
        g2.target.shift(DOWN*(self.b))
        ani2 = MoveToTarget(g2)
        ani3 = Rotate(tR3, angle=-PI/2, about_point=ptRx)
        self.play(ani1, ani2)
        self.play(ani3, ShowCreation(t2))

        ani1 = Indicate(polyX1, scale_factor=1.2)
        self.play(ani1)
        self.wait(1)

        t3.next_to(t1, RIGHT, buff=0.2)
        trans2 = ReplacementTransform(t2.copy(), t3)
        self.play(trans2, FadeOut(t2), FadeOut(polyX1))

        sg1 = VGroup(t1, t3)
        sg1.generate_target()
        sg1.target.shift(LEFT*sg1.get_center())
        move1 = MoveToTarget(sg1)
        self.play(move1)
        self.wait(1)

        # restore to 2 square.
        ani1 = Rotate(tR1, angle=-PI/2, about_point=ptAc)
        ani2 = Rotate(tR3, angle=PI/2, about_point=ptRx)
        self.play(ani1, ani2)

        g2.generate_target()
        g2.target.shift(UP*(self.b))
        ani3 = MoveToTarget(g2)
        [txtAs, txtBs] = [TexMobject(X).scale(1.5) for X in ["a^2", "b^2"]]
        txtAs.move_to(LEFT*(self.b)/2)
        txtBs.move_to(DOWN*(self.a+self.b)/2+RIGHT*(self.a)/2)
        trans3 = ReplacementTransform(sg1, title)
        self.play(ani3, ShowCreation(txtAs), ShowCreation(txtBs), trans3)
        self.wait(3)
        self.play(FadeOut(g1), FadeOut(g2), FadeIn(rAB1), FadeIn(rAB2))
        self.play(FadeOut(title))

        # 赵爽的方法
        tR1 = Polygon(ptAc, ptAd, ptCc, color=WHITE, fill_opacity=0.3)
        tR2 = Polygon(ptCc, ptBc, ptAd, color=WHITE, fill_opacity=0.3)
        tR3 = Polygon(ptAb, ptBb, ptCb, color=WHITE, fill_opacity=0.3)
        tR4 = Polygon(ptAb, ptBb, ptAd, color=WHITE, fill_opacity=0.3)
        g1 = VGroup(tR1, tR2)
        g2 = VGroup(tR3, tR4)
        g4 = VGroup(tR1, tR2, tR3, tR4)
        self.play(FadeIn(g1), FadeIn(g2), FadeOut(rAB1), FadeOut(rAB2))
        self.wait(1)

        # move the meaurement
        meA2.generate_target()
        meA2.target.shift(DOWN*(self.b))
        meB2.generate_target()
        meB2.target.shift(UP*(self.a))
        meA4.generate_target()
        meA4.target.shift(RIGHT*(self.b))
        meB4.generate_target()
        meB4.target.shift(LEFT*(self.a))
        meG = VGroup(meA2, meB2, meA4, meB4)

        tR1.generate_target()
        tR1.target.shift(RIGHT*(self.b))
        tR2.generate_target()
        tR2.target.shift(UP*(self.a))
        tR3.generate_target()
        tR3.target.shift(LEFT*(self.a)+DOWN*(self.b))
        tRs = VGroup(tR1, tR2, tR3)
        self.play(*[MoveToTarget(obj)
                    for obj in [*tRs]], *[MoveToTarget(obj)
                                          for obj in [*meG]],
                  FadeOut(txtAs), FadeOut(txtBs))
        self.wait(3)
        ani1 = Indicate(polyX2, scale_factor=1.2)
        self.play(ani1)
        self.wait(1)
        self.play(FadeOut(polyX2), FadeIn(t5))
        self.wait(1)

        self.play(ReplacementTransform(t5, t6))
        self.wait(1)

        t7.next_to(t6, RIGHT)
        self.play(ReplacementTransform(g4.copy(), t7))

        sg1 = VGroup(t6, t7)
        sg1.generate_target()
        sg1.target.shift(LEFT*sg1.get_center())
        move1 = MoveToTarget(sg1)
        self.play(move1)
        self.wait(1)

        equl.next_to(sg1, RIGHT)
        t2.next_to(equl, RIGHT)
        equl = VGroup(equl, t2)
        self.play(FadeIn(polyX2))
        trans4 = ReplacementTransform(polyX2, t2)
        self.play(trans4)

        sg1 = VGroup(equl, t6, t7)
        sg1.generate_target()
        sg1.target.shift(LEFT*sg1.get_center())
        move1 = MoveToTarget(sg1)
        self.play(move1)
        self.wait(1)

        ani1 = Indicate(t7, scale_factor=1.2)
        self.play(ani1)
        t8.next_to(equl, LEFT)
        self.play(ReplacementTransform(t7, t8))
        self.wait(1)

        ani2 = Indicate(t6, scale_factor=1.2)
        self.play(ani2)
        t9.next_to(t8, LEFT)
        self.play(ReplacementTransform(t6, t9))
        self.wait(1)

        sg1 = VGroup(t8, t9)
        t10.next_to(equl, LEFT)
        self.play(ReplacementTransform(sg1, t10))

        sg1 = VGroup(equl, t10)
        sg1.generate_target()
        sg1.target.shift(LEFT*sg1.get_center())
        move1 = MoveToTarget(sg1)
        self.play(move1)

        # ani1 = Indicate(sg1, scale_factor=1.2)
        # self.play(ani1)
        self.wait(5)


class ProofTwo(Scene):
    CONFIG = {
        "a": 1.2*3,
        "b": 1.2*4,
        "c": 1.2*5,
        "top": 8,
    }

    def construct(self):
        # origin = Dot()
        # self.play(FadeIn(origin))
        # self.wait(1)

        [txtA, txtB, txtC] = [TexMobject(X) for X in ["A", "B", "C"]]
        [txtAs, txtBs, txtCs] = [TexMobject(
            X).scale(1.5) for X in ["a^2", "b^2", "c^2"]]
        t1 = TexMobject("a^2+b^2").scale(2.5)
        t2 = TexMobject("=c^2").scale(2.5)
        t1.move_to(UP*(self.top))

        ptA = self.a * RIGHT
        ptB = self.b * UP
        ptC = ORIGIN
        l1 = Line(ptA, ptB)
        ang1 = l1.get_angle()
        # self.add(l1)

        sqA = Square(side_length=self.a, color=YELLOW, fill_opacity=0.2)
        sqA.move_to(LEFT*(self.c-self.a)/2+UP*((self.c-self.a)/2+self.a))
        sqA.rotate(angle=PI-ang1, about_point=sqA.get_corner(DL))
        sqB = Square(side_length=self.b, color=RED, fill_opacity=0.2)
        sqB.move_to(RIGHT*(self.c-self.b)/2+UP*((self.c-self.b)/2+self.b))
        sqB.rotate(angle=PI/2-ang1, about_point=sqB.get_corner(DR))
        sqC = Square(side_length=self.c, color=BLUE, fill_opacity=0.2)
        sqG = VGroup(sqA, sqB, sqC, txtAs, txtBs, txtCs)
        sqG.shift(DOWN*2.5)

        txtAs.move_to(sqA.get_center())
        txtBs.move_to(sqB.get_center())

        ptA = sqC.get_corner(UL)
        ptB = sqC.get_corner(UR)
        ptC = sqA.get_vertices()[2]
        ptC1 = ptC*RIGHT + sqC.get_bottom()*UP
        txtA.next_to(ptA, DL, buff=0.3)
        txtB.next_to(ptB, DR, buff=0.3)
        txtC.next_to(ptC, UP, buff=0.5)
        self.add(Dot(ptC), Dot(ptA), Dot(ptB))

        triangle = Polygon(ptA, ptB, ptC, color=WHITE, fill_opacity=0.1)
        self.play(ShowCreation(triangle))
        self.wait(1)
        self.play(Write(txtA), Write(txtB), Write(txtC))
        self.wait(1)
        self.play(*[FadeIn(obj) for obj in [*sqG]])
        self.wait(1)

        sqV = Square(side_length=0.4, color=WHITE, fill_opacity=0)
        sqV.move_to(ptC1+UR*0.2)
        dashLine = DashedLine(ptC, ptC1, color=WHITE)
        verLine = VGroup(dashLine, sqV)
        self.play(ShowCreation(verLine))
        self.wait(1)

        sqA1 = sqA.copy()
        self.add(sqA1)
        gA = VGroup(sqA1)

        def update1(group, alpha):
            ang = (PI-ang1)
            pts = sqA1.get_vertices()
            x1 = pts[1][0]
            x2 = ptC[0]
            X = alpha*(x2-x1)*RIGHT
            Y = alpha*(x2-x1)*np.tan(ang)*UP
            shift = X+Y

            pts[0] += shift
            pts[1] += shift
            poly = Polygon(*pts, color=WHITE, fill_color=YELLOW,
                           fill_opacity=0.2)
            ng = VGroup(poly)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(gA, update1),
                  run_time=2, rate_func=smooth)

        def update2(group, alpha):
            pts = sqA1.get_vertices()
            y1 = pts[2][1]
            y2 = ptA[1]
            Y = alpha*(y2-y1)*UP
            shift = Y

            pts[1] += shift
            pts[2] += shift
            poly = Polygon(*pts, color=WHITE, fill_color=YELLOW,
                           fill_opacity=0.2)
            ng = VGroup(poly)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(gA, update2),
                  run_time=2, rate_func=smooth)

        gA.generate_target()
        gA.target.shift(DOWN*(self.c))
        move1 = MoveToTarget(gA)
        self.play(move1, run_time=3)
        self.wait(1)

        # square B
        sqB1 = sqB.copy()
        self.add(sqB1)
        gB = VGroup(sqB1)

        pts = sqB1.get_vertices()
        print(pts)

        def update3(group, alpha):
            ang = (PI-ang1)
            ang = PI/2-ang1
            pts = sqB1.get_vertices()
            x1 = pts[0][0]
            x2 = ptC[0]
            X = alpha*(x2-x1)*RIGHT
            Y = alpha*(x2-x1)*np.tan(ang)*UP
            shift = X+Y

            pts[0] += shift
            pts[1] += shift
            poly = Polygon(*pts, color=WHITE, fill_color=RED,
                           fill_opacity=0.2)
            ng = VGroup(poly)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(gB, update3),
                  run_time=2, rate_func=smooth)

        def update4(group, alpha):
            pts = sqB1.get_vertices()
            y1 = pts[3][1]
            y2 = ptA[1]
            Y = alpha*(y2-y1)*UP
            shift = Y

            pts[0] += shift
            pts[3] += shift
            poly = Polygon(*pts, color=WHITE, fill_color=RED,
                           fill_opacity=0.2)
            ng = VGroup(poly)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(gB, update4),
                  run_time=2, rate_func=smooth)

        gB.generate_target()
        gB.target.shift(DOWN*(self.c))
        move1 = MoveToTarget(gB)
        self.play(move1, run_time=3)

        self.play(FadeOut(gA), FadeOut(gB), FadeOut(verLine))

        sg1 = VGroup(txtAs, txtBs)
        self.play(ReplacementTransform(sg1, t1))
        self.wait(1)

        t2.next_to(t1, RIGHT)
        self.play(ReplacementTransform(txtCs, t2))

        sg1 = VGroup(t1, t2)
        sg1.generate_target()
        sg1.target.shift(LEFT*sg1.get_center())
        move1 = MoveToTarget(sg1)
        self.play(move1)

        self.wait(5)


class Test(Scene):
    def construct(self):
        pass
