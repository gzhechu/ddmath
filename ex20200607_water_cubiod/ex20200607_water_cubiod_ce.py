#!/usr/bin/env python3

#
# 2021-01-06
# code fix for manim version 0.15.2
#

from manim import *
import math

# manim ex20200607_water_cubiod_ce.py WaterCubiod -p

# 长方体
class Cuboid(VGroup):
    def __init__(self, x=3, y=4, z=5, has_top=True, **kwargs):
        self.x = x
        self.y = y
        self.z = z
        self.has_top = has_top
        super().__init__(**kwargs)

    # def __str__(self):
    #     return str("class:{}, x:{}, y:{}, z:{}".format(self.name, self.x*10, self.y*10, self.z*10))

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
            face.rotate(angle=math.radians(90))
            face.shift(self.y * OUT / 2.0)
            face.apply_matrix(z_to_vector(vect))
            self.add(face)


class WaterCubiod(ThreeDScene):
    def construct(self):
        self.box_height = 60 * 0.1
        self.water_height = 50 * 0.1
        self.box_side = 60 * 0.1
        self.rod_height = 74 * 0.1
        self.sod_side = 15 * 0.1
        self.zshift = 24 * 0.1
        self.zdelta = 1.6 * 0.1
        self.txt = 11

        t1 = Tex(r"$l_{1}=60cm$").scale(1.5)
        t2 = Tex(r"$l_{2}=15cm$").scale(1.5)
        t3 = Tex(r"$h_{1}=50cm$").scale(1.5)
        t4 = Tex(r"$h_{2}=24cm$").scale(1.5)

        t1.move_to(UP*self.txt + LEFT*4)
        t2.next_to(t1, DOWN)
        t3.move_to(UP*self.txt + RIGHT*4)
        t4.next_to(t3, DOWN)

        cbox = Cuboid(x=self.box_side, y=self.box_side, z=self.box_height,
                      fill_color=WHITE, fill_opacity=0, has_top=False)
        cw = Cuboid(x=self.box_side, y=self.box_side, z=self.water_height, stroke_width=0,
                    fill_color=BLUE, fill_opacity=0.3,)
        cw.move_to(IN*(self.box_height-self.water_height)/2)

        csod1 = Cuboid(x=self.sod_side, y=self.sod_side, z=self.water_height, stroke_width=0,
                       fill_color=GOLD_C, fill_opacity=1.0,)
        csod1.move_to(IN*(self.box_height-self.water_height)/2)
        csod2 = Cuboid(x=self.sod_side, y=self.sod_side, z=0,
                       stroke_width=0, fill_color=GOLD_D, fill_opacity=1.0,)
        csod2.next_to(csod1, OUT, buff=0)
        csod3 = Cuboid(x=self.sod_side, y=self.sod_side, z=(self.rod_height-self.water_height),
                       stroke_width=0, fill_color=GOLD_E, fill_opacity=1.0,)
        csod3.next_to(csod2, OUT, buff=0)
        csod = VGroup(csod1, csod2, csod3)

        #  mark water line.
        cmark = cw.copy()
        cmark.set_fill(opacity=0)
        cmark.set_stroke(color=BLUE, width=4, opacity=1,)

        cc = VGroup(cbox, cw, csod)

        self.set_camera_orientation(phi=70 * DEGREES, theta=30*DEGREES)
        # self.play(FadeIn(cbox))
        self.add(cbox)
        self.wait(1)
        self.add_fixed_in_frame_mobjects(t1)
        self.play(Write(t1))

        self.play(Create(cw))
        self.wait(1)
        self.play(FadeIn(csod))
        # self.wait(1)
        self.add_fixed_in_frame_mobjects(t2)
        self.play(Write(t2))

        self.move_camera(phi=75*DEGREES, theta=15*DEGREES, run_time=2)
        # self.wait(1)
        self.add_fixed_in_frame_mobjects(t3)
        self.play(Write(t3))

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
                           fill_color=GOLD_C, fill_opacity=1.0,)
            csod1.move_to(IN*(self.box_height-z1)/2)

            csod2 = Cuboid(x=self.sod_side, y=self.sod_side, z=move+delta,
                           stroke_width=0, fill_color=GOLD_D, fill_opacity=1.0,)
            csod2.next_to(csod1, OUT, buff=0)
            csod3 = Cuboid(x=self.sod_side, y=self.sod_side, z=(self.rod_height-self.water_height),
                           stroke_width=0, fill_color=GOLD_E, fill_opacity=1.0,)
            csod3.next_to(csod2, OUT, buff=0)
            csod = VGroup(csod1, csod2, csod3)

            csod.shift(OUT*move)
            group.become(csod)
            return group

        trans2 = UpdateFromAlphaFunc(csod, update2)

        self.remove(cw)
        self.add_fixed_in_frame_mobjects(t4)
        self.play(trans1, trans2, Write(t4), run_time=3, rate_func=smooth)
        self.wait(1)

        ind1 = Indicate(csod2, color=RED, scale_factor=1.0)
        self.play(ind1)
        self.play(ind1)

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
                           fill_color=GOLD_C, fill_opacity=1.0,)
            csod1.move_to(IN*(self.box_height-z1)/2)

            csod2 = Cuboid(x=self.sod_side, y=self.sod_side, z=move+delta,
                           stroke_width=0, fill_color=GOLD_D, fill_opacity=1.0,)
            csod2.next_to(csod1, OUT, buff=0)
            csod3 = Cuboid(x=self.sod_side, y=self.sod_side, z=(self.rod_height-self.water_height),
                           stroke_width=0, fill_color=GOLD_E, fill_opacity=1.0,)
            csod3.next_to(csod2, OUT, buff=0)
            csod = VGroup(csod1, csod2, csod3)

            csod.shift(OUT*move)
            group.become(csod)
            return group

        trans4 = UpdateFromAlphaFunc(csod, update4)

        # 开始绕圈
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(3)
        self.play(trans3, trans4, run_time=5, rate_func=smooth)
        self.wait(6)
        self.stop_ambient_camera_rotation()

        # 拉近镜头，放大水线局部
        self.move_camera(phi=72*DEGREES, theta=100*DEGREES,
                         distance=9, run_time=3)
        self.wait(1)
        self.add(cmark)
        self.wait(1)

        self.play(trans1, trans2, run_time=3, rate_func=smooth)
        self.wait(1)

        self.move_camera(phi=75*DEGREES, distance=20, run_time=3)
        self.wait(1)

        csodx = Cuboid(x=self.sod_side, y=self.sod_side, z=self.zshift, color=WHITE,
                       stroke_width=0, fill_color=RED, fill_opacity=0.5,)
        csodx.next_to(csod3, OUT, buff=0)
        csodx.shift(IN*self.zshift*2)

        cwx = Cuboid(x=self.box_side, y=self.box_side,  z=self.zdelta, color=WHITE,
                     stroke_width=0, fill_color=RED, fill_opacity=0.5,)
        cwx.next_to(gw, OUT, buff=0)

        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(2)
        self.add(csodx)
        self.wait(3)

        self.remove(cmark)
        self.add(cwx)
        self.wait(3)
        self.stop_ambient_camera_rotation()

        # self.remove(cwx, csodx)
        # self.play(trans3, trans4, run_time=3, rate_func=smooth)
        # self.wait(1)
        # self.play(trans1, trans2, run_time=3, rate_func=smooth)
        # self.wait(1)
        self.move_camera(phi=85*DEGREES, run_time=3)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(7)

        ###################################################################
        # 第二阶段动画
        # 隐藏水痕迹
        self.remove(csodx, cwx)
        self.wait(3)

        t11 = Tex(r"$V=15^2 \times 24$").scale(2)
        t12 = Tex(r"$S=60^2-15^2$").scale(2)
        t13 = Tex(r"h=").scale(2)
        t14 = Tex(r"$\frac{V}{S}$").scale(2)
        t15 = Tex(r"$\frac{15^2\times 24}{60^2-15^2}$").scale(2)
        t16 = Tex(r"1.6cm").scale(2)
        t11.move_to(UP*7)
        t12.move_to(UP*7)
        t13.move_to(UP*7)
        t14.next_to(t13, RIGHT)

        # 显示水柱
        csody = csodx.copy()
        csody.set_fill(color=BLUE, opacity=0.2)
        csody.next_to(csod, IN, buff=0)

        self.play(FadeIn(csody), run_time=3)
        self.wait(3)

        # 水移动到表面的动画
        cwx.set_fill(color=BLUE, opacity=0.3)
        # 水流变换
        trans5 = TransformFromCopy(csody, cwx)
        self.remove(csody, cwx)
        self.play(trans4, trans5, run_time=3, rate_func=smooth)
        self.wait(2)

        trans6 = TransformFromCopy(cwx, csody)
        self.remove(csody, cwx)
        self.play(trans2, trans6, run_time=3, rate_func=smooth)
        self.wait(2)

        self.move_camera(phi=75*DEGREES, run_time=1)
        self.remove(csody, cwx)
        self.play(trans4, trans5, run_time=2, rate_func=smooth)
        self.wait(1)
        self.remove(csody, cwx)
        self.play(trans2, trans6, run_time=2, rate_func=smooth)
        self.move_camera(phi=85*DEGREES, run_time=1)
        self.wait(1)

        ind2 = Indicate(csody, color=RED, scale_factor=1.0)
        self.play(ind2)
        self.play(ind2)
        # 铁棒下移
        self.remove(csody, cwx)
        self.add_fixed_in_frame_mobjects(t11)  # 显示体积
        self.play(Write(t11), trans4, trans5, run_time=2, rate_func=smooth)
        self.wait(3)

        self.move_camera(phi=75*DEGREES, run_time=1)

        ind3 = Indicate(cwx, color=RED, scale_factor=1.0)
        self.play(ind3)
        self.play(ind3)
        self.remove(t11)
        self.add_fixed_in_frame_mobjects(t12)
        self.play(Write(t12))  # 显示面积
        self.wait(5)

        self.add_fixed_in_frame_mobjects(t13)
        self.add_fixed_in_frame_mobjects(t14)
        self.remove(t12)
        tg1 = VGroup(t13, t14)
        tg1.shift(LEFT*tg1.get_center())
        self.play(Write(t13), Write(t14))  # 高度公式
        self.wait(1)

        self.add_fixed_in_frame_mobjects(t15)
        self.remove(t14)
        t15.next_to(t13, RIGHT)
        self.play(Write(t15))  # 公式具体数值
        tg1 = VGroup(t13, t15)
        tg1.generate_target()
        tg1.target.shift(LEFT*tg1.get_center())
        move1 = MoveToTarget(tg1)
        self.play(move1)
        self.wait(1)

        self.add_fixed_in_frame_mobjects(t16)
        self.remove(t15)
        t16.next_to(t13, RIGHT)
        self.play(Write(t16))  # 结果
        tg1 = VGroup(t13, t16)
        tg1.generate_target()
        tg1.target.shift(LEFT*tg1.get_center())
        move1 = MoveToTarget(tg1)
        self.play(move1)
        self.wait(8)

        self.stop_ambient_camera_rotation()


class Test1(ThreeDScene):
    def construct(self):
        c1 = Cuboid(x=3, y=4, z=5, has_top=False,
                    fill_color=BLUE, fill_opacity=0.2,)
        c2 = Cuboid(x=6, y=1, z=3, color=RED,
                    fill_color=RED, fill_opacity=0.2,)

        self.set_camera_orientation(phi=75 * DEGREES, theta=-15*DEGREES)
        text3d = Tex(r"$V=15^2 \times 24$", font_size=120)
        text3d.to_corner(UL)

        self.play(FadeIn(c1))
        self.wait(5)
        self.begin_ambient_camera_rotation()
        self.add_fixed_in_frame_mobjects(text3d)  # <----- Add this
        self.play(Write(text3d))
        self.play(FadeIn(c2))
        self.wait(10)
