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

label story_1_1:

    image cg1-1-1 = "images/cg/CG-1-1-1.jpg"
    image cg1-1-2 = "images/cg/CG-1-1-2.png"
    image cg1-1-3 = "images/cg/CG-1-1-3.jpg"

    image effect 1-1-1 = "images/effect/施法.png"
    image effect 1-1-2 = "images/effect/八卦阵.png"

    # 该脚本定义的人物，不常出现
    define ptdz = Character("普通弟子", image = "ptdz", what_size = 28, what_prefix = "『", what_suffix = "』")
    image ptdz = "images/char/其他/普通弟子.png"
    image ptdz2 = "images/char/其他/普通弟子.png"
    image ptdz3 = "images/char/其他/普通弟子.png"
    image ptdz4 = "images/char/其他/普通弟子.png"
    image ptdz5 = "images/char/其他/普通弟子.png"
    image ptdz multi = Fixed(
    Image("images/char/其他/普通弟子.png", xalign=0.0, yalign=1.0),
    Image("images/char/其他/普通弟子.png", xalign=0.2, yalign=1.0))

    window hide
    with Pause(2.0)
    with fade
    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为“bg room.png”或“bg room.jpg”）来显示。
    play music "sound/bgm/骆集益 - 片头音乐.mp3"
    scene black

    show cg1-1-1:
        xalign 0.0
        yalign 0.0
        zoom 4
        parallel:
            linear 10 xalign 1.0
        parallel:
            linear 10 yalign 1.0
    # with fade
    nrr """
        天地初开为洪荒，上古之神造天地万物，而众生汲灵力可修炼登仙，与神平齐。

　　    万物济济，共处一方，后天帝失德，天道降屠戮，洪水滔天，毒瘴蔽日。

昊天辟三界，后神上仙登上界御天道之罚，鬼界承轮回，下界众生得存。
    """

    nvl clear
    hide cg1-1-1

    show cg1-1-2:
        xalign 0.5
        yalign 1.0
        zoom 2.5
        linear 10 yalign 0.0
    with fade
    nrr """
        三界分开后下界虽然免了灾祸，但是随之而来的灵气匮乏，导致修仙者修炼远比以往困难。

　　修炼即化天地灵气为己所用，随着修为精深，有{size=30}  炼气、筑基、金丹、元婴、化神、洞虚、大乘  {/}七层境界之分。

每突破一层，实力可十倍进益，而修炼难度亦前者十倍，至大乘末期突破后即迎来考验，历经九重雷劫后方能破界飞升。

　　修炼途中考验重重，化神后若想再行突破，非但要有万中挑一的天赋，还需有天赐的奇遇机缘。

是以距三界分辟虽已有数万年，升至上界者寥寥数人。

即便如此，求长生者依旧前赴后继，修炼之法千变万化，渐渐形成宗门林立纷争不休的局面。
    """
    nvl clear
    hide cg1-1-2

    show cg1-1-3:
        xalign 1.0
        yalign 0.0
        zoom 1.3
        parallel:
            linear 10 xalign 0.0
        parallel:
            linear 10 yalign 1.0
    with fade
    nrr """
        其中正道宗门中以云浮山天一宗为尊。

        万年间飞升寥寥数人中天一宗占其二，其一为开山师祖天一道人，于万年前登仙。

        其后日渐式微，直至两千年前，九嶷山降异象，灵气奔涌而至，水镜真人于此地悟道，得机缘修为大成，飞升前留圣物苍梧剑庇护宗门。

        而后同门师弟孤鸿尊者突破至洞虚境界，天一宗得以复兴，千年间无人敢犯。
    """
    nvl clear
    hide cg1-1-3

    show black
    with fade
    nrr """
        毕竟，孤鸿尊者是当世三名洞虚修士中修为最深的，同时天一宗还拥有三位化神期长老，而整个修真界数百宗门里尽数也不过五十余化神期修士，稍微有点理智的人都不会想不开去得罪天一宗。

　　然而这世间毕竟还有疯子存在，

比如说那正道邪道都头痛不已的魔头千面偃。
    """
    # with fade

    window hide

    with Pause(2.0)
    window hide

    scene yunfushan_far

    with Shake_screen((0, 0, 0, 0), 0.8, dist=5)
    show qmy with dissolve
    qmy jianxiao1 "哈哈哈，本君大驾光临，天一宗的小崽子们还不奉茶！"

    "只见那人面色蜡黄，眼睛细长，瘦高的身板上裹一袭明黄色道袍，头戴着高高的道冠，{p}
    不知是无心还是刻意，道冠歪向一边，背上插支拂尘，两襟画着几撇鬼画符似的图案，从头到脚散发着招摇撞骗的味道。"

    "可就是这个江湖术士打扮的家伙，将云中最古老的修真世家叶家名下七座灵脉掏空一半；{p}
    夺了岭南三大妖的内丹将他们打回原形；还在昆吾城大闹过一场，将最高那座城楼的屋顶拆下丢去凡人帝都。"
    "兴风作浪三百余年，名字常年在招讨悬赏榜前十，却无人知其来路，只知他行事乖张，喜怒无常，见了最好绕道走。"
    # hide qmy

    scene yunfushan_door
    with fade

    "来人一路畅通无阻到了大殿上，笑嘻嘻左瞧右盼一番后正想往后山去，"
    play sound "sound/audio/施法/发招.wav"
    show white:
        alpha 0
        easein 0.5 alpha 0.4
        easeout 0.5 alpha 0
    "前方忽的爆发出一阵白光，足尖一点霎时顿住身形，挥手划出屏障将自己护住。"

    show yy with dissolve
    "待白光散开后，便见一个紫袍玉冠的年轻男子挡在他面前，方才白光便是他挥出的三道灵符所致，而对方身后跟了二十余名青灰色人影。"
    "男子看来不过三十岁左右，实则已有八百年道行，只差一步便及化神，正是天一宗现任宗主云逸，在安置好门中的年轻弟子便立刻赶去，恰好在半途与他对上。"
    "如今正是门内空虚之际。\n
