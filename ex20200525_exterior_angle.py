#!/usr/bin/env python3

from manimlib.imports import *
import numpy as np

# manim ddmath/ex20200525_exterior_angle.py ExteriorAngle -r1280,720 -pm


class ExteriorAngle(Scene):
    CONFIG = {
        "color": WHITE,
        "txt": 7,
    }

    def construct(self):
        t1 = TextMobject("AB=8,BC=6").set_color(WHITE).scale(1.5)
        t1.move_to(UP*(self.txt))
        # self.play(Write(t1))
        # self.wait(1)

        def PolygonWithAngle(pts, scale=1, color=BLUE, opacity=0.2):
            ptsx = np.append(pts, pts[0])
            print(ptsx)
            angle = []
            slope = []
            lines = []
            for i in range(np.size(pts, 0)):
                j = i + 1
                k = j + 1
                l = Line(ptsx[3*i:3*j], ptsx[3*j:3*k])
                angle.append(l.get_angle())
                s = l.get_slope()
                slope.append(s)
                pt = pts[i]
                pt2 = pt + LEFT * s + UP
                l = Line(pt, pt2, color=color)
                lines.append(l)

            print(angle)
            print(slope)
            poly = Polygon(*(pts*scale), fill_color=color,
                           fill_opacity=opacity)
        
            g = VGroup(poly, *lines)

            return g

        pts = np.array([[3, 0, 0], [1, 3, 0], [-2, 0, 0]])
        pts = np.array([[3, 0, 0], [1, 3, 0], [-2, 0, 0], [1, -2, 0]])
#        pts = ((3, 0, 0), (1, 3, 0), (-2, 0, 0), (1,-2,0))
        poly = PolygonWithAngle(pts)
        self.play(ShowCreation(poly))
        self.wait(3)

        poly2 = PolygonWithAngle(pts, 0.5, color=RED)
        self.play(ReplacementTransform(poly, poly2))
        self.wait(3)

# a = [0, 0]
# b = [1, 2, 0]
# print(b[0]*RIGHT, b[1]*UP)
# print(UR)
# print(UR*UP)
