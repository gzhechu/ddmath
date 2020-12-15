#!/usr/bin/env python3

from manimlib.imports import *
from manimlib.for_3b1b_videos.pi_creature_animations import Blink

# manim ddmath/ex20201116_chase_problem.py CircleChase1 -r1280,720 -pm
# manim ddmath/ex20201116_chase_problem.py CircleChase1 -r640,360 -pl

# manim ddmath/ex20201116_chase_problem.py CircleChase2 -r1280,720 -pm
# manim ddmath/ex20201116_chase_problem.py CircleChase2 -r640,360 -pl

# ffmpeg -i CircleChase1.mp4 -i sound.m4a output.mp4

"""
ffmpeg -i voice.m4a -acodec copy v.aac -y
ffmpeg -i bg.m4a -acodec copy b.aac -y
cat b.aac v.aac >> sound.aac -y
ffmpeg -i sound.aac -acodec copy -bsf:a aac_adtstoasc sound.m4a -y
ffmpeg -i CircleChase1.mp4 -i sound.m4a output.mp4
"""


class CircleChase1(Scene):
    """
00 各位好，
01 这是一道典型的环形跑道追及问题
04 说在一条400米的环形跑道上
08 有甲乙两人速度分别是8米/秒和6米/秒
11 甲在乙前8米位置
13 问两人同向奔跑后多久甲能追上乙？
16 解决这道题的关键，
19 是找到隐藏在问题中的等式关系。
21 那么，
22 做图、思考、想象一下他们是如何运动的。
26 如图可知，当甲追上乙的时候，
27 他们运动的时间相同，而不管乙跑了多远，
29 甲为了追上乙，总会比乙多跑黄色部分的距离。
34 而这个黄色弧线的长度，是已知的。
36 所以设未知数x为追及所需的时间，列等式。
40 等式左边，是甲跑过的距离为8x
44 等式右边，是乙跑过的距离为6x
46 因为甲比乙多跑黄色弧线的距离，
50 所以在等式右边加上弧线的长度，等式即成立。
54 通过解这个方程，就可以到答案……
56 仔细思考下，你……学会了么？
    """
    CONFIG = {
        "color": WHITE,
        "r1": 0.2,
        "r2": 0.2,
        "rr": 5,
        "v1": 8,
        "v2": 6,
        "dist": 8,
        "ctime": 196,
        "perimeter": 400,
        "txt": 9,
        "eq": 6.5
    }

    def construct(self):
        tp = TexMobject("S=400m").scale(1.5)
        tg = TexMobject("dist=8m").scale(1.5)
        tv1 = TexMobject("v1=8m/s").scale(1.5)
        tv2 = TexMobject("v2=6m/s").scale(1.5)
        tp.move_to(self.txt * UP + LEFT * 3)
        tg.next_to(tp, DOWN, buff=0.3)
        tv1.move_to(self.txt * UP + RIGHT * 3)
        tv2.next_to(tv1, DOWN, buff=0.3)

        circler = Circle(radius=self.rr, color=self.color)
        self.add(circler)
        self.wait(4)
        trans1 = TransformFromCopy(circler, tp)
        self.play(trans1)

        c1 = Circle(radius=self.r1, color=self.color,
                    fill_color=RED, fill_opacity=1)
        c1.shift(UP*self.rr)

        va1 = self.dist / self.perimeter
        a1 = math.radians(-360 * va1)

        c1.rotate(angle=a1, about_point=ORIGIN)

        c2 = Circle(radius=self.r1, color=self.color,
                    fill_color=BLUE, fill_opacity=1)
        c2.shift(UP*self.rr)

        self.play(FadeIn(c1), FadeIn(c2))
        self.wait(1)

        trans2 = TransformFromCopy(c1, tv1)
        trans3 = TransformFromCopy(c2, tv2)
        self.play(trans2, trans3)
        self.wait(1)

        arc1 = Arc(radius=self.rr, color=YELLOW, stroke_width=50,
                   start_angle=math.radians(90), angle=a1)
        self.play(ShowCreation(arc1))
        ind3 = Indicate(arc1, color=YELLOW, scale_factor=2)
        self.play(ind3, run_time=0.5)
        self.play(ind3, run_time=0.5)
        trans4 = ReplacementTransform(arc1, tg)
        self.play(trans4)
        self.wait(1)

        g1 = VGroup(c1, c2)

        def update1(group, alpha):
            t = alpha * self.ctime  # 时间片
            s1 = self.v1 * t + self.dist
            s2 = self.v2 * t
            va1 = (s1 % self.perimeter) / self.perimeter
            va2 = (s2 % self.perimeter) / self.perimeter

            a1 = math.radians(-360 * va1)
            a2 = math.radians(-360 * va2)
            # print(t, s1, s2, a1, a2)

            c1 = Circle(radius=self.r1, color=self.color,
                        fill_color=RED, fill_opacity=1)
            c1.shift(UP*self.rr)
            c1.rotate(angle=a1, about_point=ORIGIN)

            c2 = Circle(radius=self.r1, color=self.color,
                        fill_color=BLUE, fill_opacity=1)
            c2.shift(UP*self.rr)
            c2.rotate(angle=a2, about_point=ORIGIN)

            new_group = VGroup(c1, c2)
            group.become(new_group)
            return group

        self.play(UpdateFromAlphaFunc(g1, update1),
                  run_time=10, rate_func=linear)

        self.wait(1)
        self.play(FadeOut(c1), FadeOut(c2))

        c1 = Circle(radius=self.r1, color=self.color,
                    fill_color=RED, fill_opacity=1)
        c1.shift(UP*self.rr)
        va1 = self.dist / self.perimeter
        a1 = math.radians(-360 * va1)
        c1.rotate(angle=a1, about_point=ORIGIN)

        c2 = Circle(radius=self.r1, color=self.color,
                    fill_color=BLUE, fill_opacity=1)
        c2.shift(UP*self.rr)

        self.play(FadeIn(c1), FadeIn(c2))
        self.wait(3)

        arc1 = Arc(radius=self.rr, stroke_width=15, color=YELLOW,
                   start_angle=a1 + math.radians(90), angle=-(TAU+a1))
        self.play(ShowCreation(arc1))
        self.wait(2)
        ind3 = Indicate(
            arc1, color=YELLOW, running_start=there_and_back_with_pause, scale_factor=1.05)
        self.play(ind3, run_time=2)
        self.wait(1)

        tx = TexMobject("x").scale(4)
        self.play(FadeIn(tx))
        self.wait(2)

        teq = TexMobject("=").scale(2)
        tqx1 = TexMobject("?").scale(3)
        tqx2 = TexMobject("X").scale(3)
        tqx2.set_color(RED)
        teq.move_to(self.eq * UP)
        tqx1.move_to(self.eq * UP)
        tqx2.move_to(self.eq * UP)
        txa = TexMobject("8x").scale(2)
        txb = TexMobject("6x").scale(2)
        txg1 = TexMobject("+(400-8)").scale(2)
        txg2 = TexMobject("+392").scale(2)
        txa.next_to(teq, LEFT)
        txb.next_to(teq, RIGHT)
        txg1.next_to(txb, RIGHT)
        txg2.next_to(txb, RIGHT)

        self.play(FadeIn(teq))

        g1 = VGroup(tv1, tx)
        g2 = VGroup(tv2, tx)
        trans1 = TransformFromCopy(g1, txa)
        trans2 = TransformFromCopy(g2, txb)
        self.play(trans1)
        self.wait(1)
        self.play(trans2)
        self.play(FadeIn(tqx1))
        # self.wait(1)
        ind4 = Indicate(tqx1, color=RED, scale_factor=2)
        self.play(ind4, run_time=0.5)
        self.play(ind4, run_time=0.5)
        self.remove(tqx1)
        self.add(tqx2)
        self.wait(1)
        trans3 = TransformFromCopy(arc1, txg1)
        self.play(trans3, FadeOut(tqx2))
        self.wait(1)
        trans4 = ReplacementTransform(txg1, txg2)
        self.play(trans4)

        sg1 = VGroup(teq, txa, txb, txg2)
        sg1.generate_target()
        sg1.target.shift(LEFT*sg1.get_center())
        move1 = MoveToTarget(sg1)
        self.play(move1)

        g2 = VGroup(c1, c2, arc1, tx)

        def update2(group, alpha):
            t = alpha * self.ctime  # 时间片
            s1 = self.v1 * t + self.dist
            s2 = self.v2 * t
            s3 = s1-s2
            va1 = (s1 % self.perimeter) / self.perimeter
            va2 = (s2 % self.perimeter) / self.perimeter
            va3 = (s3 % self.perimeter) / self.perimeter
            a1 = math.radians(-360 * va1)
            a2 = math.radians(-360 * va2)
            a3 = TAU-math.radians(360 * va3)

            c1 = Circle(radius=self.r1, color=self.color,
                        fill_color=RED, fill_opacity=1)
            c1.shift(UP*self.rr)
            c1.rotate(angle=a1, about_point=ORIGIN)

            c2 = Circle(radius=self.r1, color=self.color,
                        fill_color=BLUE, fill_opacity=1)
            c2.shift(UP*self.rr)
            c2.rotate(angle=a2, about_point=ORIGIN)

            arc1 = Arc(radius=self.rr, stroke_width=15, color=YELLOW,
                       start_angle=a1 + math.radians(90), angle=-a3)

            # tx = TexMobject("99s".format(t)).scale(4)
            tx = TexMobject("{:0.0f}s".format(t)).scale(4)
            new_group = VGroup(c1, c2, arc1, tx)
            group.become(new_group)
            return group

        self.play(UpdateFromAlphaFunc(g2, update2),
                  run_time=8, rate_func=linear)
        self.remove(arc1)
        self.wait(2)


