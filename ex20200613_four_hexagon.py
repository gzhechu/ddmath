#!/usr/bin/env python3

from manimlib.imports import *

# manim ddmath/ex20200613_four_hexagon.py SizeOfTriangle -r1280,720 -pm


class SizeOfTriangle(Scene):
    CONFIG = {
        "a": 7,
        "radius": 2.5
    }

    def sub_triangles(self, center, hex):
        pts = hex.get_vertices()
        # print(pts)
        pts = np.append(pts, pts[0])
        # print(pts)
        pts = pts.reshape(7, 3)
        # print(pts)
        tris = []
        for i in range(6):
            t = Polygon(center, pts[i], pts[i+1],
                        fill_opacity=0,)
            t.set_stroke(color=WHITE, width=1.5, opacity=0.5)
            tris.append(t)
        return tris

    def construct(self):
        # origin = Dot()
        # self.play(FadeIn(origin))
        # self.wait(1)
        h1 = RegularPolygon(n=6, color=WHITE, radius=self.radius)
        height = h1.get_vertices()[1][1]
        h2 = h1.copy()
        h1.shift(UP*height+LEFT*self.radius)
        h2.shift(UP*height+RIGHT*self.radius)
        h3 = h1.copy().shift(DOWN*height*2)
        h4 = h2.copy().shift(DOWN*height*2)
        ptCenter1 = h1.get_center()
        ptCenter2 = h2.get_center()
        ptCenter3 = h3.get_center()
        ptCenter4 = h4.get_center()
        sts1 = self.sub_triangles(ptCenter1, h1)
        sts2 = self.sub_triangles(ptCenter2, h2)
        sts3 = self.sub_triangles(ptCenter3, h3)
        sts4 = self.sub_triangles(ptCenter4, h4)
        sts = [*sts1, *sts2, *sts3, *sts4]
        hexs = [h1, h2, h3, h4]
        self.add(h1, h2, h3, h4)
        self.wait(8)
        inds = [h.copy().set_opacity(0.5).set_color(YELLOW) for h in hexs]
        ginds = VGroup(*inds)
        for h in inds:
            self.play(FadeIn(h), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(ginds), run_time=1)

        ptX0 = h1.get_vertices()[0]
        ptX1 = h1.get_vertices()[1]
        ptX2 = h3.get_vertices()[4]
        ptX3 = h4.get_vertices()[0]
        ptX4 = h4.get_vertices()[1]
        tri = Polygon(ptX1, ptX2, ptX3, fill_opacity=0.5, color=BLUE)
        tr0 = Polygon(ptX0, ptCenter3, ptCenter4, fill_opacity=0.5, color=BLUE)
        tr1 = Polygon(ptX1, ptCenter4, ptX3, fill_opacity=0.5, color=RED)
        tr2 = Polygon(ptX1, ptX2, ptX0, fill_opacity=0.5, color=YELLOW)
        tr3 = Polygon(ptCenter3, ptX2, ptX3, fill_opacity=0.5, color=WHITE)
        gtris = VGroup(tr0, tr1, tr2, tr3)
        trOne = Polygon(ptCenter4, ptX3, ptX4, fill_opacity=0.5, color=RED)

        self.play(FadeIn(tri))
        self.wait(12)
        self.play(FadeIn(gtris), FadeOut(tri))
        self.wait(6)

        # ptX11 = ptX1 * UP + ptCenter4 * RIGHT
        dotX = Dot(ptX1)
        self.play(FadeIn(dotX))
        g1 = VGroup(dotX, tr1)

        def update1(group, alpha):
            ptx = ptX1*UP+(ptCenter4*RIGHT + ptX1*LEFT*2)*alpha - ptX1*LEFT
            dot = Dot(ptx)
            tr = Polygon(ptx, ptCenter4, ptX3,
                         fill_opacity=0.5, color=RED)
            ng = VGroup(dot, tr)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(g1, update1),
                  run_time=3, rate_func=smooth)

        self.play(*[FadeIn(o)for o in sts])

        def update2(group, alpha):
            ptx = ptX1*UP+(ptCenter4*RIGHT + ptX1*LEFT*2)*(1-alpha) - ptX1*LEFT
            dot = Dot(ptx)
            tr = Polygon(ptx, ptCenter4, ptX3,
                         fill_opacity=0.5, color=RED)
            ng = VGroup(dot, tr)
            group.become(ng)
            return group

        self.play(UpdateFromAlphaFunc(g1, update2),
                  run_time=6, rate_func=there_and_back)

        self.play(FadeIn(trOne))
        ind1 = Indicate(trOne, color=YELLOW, scale_factor=1.0)
        self.play(ind1)
        self.play(ind1)
        self.play(FadeOut(trOne))
        self.wait(2)

        ind2 = Indicate(tr2, color=RED, scale_factor=1.0)
        ind3 = Indicate(tr3, color=RED, scale_factor=1.0)
        self.play(ind2)
        self.play(ind2)
        self.play(ind3)
        self.play(ind3)
        self.wait(1)

        self.play(*[FadeOut(o)for o in sts])
        self.play(FadeOut(gtris), FadeOut(dotX))
        self.play(FadeIn(tri))

        self.wait(3)


class Test(Scene):
    def construct(self):
        pass
