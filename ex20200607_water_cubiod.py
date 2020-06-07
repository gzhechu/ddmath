#!/usr/bin/env python3

from manimlib.imports import *

# manim ddmath/ex20200607_water_cubiod.py WaterCubiod -r1280,720 -pm


# 长方体
class Cuboid(VGroup):
    CONFIG = {
        "x": 3,
        "y": 4,
        "z": 5,
        "has_top": True,
    }

    def __str__(self):
        return str("class:{}, x:{}, y:{}, z:{}".format(self.name, self.x*10, self.y*10, self.z*10))

    def generate_points(self):
        for vect in IN, OUT:
            if not self.has_top and vect is OUT:
                continue
            face = Rectangle(
                height=self.y, width=self.x,
                shade_in_3d=True,
            )
            face.flip()
            face.shift(self.z * OUT / 2.0)
            face.apply_matrix(z_to_vector(vect))
            self.add(face)
        for vect in LEFT, RIGHT:
            face = Rectangle(
                height=self.y, width=self.z,
                shade_in_3d=True,
            )
            face.flip()
            face.shift(self.x * OUT / 2.0)
            face.apply_matrix(z_to_vector(vect))
            self.add(face)
        for vect in UP, DOWN:
            face = Rectangle(
                height=self.x, width=self.z,
                shade_in_3d=True,
            )
            face.flip()
            face.shift(self.y * OUT / 2.0)
            face.apply_matrix(z_to_vector(vect))
            self.add(face)

    # def set_opacity(self, opacity):
    #     self.fill_opacity = opacity
    #     pass

    # def set_stroke_width(self, width):
    #     self.stroke_width = width
    #     pass


