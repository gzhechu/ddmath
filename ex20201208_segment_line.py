#!/usr/bin/env python3

from manimlib.imports import *
from random import shuffle, randrange

try:
    import sys
    sys.path.append(os.path.dirname(os.path.realpath(__file__)))
    from utils import Measurement
except:
    pass

# manim ddmath/ex20201208_segment_line.py SegLine1 -r1280,720 -pm
# manim ddmath/ex20201208_segment_line.py SegLine1 -r640,360 -pl

# manim ddmath/ex20201208_segment_line.py SegLine2 -r1280,720 -pm
# manim ddmath/ex20201208_segment_line.py SegLine2 -r640,360 -pl

"""
ffmpeg -i voice.m4a -acodec copy v.aac -y
ffmpeg -i bg.m4a -acodec copy b.aac -y
cat b.aac v.aac >> sound.aac -y
ffmpeg -i sound.aac -acodec copy -bsf:a aac_adtstoasc sound.m4a -y
ffmpeg -i SegLine1.mp4 -i sound.m4a output.mp4
"""


class SegLine1(Scene):
    """
00 各位好，
01 这是女儿的一道线段题数学作业
04 如果掌握正确的解题思路
00 解题的过程还是比较有意思的
54 说线段AD上有BC两点
56 BC长度等于AC的三分之一
同时也等于BD的四分之一
另外E是AC的中点，F是BD的中点
已知BC长度是5，问AD的长度？
那么这道题用一元一次方程解起来简直是切菜一样
关键是要用已知条件整理出等式关系
设BC长度是x，则可知：
AC长度为3x，BD长度是4x
那么整个AD长度就是6X，注意不是7X啊
因为E是AC中点，所以EC长度是1.5x
F是BD的中点，稍微计算一下可知CF等于X
那么整个EF的长度=EC+CF=2.5X=5
则X等于2，那么线段AD的长度6X也就知道了
讲的有点快不知道明白没
可以重复看一遍整理一下思路
顺便帮我点个赞吧
好了 下次再见
    """

    CONFIG = {
        "color": WHITE,
        "a": [-3*1.5, 1, 0],
        "b": [-1*1.5, 1, 0],
        "c": [-0*1.5, 1, 0],
        "d": [3*1.5, 1, 0],
        "e": [-1.5*1.5, 1, 0],
        "f": [1*1.5, 1, 0],
        "txt": 9,
    }

    def construct(self):
        lAD = Line(self.a, self.d)
        lAC = Line(self.a, self.c, stroke_width=10, color=YELLOW)
        lBD = Line(self.b, self.d, stroke_width=10, color=RED)
        lEF = Line(self.e, self.f, stroke_width=10, color=YELLOW)
        lBC = Line(self.b, self.c, stroke_width=10, color=BLUE)

        # text message
        tx1 = TexMobject("BC=\\frac{1}{3}AC")
        tx1.move_to(self.txt * UP)
        tx1b = TexMobject("=\\frac{1}{4}BD")
        tx1b.next_to(tx1, RIGHT)
        tx2 = TexMobject("AE=EC")
        tx2.next_to(tx1, DOWN, buff=0.5)
        tx2b = TexMobject(", BF=FD")
        tx2b.next_to(tx2, RIGHT)
        tx3 = TexMobject("EF=5")
        tx3.next_to(tx2, DOWN, buff=0.5)
        txX = TexMobject("=x")

        [ptA, ptB, ptC, ptD, ptE, ptF] = [
            Dot(X) for X in [self.a, self.b, self.c, self.d, self.e, self.f]]
        [txtA, txtB, txtC, txtD, txtE, txtF] = [
            TextMobject(X) for X in ["A", "B", "C", "D", "E", "F"]]

        txtA.next_to(ptA, DOWN, buff=0.6)
        txtB.next_to(ptB, DOWN, buff=0.6)
        txtC.next_to(ptC, DOWN, buff=0.6)
        txtD.next_to(ptD, DOWN, buff=0.6)
        txtE.next_to(ptE, DOWN, buff=0.6)
        txtF.next_to(ptF, DOWN, buff=0.6)

        self.play(FadeIn(lAD), FadeIn(ptA), FadeIn(ptD), FadeIn(txtA), FadeIn(txtD))
        self.wait(5)

        self.play(FadeIn(ptB), FadeIn(ptC), FadeIn(txtB), FadeIn(txtC))
        self.play(GrowFromCenter(lBC))
        self.wait(1)

        gE = VGroup(ptE, txtE)
        gE.set_color(YELLOW)
        self.play(GrowFromCenter(lAC), run_time=0.5)
        trans1 = TransformFromCopy(lAC, tx1)
        self.play(trans1, run_time=0.5)
        self.remove(lAC)
        ptA.set_color(YELLOW)
        ptC.set_color(YELLOW)

        gF = VGroup(ptF, txtF)
        gF.set_color(RED)
        self.play(GrowFromCenter(lBD), run_time=0.5)
        trans2 = TransformFromCopy(lBD, tx1b)
        self.play(trans2, run_time=0.5)                        
        self.remove(lBD)
        ptB.set_color(RED)
        ptD.set_color(RED)

        sg1 = VGroup(tx1, tx1b)
        sg1.generate_target()
        sg1.target.shift(LEFT*sg1.get_center())
        move1 = MoveToTarget(sg1)
        self.play(move1, run_time=0.5)
        self.wait()

        ind1 = Indicate(gE, color=YELLOW,
                        running_start=double_smooth, scale_factor=1.2)
        ind2 = Indicate(gF, color=RED,
                        running_start=double_smooth, scale_factor=1.2)
        sg2 = VGroup(tx2, tx2b)
        sg2.generate_target()
        sg2.target.shift(LEFT*sg2.get_center())
        move2 = MoveToTarget(sg2)
        trans1 = TransformFromCopy(gE, tx2)
        trans2 = TransformFromCopy(gF, tx2b)
        self.play(ind1, run_time=0.5)
        self.play(trans1, run_time=0.5)
        self.play(ind2, run_time=0.5)
        self.play(trans2, run_time=0.5)
        self.play(move2)

        # 显示 EF 长度
        meEF = Measurement(lEF, invert=True, dashed=True,
                           buff=-0.5).add_tips().add_tex("5", buff=0.6, color=WHITE)
        self.play(GrowFromCenter(meEF), FadeIn(tx3))
        self.wait(1)
        meAD = Measurement(lAD, invert=True, dashed=True,
                           buff=-1.2).add_tips().add_tex("?", buff=0.6, color=WHITE)
        self.play(GrowFromCenter(meAD))
        self.wait(5)

        txX.next_to(sg1, RIGHT)
        trans1 = TransformFromCopy(lBC, txX)
        self.play(trans1)
        sg1 = VGroup(sg1, txX)
        sg1.generate_target()
        sg1.target.shift(LEFT*sg1.get_center())
        move1 = MoveToTarget(sg1)
        self.play(move1, run_time=0.5)
        self.wait()

        tx4 = TexMobject("AC=3x")
        tx4.next_to(tx3, DOWN, buff=0.5)
        tx4b = TexMobject(",BD=4x")
        tx4b.next_to(tx4, RIGHT)
        tx4c = TexMobject("AD=6x")
        tx4c.next_to(tx3, DOWN, buff=0.5)
        trans1 = TransformFromCopy(lAC, tx4)
        self.play(trans1)
        trans2 = TransformFromCopy(lBD, tx4b)
        self.play(trans2)

        sg4 = VGroup(tx4, tx4b)
        sg4.generate_target()
        sg4.target.shift(LEFT*sg4.get_center())
        move1 = MoveToTarget(sg4)
        self.play(move1, run_time=0.5)
        self.wait()

        trans1 = ReplacementTransform(sg4, tx4c)
        self.play(trans1)

        self.wait(5)


