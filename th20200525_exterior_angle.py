#!/usr/bin/env python3

from manimlib.imports import *
import numpy as np

# manimlib th20200525_exterior_angle.py ExteriorAngle -r1280,720 -pm


class ExteriorAngle(Scene):
    CONFIG = {
        "color": WHITE,
        "txt": 8,
    }

    def construct(self):
        [txtA, txtB, txtB1] = [TexMobject(X) for X in ["A", "B", "B'"]]
        eq1 = TexMobject("\\angle A+\\angle B=180^\\circ").scale(1.2)
        eq2 = TexMobject("\\angle B=\\angle B'").scale(1.2)
        eq1.move_to(UP*(self.txt))
        eq2.move_to(UP*(self.txt))

        sec_colors = [ORANGE, BLUE, RED, GREEN, YELLOW, PINK, PURPLE,
                      TEAL, GRAY, MAROON, GOLD, WHITE]

        def PolygonWithAngle(pts, scale=1, color=WHITE, opacity=0.2):
            ptsx = np.append(pts, pts[0])
            ptsx = ptsx.reshape(-1, 3)
            # print(ptsx)
            angles = []
            for i in range(np.size(pts, 0)):
                l = Line(ptsx[i], ptsx[i+1])
                ang = l.get_angle()
                angles.append(ang)

            anglex = []
            anglex.append(angles[-1])
            anglex.extend(angles)

            ptsx = pts*scale    # 缩放比例后的坐标
            poly = Polygon(*ptsx, color=color, fill_color=color,
                           fill_opacity=opacity)

            lines = []  # 角度反向放出去的延长线
            sectors = []  # 角度
            for i in range(np.size(pts, 0)):
                a1 = angles[i]+PI  # 延长的偏角度
                a2 = (anglex[i+1] - anglex[i]) % PI  # 绘制的角度
                pt = ptsx[i]
                l = Line(ORIGIN, 2*RIGHT)
                l.shift(pt)
                l.rotate(angle=a1, about_point=pt)
                lines.append(l)
                sec = Sector(outer_radius=0.8, color=sec_colors[i], fill_opacity=0.8,
                             start_angle=a1, angle=-a2)
                sec.shift(pt)
                sectors.append(sec)
            g = VGroup(poly, *lines, *sectors)
            return g

        pts1 = np.array([[3, -0.5, 0], [1, 3, 0], [-3, -0.5, 0]])
        pts2 = np.array([[-0.2, -2.3, 0], [3.1, -0.1, 0],
                         [1.1, 2.2, 0], [-2.9, 0.3, 0]])
        pts3 = np.array([[3.2, 0.6, 0], [1.8, 1.8, 0], [-1.2, 1.9, 0],
                         [-3.1, -0.1, 0], [-2.4, -1.6, 0],
                         [-0.2, -2.5, 0], [2.0, -2, 0]])

        triangle = Polygon(*pts1, color=WHITE, fill_color=WHITE,
                           fill_opacity=0.2)
        self.play(ShowCreation(triangle))
        self.wait(3)

        # compute angle
        angles = []
        for i in range(np.size(pts1, 0)-1):
            l = Line(pts1[i], pts1[i+1])
            ang = l.get_angle()
            angles.append(ang)

        a1 = angles[1]+PI  # 延长线的偏角度
        a2 = (angles[1] - angles[0]) % PI  # 绘制的角度

        pt = pts1[1]
        txtA.next_to(pt, DOWN, buff=1)
        txtB.next_to(pt, RIGHT, buff=1)
        txtB1.next_to(pt, LEFT, buff=1)

        # interior angle
        sec1 = Sector(outer_radius=0.8, color=sec_colors[0], fill_opacity=0.8,
                      start_angle=a1+PI, angle=(PI-a2))
        sec1.shift(pt)
        self.play(FadeIn(sec1), Write(txtA))
        self.wait(2)

        # exterior angle
        l1 = Line(pts1[0], pts1[1], color=BLUE)
        self.play(ShowCreation(l1))
        self.wait(1)
        l2 = Line(ORIGIN, 2*RIGHT, color=BLUE)
        l2.shift(pt)
        l2.rotate(angle=a1, about_point=pt)
        self.play(ShowCreation(l2))
        self.wait(2)
        sec2 = Sector(outer_radius=0.8, color=sec_colors[1], fill_opacity=0.8,
                      start_angle=a1, angle=-a2)
        sec2.shift(pt)
        self.play(FadeIn(sec2), Write(txtB), Write(eq1))
        self.wait(3)

        l3 = Line(ORIGIN, 2*RIGHT, color=BLUE)
        l3.shift(pt)
        l3.rotate(angle=angles[0], about_point=pt)
        sec3 = Sector(outer_radius=0.8, color=sec_colors[1], fill_opacity=0.8,
                      start_angle=a1-PI, angle=-a2)
        sec3.shift(pt)
        trans1 = ReplacementTransform(eq1, eq2)
        self.play(FadeIn(l3), FadeIn(sec3), FadeOut(sec2),
                  FadeIn(txtB1), FadeOut(txtB), trans1)
        self.wait(3)
        self.play(FadeOut(l3), FadeIn(sec2), FadeOut(
            sec3), FadeIn(txtB), FadeOut(txtB1))
        self.wait(3)

        g1 = VGroup(triangle, l1, l2, sec1, sec2)
        poly1 = PolygonWithAngle(pts1)
        self.play(FadeIn(poly1), FadeOut(g1), FadeOut(
            txtA), FadeOut(txtB), FadeOut(eq2))
        self.wait(3)

        def update1(group, alpha):
            scale = 1 - alpha
            ng = PolygonWithAngle(pts1, scale)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(poly1, update1),
                  run_time=10, rate_func=there_and_back)
        self.wait(1)

        poly1.generate_target()
        poly1.target.shift(UP*4)

        poly2 = PolygonWithAngle(pts2)
        poly2.shift(DOWN*3)

        self.play(MoveToTarget(poly1), ShowCreation(poly2))
        self.wait(1)

        def update2(group, alpha):
            scale = 1 - alpha
            p1 = PolygonWithAngle(pts1, scale)
            p1.shift(UP*4)
            p2 = PolygonWithAngle(pts2, scale)
            p2.shift(DOWN*3)
            ng = VGroup(p1, p2)
            group.become(ng)
            return group

        g = VGroup(poly1, poly2)
        self.play(UpdateFromAlphaFunc(g, update2),
                  run_time=5, rate_func=there_and_back)
        self.wait(1)

        def update3(group, alpha):
            scale = 1 - alpha
            p2 = PolygonWithAngle(pts3, scale)
            group.become(p2)
            return group

        poly3 = PolygonWithAngle(pts3)
        self.play(ReplacementTransform(g,  poly3))
        self.wait(2)
        self.play(UpdateFromAlphaFunc(poly3, update3),
                  run_time=5, rate_func=there_and_back)

        self.wait(3)