　　孤鸿尊者闭死关，三位化神期长老率大半弟子赴须弥之海。"
    "须弥之海即为那被灵气笼罩九嶷山颠，水镜真人于此飞升后，其他修真者纷涌而至，可那山头却被平地拔起，此后每五百年一现，仅存五年。\n
    其间灵气充沛，复危机重重，入而得出者仅十中三四，即便如此，开启时仍有修真者争相涌入。"
    "此次不知为何，天一宗三位化神期长老竟一起动身前往，云逸虽觉奇怪却没敢多过问，此时肠子都要悔青了。"
    show yy chensi with dissolve
    "早知道怎么也要求一个留下啊！"
    "云逸看千面偃行动自如的样子，着实有些没底气，按理护山法阵启动后灵力应该会被大幅度限制才对，但目前他还是探不出对方实力，他不知道对方这是没受影响还是被限制后仍是这等强劲，不管哪种对他来说都不是好消息。"
    "刚刚他连拍三张符，千面偃却连点事都没有，还有闲心去扶帽子一把。"
    play sound "sound/audio/多人脚步.mp3" volume 2.0
    hide yy with dissolve
    show ptdz:
        xalign 0.0
        yalign 1.0
        easein 0.3 xalign 0.05
    show ptdz2:
        xalign 0.2
        yalign 1.0
        easein 0.5 xalign 0.25
    show ptdz3:
        xalign 0.4
        yalign 1.0
        easein 0.5 xalign 0.45
    show ptdz4:
        xalign 0.6
        yalign 1.0
        easein 0.5 xalign 0.65
    show ptdz5:
        xalign 0.8
        yalign 1.0
        easein 0.5 xalign 0.85
    "这时十几道青灰色身影自后方出现，将千面偃团团围住，弟子们在十里外布下三重防御阵，不料连那魔头的衣角都没沾到就被闯了过去，追得焦头烂额却见距离越来越远。\n
    如今好不容易赶上了，脾气暴躁的几个不由分说就想冲上去，却被云逸阻住。"
    # hide ptdz with dissolve
    # hide ptdz2 with dissolve
    # hide ptdz3 with dissolve
    # hide ptdz4 with dissolve
    # hide ptdz5 with dissolve

    scene yunfushan_door
    show yy with dissolve
    "云逸左手迅速划了一个结印，作揖朗声道："
    # show yy fennu with dissolve
    yy fennu "在下云逸，敢问道友前来有何贵干？"
    hide yy with dissolve

    show qmy with dissolve
    qmy jianxiao1 "当然是有贵干。"
    "那千面偃竟也规规矩矩回了个礼，"
    qmy jianxiao1 "本君想向贵派讨个礼物，贵派地大物博，多半是不会吝啬的。"
    hide qmy with dissolve

    show yy with dissolve
    play sound "sound/audio/施法/持续施法.wav" volume 6.0 loop
    show effect 1-1-1:
        xcenter 0.5
        yalign 1.0
        alpha 0
        easein 2 alpha 0.4
        easeout 2 alpha 0
        repeat
        # easeout 0.5 alpha 0
    yy "不知道友看上鄙派何物？"
    "云逸维持着平静的神情，足下运起罡风，做好迎战准备。"
    show yy dark
    qmy "苍梧剑。"
    stop sound
    show yy
    "云逸顿时冷了脸，道："
    yy fennu "此乃本门圣物，岂容觊觎，列阵！"

    scene yunfushan_door
    with dissolve
    show ptdz:
        xalign 0.0
        yalign 1.0
        easein 0.3 xalign 0.05
    show ptdz2:
        xalign 0.2
        yalign 1.0
        easein 0.5 xalign 0.25
    show ptdz3:
        xalign 0.4
        yalign 1.0
        easein 0.5 xalign 0.45
    show ptdz4:
        xalign 0.6
        yalign 1.0
        easein 0.5 xalign 0.65
    show ptdz5:
        xalign 0.8
        yalign 1.0
        easein 0.5 xalign 0.85

    with Pause(0.5)

    show effect 1-1-2:
        xcenter 0.5
        ycenter 1
        zoom 1.5
        alpha 0.8
        on show:
            parallel:
                easein 1.5 rotate 540
            parallel:
                easein 1.5 ycenter 0.4
    with Pause(1.5)
    show effect 1-1-2:
        xcenter 0.5
        ycenter 0.4
        zoom 1.5
        alpha 0.8
        rotate 180
        ease 1 alpha 0
        ease 1 alpha 0.8
        repeat

    # show effect 1-1-2:
    #     easein 2 alpha 1
    #     easeout 2 alpha 0

    "“阵”字一出口，便见剑光爆起，转瞬间共二十八人将千面偃围在中央。\n
