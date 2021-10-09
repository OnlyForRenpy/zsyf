label story_1_2:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为“bg room.png”或“bg room.jpg”）来显示。

    stop music fadeout 2.0
    scene black
    with Pause(3.0)

    play music "sound/bgm/司夏 - 白衣渡我 (伴奏).mp3"

    image sword-1-2 = "images/bg/剑.png"

    image gif_water = SquenceAnimator("images/cg/water", interval=0.1, loop=False)

    # transform gif_speed(t=0.1):
    #     pause 0.1
    # image cg1_2_1_gif:
    #     xcenter 0.5
    #     yalign 1.0
    #     zoom 1.8
    #
    #     "images/cg/water/frame1.png"
    #     gif_speed()
    #     "images/cg/water/frame2.png"
    #     gif_speed()
    #     "images/cg/water/frame3.png"
    #     gif_speed()
    #     "images/cg/water/frame4.png"
    #     gif_speed()
    #     "images/cg/water/frame5.png"
    #     gif_speed()
    #     "images/cg/water/frame6.png"
    #     gif_speed()
    #     "images/cg/water/frame7.png"
    #     gif_speed()
    #     "images/cg/water/frame8.png"
    #     gif_speed()
    #     "images/cg/water/frame9.png"
    #     gif_speed()
    #     "images/cg/water/frame10.png"
    #     gif_speed()
    #     "images/cg/water/frame11.png"
    #     gif_speed()
    #     "images/cg/water/frame12.png"
    #     gif_speed()
    #     "images/cg/water/frame13.png"
    #     gif_speed()
    #     "images/cg/water/frame14.png"
    #     gif_speed()
    #     "images/cg/water/frame15.png"
    #     gif_speed()
    #     "images/cg/water/frame16.png"
    #     gif_speed()
    #     "images/cg/water/frame17.png"
    #     gif_speed()
    #     "images/cg/water/frame18.png"
    #     gif_speed()
    #     "images/cg/water/frame19.png"
    #     gif_speed()
    #     "images/cg/water/frame20.png"
    #     gif_speed()
    #     "images/cg/water/frame21.png"
    #     gif_speed()
    #     "images/cg/water/frame22.png"
    #     gif_speed()
    #     "images/cg/water/frame23.png"
    #     gif_speed()
    #     "images/cg/water/frame24.png"
    #     gif_speed()
    #     "images/cg/water/frame25.png"
    #     gif_speed()
    #     "images/cg/water/frame26.png"
    #     gif_speed()
    #     "images/cg/water/frame27.png"
    #     gif_speed()
    #     "images/cg/water/frame28.png"
    #     gif_speed()
    #     "images/cg/water/frame29.png"
    #     gif_speed()
    #     "images/cg/water/frame30.png"
    #     gif_speed()
    #     "images/cg/water/frame31.png"
    #     gif_speed()
    #     "images/cg/water/frame32.png"
    #     gif_speed()
    #     "images/cg/water/frame33.png"
    #     gif_speed()
    #     "images/cg/water/frame34.png"
    #     gif_speed()
    #     "images/cg/water/frame35.png"
    #     gif_speed()
    #     "images/cg/water/frame36.png"
    #     gif_speed()
    #     "images/cg/water/frame37.png"
    #     gif_speed()
    #     "images/cg/water/frame38.png"

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # “eileen happy.png”的文件来将其替换掉。

    window hide
    show gif_water:
        xcenter 0.5
        yalign 1.0
        zoom 1.8
    with Pause(5 * 0.1)
    play sound "sound/audio/水滴.wav" volume 7.5
    with Pause(37 * 0.1)

    scene sword-1-2
    with fade
    with Pause(1.0)

    nrr """
    {clear}

        八面墙上寒光潋滟，自顶上悬下的利刃密集如雨，连阁顶都铺满剑，仿佛随时会坠下。

        冷光自剑刃泛起，交织成密不透风的网。

        {clear}

        剑，器名，两刃有脊，自背至刃，谓之腊，或谓之锷。背刃以下，与柄分隔青，谓之首。

        首以下把握之处曰茎，茎端旋环曰铎。乃古之圣品也，至尊至贵，人神咸崇。

　　洛书有云：羲皇采首山之铜铸兵，以天文古字铭之，此为万剑之始，后世之兵，皆以剑为尊。

{clear}

　　斩铁如泥的宝剑，仅一柄就足以摄人心魂，此处阁楼却聚了上千把，莫说是进入，就是在阁外都难免为剑气所伤，可却见一姝端坐楼中。
    """

    window hide
    with dissolve

    show cl dazuo biyan at app_tb(y_c=400, z=0.5) with dissolve
    with Pause(2.0)
    nrr """
    {clear}

        白衣胜雪，青丝悬瀑，仿佛自水墨画卷走来，额心一点朱砂妖娆似血，勾成墨色与浅白间唯一的明艳。

        居于剑网交汇处，剑气及杀意喧嚣着，她却倘若未觉般面无表情，若非尚有轻微的呼吸起伏，当真与雕像无半点差别了。
    """
    play sound "sound/audio/刀剑/刀剑音效11秒.wav"
    nrr """
    {clear}

        灵光流转，起初只是星点，比之剑气犹如萤火，而后渐渐压过了剑气，

        到最后，剑气被全然纳入了灵光中，金戈之音自四面八方涌来，阁楼瞬间变成了杀意冲天的古战场。
    """

    window hide
    image momei = "images/obj/墨眉-背景.png"
    show momei:
        xcenter 640-150
        ycenter -0.5
        zoom 1.13
        linear 1.0 ycenter 0.5
    # with push_up

    with Pause(1.5)

    nrr """
    {clear}

        她忽地探出手，抚上身畔的黑色长匣，一柄漆黑的长剑自匣中跃出，长三尺而无锋。

        {clear}

        只见女子平平一挥，夺目剑光自刃上迸发，战鼓与杀声戛然而止。

　　霜雪彻底消融，一切归于安宁。
    """

    window hide
    hide momei
    with dissolve

    image movietext1:
        contains:
            "#000"
            size(1280,150)
            xpos 0 ypos -150
            easein 0.8 ypos -50
        contains:
            "#000"
            size(1280,600)
            xpos 0 ypos 720
            easein 0.8 ypos 350

    show movietext1

    with Pause(1.5)
    show cl dazuo:
        xcenter 0.5
        ycenter 400
        zoom 0.5
    with dissolve

    nrr """
    {clear}

        女子缓缓睁开眼，漆黑的眼眸倒映出黯然的剑墙。

        {clear}

        阁楼中再无宝剑。

    """
    hide movietext1
    with dissolve

    nrr """
    {clear}

        女子执剑而起，低垂的眼眸中仍似古潭，无一丝涟漪。
    """

    play sound "sound/audio/移动呼声/布料呼声.mp3"
    show cl dazuo at hide_extend(z=0.5, y=20, t=1.0)
    with Pause(1.5)

    jump story_1_3