class WaterCubiod(ThreeDScene):
    CONFIG = {
        "box_height": 60 * 0.1,
        "water_height": 50 * 0.1,
        "box_side": 60 * 0.1,
        "rod_height": 74 * 0.1,
        "sod_side": 15 * 0.1,
        "zshift": 24 * 0.1,
        "zdelta": 1.6 * 0.1,
        "txt": 7,
    }

    def construct(self):
        # self.set_camera_orientation(phi=90 * DEGREES)
        # axes = ThreeDAxes(z_min=-8, z_max=8,)
        # text3d = TextMobject("This is a 3D text").scale(2)
        # self.add(axes, text3d)

        cbox = Cuboid(x=self.box_side, y=self.box_side, z=self.box_height,
                      fill_color=WHITE, fill_opacity=0,)
        cw = Cuboid(x=self.box_side, y=self.box_side, z=self.water_height, stroke_width=0,
                    fill_color=BLUE, fill_opacity=0.3,)
        cw.move_to(IN*(self.box_height-self.water_height)/2)

        csod1 = Cuboid(x=self.sod_side, y=self.sod_side, z=self.water_height, stroke_width=0,
                       fill_color=GOLD_C, fill_opacity=0.8,)
        csod1.move_to(IN*(self.box_height-self.water_height)/2)
        csod2 = Cuboid(x=self.sod_side, y=self.sod_side, z=0,
                       stroke_width=0, fill_color=GOLD_D, fill_opacity=0.8,)
        csod2.next_to(csod1, OUT, buff=0)
        csod3 = Cuboid(x=self.sod_side, y=self.sod_side, z=(self.rod_height-self.water_height),
                       stroke_width=0, fill_color=GOLD_E, fill_opacity=0.8,)
        csod3.next_to(csod2, OUT, buff=0)
        csod = VGroup(csod1, csod2, csod3)

        # water mark line.
        sqmark = Square(side_length=self.box_side, color=BLUE)
        sqmark.next_to(cw, OUT, buff=0)
        # cc = VGroup(cbox, cw, csod)

        self.set_camera_orientation(phi=75 * DEGREES, theta=30*DEGREES)
        self.play(FadeIn(cbox))
        self.wait(1)
        self.play(ShowCreation(cw))
        self.wait(1)
        self.play(FadeIn(csod))
        self.wait(1)

        def update1(group, alpha):
            delta = self.zdelta * alpha

            cw = Cuboid(x=self.box_side, y=self.box_side, z=self.water_height-delta, stroke_width=0,
                        fill_color=BLUE, fill_opacity=0.3,)
            cw.move_to(IN*(self.box_height-self.water_height+delta)/2)
            # print(cw)
            ng = VGroup(cw)
            group.become(ng)
            return group

        gw = VGroup(cw)
        trans1 = UpdateFromAlphaFunc(gw, update1)

        def update2(group, alpha):
            move = self.zshift * alpha
            delta = self.zdelta * alpha

            z1 = self.water_height - move - delta
            csod1 = Cuboid(x=self.sod_side, y=self.sod_side, z=z1, stroke_width=0,
                           fill_color=GOLD_C, fill_opacity=0.8,)
            csod1.move_to(IN*(self.box_height-z1)/2)

            csod2 = Cuboid(x=self.sod_side, y=self.sod_side, z=move+delta,
                           stroke_width=0, fill_color=GOLD_D, fill_opacity=0.8,)
            csod2.next_to(csod1, OUT, buff=0)
            csod3 = Cuboid(x=self.sod_side, y=self.sod_side, z=(self.rod_height-self.water_height),
                           stroke_width=0, fill_color=GOLD_E, fill_opacity=0.8,)
            csod3.next_to(csod2, OUT, buff=0)
            csod = VGroup(csod1, csod2, csod3)

            csod.shift(OUT*move)
            group.become(csod)
            return group

        trans2 = UpdateFromAlphaFunc(csod, update2)

        self.move_camera(phi=80*DEGREES, theta=15*DEGREES, run_time=3)

        self.remove(cw)
        self.play(trans1, trans2, run_time=3, rate_func=smooth)

        self.wait(1)
        ind1 = Indicate(csod2, color=RED, scale_factor=1.0)
        self.play(ind1)
        self.play(ind1)

        self.wait(5)

        def update3(group, alpha):
            delta = self.zdelta * (1-alpha)

            cw = Cuboid(x=self.box_side, y=self.box_side, z=self.water_height-delta, stroke_width=0,
                        fill_color=BLUE, fill_opacity=0.3,)
            cw.move_to(IN*(self.box_height-self.water_height+delta)/2)
            # print(cw)
            ng = VGroup(cw)
            group.become(ng)
            return group

        trans3 = UpdateFromAlphaFunc(gw, update3)

        def update4(group, alpha):
            move = self.zshift * (1-alpha)
            delta = self.zdelta * (1-alpha)

            z1 = self.water_height - move - delta
            csod1 = Cuboid(x=self.sod_side, y=self.sod_side, z=z1, stroke_width=0,
                           fill_color=GOLD_C, fill_opacity=0.8,)
            csod1.move_to(IN*(self.box_height-z1)/2)

            csod2 = Cuboid(x=self.sod_side, y=self.sod_side, z=move+delta,
                           stroke_width=0, fill_color=GOLD_D, fill_opacity=0.8,)
            csod2.next_to(csod1, OUT, buff=0)
            csod3 = Cuboid(x=self.sod_side, y=self.sod_side, z=(self.rod_height-self.water_height),
                           stroke_width=0, fill_color=GOLD_E, fill_opacity=0.8,)
            csod3.next_to(csod2, OUT, buff=0)
            csod = VGroup(csod1, csod2, csod3)

            csod.shift(OUT*move)
            group.become(csod)
            return group

        trans4 = UpdateFromAlphaFunc(csod, update4)

        self.play(trans3, trans4, run_time=3, rate_func=smooth)
        self.wait(1)

        self.move_camera(phi=85*DEGREES, theta=5*DEGREES,
                         distance=10, run_time=3)
        self.wait(1)
        self.play(FadeIn(sqmark))
        self.wait(1)

        self.play(trans1, trans2, run_time=3, rate_func=smooth)

        self.move_camera(phi=70*DEGREES, distance=20,
                         theta=15 * DEGREES, run_time=3)
        self.wait(1)

        csodx = Cuboid(x=self.sod_side, y=self.sod_side, z=self.zshift, color=WHITE,
                       stroke_width=2, fill_color=GOLD_A, fill_opacity=0.5,)
        csodx.next_to(csod3, OUT, buff=0)
        csodx.shift(IN*self.zshift*2)
        self.play(FadeIn(csodx))
        ind2 = Indicate(csodx, color=RED, scale_factor=1.0)
        self.play(ind2)

        cwx = Cuboid(x=self.box_side, y=self.box_side, color=WHITE,
                     z=self.zdelta, stroke_width=2, fill_opacity=0,)
        cwx.next_to(gw, OUT, buff=0)
        self.play(FadeOut(sqmark), FadeIn(cwx))
        self.wait(1)
        ind3 = Indicate(cwx, color=RED, scale_factor=1.0)
        self.play(ind3)
        self.wait(1)

        # self.remove(cwx, csodx)

        # self.play(trans3, trans4, run_time=3, rate_func=smooth)
        # self.wait(1)
        # self.play(trans1, trans2, run_time=3, rate_func=smooth)
        # self.wait(1)

        self.wait(5)


class Test(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES)

        c1 = Cuboid(has_top=False, stroke_width=3,
                    fill_color=WHITE, fill_opacity=0,)
        cw = Cuboid(z=3, stroke_width=0, fill_color=BLUE, fill_opacity=0.3,)
        cw.move_to(1*IN)
        cc = VGroup(c1, cw)
        self.play(ShowCreation(c1))
        self.wait(3)

        self.move_camera(phi=75*DEGREES, theta=-45*DEGREES, run_time=3)
        self.wait(1)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(1)
        self.play(ShowCreation(cw))
        cc.generate_target()
        cc.target.shift(IN*3)
        trans1 = MoveToTarget(cc)
        self.play(trans1)
        self.wait(10)
