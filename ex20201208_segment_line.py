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
ffmpeg -i SegLine1.mp4 -i v1.m4a output.mp4 -y
ffmpeg -i SegLine2.mp4 -i v2.m4a output.mp4 -y
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

        self.play(FadeIn(lAD), FadeIn(ptA), FadeIn(
            ptD), FadeIn(txtA), FadeIn(txtD))
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
02 说已知点B是线段AC上一点
03 M是线段AB的中点
04 N是线段AC的中点
05 P是线段AN的中点
06 Q是线段AM的中点
07 问：线段BC与PQ的比值
08 由于这道题的条件有点多
09 所以画个辅助线帮助记录下各线段的中点
10 那么，一开始我使用的传统方法
11 列出线段BC和PQ的长度计算关系
12 然后依据各个线段的中点
13 通过等长代换，就像这样
14 一步一步代换来算出结果
15 视频播放过程中
16 可以按暂停仔细看下计算过程
最后消元即可得到答案
15 但这种计算方法
16 很容易写错字母导致出错
17 而且计算过程比较麻烦
18 所以，我们还想出了另一种方法
19 用数轴座标系结合二元一次方程来解题
20 新方法能够比较直观、迅速的求解
21 由于时间关系这次就不讲了
23 如果你想知道 请关注我 下集我来讲
"""
        "color": WHITE,
        # A, Q, P, M, N, B,  C
        # 0, 3, 4, 6, 8, 12, 16
        "a": [-8*0.7, 1, 0],
        "b": [4*0.7, 1, 0],
        "c": [8*0.7, 1, 0],
        "m": [-2*0.7, 1, 0],
        "n": [0*0.7, 1, 0],
        "p": [-4*0.7, 1, 0],
        "q": [-5*0.7, 1, 0],
        "txt": 9,
    }

    def construct(self):
        lALL = Line(self.a, self.c)
        lAC = Line(self.a, self.c, stroke_width=15, color=BLUE)
        lAB = Line(self.a, self.b, stroke_width=15, color=RED)
        lAM = Line(self.a, self.m, stroke_width=15, color=BLUE)
        lAN = Line(self.a, self.n, stroke_width=15, color=GREEN)
        lNP = Line(self.n, self.p, stroke_width=15, color=BLUE)
        lMQ = Line(self.m, self.q, stroke_width=15, color=GREEN)
        lPQ = Line(self.p, self.q, stroke_width=15, color=YELLOW)
        lBC = Line(self.b, self.c, stroke_width=15, color=BLUE)

        tx1 = TexMobject("BC").scale(1.5)
        tx1.move_to(self.txt * UP)
        tx1a = TexMobject("=AC-AB").scale(1.5)
        tx1a.next_to(tx1, RIGHT)
        tx2 = TexMobject("PQ").scale(1.5)
        tx2.next_to(tx1, DOWN, buff=0.8)
        tx2a = TexMobject("=AP-AQ").scale(1.5)
        tx2a.next_to(tx2, RIGHT)
        tx2b = TexMobject("=NP-MQ").scale(1.5)
        tx2c = TexMobject("=\\frac{1}{2}AN-\\frac{1}{2}AM").scale(1.5)
        tx2d = TexMobject(
            "=\\frac{1}{2}\\times(\\frac{1}{2}AC)-\\frac{1}{2}\\times(\\frac{1}{2}AB)").scale(1.5)
        tx2e = TexMobject("=\\frac{1}{4}(AC-AB)").scale(1.5)

        tx3 = TexMobject("\\frac{BC}{PQ}").scale(1.5)
        tx3q = TexMobject("=?").scale(2.5)
        tx3a = TexMobject("=\\frac{AC-AB}{\\frac{1}{4}(AC-AB)}").scale(1.5)
        tx3b = TexMobject("=\\frac{1}{\\frac{1}{4}}").scale(1.5)
        tx3c = TexMobject("=4").scale(2.5)

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
        self.wait(5)

        self.play(FadeIn(ptB), FadeIn(txtB))
        self.wait(1)

        self.play(GrowFromCenter(lAB), Indicate(ptM), FadeIn(txtM))
        self.wait(1)
        self.remove(lAB)

        self.play(GrowFromCenter(lAC), Indicate(ptN), FadeIn(txtN))
        self.wait(1)
        self.remove(lAC)

        self.play(GrowFromCenter(lAN), Indicate(ptP), FadeIn(txtP))
        self.wait(1)
        self.remove(lAN)

        self.play(GrowFromCenter(lAM), Indicate(ptQ), FadeIn(txtQ))
        self.wait(1)
        self.remove(lAM)

        self.play(GrowFromCenter(lBC))
        self.play(GrowFromCenter(lPQ))

        # 显示问题
        tx3.move_to((self.txt - 1) * UP)
        tx3q.next_to(tx3, RIGHT)
        self.play(TransformFromCopy(lBC, tx3), TransformFromCopy(lPQ, tx3q))
        vt3x = VGroup(tx3, tx3q)
        vt3x.generate_target()
        vt3x.target.shift(LEFT*vt3x.get_center())
        move3 = MoveToTarget(vt3x)
        self.play(move3, run_time=0.5)
        self.wait(2)
        self.play(FadeOut(vt3x))


        # 显示标记
        meAC = Measurement(lAC, dashed=True, buff=0.8).add_tips().add_tex(
            "N'", color=WHITE)
        meAB = Measurement(lAB, dashed=True, buff=1.6).add_tips().add_tex(
            "M'", color=WHITE)
        meAN = Measurement(lAN, dashed=True, buff=2.4).add_tips().add_tex(
            "P'", color=WHITE)
        meAM = Measurement(lAM, dashed=True, buff=3.2).add_tips().add_tex(
            "Q'", color=WHITE)

        self.play(GrowFromCenter(meAC), run_time=0.25)
        self.play(GrowFromCenter(meAB), run_time=0.25)
        self.play(GrowFromCenter(meAN), run_time=0.25)
        self.play(GrowFromCenter(meAM), run_time=0.25)
        self.wait(1)

        # step 0
        self.play(FadeIn(tx1))
        self.play(TransformFromCopy(lBC, tx1a))
        vt1x = VGroup(tx1, tx1a)
        vt1x.generate_target()
        vt1x.target.shift(LEFT*vt1x.get_center())
        move1 = MoveToTarget(vt1x)
        self.play(move1, run_time=0.5)

        self.play(FadeIn(tx2))
        self.play(TransformFromCopy(lPQ, tx2a))
        vt2x = VGroup(tx2, tx2a)
        vt2x.generate_target()
        vt2x.target.shift(LEFT*vt2x.get_center())
        move2 = MoveToTarget(vt2x)
        self.play(move2, run_time=0.5)
        self.wait()

        # step 1, transform
        tx2b.next_to(tx2, RIGHT)
        self.play(ReplacementTransform(lNP, tx2a),
                  ReplacementTransform(lMQ, tx2a))
        self.play(ReplacementTransform(tx2a, tx2b))
        self.remove(tx2a)
        # self.remove(tx2a)

        vt2x = VGroup(tx2, tx2b)
        vt2x.generate_target()
        vt2x.target.shift(LEFT*vt2x.get_center())
        move2 = MoveToTarget(vt2x)
        self.play(move2, run_time=0.5)
        self.wait()

        # step 2
        tx2c.next_to(tx2, RIGHT)
        self.play(ReplacementTransform(lAN, tx2b),
                  ReplacementTransform(lAM, tx2b))
        self.play(ReplacementTransform(tx2b, tx2c))
        self.remove(tx2b)

        vt2x = VGroup(tx2, tx2c)
        vt2x.generate_target()
        vt2x.target.shift(LEFT*vt2x.get_center())
        move2 = MoveToTarget(vt2x)
        self.play(move2, run_time=0.5)
        self.wait()

        # step 3
        tx2d.next_to(tx2, RIGHT)
        self.play(ReplacementTransform(lAC, tx2c),
                  ReplacementTransform(lAB, tx2c))
        self.play(ReplacementTransform(tx2c, tx2d))
        self.remove(tx2c)

        vt2x = VGroup(tx2, tx2d)
        vt2x.generate_target()
        vt2x.target.shift(LEFT*vt2x.get_center())
        move2 = MoveToTarget(vt2x)
        self.play(move2, run_time=0.5)
        self.wait()

        # step 4
        tx2e.next_to(tx2, RIGHT)
        self.play(ReplacementTransform(tx2d, tx2e))
        self.remove(tx2d)

        vt2x = VGroup(tx2, tx2e)
        vt2x.generate_target()
        vt2x.target.shift(LEFT*vt2x.get_center())
        move2 = MoveToTarget(vt2x)
        self.play(move2, run_time=0.5)
        self.wait()

        ind1 = Indicate(tx1, running_start=double_smooth, scale_factor=1.2)
        ind2 = Indicate(tx2, running_start=double_smooth, scale_factor=1.2)
        self.play(ind1)
        self.play(ind2)

        tx3.move_to((self.txt - 1) * UP + 3*LEFT)
        gx1 = VGroup(tx1, tx2)
        self.play(ReplacementTransform(gx1, tx3))
        tx3a.next_to(tx3, RIGHT)
        gx2 = VGroup(tx1a, tx2e)
        self.play(ReplacementTransform(gx2, tx3a))

        vt3x = VGroup(tx3, tx3a)
        vt3x.generate_target()
        vt3x.target.shift(LEFT*vt3x.get_center())
        move3 = MoveToTarget(vt3x)
        self.play(move3, run_time=0.5)
        self.wait()


        tx3b.next_to(tx3, RIGHT)
        self.play(ReplacementTransform(tx3a, tx3b))
        vt3x = VGroup(tx3, tx3b)
        vt3x.generate_target()
        vt3x.target.shift(LEFT*vt3x.get_center())
        move3 = MoveToTarget(vt3x)
        self.play(move3, run_time=0.5)
        self.wait()

        tx3c.next_to(tx3, RIGHT)
        self.play(ReplacementTransform(tx3b, tx3c))
        vt3x = VGroup(tx3, tx3c)
        vt3x.generate_target()
        vt3x.target.shift(LEFT*vt3x.get_center())
        move3 = MoveToTarget(vt3x)
        self.play(move3, run_time=0.5)
        self.wait()

        # meAP = Measurement(lAP, dashed=True, buff=-1.5).add_tips().add_tex(
        #     "x", color=WHITE)
        # meAQ = Measurement(lAQ, dashed=True, buff=-2.0).add_tips().add_tex(
        #     "y", color=WHITE)
        # self.play(GrowFromCenter(meAP), run_time=0.25)
        # self.play(GrowFromCenter(meAQ), run_time=0.25)
        # self.wait(1)

        self.wait(5)
