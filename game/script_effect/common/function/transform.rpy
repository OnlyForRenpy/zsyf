transform CG_800_600:
    xcenter 0.5
    ycenter 0.5
    zoom 1.6

transform objpos(x=0.5, y=1.0, z=0.55, a=1.0):
    subpixel True
    ycenter y
    xcenter x
    yoffset 0
    zoom z*1.00
    alpha a

# transform pos_cl:
#     pos(y=360+160, z=0.5)


transform appear_center_extend(x_c=0.5, y_a=1.0, z=0.75, t=0.2):
    subpixel True
    xcenter x_c
    yalign y_a
    zoom z
    alpha 0.00
    parallel:
        easein t alpha 1.0
    parallel:
        easein t zoom z * 1.05
        easein t zoom z
    # time t
    # ycenter 1.12 yoffset 0

transform appear_tb(x_c=0.5, y_c=1.0, y_o=-10, z=1.0, t=0.25):
    subpixel True
    on show:
        xcenter x_c
        # yalign y_a
        ycenter y_c
        yoffset y_o
        zoom z*0.95
        alpha 0.00
        easein t yoffset 0 zoom z*1.00 alpha 1.00
    on replace:
        alpha 1.00
        easein t xcenter x_c zoom z*1.00 yoffset 0 ycenter 1.12

transform app_tb(x_c=0.5, y_c=1.0, z=1.0, t=0.25):
    appear_tb(x_c=x_c, y_c=y_c, z=z, t=t)
transform app_tb21(x_c=0.3, y_c=1.0, z=1.0, t=0.25):
    appear_tb(x_c=x_c, y_c=y_c, z=z, t=t)
transform app_tb22(x_c=0.7, y_c=1.0, z=1.0, t=0.25):
    appear_tb(x_c=x_c, y_c=y_c, z=z, t=t)
transform app_tb31(x_c=0.185, y_c=1.0, z=1.0, t=0.25):
    appear_tb(x_c=x_c, y_c=y_c, z=z, t=t)
transform app_tb32(x_c=0.5, y_c=1.0, z=1.0, t=0.25):
    appear_tb(x_c=x_c, y_c=y_c, z=z, t=t)
transform app_tb33(x_c=0.815, y_c=1.0, z=1.0, t=0.25):
    appear_tb(x_c=x_c, y_c=y_c, z=z, t=t)
transform app_tb41(x_c=0.2, y_c=1.0, z=1.0, t=0.25):
    appear_tb(x_c=x_c, y_c=y_c, z=z, t=t)
transform app_tb42(x_c=0.4, y_c=1.0, z=1.0, t=0.25):
    appear_tb(x_c=x_c, y_c=y_c, z=z, t=t)
transform app_tb43(x_c=0.6, y_c=1.0, z=1.0, t=0.25):
    appear_tb(x_c=x_c, y_c=y_c, z=z, t=t)
transform app_tb44(x_c=0.8, y_c=1.0, z=1.0, t=0.25):
    appear_tb(x_c=x_c, y_c=y_c, z=z, t=t)

transform appear_rl(x_c=0.5, y_c=1.0, z=1.0, t=0.25):
    subpixel True
    on show:
        xcenter x_c
        xoffset 110
        ycenter y_c
        zoom z*0.98
        alpha 0.00
        easein t*2 xoffset 0 zoom z*1.00 alpha 1.00
    on replace:
        alpha 1.00
        easein t xcenter x_c zoom z*1.00 yoffset 0 ycenter 1.12
transform app_rl(x_c=0.5, y_c=1.0, z=1.0, t=0.25):
    appear_rl(x_c=x_c, y_c=y_c, z=z, t=t)
transform app_rl21(x_c=0.3, y_c=1.0, z=1.0, t=0.25):
    appear_rl(x_c=x_c, y_c=y_c, z=z, t=t)
transform app_rl22(x_c=0.7, y_c=1.0, z=1.0, t=0.25):
    appear_rl(x_c=x_c, y_c=y_c, z=z, t=t)
transform app_rl31(x_c=0.185, y_c=1.0, z=1.0, t=0.25):
    appear_rl(x_c=x_c, y_c=y_c, z=z, t=t)
transform app_rl32(x_c=0.5, y_c=1.0, z=1.0, t=0.25):
    appear_rl(x_c=x_c, y_c=y_c, z=z, t=t)
transform app_rl33(x_c=0.815, y_c=1.0, z=1.0, t=0.25):
    appear_rl(x_c=x_c, y_c=y_c, z=z, t=t)
