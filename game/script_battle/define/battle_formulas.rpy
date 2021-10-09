# 所有的数值计算

init python:
    def atkAll():
        renpy.play(atk_sfx)
        renpy.pause(0.2, hard=True)
        for t in battle_monsters:   # 对所有怪
            if not t.dead:
                if accFormula(currentplayer, t):
                    dmgFormula(t)
                    t._hp -= t.finaldmg
                    t._mp -= mpdmg
        renpy.show_screen("monster_dmg")
        renpy.with_statement(s_trans)   # 转场

    def atkRow():
        renpy.play(atk_sfx)
        renpy.pause(0.2, hard=True)
        for t in picked_targs:      # 对列表里的怪
            if accFormula(currentplayer, t):
                dmgFormula(t)
                t._hp -= t.finaldmg
                t._mp -= mpdmg
                renpy.show_screen("monster_dmg")
                renpy.with_statement(s_trans)

    def atkEnemy():
        for t in picked_targs:
            renpy.play(atk_sfx)
            renpy.pause(0.2, hard=True)
            if accFormula(currentplayer, t):    # 对单个怪
                dmgFormula(t)
                t._hp -= t.finaldmg
                t._mp -= mpdmg
                renpy.show_screen("monster_dmg")
                renpy.with_statement(s_trans)
                afterFX(b_skill, t)

    # 对队友造成伤害，宝可梦式战斗
    def atkAlly():
        for t in picked_targs:
            renpy.play(atk_sfx)
            renpy.pause(0.2, hard=True)
            t._hp -= damage
            t._mp -= mpdmg
            renpy.with_statement(s_trans)

    def atkSelf():
        renpy.play(atk_sfx)
        renpy.pause(0.2, hard=True)
        currentplayer._hp -= damage
        currentplayer._mp -= mpdmg
        renpy.with_statement(s_trans)

    def Defend():
        currentplayer.defending = True
        renpy.play("sound/battle_system/battle/skills/defend.ogg")
        renpy.with_statement(vpunch)

    def Attack():
        global damage
        global message
        global msg_mons
        for t in picked_targs:
            damage = currentplayer.atk
            msg_mons = t.name
            message = "attack_skill"
            renpy.play("sound/battle_system/battle/skills/sword.ogg")
            renpy.pause(0.2, hard=True)
            if accFormula(currentplayer, t):
                t.state = "hit"
                dmgFormula(t)
                t._hp -= t.finaldmg
                t._mp -= mpdmg
                renpy.show_screen("monster_dmg")
                renpy.with_statement(hpunch)
                renpy.pause(0.2)
                t.state = None

    # 与命中相关的
    def accFormula(a, d):
        global miss_roll
        global message
        global atk_sfx
        global damage
        misschance = 0
        if d.lvl > a.lvl:
            misschance = d.lvl - a.lvl
        accuracy = 10 - int(misschance*0.7)
        miss_roll = renpy.random.randint(1, 10)
        if miss_roll > accuracy:
            missed_t.append(d)
            renpy.play(sfx_whoosh.draw())
            renpy.show_screen("monster_dmg")
            return False
        else:
            return True

    # 伤害计算，一般需要加一些随机数之类的
    def dmgFormula(m):
        global damage
        pre_dmg = int(damage*1.1 - (damage * renpy.random.randint(1, 20) / 100))
        m.finaldmg = int(pre_dmg*(100/(100+m.dfn)))
        hit_t.append(m)

    # 经验计算
    def expFormula():
        global players
        global curr_exp
        global monsters_total
        curr_exp = 0
        playersCnt()
        for m in battle_monsters:
            curr_exp += m.exp
            # if monsters_total > 0:
            #     curr_exp += m.exp
            #     monsters_total -= 1
        curr_exp /= players
        for p in battle_players:
            if p.hp > 0:
                p.exp += curr_exp
                # renpy.play("sound/battle_system/game/exp.ogg")
                renpy.say(None, "%s 获得 %i 经验值!" % (p.name, curr_exp))
                while p.exp >= (p.lvl+1)**3:
                    p.lvl += 1
                    # renpy.play("sound/battle_system/game/lvlup.ogg")
                    renpy.say(None, "%s 升到了等级 %i!" % (p.name, p.lvl))
