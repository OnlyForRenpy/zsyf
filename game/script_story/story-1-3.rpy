# 文字的标签设置
#"请{size=45}完善故事{/size}111"
#"请{color=#00ffff}完善故事{/color}111"
#"请{alpha=0.5}完善故事{/}111"
#"请{b}粗体{/b}111"
#"请{i}斜体{/i}111"
#"{cps=5}每秒字符数{/cps}111"

# 角色say模板
# cl confused "请完善故事111"
# cl suprized ""
# "请完善故事333"
# 换行还需{p}标签

# 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
# “eileen happy.png”的文件来将其替换掉。

# show cl:
#     xcenter 0.5              # 注意后面的同名图像位置不会改变,除非再次定义
#     yalign 1.0
#     zoom 0.75
#     # linear 3 xcenter 0.2
# with dissolve

label story_1_3:

    scene black
    with fade
    with Pause(1.5)

    scene yunfushan_door
    with fade
    show yy with dissolve
    yy fennu "一起上，拿下这魔头！"
    "有护山大阵庇护，云逸不再犹豫，一声令下，在场所有弟子都祭出法宝攻了上来。"
    image CG_fashu_jineng_feidan = "images/cg/法术-技能-飞弹.png"
    show CG_fashu_jineng_feidan:
        xcenter 0.5
        ycenter 0.5
        zoom 1.7
    play sound "sound/audio/爆炸.wav" volume 0.5
    with ImageDissolve("script_effect/common/rule/fogtran.png", 1.0, 64)
    with Shake_screen((0, 0, 0, 0), 3.5, dist=25)
    "疾风暴雨的攻击将千面偃逼得寸步难行，不管他掏出什么宝具，对天一宗的门人都产生不了多少伤害，不多时就有些捉襟见肘，道冠又歪到了一边。"
    # hide cg_fashu with ImageDissolve("effects_utils/common/transition/fogtran.png", 1.0, 64)

    scene yunfushan_door
    show qmy yinchen with dissolve
    with Pause(2.0)
    hide qmy with dissolve
    show yy with dissolve
    "眼看不多时便可将那魔头赶走，云逸露出一丝微笑，可这份轻松没能维持多久。"
    show yy dark
    qmy "让我看看会多有趣!"

    scene yunfushan_door
    show qmy jiaoxiao2
    transform show_yu1:
        zoom 1.0
        xcenter 640
        ycenter 360
        alpha 0
        parallel:
            easein 1.5 xcenter 640-300 ycenter 360-20
        parallel:
            easein 1.2 alpha 1.0
    transform show_yu2:
        zoom 1.0
        xcenter 640
        ycenter 360
        alpha 0
        parallel:
            easein 1.5 xcenter 640-100 ycenter 360+40
        parallel:
            easein 1.2 alpha 1.0
    transform show_yu3:
        zoom 1.0
        xcenter 640
        ycenter 360
        alpha 0
        parallel:
            easein 1.5 xcenter 640+100 ycenter 360+40
        parallel:
            easein 1.2 alpha 1.0
    transform show_yu4:
        zoom 1.0
        xcenter 640
        ycenter 360
        alpha 0
        parallel:
            easein 1.5 xcenter 640+300 ycenter 360-20
        parallel:
            easein 1.2 alpha 1.0
    image yu_muti:
        contains:
            "images/obj/玉石.png"
            show_yu1
        contains:
            "images/obj/玉石.png"
            show_yu2
        contains:
            "images/obj/玉石.png"
            show_yu3
        contains:
            "images/obj/玉石.png"
            show_yu4
    play sound "sound/audio/施法/发招.wav"
    show yu_muti with dissolve
    "千面偃突地大笑三声，双手结印，袖中飞出几块拳头大的石块，绕着周身转个不停，俨然布成小小的石阵。"

    scene yunfushan_door
    with dissolve
    show yy with dissolve
    "握剑之手颤抖起来，云逸说不出是哪里不对劲，千面偃分明还是之前江湖术士的模样，可置身石阵中散发出的气息却带着恐怖的威压，叫人几乎要站立不住。"
    hide yy with dissolve
    show qmy jianxiao1 with dissolve
    "再细看时，云逸忽地发现那双细长的眸子里竟闪烁着诡异的紫色，"
    show qmy jianxiao1 at hide_tb(y=-50)
    queue sound [ "sound/audio/移动呼声/布料呼声.mp3", "sound/audio/拳击打中.wav", "sound/audio/拳击打中.wav", "sound/audio/拳击打中.wav", "sound/audio/拳击打中.wav", "sound/audio/拳击打中.wav", "sound/audio/倒地.wav"]
    with Pause(1.0)
    "就在他咬牙试图看清时，千面偃突然消失在视野中，他不禁睁大眼，在听到门人的惨叫时才惊觉对方不是消失，而是移动得太快。"
    "只一瞬，只见弟子们都飞了出去，一个个昏死在地，若非有护山法阵保护，非得摔成肉泥不可。"

    show yy with dissolve
    "下一个就是自己，云逸心中胆寒，难道要丧命于那魔头手下了么？"
    "他惨然一笑，目光一凛，咬破舌尖借血腥强撑神智，决心待那魔头靠近就自爆元婴。"

    "但见毗邻山头忽地升腾起一派剑光，与此同时，白光自那方飞来，直奔千面偃。"

    play sound "sound/audio/刀剑/破风剑光.wav"
    image CG_yuanjulidaji = "images/cg/远距离打击.png"
    scene black with tran_lf
    show CG_yuanjulidaji:
        xalign 0.0
        yalign 1.0
        zoom 2.0
        ease 3.0 xalign 1.0 yalign 0.0
        pause 0.6
        parallel:
            ease 0.3 xalign 0.5 yalign 0.5
        parallel:
            easein 0.3 zoom 1.6
        pause 1.0
    with tran_lf
    with Pause(6.0)
    yy "这是？"
    "云逸感受到熟悉的灵力，脸色一变，可那身影速度太快了，他什么都来不及说，便见白光越过自己。"
    window hide

    scene yunfushan_door with tran_lf
    show qmy jianxiao1 with dissolve
    image daoshifazhen = "images/effect/道士法阵.png"
    show daoshifazhen:
        xcenter 0.5
        ycenter 0.5
        zoom 0.2
        alpha 0.0
        parallel:
            easein 2.0 alpha 0.5
        parallel:
            easein 1.0 zoom 0.22
            easein 1.0 zoom 0.2
            repeat
    with Pause(3)
    "千面偃不由挑眉，嘴角勾勒出一抹笑意，右手凭空画了几道，转瞬便在身前结成重重屏障，总计十八重。"
    window hide

    show CG_yuanjulidaji:
        xalign 0.0
        yalign 1.0
        zoom 1.6
    with tran_lf
    with Pause(0.8)
    hide CG_yuanjulidaji with tran_lf
    "只是可惜来人速度比他想象得还快。"
    play sound "sound/audio/彻底碎.wav"
    with Pause(0.8)
    show daoshifazhen at hide_extend(z=0.22, y=0)
    "屏障尽碎的同时，剑气已至。"

    image zongqie = "images/cg/纵切.png"
    play sound "sound/audio/刀剑/se104.wav"
    show zongqie:
        xalign 0.0
        yalign 1.0
        zoom 1.6
    with ImageDissolve("script_effect/common/rule/s2.png", 0.3, 64)
    with Pause(0.5)
    hide qmy
    hide zongqie with ImageDissolve("script_effect/common/rule/s2.png", 0.3, 64)

    queue sound ["sound/audio/刀剑/刀剑碰撞1.wav", "sound/audio/金属爆炸.wav"]
    with Shake_screen((0, 0, 0, 0), 3.5, dist=25)

    show yy fennu
    "相交的法力在空中炸裂，扩散的灵压风压得云逸气血一阵翻涌。"
    hide yy with dissolve
    with Pause(0.8)
    show cl zhijian at pos_cl_zhijian
    "待一切静止后，只见一顶道冠悠悠然飘落，一名白衣女子与千面偃相对而立，长剑横握，冰冷的剑尖贴在千面偃脖颈，只消再往前送一点，便能割破咽喉。"
    "可惜分寸难动。"
    "千面偃的目光落在执剑之手上，那只手如今被他抓在手中，脆弱得好似易碎的瓷器，只消稍用劲就可以拧断。"
    qmy "你的剑法还不错。"
    transform wobbly_stand1(x=5, y=3, y_c_b=0.8, y_c_e=0.65, t=0.1, tmove=2.5):
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
            ycenter y_c_b
            ease 2.5 ycenter y_c_e

    play sound "sound/audio/拉扯粗麻绳.wav"
    show cl zhijian at wobbly_stand1(x=3, y=2, y_c_b=0.7, y_c_e=0.65, t=0.05, tmove=2.5)
    "他咧开嘴笑得更欢，下一刻却是眸色一沉，紫眸中闪过杀意，抓住女子的脖颈将将提起，"
    qmy "……不过还是不够！"
    stop sound

    scene black with tran_lf
    scene yunfushan_door with tran_lf

    show yy fennu with dissolve
    yy fennu "师妹！"
    show yy:
        easein 0.1 zoom 1.1
    play sound "sound/audio/拳击打中.wav"
    image daji_effect = "images/effect/打击.png"
    show daji_effect:
        subpixel True
        xcenter 0.5
        ycenter 0.7
        zoom 0.5
        alpha 0.0
        parallel:
            easein 0.25 alpha 0.2
            easein 0.25 alpha 0
        parallel:
            easein 0.5 zoom 0.5*1.1

    show yy:
        easein 0.1 zoom 1.0
    show yy at wobbly
    with Pause(1.5)
    show yy at hide_tb(y=200, t=1.5)
    "云逸心急扑上，他这个师妹本在闭关，没料到竟在这时候破关而出。\n