transform app_rl41(x_c=0.2, y_c=1.0, z=1.0, t=0.25):
    appear_rl(x_c=x_c, y_c=y_c, z=z, t=t)
transform app_rl42(x_c=0.4, y_c=1.0, z=1.0, t=0.25):
    appear_rl(x_c=x_c, y_c=y_c, z=z, t=t)
transform app_rl43(x_c=0.6, y_c=1.0, z=1.0, t=0.25):
    appear_rl(x_c=x_c, y_c=y_c, z=z, t=t)
transform app_rl44(x_c=0.8, y_c=1.0, z=1.0, t=0.25):
    appear_rl(x_c=x_c, y_c=y_c, z=z, t=t)

#小身体
transform fss11(x=0.5, z=0.36):
    subpixel True
    xcenter x zoom z*1.00 yoffset 0 ycenter 0.84
transform show_fast(x=0.5, z=0.36):
    subpixel True
    on show:
        ycenter 0.84
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -22
        easein .25 yoffset 0 zoom z*1.00 alpha 1.00
    on replace:
        alpha 1.00
        easein .25 xcenter x zoom z*1.00 yoffset 0 ycenter 0.84
transform sb11:
    show_commmon(0.5)
transform sb21:
    show_commmon(0.3)
transform sb22:
    show_commmon(0.7)
transform sb31:
    show_commmon(0.185)
transform sb32:
    show_commmon(0.5)
transform sb33:
    show_commmon(0.815)
transform sb41:
    show_commmon(0.2)
transform sb42:
    show_commmon(0.4)
transform sb43:
    show_commmon(0.6)
transform sb44:
    show_commmon(0.8)

transform show_fastrl(x=0.5, z=0.36):
    subpixel True
    on show:
        ycenter 0.84
        zoom z*0.98 alpha 0.00
        xcenter x xoffset 72
        easein .25 xoffset 0 zoom z*1.00 alpha 1.00
    on replace:
        alpha 1.00
        easein .25 xcenter x zoom z*1.00 yoffset 0 ycenter 0.84
transform sb11rl:
    show_commmonrl(0.5)
transform sb21rl:
    show_commmonrl(0.3)
transform sb22rl:
    show_commmonrl(0.7)
transform sb31rl:
    show_commmonrl(0.185)
transform sb32rl:
    show_commmonrl(0.5)
transform sb33rl:
    show_commmonrl(0.815)
transform sb41rl:
    show_commmonrl(0.2)
transform sb42rl:
    show_commmonrl(0.4)
transform sb43rl:
    show_commmonrl(0.6)
transform sb44rl:
    show_commmonrl(0.8)


#大头
transform fsb(x=0.5, z=1.0):
    subpixel True
    alpha 1.00
    easein .25 xcenter x zoom z*1.00 yoffset 0 ycenter 1.75
transform show_commmon(x=0.5, z=1.0):
    subpixel True
    on show:
        ycenter 1.0
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -40
        easein .25 yoffset 0 zoom z*1.00 alpha 1.00
    on replace:
        alpha 1.00
        easein .25 xcenter x zoom z*1.00 yoffset 0 ycenter 1.75
transform ss11:
    show_fast(0.5)
transform ss21:
    show_fast(0.3)
transform ss22:
    show_fast(0.7)
transform ss31:
    show_fast(0.185)
transform ss32:
    show_fast(0.5)
transform ss33:
    show_fast(0.815)

transform show_commmonrl(x=0.5, z=1.0):
    subpixel True
    on show:
        ycenter 1.75
        zoom z*0.98 alpha 0.00
        xcenter x xoffset 200
        easein .25 xoffset 0 zoom z*1.00 alpha 1.00
    on replace:
        alpha 1.00
        easein .25 xcenter x zoom z*1.00 yoffset 0 ycenter 1.75
transform ss11rl:
    show_fastrl(0.5)
transform ss21rl:
    show_fastrl(0.3)
transform ss22rl:
    show_fastrl(0.7)
transform ss31rl:
    show_fastrl(0.185)
transform ss32rl:
    show_fastrl(0.5)
transform ss33rl:
    show_fastrl(0.815)

# 走路
transform walk(x_c_b=0.0, x_c_e=0.5, y_c=1.0, y_o=-10, z=1.0, t=0.25):
    subpixel True
    xcenter x_c_b
    ycenter y_c
    zoom z
    parallel:
        ease 1.6 xcenter x_c_e
    parallel:
        ease 0.2 yoffset y_o
        ease 0.2 yoffset 0
        repeat
    time 1.6

