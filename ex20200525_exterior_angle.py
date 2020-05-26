#!/usr/bin/env python3

from manimlib.imports import *
import numpy as np

# manim ddmath/ex20200525_exterior_angle.py ExteriorAngle -r1280,720 -pm


class ExteriorAngle(Scene):
    CONFIG = {
        "color": WHITE,
        "txt": 9,
    }

    def construct(self):
        t1 = Text("多边形外角和", font="仿宋").set_color(BLUE).scale(2)
        t1.move_to(UP*(self.txt))
        self.play(Write(t1))
        self.wait(1)

        sec_colors = [TEAL, RED, YELLOW, BLUE, PINK, GREEN, PURPLE,
                      GRAY, MAROON, GOLD, ORANGE, WHITE]

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

            lines = []  # 放出去的延长线
            sectors = []  # 角度线
            for i in range(np.size(pts, 0)):
                a1 = angles[i]+PI  # 延长的偏角度
                a2 = (anglex[i+1] - anglex[i]) % PI  # 往顺时针绘制的角度
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
        pts2 = np.array([[-2.9, 0.3, 0], [-0.2, -2.3, 0],
                         [3.1, -0.1, 0], [1.1, 2.2, 0]])
        pts3 = np.array([[3.2, 0.6, 0], [1.8, 1.8, 0], [-1.2, 1.9, 0],
                         [-3.1, -0.1, 0], [-2.4, -1.6, 0],
                         [-0.2, -2.2, 0], [2.0, -2, 0]])

        poly = Polygon(*pts1, color=WHITE, fill_color=WHITE,
                       fill_opacity=0.2)
        self.play(ShowCreation(poly))
        self.wait(3)

        poly1 = PolygonWithAngle(pts1)
        self.play(ShowCreation(poly1), FadeOut(poly))
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

        g = VGroup(poly1, poly2)
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

        self.play(UpdateFromAlphaFunc(g, update2),
                  run_time=10, rate_func=there_and_back)
        self.wait(1)

        def update3(group, alpha):
            scale = 1 - alpha
            p2 = PolygonWithAngle(pts3, scale)
            group.become(p2)
            return group

        poly3 = PolygonWithAngle(pts3)
        self.play(ReplacementTransform(g,  poly3))
        self.wait(1)
        self.play(UpdateFromAlphaFunc(poly3, update3),
                  run_time=6, rate_func=there_and_back)

        self.wait(6)
