
###音乐渐变时间
define config.fade_music = 1.0

###图像变换
define config.say_attribute_transition = Dissolve(0.4)

###nvl变换
define config.adv_nvl_transition = Dissolve(0.4)
define config.nvl_adv_transition = Dissolve(0.4)

define config.developer = 'auto'
init -2000 python:
    import sys
    import math
    import time as pytime
    sys.setrecursionlimit(100000)
    ###注册音轨
    renpy.music.register_channel('second_sound', mixer="music", loop=False, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False)
    renpy.music.register_channel('third_sound', mixer="music", loop=False, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False)
    renpy.music.register_channel('second_music', mixer="music", loop=True, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False)
    renpy.music.register_channel('third_sound', mixer="music", loop=False, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False)
    def getTime():
        return pytime.localtime()
    class Blood(object):
        def __init__(self, theDisplayable, density=120.0, particleTime=1.0, dripChance=0.05, dripSpeedX=0.0, dripSpeedY=120.0, dripTime=180.0, burstSize=100, burstSpeedX=100.0, burstSpeedY=200.0, numSquirts=4, squirtPower=400, squirtTime=0.25):
            self.sm = SpriteManager(update=self.update)
            self.drops = []
            self.squirts = []
            self.displayable = theDisplayable
            self.density = density
            self.particleTime = particleTime
            self.dripChance = dripChance
            self.dripSpeedX = dripSpeedX
            self.dripSpeedY = dripSpeedY
            self.gravity = 800.0
            self.dripTime = dripTime
            self.burstSize = burstSize
            self.burstSpeedX = burstSpeedX
            self.burstSpeedY = burstSpeedY
            self.lastUpdate = 0
            self.delta = 0.0

            for i in range(burstSize): self.add_burst(theDisplayable, 0)
            for i in range(numSquirts): self.add_squirt(squirtPower, squirtTime)

        def add_squirt(self, squirtPower, squirtTime):
            angle = random.random() * 6.283
            xSpeed = squirtPower * math.cos(angle)
            ySpeed = squirtPower * math.sin(angle)
            self.squirts.append([xSpeed, ySpeed, squirtTime])

        def add_burst(self, d, startTime):
            s = self.sm.create(d)
            xSpeed = (random.random() - 0.5) * self.burstSpeedX + 20
            ySpeed = (random.random() - 0.75) * self.burstSpeedY + 20
            pTime = self.particleTime
            self.drops.append([s, xSpeed, ySpeed, pTime, startTime])

        def add_drip(self, d, startTime):
            s = self.sm.create(d)
            xSpeed = (random.random() - 0.5) * self.dripSpeedX + 20
            ySpeed = random.random() * self.dripSpeedY + 20
            pTime = self.particleTime
            self.drops.append([s, xSpeed, ySpeed, pTime, startTime])

        def update(self, st):
            delta = st - self.lastUpdate
            self.delta += st - self.lastUpdate
            self.lastUpdate = st

            sindex = 0
            for xSpeed, ySpeed, squirtTime in self.squirts:
                if st > squirtTime: self.squirts.pop(sindex)
                sindex += 1

            pindex = 0
            if st < self.dripTime:
                while self.delta * self.density >= 1.0:
                    self.delta -= (1.0 / self.density)
                    if random.random() >= 1 - self.dripChance: self.add_drip(self.displayable, st)
                    for xSpeed, ySpeed, squirtTime in self.squirts:
                        s = self.sm.create(self.displayable)
                        s.x += (random.random() - 0.5) * 5
                        s.y += (random.random() - 0.5) * 5
                        self.drops.append([s, xSpeed + (random.random() - 0.5) * 20, ySpeed + (random.random() - 0.5) * 20, self.particleTime, st])
            for s, xSpeed, ySpeed, particleTime, startTime in self.drops:
                if (st - startTime < particleTime):
                    s.x += xSpeed * delta
                    s.y += ySpeed * delta
                    self.drops[pindex][2] += self.gravity * delta
                else:
                    s.destroy()
                    self.drops.pop(pindex)
                pindex += 1
            return 0