#蹲下
transform move_down(y=44, t=0.5):
    subpixel True
    on show:
        yoffset 0
        easein t yoffset y alpha 1.00
    on replace:
        easein t yoffset y alpha 1.00

transform move_right(y=44, t=0.5):
    subpixel True
    on show:
        xoffset 0
        easein t xoffset x alpha 1.00
    on replace:
        easein t xoffset x alpha 1.00

#点头
transform nod(y=20, t=0.24):
    subpixel True
    easein t yoffset y alpha 1.00
    easeout t yoffset 0 alpha 1.00

# 摇头
transform shake_head(x=20, t=0.15):
    subpixel True
    easein t xoffset x alpha 1.0
    easeout t xoffset 0
    easein t xoffset x * -0.75
    easeout t xoffset 0
    easein t xoffset x * 0.5
    easeout t xoffset 0
    easein t xoffset x * -0.25
    ease t xoffset 0

# 持续摇头
transform shake_head_r(x=20, t=0.15):
    subpixel True
    block:
        easein t xoffset x
        easeout t xoffset 0
        easein t xoffset -x
        easeout t xoffset 0
        repeat

# 持续上下移动
transform nod_r(y=20, t=0.15):
    subpixel True
    block:
        easein t yoffset y
        easeout t yoffset 0
        easein t yoffset -y
        easeout t yoffset 0
        repeat


#hide
transform hide_extend(z=1.0, y=33, t=0.25):
    # on hide:
    subpixel True
    alpha 1.0
    easein t zoom z*1.02 alpha 0.00 yoffset -y

transform hide_tb(y=100, t=0.25):
    subpixel True
    alpha 1.0
    yoffset 0
    parallel:
        easein t alpha 0.0
    parallel:
        linear t*2 yoffset y

transform hide_rl(x=100, t=0.5):
    subpixel True
    xoffset 0
    parallel:
        easein t alpha 0.0
    parallel:
        linear t xoffset x


####表情
#疑问
transform show_why(x=640, y=150, z=0.4):
    subpixel True
    xcenter x-95
    ycenter y
    zoom z
    alpha 0.00
    easein 0.3 xcenter x-115 ycenter y-40 alpha 1.00
    easein 0.4 xcenter x-95 ycenter y
    easein 0.5
    easein 1.0 xcenter x-75 ycenter y+40 alpha 0.00
image why_icon:
    "/common/facial/why.png"
    show_why(x=640)

#汗
transform show_sweat(x=640, y=265, z=0.3):
    xcenter x+120
    ycenter 265
    zoom z
    alpha 0.00
    subpixel True
    parallel:
        easein 1.5 ycenter y
    parallel:
        linear 0.25 alpha 1.0
    time 1.0
    linear 0.5 alpha 0.0
image sweat_icon:
    "script_effect/common/facial/water.png"
    show_sweat(x=640)

#混乱
transform show_dizzy(x=640, y=155, z=0.5):
    xcenter x-107
    ycenter y
    zoom z
    alpha 0.00
    subpixel True
    parallel:
        linear 0.25 alpha 1.00 zoom z*0.5
        time 2.0
        linear 0.25 alpha 0.00 zoom z
    parallel:
        easeout_bounce 0.13 xcenter x-102
        easeout_bounce 0.13 xcenter x-112
        repeat
    parallel:
        easeout_bounce 0.2 ycenter y+10
        easeout_bounce 0.2 ycenter y-10
        repeat
image dizzy_icon:
    "script_effect/common/facial/emmm.png"
    show_dizzy(x=640)

#慌张
transform show_panic(x=640, y=320, z=0.5):
    xcenter x
    ycenter y
    zoom z
    alpha 1.00
    subpixel True
    pause 0.1
image panic_icon:
    "script_effect/common/facial/amazing_1.png"
    show_panic()
    "script_effect/common/facial/amazing_2.png"
    show_panic()
    repeat
    time 1.0
    linear 1.0 alpha 0.0

#惊讶
transform show_amazing(x=640, y=150, z=0.5):
    xcenter x-125
    ycenter y
    zoom z
    alpha 1.00
    subpixel True
    block:
        linear 0.2 alpha 1.0
        linear 0.0 alpha 0.0
        linear 0.2 alpha 0.0
        linear 0.0 alpha 1.0
        linear 0.2 alpha 1.0
        linear 0.0 alpha 0.0
        linear 0.2 alpha 0.0
        linear 0.0 alpha 1.0
        linear 0.5 alpha 1.0
        linear 0.3 alpha 0.0