他虽有心想护她，然而双方实力悬殊，千面偃只挥了挥袖子，就将他打得吐血不止。"

    scene black with tran_lf
    scene yunfushan_door with tran_lf

    play sound "sound/audio/拉扯粗麻绳.wav"
    show cl zhijian at pos_cl_zhijian
    show cl zhijian at wobbly_stand1(x=3, y=2, y_c_b=0.65, y_c_e=0.65, t=0.05, tmove=2.5)
    "五指渐渐用劲，千面偃玩味地歪头，似乎正在思考那女子能坚持几刻。"
    "他无聊地数着数，目光四下游走，却发现女子竟是越发捏紧剑柄，即便已危在旦夕，那把剑却无一丝颤抖。"
    image shifa = "images/effect/施法.png"
    show shifa:
        xcenter 0.5
        yalign 1.0
        alpha 0
        easein 2 alpha 0.4
        easeout 2 alpha 0
        repeat
    "他忽地有种不好的预感，未及细想，便见白衣女子周身被一层若有若无的青气覆盖。"
    play sound "sound/audio/被剑刺中.wav"
    image blood a = "images/cg/血1.png"
    image blood b = "images/cg/血2.png"
    show blood a at CG_800_600
    with dissolve
    with Pause(0.5)
    show blood b at CG_800_600
    with dissolve
    "不好！\n
