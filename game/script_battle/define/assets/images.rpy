image bb1 = "images/battle/bg/1.jpg"
image bb2 = "images/battle/bg/2.jpg"
image bb3 = "images/battle/bg/3.jpg"

image failure = "images/battle/battle/战斗失败.png"

image zmz_head = TransitionConditionSwitch(Dissolve(0.5, alpha=True),
    "currentplayer == zmz_b","images/battle/char/head/glow/zmz_battle.png",
    "zmz_b.dead == True","images/battle/char/head/dead/zmz_battle.png",
    "True", "images/battle/char/head/zmz_battle.png")
image cl_head = TransitionConditionSwitch(Dissolve(0.5, alpha=True),
    "currentplayer == cl_b","images/battle/char/head/glow/cl_battle.png",
    "cl_b.dead == True","images/battle/char/head/dead/cl_battle.png",
    "True", "images/battle/char/head/cl_battle.png")

image player_head = TransitionConditionSwitch(Dissolve(0.5, alpha=True),
    "currentplayer == a","images/battle/char/head/glow/player_battle.webp",
    "a.dead == True","images/battle/char/head/blank.webp",
    "True", "images/battle/char/head/player_battle.webp")
image yu_head = TransitionConditionSwitch(Dissolve(0.5, alpha=True),
    "currentplayer == y","images/battle/char/head/glow/yu_battle.webp",
    "y.dead == True","images/battle/char/head/blank.webp",
    "True", "images/battle/char/head/yu_battle.webp")
image chie_head = TransitionConditionSwitch(Dissolve(0.5, alpha=True),
    "currentplayer == c","images/battle/char/head/glow/zmz_battle.png",
    "c.dead == True","images/battle/char/head/blank.webp",
    "True", "images/battle/char/head/chie_battle.webp")
image fuuka_head = TransitionConditionSwitch(Dissolve(0.5, alpha=True),
    "currentplayer == f","images/battle/char/head/glow/fuuka_battle.webp",
    "f.dead == True","images/battle/char/head/blank.webp",
    "True", "images/battle/char/head/fuuka_battle.webp")
image rise_head = TransitionConditionSwitch(Dissolve(0.5, alpha=True),
    "currentplayer == r","images/battle/char/head/glow/rise_battle.webp",
    "r.dead == True","images/battle/char/head/blank.webp",
    "True", "images/battle/char/head/rise_battle.webp")

image image_zoom:
    "chie_head"
    zoom 0.3


image zmz_battle = TransitionConditionSwitch(Dissolve(0.5, alpha=True),
    "currentplayer == zmz_b", "images/battle/char/battle/current/zhandoumoxing_zmz.png",
    "zmz_b.dead == True", "images/battle/char/battle/dead/zhandoumoxing_zmz.png",
    "True", "images/battle/char/battle/zhandoumoxing_zmz.png")
image cl_battle = TransitionConditionSwitch(Dissolve(0.5, alpha=True),
    "currentplayer == cl_b", "images/battle/char/battle/current/zhandoumoxing_cl.png",
    "cl_b.dead == True", "images/battle/char/battle/dead/zhandoumoxing_cl.png",
    "True", "images/battle/char/battle/zhandoumoxing_cl.png")

image player_battle = TransitionConditionSwitch(Dissolve(0.5, alpha=True),
    "currentplayer == a", "images/battle/char/battle/current/zhandoumoxing_1.png",
    "a.dead == True", "images/battle/char/battle/dead/zhandoumoxing_1.png",
    "True", "images/battle/char/battle/zhandoumoxing_1.png")
image yu_battle = TransitionConditionSwitch(Dissolve(0.5, alpha=True),
    "currentplayer == y", "images/battle/char/battle/current/zhandoumoxing_2.png",
    "y.dead == True", "images/battle/char/battle/dead/zhandoumoxing_2.png",
    "True", "images/battle/char/battle/zhandoumoxing_2.png")
image chie_battle = TransitionConditionSwitch(Dissolve(0.5, alpha=True),
    "currentplayer == c", "images/battle/char/battle/current/zhandoumoxing_3.png",
    "c.dead == True", "images/battle/char/battle/dead/zhandoumoxing_3.png",
    "True", "images/battle/char/battle/zhandoumoxing_3.png")
image fuuka_battle = TransitionConditionSwitch(Dissolve(0.5, alpha=True),
    "currentplayer == f", "images/battle/char/battle/current/zhandoumoxing_4.png",
    "f.dead == True", "images/battle/char/battle/dead/zhandoumoxing_4.png",
    "True", "images/battle/char/battle/zhandoumoxing_4.png")
image rise_battle = TransitionConditionSwitch(Dissolve(0.5, alpha=True),
    "currentplayer == r", "images/battle/char/battle/current/zhandoumoxing_5.png",
    "r.dead == True", "images/battle/char/battle/dead/zhandoumoxing_5.png",
    "True", "images/battle/char/battle/zhandoumoxing_5.png")

image radar_anim = At("images/battle/anim/radar.webp", idle_sway)