image amazing_icon:
    "script_effect/common/facial/happy_2.png"
    show_amazing()

#高兴
transform show_happy(x=640, y=150, z=0.5):
    xcenter x-125
    ycenter y
    zoom z
    alpha 1.00
    subpixel True
    pause 0.4
image happy_icon:
    "script_effect/common/facial/happy_1.png"
    show_happy()
    "script_effect/common/facial/happy_2.png"
    show_happy()
    repeat
    time 2.0
    linear 1.0 alpha 0.0

#愤怒
transform show_angry(x=640, y=150, z=0.3):
    xcenter x+100
    ycenter y
    zoom z
    alpha 0.00
    subpixel True
    parallel:
        dizzy(m=1.6, t=0.1, subpixel=True, k = 1)
    parallel:
        linear 0.25 alpha 1.0
    time 2.0
    linear 0.25 alpha 0.0
image angry_icon:
    "script_effect/common/facial/angry.png"
    show_angry()

#生气
transform show_sign(x=640, y=250, z=0.3):
    xcenter x+150
    ycenter y
    zoom z
    alpha 0.00
    subpixel True
    easein 0.3 xcenter x+250 ycenter y-100 alpha 1.00
    easein 1.0
    easein 0.3 alpha 0.00
image sign_icon:
    "script_effect/common/facial/steam.png"
    show_sign()

#微妙
transform show_subtle(x=640, y=150, z=0.5):
    xcenter x
    ycenter y-75
    zoom z
    alpha 0.00
    subpixel True
    parallel:
        linear 0.5 ycenter y
    parallel:
        linear 0.2 alpha 1.0
        linear 1.0
        linear 0.3 alpha 0.0
image subtle_icon:
    "script_effect/common/facial/sub.png"
    show_subtle()

#音乐
transform show_humming1(x=640, y=200, z=0.35):
    xcenter x+100
    ycenter y
    zoom z
    alpha 0.00
    rotate 40
    subpixel True
    parallel:
        linear 2.0 rotate -20 xcenter x+300 ycenter 100
    parallel:
        linear 0.5 alpha 1.0
        linear 1.0 alpha 1.0
        linear 0.5 alpha 0.0
transform show_humming2(x=640, y=250, z=0.37):
    xcenter x+125
    ycenter y
    zoom z
    alpha 0.00
    rotate -20
    subpixel True
    time 0.8
    parallel:
        linear 2.0 rotate 40 xcenter x+300 ycenter 175
    parallel:
        linear 0.5 alpha 1.0
        linear 1.0 alpha 1.0
        linear 0.5 alpha 0.0
image humming_icon:
    contains:
        "script_effect/common/facial/munote.png"
        show_humming1()
    contains:
        "script_effect/common/facial/munote.png"
        show_humming2()


# transform floweralt(x=640):
#     xcenter x ycenter 275 zoom 0.27 alpha 0.00 subpixel True
#     parallel:
#         linear 0.25 zoom 0.54
#     parallel:
#         linear 0.25 alpha 1.0
#         linear 1.75 alpha 1.0
#         linear 0.25 alpha 0.0
# image flower11:
#     contains:
#         "liluo_common/common/facial/flower1.png"
#         floweralt(640 - 220)
#     contains:
#         "liluo_common/common/facial/flower2.png"
#         floweralt(640 + 220)
# image flower21:
#     contains:
#         "liluo_common/common/facial/flower1.png"
#         floweralt(384 - 220)
#     contains:
#         "liluo_common/common/facial/flower2.png"
#         floweralt(384 + 220)
# image flower22:
#     contains:
#         "liluo_common/common/facial/flower1.png"
#         floweralt(896 - 220)
#     contains:
#         "liluo_common/common/facial/flower2.png"
#         floweralt(896 + 220)
# image flower31:
#     contains:
#         "liluo_common/common/facial/flower1.png"
#         floweralt(237 - 220)
#     contains:
#         "liluo_common/common/facial/flower2.png"
#         floweralt(237 + 220)
# image flower32:
#     contains:
#         "liluo_common/common/facial/flower1.png"
#         floweralt(640 - 220)
#     contains:
#         "liluo_common/common/facial/flower2.png"
#         floweralt(640 + 220)
# image flower33:
#     contains:
#         "liluo_common/common/facial/flower1.png"
#         floweralt(1043 - 220)
#     contains:
#         "liluo_common/common/facial/flower2.png"
#         floweralt(1043 + 220)



