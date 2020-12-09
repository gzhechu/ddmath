#!/usr/bin/env python3

from manimlib.imports import *
from random import shuffle, randrange

# manim ddmath/ex20201122_cut_rect.py CutRect1 -r1280,720 -pm
# manim ddmath/ex20201122_cut_rect.py CutRect1 -r640,360 -pl
# ffmpeg -i CutRect1.mp4 -i sound.m4a output.mp4

"""
ffmpeg -i voice.m4a -acodec copy v.aac -y
ffmpeg -i bg.m4a -acodec copy b.aac -y
cat b.aac v.aac >> sound.aac -y
ffmpeg -i sound.aac -acodec copy -bsf:a aac_adtstoasc sound.m4a -y
ffmpeg -i CutRect1.mp4 -i sound.m4a output.mp4
"""


class CutRect1(Scene):
    CONFIG = {
        "color": WHITE,
        "w": 5,
        "h": 3,
        "c": 1.6,
        "txt": 7,
    }

    def construct(self):
        rect = Rectangle(height=self.h*self.c, width=self.w*self.c, fill_color=BLUE,
                         fill_opacity=0.5)
        self.play(ShowCreation(rect))
        self.wait(1)

        [tx3, tx5] = [TexMobject(x).scale(2) for x in ["3", "5"]]
        tx3.move_to(LEFT*self.c*(1.5 + 1))
        tx5.move_to(UP*self.c*(2.5 + 1))

        pl = []
        for x in range(self.w + 1):
            pt = Dot()
            pt.move_to(UP*self.c*(1.5) + LEFT*self.c*(x-2.5))
            pl.append(pt)
            pt = Dot()
            pt.move_to(DOWN*self.c*(1.5) + LEFT*self.c*(x-2.5))
            pl.append(pt)
        for x in range(self.h + 1):
            pt = Dot()
            pt.move_to(UP*self.c*(x-1.5) + LEFT*self.c*(2.5))
            pl.append(pt)
            pt = Dot()
            pt.move_to(UP*self.c*(x-1.5) + RIGHT*self.c*(2.5))
            pl.append(pt)

        self.play(*[FadeIn(p, run_time=1.0) for p in pl])
        self.wait(3)

        c1 = Rectangle(height=self.c, width=self.c, fill_color=YELLOW,
                       fill_opacity=0.5)
        self.play(ShowCreation(c1))

        # scale to big size
        c2 = Rectangle(height=self.c*self.h, width=self.c*self.h, fill_color=YELLOW,
                       fill_opacity=0.5)
        c2.move_to(LEFT*self.c*(1))
        trans1 = TransformFromCopy(c1, c2)
        self.remove(c1)
        self.play(trans1)

        # scale to small size
        c1.move_to(UP*self.c*(1) + LEFT*self.c*(2))
        trans1 = TransformFromCopy(c2, c1)
        self.remove(c2)
        self.play(trans1)

        # scale to big size
        trans1 = TransformFromCopy(c1, c2)
        self.remove(c1)
        self.play(trans1)

        # move to right
        c2.generate_target()
        c2.target.shift(RIGHT*self.c*(2))
        trans1 = MoveToTarget(c2)
        self.play(trans1)

        # move to left
        c2.generate_target()
        c2.target.shift(LEFT*self.c*(2))
        trans1 = MoveToTarget(c2)
        self.play(trans1)
        rect_left = c2

        c2 = Rectangle(height=self.c*3, width=self.c*2)
        c2.move_to(RIGHT*self.c*1.5)
        self.play(FadeIn(c2))
        rect_right = c2

        self.wait(3)

        cl = []
        for x in reversed(range(self.w)):
            for y in reversed(range(self.h)):
                c = Rectangle(height=self.c, width=self.c, fill_color=RED,
                              fill_opacity=0.5)
                c.move_to(UP*self.c*(y-1) + LEFT*self.c*(x-2))
                cl.append(c)

        self.play(*[FadeIn(c, run_time=1.0) for c in cl])
        self.remove(rect_left, rect_right)
        for x in range(self.h * (self.w)):
            self.play(FadeIn(cl[x], run_time=0.06))
        self.play(FadeIn(rect_left), FadeIn(rect_right),
                  *[FadeOut(c, run_time=1.0) for c in cl])
        self.wait(3)