他情急之下一掌重重拍上那女子肩头将其推远，身子猛退同时再结出数十道屏障，却仍晚了一步，血珠飞溅，右肩上多出一道深可见骨的口子。"

    scene yunfushan_far
    with fade
    "余光中，后山似乎也笼上一层青光，细看时却已消失了。"

    scene yunfushan_door
    with fade
    play sound "sound/audio/鞋摩擦.mp3" volume 5.0
    show cl yingzhan blood:
        ycenter 0.65
        xcenter 0.45
        yoffset 0
        zoom 0.55*1.50
        alpha 1.00
        easein 0.3 zoom 0.55
    with Pause(1.0)
    hide cl yingzhan blood with dissolve
    show cl zhijian blood at pos_cl_zhijian
    "千面偃略显狼狈的捂住伤口，细长的眼中的紫色已消失，他第一次细细打量起面前的白衣女子。"
    "面若玉琢，眸色如墨，粉黛不施，仅眉间一点朱砂为缀，她身上那层青光已经消失了，一袭白衣寡淡得不沾半点人烟气。"
    qmy "你叫什么名字？"
    "千面偃问道。"
    cl zhijian blood "长离。"
    "声音平静似雪山上冰封的河川，漆黑的眸子盯着千面偃。她受了足以致命的一掌，可还是紧紧握住剑柄，血不住自其指缝间渗出，长剑没有丝毫颤抖。"
    "嫣红的血顺着剑身滑落，与千面偃的血混同，最后自剑尖滴落，几滴落在斗争中纤尘不染的裙角上，好似梅花于雪地怒放。"
    with Shake_screen((0, 0, 0, 0), 2.5, dist=10)
    "千面偃的目光自女子脸上移至裙角，眸中阴沉不定，片刻后大声笑了起来，肆意得不像一个受伤的人。"
    "像是找到有趣的物事，笑够后，他高声喊道："
    qmy "竖子伤我，以天为誓，日后必叫天一宗数倍奉还!"

    scene yunfushan_far
    with fade
    nrr """
    {clear}

        话音未落，身影便消失于天际。

        {clear}

        天一宗弟子长离以不足两百之龄达元婴修为，继而于宗门临危之际重创千面偃，魔头就此失去了踪迹，堪称百年来几大幸事之一，正邪两道无人不拍手称快。

　　此后，长离仙子之名传遍天下，仰慕者济济，被竞相引为美谈。

    """

    scene black
    with fade
    window hide

    jump story_2_1