######## 其它效果
transform flicker:
    alpha 1.00
    linear 0.2 alpha 0.7
    0.1
    alpha 0.4
    linear 0.1 alpha 0.90
    alpha 0.0
    0.1
    repeat

transform layerflicker:
    alpha 0.1
    linear 0.25 alpha 0.1
    linear 0.25 alpha 0.2
    linear 0.25 alpha 0.1
    linear 0.25 alpha 0.3
    linear 0.25 alpha 0.2
    linear 0.25 alpha 0.4
    linear 0.25 alpha 0.3
    linear 0.25 alpha 0.4
    linear 0.25 alpha 0.2
    repeat

transform wobbly(x=5, y=3, t=0.1):
    subpixel True
    parallel:
        xoffset 0
        ease t xoffset x
        ease t xoffset x*0.5
        ease t xoffset x*-0.5
        ease t xoffset x*-0.25
        ease t xoffset x*-0.75
        ease t xoffset 0
        ease t xoffset x*0.5
        ease t xoffset 0
        repeat
    parallel:
        yoffset 0
        ease 0.55 yoffset y
        ease 1.05 yoffset -y
        easein 0.25 yoffset 0
        repeat

transform wobbly_stand(x=5, y=3, y_c_b=0.8, y_c_e=0.65, t=0.1, tmove=2.5):
    subpixel True
    parallel:
        xoffset 0
        ease t xoffset x
        ease t xoffset x*0.5
        ease t xoffset x*-0.5
        ease t xoffset x*-0.25
        ease t xoffset x*-0.75
        ease t xoffset 0
        ease t xoffset x*0.5
        ease t xoffset 0
        repeat
    parallel:
        yoffset 0
        ease 0.55 yoffset y
        ease 1.05 yoffset -y
        easein 0.25 yoffset 0
        repeat
    parallel:
        ycenter 1.0
        ease tmove ycenter 0.65
    time 2.5


###
define close_eyes = MultipleTransition([False, Dissolve(0.5), Solid("#000"), Pause(0.25), True])
define open_eyes = MultipleTransition([False, Dissolve(0.5), True])
define push_left = CropMove(2.0, "custom", startcrop=(0.5, 0.0, 0.0, 1.0), endcrop=(0.0, 0.0, 1.0, 1.0))
define clockwise = ImageDissolve("script_effect/common/rule/clockwise.png", 1.0, 64)
define anticlockwise = ImageDissolve("script_effect/common/rule/anticlockwise.png", 1.0, 64)
define tran_clockwise = MultipleTransition([False, clockwise ,Solid("#000"), clockwise, True])
define close = ImageDissolve("script_effect/common/rule/close.png", 0.5, 128, reverse = True)
define tran_close = MultipleTransition([False, close ,Solid("#000"), close ,True])
define tran_water = ImageDissolve("script_effect/common/rule/watertran.png", 1.5, 256)
define tran_light = ImageDissolve("script_effect/common/rule/snaketran.png", 0.5, 128)
define tran_fog = ImageDissolve("script_effect/common/rule/fogtran.png", 1.0, 256)
define tran_crystal = ImageDissolve("script_effect/common/rule/crystal_bt.png", 1.0, 32)
define tran_fast = ImageDissolve("script_effect/common/rule/fasttran.png", 0.5, 64)
define tran_updown = ImageDissolve("script_effect/common/rule/updowntran.png", 0.5, 64)
define tran_uf = ImageDissolve("script_effect/common/rule/s2.png", 0.5, 64)
define tran_df = ImageDissolve("script_effect/common/rule/s1.png", 0.5, 64)
define tran_rf = ImageDissolve("script_effect/common/rule/right.png", 0.5, 64)
define tran_lf = ImageDissolve("script_effect/common/rule/走る感じ.png", 0.5, 256, reverse=True)
define tran_lu = ImageDissolve("script_effect/common/rule/左上から右下へ.png", 0.5, 128, reverse=True)
define push_up = CropMove(0.4, "custom",startcrop=(0.0, 1.0, 1.0, 1.0), endcrop=(0.0, 0.0, 1.0, 1.0))

define config.window_hide_transition = close
define config.window_show_transition = close
