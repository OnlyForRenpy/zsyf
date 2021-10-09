init python:
    import copy
    class Char(object):
        def __init__(self, name, img="player", img_m="player", atk=5, dfn=0, lvl=1, exp=0, hpmax=60, mpmax=100, skills=[], p_skills=[], equip={'hand': None, 'head': None, 'chest': None, 'accs': None},
        condition={'burn': False, 'freeze': False, 'paral': False, 'poison': False, 'sleep': False, 'stun': False, 'confus': False, 'wound': False, 'rage': False}, turn=False, defending=False,
        dead=False, bonus_atk=0, bonus_dfn=0, img_pos=0, img_m_xpos=0, img_m_ypos=0, bar_pos=0, dmg_xpos=0, dmg_ypos=0):
            self.name = name
            self.img = img
            self.img_m = img_m
            self.atk = atk
            self.dfn = dfn
            self.lvl = lvl
            self.exp = exp
            self.hpmax = hpmax
            self._hp = 60
            self.mpmax = mpmax
            self._mp = 100
            self.skills = skills
            self.p_skills = p_skills
            self.equip = equip
            self.turn = turn
            self.defending = defending
            self.condition = condition
            self.dead = dead
            self.bonus_atk = bonus_atk
            self.bonus_dfn = bonus_dfn
            self.img_pos = img_pos
            self.img_m_xpos = img_m_xpos
            self.img_m_ypos = img_m_ypos
            self.bar_pos = bar_pos
            # self.dmg_pos = dmg_pos
            self.dmg_xpos = self.img_m_xpos + 20
            self.dmg_ypos = self.img_m_ypos - 60
        @property
        def hp(self):
            value = self._hp
            if not ( 0 <= value <= self.hpmax ):
                value = max( 0, min( self.hpmax, value ) )
                self._hp = value
            return self._hp
        @property
        def mp(self):
            value = self._mp
            if not ( 0 <= value <= self.mpmax ):
                value = max( 0, min( self.mpmax, value ) )
                self._mp = value
            return self._mp

        def addEquip(self, slot, item):
            if self.equip[slot] == None:
                self.equip[slot] = item
                renpy.say(None, "You equipped {0}.".format(self.equip[slot]))
            else:
                renpy.say(None, "Replacing {0} for {1}.".format(self.equip[slot],item))
        def removeEquip(self, slot, item):
            renpy.say(None, "Removed {0}.".format(self.equip[slot]))
            self.equip[slot] = None

define character.p1 = Character("p1")
default p1 = Char("p1")
define character.p2 = Character("p2")
default p2 = Char("p2")

define character.zmz_b = Character("钟明烛", image="zmz")
default zmz_b = Char("钟明烛", img_m="zmz", lvl=1, hpmax=200, img="zmz", skills=[yanzhou, yanshazhou, sanweizhenhuo, lianyuzhenhuo, qiliaoshu, zhenyuanhuti], p_skills=[passive2], equip={'hand': None, 'head': None, 'chest': None, 'accs': None})

define character.cl_b = Character("长离", image="cl")
default cl_b = Char("长离", img_m="cl", lvl=10, hpmax=300, img="cl", skills=[sanhuantaoyue, wanjianguizong, bahuangguiyuan, tianjian, jianchuhongmeng], p_skills=[passive2], equip={'hand': None, 'head': None, 'chest': None, 'accs': None})

define character.a = Character("Player", image="player")
default a = Char("Player", img_m="player", skills=[arrowhail, mindfreeze, thunderbolt], p_skills=[passive1], equip={'hand': "Bow", 'head': None, 'chest': None, 'accs': None})

define character.y = Character("Yu", image="yu")
default y = Char("Yu", img_m="yu", lvl=3, hpmax=102, img="yu", skills=[lavaburst, deathmissile, meteorshower, hellrage], p_skills=[radar], equip={'hand': None, 'head': None, 'chest': None, 'accs': None})

define character.c = Character("Chie", image="chie")
default c = Char("Chie", img_m="chie", lvl=4, hpmax=110, img="zmz", skills=[yanzhou, yanshazhou, sanweizhenhuo, lianyuzhenhuo, qiliaoshu, zhenyuanhuti], p_skills=[passive2], equip={'hand': None, 'head': None, 'chest': None, 'accs': None})

define character.f = Character("Fuuka", image="fuuka")
default f = Char("Fuuka", img_m="fuuka", lvl=5, hpmax=90, img="fuuka", skills=[iceball, lifedrain, devastationbeam, energybeams, giftofangels], p_skills=[passive1], equip={'hand': None, 'head': None, 'chest': None, 'accs': None})

define character.r = Character("Rise", image="rise")
default r = Char("Rise", img_m="rise", lvl=2, hpmax=130, img="rise", skills=[asteroid, swordofdeath, rockthrow, spikeshield, doubleattack], p_skills=[radar], equip={'hand': None, 'head': None, 'chest': None, 'accs': None})
