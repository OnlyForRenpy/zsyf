
# 核心函数
label battle:
    call load_setup from _call_load_setup
    $ stopEvent()
    if fixedset:
        $ monstersFixed()
        $ monster_slot = [m1,m2,m3,m4,m5,m6]
        $ fixedset = None
    else:
        $ monstersRoll()
        $ monster_slot = [m1,m2,m3,m4,m5,m6]
        $ renpy.random.shuffle(monster_slot)
    $ asignPos()    # 给slot分配位置
    # 一场战斗的全局变量
    $ row1btn = False
    $ row2btn = False
    $ missed_t = []
    $ win = False
    $ battleEnd = False
    $ monsters_dead = 0
    $ currentplayer = None
    show screen battle_tooltip      # 显示tooltip

    call battle_music from _call_battle_music

    random:
        scene bb1
        scene bb2
        scene bb3
    with Fade(0.5, 0.0, 0.5, color="#000")

    $ set_player_head_pos()
    show screen display_monsters with diss
    # show screen battle_message
    show screen battle_overlay with diss    # 人物screen
    # jump battling

init python:
    def set_player_head_pos():
        if p1:
            battle_players.append(p1)
            p1.img_pos = 210   # 调整头像的x坐标
            p1.img_m_xpos = 790
            p1.img_m_ypos = 380
            p1.bar_pos = 440   # 调整UI的x坐标
            p1.dmg_xpos = p1.img_m_xpos + 220  # 伤害数字显示位置
            p1.dmg_ypos = p1.img_m_ypos
        if p2:
            battle_players.append(p2)
            p2.img_pos = -120
            p2.img_m_xpos = 650
            p2.img_m_ypos = 430
            p2.bar_pos = 110
            p2.dmg_xpos = p2.img_m_xpos + 220
            p2.dmg_ypos = p2.img_m_ypos
        if p3:
            battle_players.append(p3)
            p3.img_pos = 640
            p3.img_m_xpos = 930
            p3.img_m_ypos = 330
            p3.bar_pos = 760
            p3.dmg_xpos = p3.img_m_xpos + 220
            p3.dmg_ypos = p3.img_m_ypos
        return

screen select_p1():
    style_prefix "confirm"
    frame:
        yalign 0.2
        has vbox:
            label "选择人物1"
            for c in party_list:
                if c != a:
                    textbutton "[c.name]" xalign 0.5 action Return(c)
            textbutton "None" xalign 0.5 action Return("none")

screen select_p2():
    style_prefix "confirm"
    frame:
        yalign 0.2
        has vbox:
            label "选择人物2"
            for c in party_list:
                if c != p1 and c != a:
                    textbutton "[c.name]" xalign 0.5 action Return(c)
            textbutton "None" xalign 0.5 action Return("none")

screen battle_tooltip():
    zorder 20
    $ tooltip = GetTooltip()
    if tooltip:
        timer 1 action SetVariable("tt_timer", True)
        if tt_timer:
            add MouseTooltip()
            $ mouse_pos = renpy.get_mouse_pos()
            $ renpy.set_mouse_pos(mouse_pos[0], mouse_pos[1])
    else:
        timer 0.001 action SetVariable("tt_timer", False)

screen battle_overlay():
    fixed:
        xoffset 140
        for p in battle_players:
            # if currentplayer == p:
            #     add p.img + "_head" yalign 1.0 xpos p.img_pos at char_sway
            #     add p.img_m + "_battle" xpos p.img_m_xpos ypos p.img_m_ypos
            # else:
            # 根据设置的位置显示头像和血条UI
            imagebutton:
                at transform:
                    zoom 0.6
                focus_mask True
                yalign 1.0 xpos p.img_pos
                idle p.img + "_head"
                tooltip "{0}\n攻击: {1}\n防御: {2}\n{3}".format(p.name, p.atk, p.dfn, p.p_skills[0].name)
                action  Function(playerAction(p))
            fixed:
                pos p.bar_pos, 600
                vbox:
                    if currentplayer == p:
                        text "[p.name!u]" anchor (1.0,1.0) yoffset 20 xoffset 100 style_group "battle_playername" color "#ffcc66"
                    else:
                        text "[p.name!u]" anchor (1.0,1.0) yoffset 20 xoffset 100 style_group "battle_playername"
                    text "LVL.[p.lvl] " anchor (1.0,1.0) yoffset 0 xoffset 100 style_group "battle_playerlvl"
                    fixed:
                        xoffset 24
                        yoffset -24
                        bar style "bar_hp" value AnimatedValue(value=p.hp, range=p.hpmax, delay=0.25) xanchor .5
                        bar style "bar_mp" value AnimatedValue(value=p.mp, range=p.mpmax, delay=0.25) xanchor .5 yalign 0.05
                        text "[p.hp]/[p.hpmax]" xanchor .5 yalign 0.0075 size 16
                        text "[p.mp]/[p.mpmax]" xanchor .5 yalign 0.0575 size 16
            # 根据设置的位置战斗模型
            add p.img_m + "_battle" xpos p.img_m_xpos ypos p.img_m_ypos