刚刚云逸那个结印便是列阵的指示。"
    "此乃开宗的天一道人留下的四灵诛邪阵，列阵二十八人修为不高，大多为金丹期，在阵法加持下齐力可斩化神高手。"
    "云逸见弟子们步法错落有致，心中不安稍稍散开，可下一瞬便听到三声冷笑。"

    scene yunfushan_door
    with dissolve
    show qmy with dissolve
    qmy "乱七八糟的，拿去杀狗都不配!"
    show qmy at nod(y=10, t=0.1)
    play sound "sound/audio/移动呼声/布料呼声.mp3" volume 3.0
    image zhaohunfan = "images/obj/招魂幡.png"
    show zhaohunfan:
        zoom 3.5
        xcenter 640-150
        yalign 1.2
    "千面偃手一扬，掌中现出一丈多长的招魂幡，口中念念有词，"
    qmy fennu "魂兮归来！"
    show qmy:
        alpha 0.7
    play sound "sound/audio/碎裂.wav" volume 0.5
    "声音刚落，便听得西方昴宿的门人惊呼，原来是他想要踩的方位先一步被一团白雾占了，动作一滞，阵型顿时乱了。"

    scene yunfushan_door with dissolve
    show yy fennu  with dissolve
    "糟糕！云逸在旁看得真切，心下一片冰凉。"
    "那门人的确慢了分毫，但那是云逸参悟此阵两百年，方能一眼看出，可千面偃应是第一次见识此阵，竟能一瞬抓住空隙。"
    "他到底是什么人？"

    scene yunfushan_door with dissolve
    show qmy with dissolve
    qmy yinchen "怎么就一团影子？"
    "千面偃没看被搅乱的阵型，也没去理会云逸煞白的脸色，而是皱着眉晃了晃招魂幡，低声抱怨几句后再度念念有词，"
    qmy fennu "魑魅魍魉，横行无忌！"

    scene yunfushan_door with dissolve
    show ptdz:
        xalign 0.0
        yalign 1.0
    show ptdz2:
        xalign 0.2
        yalign 1.0
    show ptdz3:
        xalign 0.4
        yalign 1.0
    show ptdz4:
        xalign 0.6
        yalign 1.0
    show ptdz5:
        xalign 0.8
        yalign 1.0
    show effect 1-1-2:
        xcenter 0.5
        ycenter 0.4
        zoom 1.5
        alpha 0.8
    with Pause(1.0)
    queue sound [ "sound/audio/碎裂.wav", "sound/audio/彻底碎.wav" ]
    with Pause(3.0)
    show effect 1-1-2 at hide_extend(z=1.5, y=0, t=0.7)

    "这次三团雾影占据东南北三角，另外一团竟径直占了阵眼，将原本微乱的阵型彻底摧毁，二十八位弟子霎时被震得四散，一个个面色惨白，神魂不定。"
    show ptdz at hide_tb(t=0.3)
    show ptdz2 at hide_tb(t=0.3)
    show ptdz3 at hide_tb(t=0.3)
    show ptdz4 at hide_tb(t=0.3)
    show ptdz5 at hide_tb(t=0.3)

    with Pause(1.0)
    show qmy fennu with dissolve
    show qmy fennu at wobbly
    "这般战绩，换作其他人怕是要吹嘘百年，可千面偃却是一脸怒容瞪着招魂幡。"
    qmy fennu "骗子！"
    "只听他怒喝一声，而后扬手将那招魂幡折成两段往地上一丢，指着断裂的幡杆跳脚骂道，"
    qmy fennu "说是能召实体鬼魂呢！可好花了我两千灵石！"

    scene yunfushan_door with dissolve
    show yy  with dissolve
    "云逸额头顿时冷汗涔涔，他看出那招魂幡是元婴期以上的法宝，竟被弃之如敝履，其余门人亦是目瞪口呆看那千面偃自顾自唱起独角戏。"
    "——怕真是个疯子。\n