# 屏幕震动效果
# Shake(position, duration, maximum distance) with 'position' being a tuple of 4 values : x-position, y-position, xanchor, yanchor.
init:
    python:
        import math
        class Shaker(object):
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to integers.
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x
                # 因为是关于屏幕的，所以把以下几个数都转化为整数(开始的点)
                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]
                xpos = xpos - xanchor
                ypos = ypos - yanchor
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                return (int(nx), int(ny), 0, 0)
        def _Shake_screen(start, time, child=None, dist=100.0, **properties):
            move = Shaker(start, child, dist=dist)
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        class Noder(object):
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to integers.
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x
                # 因为是关于屏幕的，所以把以下几个数都转化为整数(开始的点)
                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]
                xpos = xpos - xanchor
                ypos = ypos - yanchor
                # nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                if t < 0.5:
                    ny = ypos + t * 2 * self.dist
                else:
                    ny = ypos + (1.0 - t) * 2 * self.dist
                return (0, int(ny), 0, 0)
        def _Nod_screen(start, time, child=None, dist=100.0, **properties):
            move = Noder(start, child, dist=dist)
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        class ShookHead(object):
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to integers.
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x
                # 因为是关于屏幕的，所以把以下几个数都转化为整数(开始的点)
                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]
                xpos = xpos - xanchor
                ypos = ypos - yanchor
                # nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                if t < 0.25:
                    nx = xpos + t * 4 * self.dist
                elif t < 0.75:
                    nx = xpos + (0.5 - t) * 4 * self.dist
                else:
                    nx = xpos + (t - 1.0) * 4 * self.dist
                return (int(nx), 0, 0, 0)
        def _Shookhead_screen(start, time, child=None, dist=100.0, **properties):
            move = ShookHead(start, child, dist=dist)
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake_screen = renpy.curry(_Shake_screen)
        Nod_screen = renpy.curry(_Nod_screen)
        Shookhead_screen = renpy.curry(_Shookhead_screen)


init python:
    # -*- coding: UTF-8 -*-
    import re

    # 排序关键字匹配
    # 匹配开头数字序号
    def sort_key(s):
        if s:
            try:
                c = re.findall('\d+', s)[0]
            except:
                c = -1
        return int(c)

    def strsort(alist):
        alist.sort(key=sort_key)
        return alist

    class SquenceAnimator(renpy.Displayable):
        def __init__(self, path, prefix="", suffix="", begin_index=0, end_index=0, interval=0.12, loop=True, **kwargs):
            super(SquenceAnimator, self).__init__(**kwargs)
            self.path = path
            self.prefix = prefix
            self.suffix = suffix
            self.begin_index = begin_index
            self.end_index = end_index
            self.length = end_index - begin_index
            self.interval = interval
            self.loop = loop

            self.sequence = []
            if not self.prefix: # 如果没有输入文件的前缀，就读取文件夹里所有的图片
                resource_list = renpy.list_files()
                for resource in resource_list:
                    i = re.search(r'(%s/.*?)' %path, resource)
                    if i:
                        self.sequence.append(resource)
                # 按数字大小排列
                self.sequence = strsort(self.sequence)
                for i in range(len(self.sequence)):
                    self.sequence[i] = renpy.displayable(self.sequence[i])
            else:
                for i in range(begin_index, end_index+1):
                    self.sequence.append(renpy.displayable(self.path + "/" + self.prefix + str(i) + "." + self.suffix))

            if self.length <= 0:
                self.length = len(self.sequence) - 1
            else:
                self.sequence = self.sequence[self.begin_index: self.end_index]

            # self.length -= 1
            self.current_index = 0
            self.show_timebase = 0

        def render(self, width, height, st, at):
            if (st >= (self.show_timebase + self.interval)):
                self.show_timebase = st
                self.current_index += 1
                if self.current_index >= self.length:
                    if self.loop:
                        self.current_index = 0
                    else:
                        self.current_index = self.length

            render = renpy.render(self.sequence[self.current_index], width, height, st, at)
            renpy.redraw(self, 0)

            return render

    # class SquenceAnimator2(renpy.Displayable):
    #
    #     def __init__(self, path, prefix, suffix, begin_index, end_index, interval, loop=True, **kwargs):
    #         super(SquenceAnimator2, self).__init__(**kwargs)
    #         self.path = path
    #         self.prefix = prefix
    #         self.suffix = suffix
    #         self.begin_index = begin_index
    #         self.end_index = end_index
    #         self.length = end_index - begin_index - 1
    #
    #
    #         self.sequence = []
    #         for i in range(begin_index, end_index+1):
    #             self.sequence.append(renpy.displayable(self.path + "/" + self.prefix + str(i) + "." + self.suffix))
    #
    #         self.current_index = 0
    #         self.show_timebase = 0
    #
    #         self.interval = interval
    #         self.loop = loop
    #
    #     def render(self, width, height, st, at):
    #         if (st >= (self.show_timebase + self.interval)):
    #             self.show_timebase = st
    #             self.current_index += 1
    #             if self.current_index >= self.length:
    #                 if self.loop:
    #                     self.current_index = 0
    #                 else:
    #                     self.current_index = self.length
    #
    #         render = renpy.render(self.sequence[self.current_index], width, height, st, at)
    #         renpy.redraw(self, 0)
    #
    #         return render

# 显示暗图像
init -10 python:
    def darken(s):
        return im.MatrixColor(s, im.matrix.tint(0.5, 0.5, 0.5))
    config.displayable_prefix["dark"] = darken
