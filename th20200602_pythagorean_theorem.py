#!/usr/bin/env python3

# manim th20200602_pythagorean_theorem.py ProofOne -r1280,720 -p -qm
# manim th20200602_pythagorean_theorem.py ProofTwo -r1280,720 -p -qm
# manim th20200602_pythagorean_theorem.py ProofThree -r1280,720 -p -qm

from manim import *

try:
    import os
    import sys
    import inspect
    currentdir = os.path.dirname(os.path.abspath(
        inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0, parentdir)
    from utils import Measurement
except:
    pass


class ProofOne(Scene):
    def construct(self):
        self.a = 5
        self.b = 2
        self.top = 6
        # origin = Dot()
        # self.play(FadeIn(origin), FadeIn(txtO))
        # self.wait(1)

        title = Tex("Pythagoras Theorem").scale(2)
        title.move_to(UP*self.top)
        t1 = MathTex("a^2+b^2").scale(2)
        t2 = MathTex("c^2").scale(2)
        t3 = MathTex("=c^2").scale(2)
        t5 = MathTex("(a-b)^2").scale(1.2)
        equl = MathTex("=").scale(2)
        t6 = MathTex("(a-b)^2").scale(2)
        t7 = MathTex("+\\frac{1}{2}ab\\times 4").scale(2)
        t8 = MathTex("+2ab").scale(2)
        t9 = MathTex("a^2+b^2-2ab").scale(2)
        t10 = MathTex("a^2+b^2").scale(2)
        t1.move_to(UP*(self.top))
        t2.move_to(DOWN*self.b/2)
        t5.move_to(DOWN*self.b/2)
        t6.move_to(UP*self.top)
        t8.move_to(UP*self.top)
        t9.move_to(UP*self.top)
        t10.move_to(UP*self.top)

        # self.add(t1, t2)

        [txtA, txtB] = [MathTex(X) for X in ["a", "b"]]

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

        [txtAs, txtBs] = [MathTex(X).scale(1.5) for X in ["a^2", "b^2"]]
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
        [txtAs, txtBs] = [MathTex(X).scale(1.5) for X in ["a^2", "b^2"]]
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
        self.a = 1.2*3
        self.b = 1.2*4
        self.c = 1.2*5
        self.top = 8
        # origin = Dot()
        # self.play(FadeIn(origin))
        # self.wait(1)

        [txtA, txtB, txtC] = [MathTex(X) for X in ["A", "B", "C"]]
        [txtAs, txtBs, txtCs] = [MathTex(
            X).scale(1.5) for X in ["a^2", "b^2", "c^2"]]
        t1 = MathTex("a^2+b^2").scale(2.5)
        t2 = MathTex("=c^2").scale(2.5)
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


class ProofThree(Scene):
    def construct(self):
        self.a = 5
        self.b = 2
        self.top = 7

        t1 = MathTex("c^2").scale(2)
        t2 = MathTex("=a^2+b^2").scale(2)
        t3 = MathTex("=(a-b)^2+2ab").scale(2)
        t4 = MathTex("=a^2+b^2-2ab+2ab").scale(2)
        t5 = MathTex("=a^2+b^2").scale(2)
        t1.move_to(UP*(self.top))
        t2.next_to(t1, RIGHT)

        [txtA, txtB, txtC] = [Tex(X, tex_template=TexTemplateLibrary.ctex)
                              for X in ["勾(a)", "股(b)", "弦(c)"]]

        lA = Line(LEFT * self.a / 2, RIGHT * self.a / 2, color=WHITE)
        lB = Line(UP * self.b/2, DOWN * self.b/2, color=WHITE)
        lB.move_to(RIGHT*(self.a)/2+UP*(self.b)/2)
        ptA = lA.get_start()
        ptB = lA.get_end()
        ptC = lB.get_start()
        lC = Line(ptA, ptC, color=WHITE)
        print(ptA, ptB, ptC)
        tri1 = Polygon(ptA, ptB, ptC, color=WHITE)

        sA = Square(side_length=np.sqrt(np.square(self.a) +
                                        np.square(self.b)), color=BLUE, fill_opacity=0.5)
        sA.rotate(angle=np.pi - np.arctan(self.b/self.a)*np.pi)
        sB = Square(side_length=(self.a-self.b),
                    color=YELLOW, fill_opacity=0.5)
        sC = Square(side_length=(self.a+self.b),
                    color=WHITE, fill_opacity=0)
        sqA = Square(side_length=self.a, color=BLUE, fill_opacity=0.5)
        sqB = Square(side_length=self.b, color=BLUE, fill_opacity=0.5)
        sqA.shift(LEFT*self.b/2+DOWN*self.b/2)
        sqB.shift(RIGHT*self.a/2+DOWN*self.a/2)

        txtA.next_to(lA, DOWN, buff=0.5)
        txtB.next_to(lB, RIGHT, buff=0.5)
        txtC.next_to(lA, UP, buff=1.6)
        txtTs = VGroup(txtA, txtB, txtC)
        triA = VGroup(tri1, txtTs)

        # 整体移动
        vg = VGroup(sA, sB, sC, sqA, sqB)
        vg.shift(UP*self.b)

        [ptAc, ptAa, ptAb, ptAd] = sA.get_vertices()
        print(ptAa, ptAb, ptAc, ptAd)
        dots = [Dot(X)for X in [ptAa, ptAb, ptAc, ptAd]]
        [ptBa, ptBb, ptBc, ptBd] = [sB.get_corner(X)for X in [UL, UR, DL, DR]]
        [ptCa, ptCb, ptCc, ptCd] = [sA.get_corner(X)for X in [UL, UR, DL, DR]]

        # 三角形
        self.play(ShowCreation(triA))
        self.wait(1)

        triA.generate_target()
        triA.target.shift(DOWN*(self.a-self.b)/2+RIGHT*self.b/2)
        self.play(MoveToTarget(triA))

        triA = tri1.copy()
        triB = tri1.copy()
        triC = tri1.copy()
        triD = tri1.copy()
        triA.generate_target()
        triA.target.rotate(angle=-PI/2, about_point=ptAd)
        transA = MoveToTarget(triA)
        triB.generate_target()
        triB.target.rotate(angle=PI/2, about_point=ptAc)
        transB = MoveToTarget(triB)
        triC.generate_target()
        triC.target.shift(LEFT*self.b+UP*(self.a))
        transC = MoveToTarget(triC)
        triD.generate_target()
        triD.target.rotate(angle=PI, about_point=triD.get_center())
        transD = MoveToTarget(triD)

        triG = VGroup(triA, triB, triC, triD)

        [txtAs, txtBs, txtCs] = [MathTex(X).scale(1.8) for X in [
            "a^2", "b^2", "c^2"]]
        txtAs.move_to(sqA.get_center())
        txtBs.move_to(sqB.get_center())

        txtCs.move_to(sA.get_center())
        self.play(FadeIn(sA), Write(txtCs), FadeOut(txtTs))
        self.wait(1)

        self.play(ReplacementTransform(txtCs, t1))
        self.wait(1)

        # self.play(transA, transB, transC, transD)
        self.play(transA)
        self.play(transB)
        self.play(transC)
        self.play(transD)
        [X.set_style(stroke_color=RED, fill_color=RED, fill_opacity=0.5)
         for X in [*triG]]
        self.play(FadeOut(sA), FadeOut(tri1), FadeIn(triG), FadeIn(sB))
        # self.remove(sA)
        # self.add(sB)
        self.wait(1)

        meA1 = Measurement(Line(ptAa, ptCc), invert=True, dashed=True,
                           buff=0.5).add_tips().add_tex("a", buff=-3, color=WHITE)
        meA2 = Measurement(Line(ptAc, ptCd), invert=True, dashed=True,
                           buff=0.5).add_tips().add_tex("a", buff=-4, color=WHITE)
        meB1 = Measurement(Line(ptCc, ptAc), invert=True, dashed=True,
                           buff=0.5).add_tips().add_tex("b", buff=-3, color=WHITE)
        meB2 = Measurement(Line(ptCd, ptAd), invert=True, dashed=True,
                           buff=0.5).add_tips().add_tex("b", buff=-4, color=WHITE)

        mgA = VGroup(meA1, meA2, meB1, meB2)
        self.play(*[GrowFromCenter(obj)
                    for obj in [*mgA]], run_time=1)
        self.wait(1)

        triA.generate_target()
        triA.target.shift(LEFT*self.a+DOWN*self.b)
        transA = MoveToTarget(triA)
        triC.generate_target()
        triC.target.shift(RIGHT*self.b+DOWN*self.a)
        transC = MoveToTarget(triC)
        self.play(transA)
        self.play(transC)
        self.wait(1)

        meB1.generate_target()
        meB1.target.shift(RIGHT*self.a)
        trans1 = MoveToTarget(meB1)
        meA2.generate_target()
        meA2.target.shift(LEFT*self.b)
        trans2 = MoveToTarget(meA2)

        ind1 = Indicate(sqA, scale_factor=1, color=BLUE)
        ind2 = Indicate(sqB, scale_factor=1, color=BLUE)

        gABs = VGroup(txtAs, txtBs)
        self.play(ind1, ind2,  Write(gABs),
                  trans1, trans2, FadeOut(triG), FadeOut(sB))
        self.wait(1)

        self.play(ReplacementTransform(gABs, t2))
        sg1 = VGroup(t1, t2)
        sg1.generate_target()
        sg1.target.shift(LEFT*sg1.get_center())
        move1 = MoveToTarget(sg1)
        self.play(move1)
        self.wait(3)

        t3.next_to(t1, RIGHT)
        self.play(FadeOut(sqA), FadeOut(sqB), FadeIn(triG),
                  FadeIn(sB), ReplacementTransform(t2, t3))
        sg2 = VGroup(t1, t3)
        sg2.generate_target()
        sg2.target.shift(LEFT*sg2.get_center())
        move2 = MoveToTarget(sg2)
        self.play(move2)
        self.wait(1)

        triA.generate_target()
        triA.target.shift(RIGHT*self.a+UP*self.b)
        transA = MoveToTarget(triA)
        triC.generate_target()
        triC.target.shift(LEFT*self.b+UP*self.a)
        transC = MoveToTarget(triC)
        self.play(transA)
        self.play(transC)

        self.play(FadeIn(sC))
        self.wait(1)

        t4.next_to(t1, RIGHT)
        meB1.generate_target()
        meB1.target.shift(LEFT*self.a)
        trans1 = MoveToTarget(meB1)
        meA2.generate_target()
        meA2.target.shift(RIGHT*self.b)
        trans2 = MoveToTarget(meA2)
        self.play(trans1, trans2, ReplacementTransform(t3, t4))

        sg3 = VGroup(t1, t4)
        sg3.generate_target()
        sg3.target.shift(LEFT*sg3.get_center())
        move3 = MoveToTarget(sg3)
        self.play(move3)
        self.wait(2)

        t5.next_to(t1, RIGHT)
        self.play(FadeOut(t4), FadeIn(t5))

        sg4 = VGroup(t1, t5)
        sg4.generate_target()
        sg4.target.shift(LEFT*sg4.get_center())
        move4 = MoveToTarget(sg4)
        self.play(move4)

        self.wait(3)


class Test(Scene):
    def construct(self):
        tex = Tex('Hello 你好 \\LaTeX', tex_template=TexTemplateLibrary.ctex).scale(3)
        self.add(tex)
        self.wait(5)