screen display_monsters():
    fixed:
        pos (150, 200)
        for m in monster_slot[0:3]:
            fixed:
                xpos m.sprite_xpos
                ypos m.sprite_ypos
                if not m.dead:
                    imagebutton at m.anim:
                        hover im.MatrixColor(getImage(m), im.matrix.brightness(0.1))
                        action Return(m), SensitiveIf(canTarget(m))
                        idle monsterImg(m) anchor (0.5,1.0) yoffset -20
                        if renpy.get_screen("select_monster"):
                            insensitive im.MatrixColor(getImage(m), im.matrix.saturation(0.1))
                        tooltip "{0}\nHP: {1}".format(m.name, m.hp)
                    bar style "bar_mhp" value AnimatedValue(value=m.hp, range=m.hpmax, delay=0.25) anchor (0.5,1.0)
                    text "[m.hp]" xanchor 0.5 yoffset -15 size 16
    fixed:
        pos (330, 330)
        for m in monster_slot[3:6]:
            fixed:
                xpos m.sprite_xpos
                ypos m.sprite_ypos
                if not m.dead:
                    imagebutton at m.anim:
                        hover im.MatrixColor(getImage(m), im.matrix.brightness(0.1))
                        action Return(m), SensitiveIf(canTarget(m))
                        idle monsterImg(m) anchor (0.5,1.0) yoffset -20
                        if renpy.get_screen("select_monster"):
                            insensitive im.MatrixColor(getImage(m), im.matrix.saturation(0.1))
                        tooltip "{0}\nHP: {1}".format(m.name, m.hp)
                    bar style "bar_mhp" value AnimatedValue(value=m.hp, range=m.hpmax, delay=0.25) anchor (0.5,1.0)
                    text "[m.hp]" xanchor 0.5 yoffset -15 size 16

screen battle_message():
    add "images/battle/battle/messagebox.png" xcenter 0.5
    hbox:
        xcenter 0.5 ypos 30
        if message == "attack":
            text "Who will attack?"
        elif message == "skill":
            text "What will {0} do?".format(currentplayer.name)
        elif message == "item":
            text "Select an item"
        elif message == "other_skill":
            text "[msg_skill]".format(currentplayer.name)
        elif message == "attack_skill":
            text "{0} attacked [msg_mons]!".format(currentplayer.name)
        elif message == "defend":
            text "{0} raises defense!".format(currentplayer.name)
        elif message == "m_skill":
            text "[msg_mons] attacks with [msg_skill]!"
        elif message == "m_atk":
            text "[msg_mons] attacks {0}!".format(roll_target.name)
        elif message == "target_who":
            text "Who is the target?"
        elif message == "m_dead":
            text "[msg_mons] died!"
        elif message == "player_ko":
            text "[koplayer] is out of combat!"
        elif message == "you_win":
            text "Congrats! You've won!"
        elif message == "lost":
            text "You lost..."
        elif message == "use_on_who":
            text "Use skill on whom?"
        elif message == "none":
            text ""

label battling:
    $ inCombat = True
    while inCombat:
        if battleEnd == True:
            $ inCombat = False
            jump end_battle
        # 初始化一些战斗参数
        $ startPlayersTurn()
        $ message = "attack"
        call turn_actions from _call_turn_actions
        $ message = "none"
        $ monsterTurns()

label end_battle:
    hide screen battle_overlay
    with dissolve
    if win:
        stop music
        play sound fanfare
        # "You win!"
        # stop sound
        $ expFormula()

        hide screen display_monsters
        hide screen battle_overlay
        $ partyRevive()
        if is_in_wild:
            call screen map_screen(current_map)

    else:
        stop music
        play sound failure
        hide screen display_monsters
        hide screen battle_overlay
        scene failure with dissolve
        $ renpy.pause(5, hard=True)
        $ partyRevive()
        $ renpy.full_restart()
        # jump main_menu
        # screen main_menu

    # hide screen battle_message
    # hide screen display_monsters
    # hide screen battle_overlay
    # $ partyRevive()
    # return