众人脑海中不约而同浮现出这个想法。"
    show yy biyan with dissolve
    "云逸毕竟是宗门之主，很快镇定下来，祭出本命法具，朝千面偃冲去，同时下令道："
    yy fennu "金丹期弟子速回后山，余下弟子速速前来相助。"
    hide yy with dissolve

    show qmy jianxiao1 with dissolve
    image yushi = "images/obj/玉石.png"
    show yushi:
        zoom 1.0
        xcenter 640-50
        ycenter 0.5
    with dissolve
    with Pause(1.0)
    "千面偃见他冲来，面上露出一丝轻蔑，手一翻，掌心托起一方印石掷去。"
    show yushi at hide_extend(t=1.0)
    with Pause(1.0)
    show white:
        alpha 0
        easein 1.5 alpha 0.4
        easeout 1.5 alpha 0

    play sound "sound/audio/爆炸坍塌.wav" volume 0.5
    with Shake_screen((0, 0, 0, 0), 5, dist=15)

    scene yunfushan_door
    with tran_lf
    show yy fennu with dissolve
    with Pause(1.0)
    image feidan = "images/cg/法术-技能-飞弹.png"
    show feidan:
        zoom 1.6
    with close
    "两件宝具相撞，一阵灵气动荡后，那印石竟直接击碎了云逸的法具，直奔他脑门而去。"
    hide feidan
    with close
    with Pause(1.0)
    "眼看印石击中云逸眉心在即，地上蓦地浮起一道柔和的青光罩住云逸，"
    play sound "sound/audio/施法/发招.wav"
    image huzhao = "images/effect/护罩.png"
    show huzhao:
        xcenter 0.5
        yalign 1.0
        zoom 3.5
        alpha 1.0
        ease 1 alpha 0
        ease 1 alpha 1.0
        repeat

    with Pause(1.0)
    show feidan:
        zoom 1.6
    with close
    hide feidan
    with close

    play sound "sound/audio/爆炸.wav" volume 0.5
    with Shake_screen((0, 0, 0, 0), 2, dist=15)
    "只见印石重重撞上青光，冲击将云逸撞得晃了晃，分毫无损。"
    "云逸一愣，随后立刻反应过来，"
    yy "护山法阵！"

    jump story_1_2
