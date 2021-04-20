#!/usr/bin/env python3

from manim import *
import math

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

# manim ex20200518_two_squares.py Diff2Square -p -qm -r1280,720
# manim ex20200518_two_squares.py Sum2Square -p -qm -r1280,720
# manim ex20200518_two_squares.py PerfectSquare -r1280,720 -p -qm

"""
各位好
前不久给女儿讲平方差公式
作了这个动画
说有数值a和b
那么a和b的平方
可以用以a,b为边长的正方形面积来表示
大正方形中去掉小正方形的面积
即为ab的平方差
剩下的不多讲
看视频就可以明白

顺便的
我也做了完全平方公式的动画

女儿很愉快的看完并说看懂了
但是她随即问了一个问题
“做这些题，学这些公式有什么用”

我想了很久后告诉她
做这些题是为了锻炼思维能力
那么经过训练后的大脑
将来碰到未知问题的时候

会因为长期训练和积累
而迅速找到解决办法
这就是做题和理解公式的意义
而且公式本身
就是经验的提炼总结
学习公式就是站在巨人的肩膀上

退一万步讲
如果你掌握了这些数学题
在二十多年后
你也会有自己的宝宝
当他问你这些题时
你能够快速的回答出来不会被嫌弃
这也算是意义之一吧

你们觉得我这样说合适么
请给我留言说你对这个问题的看法
好嘛，下期再见！

"""


class Diff2Square(Scene):
    def construct(self):
        self.a = 7
        self.b = 2
        self.top = 6

        t1 = TexMobject("a^2-b^2").scale(2)
        t2 = TexMobject("=(a+b)\\times(a-b)").scale(2)
        t1.move_to(UP*(self.a))

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

        vg = VGroup(meA1, meAB1, rAB1, rAB2, t1)
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

        vg = VGroup(rAB1, rAB2)
        t2.next_to(t1, RIGHT, buff=0.2)
        trans2 = ReplacementTransform(vg.copy(), t2)
        self.play(trans2, *[GrowFromCenter(obj) for obj in [*mg]])

        sg2 = VGroup(t1, t2)
        sg2.generate_target()
        sg2.target.shift(LEFT*sg2.get_center())
        move2 = MoveToTarget(sg2)
        self.play(move2)

        self.wait(5)


class Sum2Square(Scene):
    def construct(self):
        self.a = 5
        self.b = 2
        self.top = 6

        t1 = TexMobject("a^2+b^2").scale(2)
        t2 = TexMobject("a^2+b^2=(a+b)^2-2ab").scale(2)
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
                  run_time=1, rate_func=smooth)
        self.play(FadeOut(arc1))

        sC = Square(side_length=self.a+self.b)
        sC.move_to(DOWN*(self.b)/2)
        self.play(ShowCreation(sC), FadeOut(l1), run_time=3)
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


class PerfectSquare(Scene):
    def construct(self):
        self.a = 5
        self.b = 2
        self.top = 6

        t1 = TexMobject("a^2+b^2").scale(2)
        t2 = TexMobject("+2\\times ab").scale(2)
        t3 = TexMobject("=(a+b)^2").scale(2)
        t1.move_to(UP*(self.top))

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

        sg0 = VGroup(txtAs, txtBs)
        sg1 = VGroup(sA.copy(), sB.copy())
        trans1 = ReplacementTransform(sg1, t1)
        self.play(FadeOut(sg0), trans1)
        self.wait(2)

        t2.next_to(t1, RIGHT, buff=0.2)
        sg2 = VGroup(rAB1, rAB2)
        trans2 = ReplacementTransform(sg2, t2)
        self.play(trans2)

        sg1 = VGroup(t1, t2)
        sg1.generate_target()
        sg1.target.shift(LEFT*sg1.get_center())
        move1 = MoveToTarget(sg1)
        self.play(move1)
        self.wait(2)

        t3.next_to(t2, RIGHT, buff=0.2)
        trans3 = ReplacementTransform(sC.copy(), t3)
        self.play(trans3)

        sg2 = VGroup(t1, t2, t3)
        sg2.generate_target()
        sg2.target.shift(LEFT*sg2.get_center())
        move2 = MoveToTarget(sg2)
        self.play(move2)

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