class Logo(Scene):
    def construct(self):
        # ======= params of the logo =======
        # Dimension of the maze
        w = 11
        h = 11
        dim = max(w, h)
        # random seed
        random.seed()
        # Scale of the maze
        scale = 3.0
        # Noise added on the line coordinate
        eps = 0.015

        # ======= Making the maze =======
        # First step : Find a code that creates a maze
        # from http://rosettacode.org/wiki/Maze_generation#Python
        # Border are stored into a list of list
        # First dim : vertical coordinate
        # Second    : horizontal coordinate

        # 2d visibility array
        vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
        # Vertical border
        ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
        # Horizontal border
        hor = [["+--"] * w + ['+'] for _ in range(h + 1)]
        # Walk fun

        def walk(x, y):
            vis[y][x] = 1
            d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            shuffle(d)
            for (xx, yy) in d:
                if vis[yy][xx]:
                    continue
                if xx == x:
                    hor[max(y, yy)][x] = "+  "
                if yy == y:
                    ver[y][max(x, xx)] = "   "
                walk(xx, yy)
        walk(randrange(w), randrange(h))
        # Adding the entrance / exit
        hor[0][int(w/2)] = '+  '
        hor[h][int(w/2)] = '+  '
        # Print it for debug
        s = ""
        for (a, b) in zip(hor, ver):
            s += ''.join(a + ['\n'] + b + ['\n'])
        print(s)

        # ======= Extracting the line of the maze =======
        # Create a maze centered at (0,0)
        line = []
        do_line = False
        ss = 0
        # Create the horizontal line
        for hh in range(h+1):
            for ww in range(w+1):
                # If we are on a wall and we are not drawing a line,
                # This is the begining, save the horizonal coordinate
                if hor[hh][ww] == "+--" and (not do_line):
                    ss = ww
                    do_line = True
                # If we find a bordel of a line and we are actually on a line
                if (hor[hh][ww] == "+  " or hor[hh][ww] == '+') and do_line:
                    do_line = False
                    # Save the line.
                    ll = Line(np.array([((ss/dim)-0.5)*scale + random.uniform(-eps, eps),
                                        ((hh/dim)-0.5)*scale + random.uniform(-eps, eps), 0]),
                              np.array([((ww/dim)-0.5)*scale + random.uniform(-eps, eps),
                                        ((hh/dim)-0.5)*scale + random.uniform(-eps, eps), 0]),
                              color=WHITE)
                    line.append(ll)

        # Create the vertical line
        # There is no final border, the last case should be taken into account.
        def is_wall(tt):
            return (tt == "|" or tt == "|  ")
        do_line = False
        ss = 0
        for ww in range(w+1):
            for hh in range(h):
                if (is_wall(ver[hh][ww]) and (not do_line)):
                    ss = hh
                    do_line = True
                if ((ver[hh][ww] == "   ") and do_line) or (hh == (h-1) and is_wall(ver[hh][ww])):
                    pad = 0
                    # If there is a line and this is the last element
                    if ((hh == (h-1) and is_wall(ver[hh][ww]))):
                        pad = 1
                    ll = Line(np.array([((ww/dim)-0.5)*scale + random.uniform(-eps, eps),
                                        ((ss/dim)-0.5)*scale + random.uniform(-eps, eps), 0]),
                              np.array([((ww/dim)-0.5)*scale + random.uniform(-eps, eps),
                                        (((hh+pad)/dim)-0.5)*scale + random.uniform(-eps, eps), 0]),
                              color=WHITE)
                    line.append(ll)
                    do_line = False
            ss = 0
            do_line = False

        # Shuffle the line array
        random.shuffle(line)
        for ll in line:
            ll.shift((scale/3)*UP)

        # Create two groupes of line
        # Divide the list into n partitions
        def chunks(lst, n):
            for i in range(0, len(lst), n):
                yield lst[i:i + n]
        line_c = chunks(line, int(len(line)/2) + 1)

        # Create the arrow and its background
        tip = Arrow(np.array([-scale, scale/3, 0]),
                    np.array([scale, scale/3, 0]), color=BLUE)
        rect = SurroundingRectangle(tip, color=BLACK)
        rect.set_fill(BLACK, opacity=1)
        rect.set_stroke(width=0)

        # Create Manim group of objects
        vg1 = VGroup(*next(line_c))
        vg2 = VGroup(*next(line_c))
        vg3 = VGroup(vg1, vg2, rect, tip)

        # ======= starting the animation ============
        # Start showing the two groupe of line
        for lll in [vg1, vg2]:
            self.play(*[
                ShowCreation(ll, run_time=1.0)
                for ll in lll
            ])
        # Add the background rectangle
        self.add(rect)
        self.wait(3)
        return
        # Draw the arrow
        self.play(Write(tip), run_time=1.5)

        # Rotation of the maze and arrow
        self.play(vg3.rotate, 25*DEGREES, about_point=np.array([0, 0]))

        # Drawing the text
        title1 = TextMobject("Random Access").next_to(
            Point(np.array([0, -scale/3, 0])), DOWN)
        title1.scale(1.6)
        title2 = TextMobject("Simplicity").next_to(title1, DOWN)
        title2.scale(1.8)
        self.play(Write(title1), Write(title2), run_time=1.5)
        self.wait(3)


class Test(Scene):
    def construct(self):
        sector1 = Sector(outer_radius=5, color=RED, angle=TAU / 4,
                         start_angle=np.deg2rad((np.arcsin(4/5)*180)/np.pi),
                         fill_opacity=0.5).shift(DOWN*2.5)
        self.play(ShowCreation(sector1))
        self.wait(2)
