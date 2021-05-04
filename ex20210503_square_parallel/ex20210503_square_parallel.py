#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# develop and render undder manim version 0.5.0
#

"""
manim ex20210503_square_parallel.py SquareParallel -r1280,720 -pqm
manim ex20210503_square_parallel.py SquareParallel -r640,360 -pql

ffmpeg -i SquareParallel.mp4 -i SquareParallel.m4a SquareParallelRelease.mp4 -y
"""

from manim import *


def Range(in_val, end_val, step=1):
    return list(np.arange(in_val, end_val+step, step))


class GetIntersections:
    def get_coord_from_proportion(self, vmob, proportion):
        return vmob.point_from_proportion(proportion)

    def get_points_from_curve(self, vmob, dx=0.005):
        coords = []
        for point in Range(0, 1, dx):
            dot = Dot(self.get_coord_from_proportion(vmob, point))
            coords.append(dot.get_center())
        return coords

    def get_intersections_between_two_vmobs(self, vmob1, vmob2,
                                            tolerance=0.05,
                                            radius_error=0.2,
                                            use_average=True,
                                            use_first_vmob_reference=False):
        coords_1 = self.get_points_from_curve(vmob1)
        coords_2 = self.get_points_from_curve(vmob2)
        intersections = []
        for coord_1 in coords_1:
            for coord_2 in coords_2:
                distance_between_points = get_norm(coord_1 - coord_2)
                if use_average:
                    coord_3 = (coord_2 - coord_1) / 2
                    average_point = coord_1 + coord_3
                else:
                    if use_first_vmob_reference:
                        average_point = coord_1
                    else:
                        average_point = coord_2
                if len(intersections) > 0 and distance_between_points < tolerance:
                    last_intersection = intersections[-1]
                    distance_between_previus_point = get_norm(
                        average_point - last_intersection)
                    if distance_between_previus_point > radius_error:
                        intersections.append(average_point)
                if len(intersections) == 0 and distance_between_points < tolerance:
                    intersections.append(average_point)
        return intersections


class SquareParallel(Scene, GetIntersections):
    """
这题太简单，没动力继续做了。
    """

    def construct(self):
        width = 4.0
        height = np.sin(np.deg2rad(28)) * width

        a = [-width, height, 0]
        b = [width, height, 0]
        c = [width, -height, 0]
        d = [-width, -height, 0]

        ptA = Dot(a)
        ptB = Dot(b)
        ptC = Dot(c)
        ptD = Dot(d)

        [txtA, txtB, txtC, txtD, txtE, txtF, txtG] = [
            Tex(X) for X in ["A", "B", "C", "D", "E", "F", "G"]]

        [txt1, txt2, txt3, txt4, txt5] = [
            Tex(X) for X in ["1", "2", "3", "4", "5"]]

        txtA.next_to(ptA, UL)
        txtB.next_to(ptB, UR)
        txtC.next_to(ptC, DR)
        txtD.next_to(ptD, DL)

        ptTxts = [txtA, txtB, txtC, txtD]
        vgTxts = VGroup(*ptTxts)

        vgPt = VGroup(ptA, ptB, ptC, ptD)

        # 正方形 及坐标网格
        rect = Rectangle(height=height*2.0,
                         width=width*2.0)
        self.play(FadeIn(vgPt), Create(rect))
        self.wait()
        # 显示顶点
        self.play(FadeIn(vgTxts))
        self.wait()

        lDB = Line(d, b)
        lAE = Line([0, 0, 0], [height*2.0, 0, 0])
        lAE.rotate_about_origin(angle=np.deg2rad(28))
        lAE.shift(height * UP + LEFT * width)
        e = lAE.get_end()
        # print(e)
        ptE = Dot(e)
        txtE.next_to(ptE, RIGHT)

        lAF = Line([0, 0, 0], [2.0 * height/np.sin(np.deg2rad(31)), 0, 0])
        lAF.rotate_about_origin(angle=np.deg2rad(-31))
        lAF.shift(height * UP + LEFT * width)
        f = lAF.get_end()
        # print(f)
        ptF = Dot(f)
        txtF.next_to(ptF, DR)

        lEF = Line(e, f)

        self.play(Write(lDB), Write(lAE), FadeIn(ptE), FadeIn(txtE),)
        self.wait()
        self.play(Write(lAF), Write(txtF))

        tADF = Polygon(a, d, f, color=BLUE, fill_opacity=0.2)
        self.play(Write(tADF))

        g = self.get_intersections_between_two_vmobs(lAF, lDB)[0]
        print(g)
        ptG = Dot(g)
        txtG.next_to(ptG, DOWN)
        self.play(Write(ptG), Write(txtG))

        direction = [-1/np.tan(np.deg2rad(31)), 1, 0]
        rotate1 = Rotate(tADF, angle=PI, axis=direction, about_point=a)
        self.play(FadeIn(lEF), rotate1, run_time=3)

        ang1 = Sector(outer_radius=1, color=BLUE, fill_opacity=0.5,
                      angle=np.deg2rad(28))
        ang1.shift(d)
        txt1.next_to(ang1, RIGHT)

        ang2 = Sector(outer_radius=1, color=RED, fill_opacity=0.5,
                      angle=np.deg2rad(-31))
        ang2.shift(a)
        txt2.next_to(ang2, RIGHT)

        ang3 = Sector(outer_radius=1, color=YELLOW, fill_opacity=0.5,
                      start_angle=np.deg2rad(180), angle=np.deg2rad(-31))
        ang3.shift(f)
        txt3.next_to(ang3, LEFT)

        ang4 = Sector(outer_radius=1, color=GREEN, fill_opacity=0.5,
                      start_angle=np.deg2rad(149), angle=np.deg2rad(-31))
        ang4.shift(f)
        txt4.next_to(ang4, UL)

        ra1 = RightAngle(lAE, lEF, other_angle=False)
        ang5 = RightAngle(lDB, lEF, other_angle=True)
        txt5.next_to(ang5, RIGHT)

        self.play(Write(ang1), Write(ang2), Write(ang3), Write(ang4))
        self.play(Write(txt1), Write(txt2), Write(txt3), Write(txt4))
        self.play(Write(ra1), Write(ang5), Write(txt5))

        self.play(Indicate(ang1), scale_factor=2)
        self.play(Indicate(ang2), scale_factor=2)
        self.play(Indicate(ang3), scale_factor=2)
        self.play(Indicate(ang4), scale_factor=2)
        # self.play(Indicate(ra1), scale_factor=2)
        self.play(Indicate(ang5), scale_factor=2)
        self.wait(5)