class SegLine2(Scene):
    CONFIG = {
        """
00 各位好，
01 今天讲一道我个人觉得很有意思也有代表性的线段计算题
02 说已知B是AC上一点
03 M是线段AB的中点
04 N是线段AC的中点
05 P是线段AN的中点
06 Q是线段AM的中点
07 问：BC比PQ的值

"""
        "color": WHITE,
        # A, Q, P, M, N, B,  C
        # 0, 3, 4, 6, 8, 12, 16
        "a": [-8*0.8, 1, 0],
        "b": [4*0.8, 1, 0],
        "c": [8*0.8, 1, 0],
        "m": [-2*0.8, 1, 0],
        "n": [0*0.8, 1, 0],
        "p": [-4*0.8, 1, 0],
        "q": [-5*0.8, 1, 0],
        "txt": 9,
    }

    def construct(self):
        lALL = Line(self.a, self.c)
        lAC = Line(self.a, self.c, stroke_width=15, color=BLUE)
        lAB = Line(self.a, self.b, stroke_width=15, color=RED)
        lAM = Line(self.a, self.m, stroke_width=15, color=BLUE)
        lAN = Line(self.a, self.n, stroke_width=15, color=GREEN)
        lAP = Line(self.a, self.p, stroke_width=15, color=BLUE)
        lAQ = Line(self.a, self.q, stroke_width=15, color=GREEN)
        lPQ = Line(self.p, self.q, stroke_width=15, color=YELLOW)
        lBC = Line(self.b, self.c, stroke_width=15, color=BLUE)

        tx1 = TexMobject("BC=\\frac{1}{3}AC")
        tx1.move_to(self.txt * UP)
        tx1b = TexMobject("=\\frac{1}{4}BD")
        tx1b.next_to(tx1, RIGHT)
        tx2 = TexMobject("AE=EC")
        tx2.next_to(tx1, DOWN, buff=0.5)
        tx2b = TexMobject(", BF=FD")
        tx2b.next_to(tx2, RIGHT)
        tx3 = TexMobject("EF=5")
        tx3.next_to(tx2, DOWN, buff=0.5)

        [ptA, ptB, ptC, ptM, ptN, ptP, ptQ] = [
            Dot(X) for X in [self.a, self.b, self.c, self.m, self.n, self.p, self.q]]
        [txtA, txtB, txtC, txtM, txtN, txtP, txtQ] = [
            TextMobject(X) for X in ["A", "B", "C", "M", "N", "P", "Q"]]

        txtA.next_to(ptA, DOWN, buff=0.6)
        txtB.next_to(ptB, DOWN, buff=0.6)
        txtC.next_to(ptC, DOWN, buff=0.6)
        txtM.next_to(ptM, DOWN, buff=0.6)
        txtN.next_to(ptN, DOWN, buff=0.6)
        txtP.next_to(ptP, DOWN, buff=0.6)
        txtQ.next_to(ptQ, DOWN, buff=0.6)

        self.play(FadeIn(lALL), FadeIn(ptA), FadeIn(ptC),
                  FadeIn(txtA), FadeIn(txtC))
        self.wait(3)

        self.play(FadeIn(ptB), FadeIn(txtB))
        self.wait(1)

        self.play(GrowFromCenter(lAC), Indicate(ptN), FadeIn(txtN))
        self.wait(1)
        self.remove(lAC)

        self.play(GrowFromCenter(lAB), Indicate(ptM), FadeIn(txtM))
        self.wait(1)
        self.remove(lAB)

        self.play(GrowFromCenter(lAN), Indicate(ptP), FadeIn(txtP))
        self.wait(1)
        self.remove(lAN)

        self.play(GrowFromCenter(lAM), Indicate(ptQ), FadeIn(txtQ))
        self.wait(1)
        self.remove(lAM)

        self.play(GrowFromCenter(lBC))
        self.play(GrowFromCenter(lPQ))
        self.wait(1)

        # 显示标记
        meAC = Measurement(lAC, dashed=True, buff=0.5).add_tips().add_tex(
            "N'", color=WHITE)
        meAB = Measurement(lAB, dashed=True, buff=1.0).add_tips().add_tex(
            "M'", color=WHITE)
        meAN = Measurement(lAN, dashed=True, buff=1.5).add_tips().add_tex(
            "P'", color=WHITE)
        meAM = Measurement(lAM, dashed=True, buff=2.0).add_tips().add_tex(
            "Q'", color=WHITE)

        meAP = Measurement(lAP, dashed=True, buff=-1.5).add_tips().add_tex(
            "x", color=WHITE)
        meAQ = Measurement(lAQ, dashed=True, buff=-2.0).add_tips().add_tex(
            "y", color=WHITE)

        self.play(GrowFromCenter(meAC), run_time=0.25)
        self.play(GrowFromCenter(meAB), run_time=0.25)
        self.play(GrowFromCenter(meAN), run_time=0.25)
        self.play(GrowFromCenter(meAM), run_time=0.25)
        self.wait(1)

        self.play(GrowFromCenter(meAP), run_time=0.25)
        self.play(GrowFromCenter(meAQ), run_time=0.25)
        self.wait(1)

        self.wait(5)