class CircleChase2(Scene):
    """
00 各位好，
01 这又是一道典型的环形跑道追及问题
04 说甲乙两人在400米的环形跑道上同一起点同时背向起跑
08 40秒后相遇
11 若甲先从起点出发
13 半分钟后乙也从该点出发追赶甲
再过3分钟后乙追上甲
问甲乙两人的速度
16 解决这道题的关键，
19 是找到隐藏在问题中的等式关系。
21 那么，
22 做图、思考、想象一下他们是如何运动的。
26 如图可知，当甲追上乙的时候，
27 他们运动的时间相同，而不管乙跑了多远，
29 甲为了追上乙，总会比乙多跑黄色部分的距离。
34 而这个黄色弧线的长度，是已知的。
36 所以设未知数x为追及所需的时间，列等式。
40 等式左边，是甲跑过的距离为8x
44 等式右边，是乙跑过的距离为6x
46 因为甲比乙多跑黄色弧线的距离，
50 所以在等式右边加上弧线的长度，等式即成立。
54 通过解这个方程，就可以到答案……
56 仔细思考下，你……学会了么？
    """
    CONFIG = {
        "color": WHITE,
        "r1": 0.2,
        "r2": 0.2,
        "rr": 5,
        "v1": 60/13,
        "v2": 70/13,
        "t1": 40/30,
        "t2": 30/30,
        "t3": 180/30,
        "perimeter": 400/30,
        "txt": 9,
        "eq": 6.5
    }

    def construct(self):
        tp = TexMobject("S=400m").scale(1.5)
        tg = TexMobject("dist=8m").scale(1.5)
        t1 = TexMobject("t1=40s").scale(1.5)
        t2 = TexMobject("t2=30s").scale(1.5)
        t3 = TexMobject("t3=180s").scale(1.5)

        tv1 = TexMobject("v1={\\frac{60}{13}}m/s").scale(1.5)
        tv2 = TexMobject("v2={\\frac{70}{13}}m/s").scale(1.5)
        tp.move_to(self.txt * UP + LEFT * 3)
        t1.next_to(tp, DOWN, buff=0.3)
        t2.next_to(t1, DOWN, buff=0.3)
        t3.next_to(t2, DOWN, buff=0.3)
        tv1.move_to(self.txt * UP + RIGHT * 3)
        tv2.next_to(tv1, DOWN, buff=0.3)

        circler = Circle(radius=self.rr, color=self.color)
        self.add(circler)
        self.wait(4)
        trans1 = TransformFromCopy(circler, tp)
        self.play(trans1, FadeIn(tv1), FadeIn(tv2))
        # self.play(FadeIn(t1), FadeIn(t2), FadeIn(t3))

        c1 = Circle(radius=self.r1, color=self.color,
                    fill_color=RED, fill_opacity=1)
        c1.shift(UP*self.rr)

        c2 = Circle(radius=self.r1, color=self.color,
                    fill_color=BLUE, fill_opacity=1)
        c2.shift(UP*self.rr)

        self.play(FadeIn(c1), FadeIn(c2))
        self.wait(1)

        g1 = VGroup(c1, c2)

        def update1(group, alpha):
            t = alpha * self.t1  # 时间片
            s1 = self.v1 * t
            s2 = self.v2 * t
            va1 = (s1 % self.perimeter) / self.perimeter
            va2 = (s2 % self.perimeter) / self.perimeter

            a1 = math.radians(360 * va1)
            a2 = math.radians(-360 * va2)
            # print(t, s1, s2, a1, a2)

            c1 = Circle(radius=self.r1, color=self.color,
                        fill_color=RED, fill_opacity=1)
            c1.shift(UP*self.rr)
            c1.rotate(angle=a1, about_point=ORIGIN)

            c2 = Circle(radius=self.r1, color=self.color,
                        fill_color=BLUE, fill_opacity=1)
            c2.shift(UP*self.rr)
            c2.rotate(angle=a2, about_point=ORIGIN)

            new_group = VGroup(c1, c2)
            group.become(new_group)
            return group

        self.play(UpdateFromAlphaFunc(g1, update1),
                  run_time=self.t1, rate_func=linear)

        self.wait(1)
        self.play(FadeOut(c1), FadeOut(c2))

        # 第二轮
        c1 = Circle(radius=self.r1, color=self.color,
                    fill_color=RED, fill_opacity=1)
        c1.shift(UP*self.rr)

        c2 = Circle(radius=self.r1, color=self.color,
                    fill_color=BLUE, fill_opacity=1)
        c2.shift(UP*self.rr)
        self.play(FadeIn(c1), FadeIn(c2))
        self.wait(1)
        g1 = VGroup(c1, c2)

        def update2(group, alpha):
            t = alpha * self.t2  # 时间片
            s1 = self.v1 * t
            s2 = 0
            va1 = (s1 % self.perimeter) / self.perimeter
            va2 = (s2 % self.perimeter) / self.perimeter

            a1 = math.radians(-360 * va1)
            a2 = math.radians(-360 * va2)
            # print(t, s1, s2, a1, a2)

            c1 = Circle(radius=self.r1, color=self.color,
                        fill_color=RED, fill_opacity=1)
            c1.shift(UP*self.rr)
            c1.rotate(angle=a1, about_point=ORIGIN)

            c2 = Circle(radius=self.r1, color=self.color,
                        fill_color=BLUE, fill_opacity=1)
            c2.shift(UP*self.rr)
            c2.rotate(angle=a2, about_point=ORIGIN)

            new_group = VGroup(c1, c2)
            group.become(new_group)
            return group

        self.play(UpdateFromAlphaFunc(g1, update2),
                  run_time=self.t2, rate_func=linear)

        # 第二轮
        def update3(group, alpha):
            t = alpha * self.t3  # 时间片
            s1 = self.v1 * (t + self.t2)
            s2 = self.v2 * t
            va1 = (s1 % self.perimeter) / self.perimeter
            va2 = (s2 % self.perimeter) / self.perimeter

            a1 = math.radians(-360 * va1)
            a2 = math.radians(-360 * va2)
            # print(t, s1, s2, a1, a2)

            c1 = Circle(radius=self.r1, color=self.color,
                        fill_color=RED, fill_opacity=1)
            c1.shift(UP*self.rr)
            c1.rotate(angle=a1, about_point=ORIGIN)

            c2 = Circle(radius=self.r1, color=self.color,
                        fill_color=BLUE, fill_opacity=1)
            c2.shift(UP*self.rr)
            c2.rotate(angle=a2, about_point=ORIGIN)

            new_group = VGroup(c1, c2)
            group.become(new_group)
            return group

        self.play(UpdateFromAlphaFunc(g1, update3),
                  run_time=self.t3, rate_func=linear)

        self.wait(1)
        self.play(FadeOut(c1), FadeOut(c2))
