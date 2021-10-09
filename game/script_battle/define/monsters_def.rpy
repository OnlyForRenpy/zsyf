label load_monsters:
    # var = Monster(name, hpmax, atk, dfn, exp, lvl, img, sfx_atk, anim, skills)
    $ empty = Monster(None, 0, 0, 0, 0, 0, 0, 0, dead=True)
    $ mon1 = Monster("小幽灵", 20, 15, 1.0, 50, 3, "images/battle/monsters/小幽灵.png", "water", anim=idle_y, skills=[arrowhail])
    $ mon2 = Monster("小白雪人", 50, 20, 6.0, 50, 4, "images/battle/monsters/小白雪人.png", "pound", anim=idle_y, skills=[mindfreeze])
    $ mon3 = Monster("甲壳虫", 30, 40, 3.0, 50, 5, "images/battle/monsters/甲壳虫.png", "tackle", anim=idle_y, skills=[lifedrain])
    $ mon4 = Monster("花蘑菇", 25, 10, 10.0, 50, 4, "images/battle/monsters/花蘑菇.gif", "water", anim=idle_y, skills=[devastationbeam])
    $ mon5 = Monster("黑幽灵", 45, 35, 10.0, 50, 4, "images/battle/monsters/黑幽灵.png", "thunder", anim=idle_y, skills=[asteroid])
    $ mon6 = Monster("黑雪人", 70, 50, 9.0, 50, 8, "images/battle/monsters/黑雪人.gif", "fire", anim=idle_y, skills=[swordofdeath])
    $ mon7 = Monster("人参精", 15, 50, 7.0, 50, 5, "images/battle/monsters/人参精.png", "cut", anim=idle_y, skills=[rockthrow])
    $ mon8 = Monster("三眼章鱼", 55, 25, 2.0, 50, 4, "images/battle/monsters/三眼章鱼.gif", "scratch", anim=idle_y, skills=[mindburn])
    $ mon9 = Monster("大幽灵", 60, 40, 3.0, 50, 6, "images/battle/monsters/大幽灵.gif", "leaf", anim=idle_y, skills=[lavaburst])
    $ mon10 = Monster("土龙", 90, 95, 4.0, 50, 8, "images/battle/monsters/土龙.gif", "fire", anim=idle_y, skills=[deathmissile])

    $ boss_xiexiu = Monster("邪修", 85, 85, 5.0, 50, 5, "images/battle/monsters/邪修.png", "water", anim=idle_y, skills=[thunderbolt])
    return

init python:
    class Monster(object):
        def __init__(self, name, hpmax, atk, dfn, exp, lvl, img, sfx_atk, anim=idle_shake, skills=[], state=None, dead=False, finaldmg=0, slot=1, sprite_xpos=0, sprite_ypos=0,dmg_pos=(0,0)):
            self.name = name
            self.hpmax = hpmax
            self._hp = 0
            self._mp = 0
            self.atk = atk
            self.dfn = dfn
            #self.vel = vel
            self.state = state
            self.lvl = lvl
            self.exp = exp
            self.dead = dead
            self.skills = skills
            self.img = img
            self.sfx_atk = sfx_atk
            #self.sfx_cry = sfx_cry
            #self.sfx_die = sfx_die
            self.finaldmg = finaldmg
            self.slot = slot
            self.anim = anim
            self.sprite_xpos = sprite_xpos
            self.sprite_ypos = sprite_ypos
            self.dmg_pos = dmg_pos
            #self.rarity = rarity
        @property
        def hp(self):
            value = self._hp
            if not ( 0 <= value <= self.hpmax ):
                value = max( 0, min( self.hpmax, value ) )
                self._hp = value
            return self._hp
