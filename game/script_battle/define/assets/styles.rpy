style pixel:
    font "FZKTJW.TTF"
    outlines [(3, "#658791", 1, 1)]
    color "#b4c5cb"
    size 20

style dmg_text:
    font "FZKTJW.TTF"
    color "#f00"
    size 30
    outlines [(4.5, "#ffffff", 3.5, 3.5)]

style battle_playerlvl_text:
    font "FZKTJW.TTF"
    color "#ffffff"
    outlines [(2, "#00000080", 1, 1)]
    size 16

style battle_playername_text:
    font "FZKTJW.TTF"
    outlines [(4, "#00000025", 2, 2), (2, "#900c3f", 0, 0)]
    color "#ff5733"
    size 24

style skills_button_text:
    size 30
    anchor (.5,.5)
    align (.5,.5)

init python:
    style.bar_mhp = Style(style.default)
    style.bar_mhp.left_bar = Frame("images/battle/battle/mhp_full.png", 0, 0)
    style.bar_mhp.right_bar = Frame("images/battle/battle/mhp_empty.png", 0, 0)
    style.bar_mhp.xmaximum = 100
    style.bar_mhp.ymaximum = 10

    style.bar_hp = Style(style.default)
    style.bar_hp.left_bar = Frame("images/battle/battle/hp_full.png", 0, 0)
    style.bar_hp.right_bar = Frame("images/battle/battle/hp_empty.png", 0, 0)
    style.bar_hp.xmaximum = 150
    style.bar_hp.ymaximum = 25

    style.bar_mp = Style(style.default)
    style.bar_mp.left_bar = Frame("images/battle/battle/mp_full.png", 0, 0)
    style.bar_mp.right_bar = Frame("images/battle/battle/mp_empty.png", 0, 0)
    style.bar_mp.xmaximum = 150
    style.bar_mp.ymaximum = 25

style statusgui_text:
    size 35 bold True drop_shadow [(-1,-1),(1,-1),(-1,1),(1,1)]
