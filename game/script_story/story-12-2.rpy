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

label story_12_2:

    image cg12-2-1 = "images/cg/CG-12-1-1.jpg"
    image cg12-2-2 = "images/cg/CG-12-1-2.jpg"
    image cg12-2-3 = "images/cg/CG-12-1-3.jpg"

    stop music fadeout 2.0
    scene tiantaifeng xiaowu2 with Fade(0.8, 0.8, 0.8)
    with Pause(0.5)
    show ltl at pos_ltl with dissolve
    with Pause(1.5)
    nrr """
    {clear}

    回到住所，钟明烛一眼就看到长离坐在院子里，而对面有个银发黑袍人。\n\n

    这还是她第一次在重明居看到客人。
    """
    play sound "sound/audio/移动呼声/布料呼声.mp3"
    zmz "师父，我回来了。"
    "落地后，她和长离打了个招呼，就往那黑衣人看去，发现对方虽然一头银发，模样却是个女童。"
    "约莫十一二岁，比她入门时候年纪还小，手里捧着一杯茶坐在椅子上，双脚悬空，不停晃荡着，面前摆了个空碟子，看起来有些百无聊赖的模样。"
    "难道是新入门的弟子？"
    "她立刻打消了这个念头，新入门的弟子皆是青衫，而且也不可能出现在天台峰，还和长离相对而坐。"
    ltl "这就是你收来的徒弟？"
    "女童问长离，看都没看钟明烛一眼，声音软软的，有些有气无力，像是在犯困一样。"
    cl "是。"
    "长离一如既往地言简意赅，瞥见钟明烛脸上的疑惑，便向她介绍道，"
    cl "这位是我师叔。"
    ltl "龙田鲤。"
    "银发女童补充道。"
    window hide
    with Pause(1.0)
    "钟明烛震惊了。"
    "这个名字她当然还记得，当年就是因为觉得这名字很有趣才会揭了那玉牒，之后才得以遇到长离。{p}之后她就再也没有遇到她发布的任务，还耿耿于怀了很久。"
    "自从知道龙田鲤是怀有千年修为的化神期长老，她一直以为会是个白发老妪或者是风韵犹存的中年妇人，怎么也没想到会是个十多岁女童。{p}虽然一头白发，但配着那张稚嫩的脸庞，根本就没有苍老的感觉，反而有种别样的超然感。"
    zmz "太师叔好，我叫钟明烛。"
    "她恭恭敬敬行了个礼，抬起头后眼神里还是满满的好奇，仔细打量着龙田鲤的脸，试图找出一丝皱纹来。"
    "注意到她的眼神，龙田鲤问："
    ltl "你想知道我为什么是这个模样？"
    "钟明烛想也没想就点了点头，活了上千年却长这样，很难叫人不在意啊。"
    ltl "你不怕我？"
    "龙田鲤还是那副困倦的模样，却稍稍侧过头，打量起钟明烛。"
    hide ltl with dissolve
    show zmz b at pos_zmz with dissolve
    zmz b chijing "为什么要怕你？"
    "钟明烛不解，下一瞬便见龙田鲤眸底掠过一丝晦暗不明的光。{p}还未及分辨那是什么，便觉一股灵压迎面而来。"
    play music "sound/bgm/董冬冬 - 悬念.mp3"
    # hide zmz with dissolve
    show zmz b toutong at pos_zmz_toutong with dissolve
    with Pause(0.5)
    show white:
        alpha 0.0
        linear 0.15 alpha 1.0
        linear 0.15 alpha 0.0
    with Pause(0.3)
    show white:
        alpha 0.0
        linear 0.15 alpha 1.0
        linear 0.15 alpha 0.0
    "难以形容的强大，钟明烛觉得自己仿佛只是洪流中的一粒米粟，顷刻便会被压得粉碎。浅色的眸子里倒映出飞扬的白发，龙田鲤还是捧着茶坐在那，可她却觉得前额被什么刺透，探入了灵海。"
    window hide
    play sound "sound/audio/耳鸣.wav" loop
    show red:
        alpha 0.0
        linear 0.15 alpha 1.0
        linear 0.15 alpha 0.0
    with Pause(0.3)
    show red:
        alpha 0.0
        linear 0.15 alpha 1.0
        linear 0.15 alpha 0.0
    with Pause(1.0)
    image cg-5-1-2_red = im.MatrixColor(
        "images/cg/CG-5-1-2.jpg",
        im.matrix.tint(1.0, 0.2, 0.2)
    )
    image cg-10-1-1_red = im.MatrixColor(
        "images/cg/CG-10-1-1.jpg",
        im.matrix.tint(1.0, 0.2, 0.2)
    )
    image cg-7-1-1_red = im.MatrixColor(
        "images/cg/CG-7-1-1.jpg",
        im.matrix.tint(1.0, 0.2, 0.2)
    )
    image tiantaifeng_red = im.MatrixColor(
        "images/bg/天台峰-房间2.jpg",
        im.matrix.tint(1.0, 0.2, 0.2)
    )
    image yunfushan_red = im.MatrixColor(
        "images/bg/云浮山-广场.jpg",
        im.matrix.tint(1.0, 0.2, 0.2)
    )
    image shanmen_red = im.MatrixColor(
        "images/bg/山门.jpg",
        im.matrix.tint(1.0, 0.2, 0.2)
    )
    image zhaizi_red = im.MatrixColor(
        "images/bg/废弃古宅.jpg",
        im.matrix.tint(1.0, 0.2, 0.2)
    )
    image yangshan_red = im.MatrixColor(
        "images/bg/阳山2.png",
        im.matrix.tint(1.0, 0.2, 0.2)
    )
    show cg-5-1-2_red with close
    with Pause(0.5)
    show cg-7-1-1_red with dissolve
    with Pause(0.5)
    show yunfushan_red with dissolve
    with Pause(0.5)
    show tiantaifeng_red with dissolve
    with Pause(0.5)
    show cg-10-1-1_red with dissolve
    with Pause(0.5)
    show shanmen_red with dissolve
    with Pause(0.5)
    show zhaizi_red with dissolve
    with Pause(0.5)
    show yangshan_red with dissolve
    with Pause(1.0)
    show blood a at CG_800_600 with dissolve
    with Pause(0.8)
    show blood b at CG_800_600 with dissolve

    nrr """
    {clear}

    剧烈的疼痛自灵海深处传来，破碎的画面在眼前飞旋，有与长离一起的，也有外门弟子时期的，最后停留在缓缓流淌的鲜血中。

    她试图说什么，却什么声音都发不出，几乎要将身体都撕裂疼痛毫不留情地侵入每一个关节，就在她觉得自己快无法承受的时候，身子忽然一轻。
    """

    window hide
    play sound "sound/audio/移动呼声/布料呼声.mp3"
    image tiankong_blur_1 = im.Blur("images/bg/天空-云朵(6)_720.jpg", 100)
    image tiankong_blur_2 = im.Blur("images/bg/天空-云朵(6)_720.jpg", 10)
    scene tiankong_blur_1 with tran_close
    with Pause(2.0)

    nrr """
    {clear}

    空气与灵力一起涌入心脾，她大口喘着气，像刚被救上岸的溺水者，睁着眼却只能看到一片混沌，周围一切都迷迷糊糊的，索性直接闭上眼。

    终于能发声时，她骂了一句脏话，然后上气不接下气瘫软了身子想往一边倒下，但立刻被扯住了。
    """
    scene tiankong_blur_2 with tran_close
    nrr """
    {clear}

    “站稳。”\n耳边传来这般嘱咐。
    """

    image cg12-2-1_blur = im.Blur("images/cg/CG-12-1-1.jpg", 5)
    scene cg12-2-1_blur with tran_close
    show cg12-2-1:
        alpha 0.0
        easein 1.0 alpha 1.0
        easein 1.0 alpha 0.0
        pause 1.0
        easein 1.0 alpha 1.0
        easein 1.0 alpha 0.0
        pause 1.0
        easein 1.0 alpha 1.0
    with Pause(9.0)
    nrr """
    {clear}

    她才发现正处在高空，确切来说，正站在长离飞剑上，更确切一点，是倚在长离怀中。

    被冷香包围，她的个子快和长离差不多高了，无需抬头，就可以看见她修长的睫毛，以及睫毛下漆黑的眼眸。\n\n

    漆黑如浓墨，却比墨色多了几分清亮。

    更像星辰闪耀的夜空吧，钟明烛昏沉沉地想。
    """
    window hide

    show cl zhijian at pos_cl_zhijian with dissolve
    image gif_jian = SquenceAnimator("images/effect/剑", interval=0.15)
    play sound "sound/audio/刀剑/刀剑音效11秒.wav"
    show gif_jian:
        xcenter 0.5
        yalign 1.0
        zoom 2.5
        alpha 0.0
        easein 0.5 alpha 0.5
    with Pause(2.0)
    "长离左手揽着她，右手握着一把通体漆黑的长剑，还有数不清的剑影绕着她不停旋转，发出阵阵清啸，正在与那股灵压对抗。"
    cl "不知师叔此举何意？"
    "她一眼不眨看着住所方向，问道。"
    "从开始到结束其实只是几个眨眼的功夫，那偌大的庭院如今看起来只是个小黑点，长离速度之快可见一斑。"
    ltl "离儿的身手见长了呢。"
    "龙田鲤的声音清晰地传来,"
    ltl "回来吧。"
    show gif_jian:
        easein 1.0 alpha 0.0
    show cl at pos_cl with dissolve
    play sound "sound/audio/刀剑/破风剑光.wav"
    with Pause(1.0)
    cl "是。"
    "长离答应后就松开剑，那些剑影长吟了一声与那柄剑合为一体，原来都是自那剑中分出的剑气。"

    play sound "sound/audio/移动呼声/布料呼声.mp3"
    scene tiantaifeng xiaowu2 with tran_df
    "之后钟明烛觉得眼前一花，便又站回了院子里，她还有点头晕，所以抱着长离的胳膊不放，瞪了龙田鲤半晌忽而怒道："
    zmz "就算这样我也不怕你。"
    show ltl at pos_ltl with dissolve
    ltl "哦？倒是有骨气。"
    "龙田鲤放下茶杯，自椅子上跳下来，朝她走过来。"
    hide ltl with dissolve
    show cl at pos_cl with dissolve
    "长离见状不动神色将钟明烛塞到自己身后，将方才的问题又问了一遍："
    cl "不知师叔此举何意？"
    hide cl with dissolve
    show ltl at pos_ltl with dissolve
    ltl "这么胆大包天的小崽子，我看看她是不是被人夺舍了。"
    "龙田鲤漫不经心地挥了挥手，仿佛刚刚只是给钟明烛把了个脉，而不是将她的灵海搅了一番似的，末了还轻描淡写加了句保证，"
    ltl "安心，死不了的，死了我负责给她重塑肉身召回三魂六魄。"
    stop music fadeout 2.0
    hide ltl with dissolve
    show zmz b shengqi at pos_zmz with dissolve
    "这种话根本不会让人安心好吗！"
    "磨了磨牙，钟明烛强忍住破口大骂的冲动，她回想起当初看到的第一份任务末尾重复了三遍的话，顿时觉得发生在自己身上就一点都不好笑了。"
    "这老太婆肯定是个疯子！"
    "她斜眼看着走到自己身前的银发女童，故意抬高下巴，自牙缝里挤出不冷不热的声音："
    zmz b shengqixiao "那太师叔可有发现我被何人夺舍。"
    hide zmz with dissolve
    show ltl at pos_ltl with dissolve
    ltl "没有，你这自寻死路的性格大约是天生的。"
    "龙田鲤打了个哈欠，像是彻底失了和她计较的兴致，"
    ltl "不过你灵海有一处缺损，可是受过伤？"
    hide ltl with dissolve
    show zmz b chijing at pos_zmz with dissolve
    zmz "受伤？"
    show zmz b sikao at pos_zmz_sikao with dissolve
    "钟明烛一愣，寻思道自己似乎没受过什么伤，而后想起最初被邪修所掳之事，心想只会和那个有关，便将其一一说来。"
    hide zmz with dissolve
    show ltl at pos_ltl with dissolve
    ltl "原来如此。你失忆应当和那处灵海受损有关。"
    zmz "可有办法救治？"
    "对于自己以前是什么样的人，钟明烛还是有点好奇的。"
    "龙田鲤却摇了摇头，答道："
    ltl "灵海与仙骨为一体，修复灵海与重铸仙骨方法一致，在连山经上曾有记载，但我手上只有残本，只提及所需的部分灵材，而无炼药之法。"
    ltl "不过那灵物十分罕见，说不定已经绝迹，即使有炼药之法也难以凑齐素材，再者从未在其他记载上见过重铸仙骨之法，连山经上所言也不可尽信。"
    "说到医药相关时，她语气中的困倦一扫而空，时而热切时而惋惜，表情也丰富了许多。"
    zmz "不知需要那些灵物？"
    ltl "残片上记了的是真龙之骨和女娲大神补天的五色石。"
    hide ltl with dissolve
    show zmz b at pos_zmz with dissolve
    zmz b ganga "啊，那的确是……"
    "钟明烛摸了摸鼻子，干笑起来。"
    "真龙为神，下界哪里还有踪迹，而那五色石石根本就是上古神话中才有的，连是否存在都不得而知，就算存在，要集齐这两样怕是比渡劫飞升还难。"
    show zmz b tanqi with dissolve
    "看来只能继续猜了，自己以前是怎样的人，不过还是稍微有些遗憾的。"
    hide zmz with dissolve
    show cl at pos_cl with dissolve
    with Pause(0.6)
    show cl kunhuo with dissolve
    "她揉了揉额心，轻轻叹了一口气，长离看了她一眼，很快移开目光。"

    scene tiantaifeng xiaowu2 with fade
    nrr """
    {clear}

    又喝了几杯茶，龙田鲤才告辞，她没有御剑，而是招来了一只白鹤。
    """
    play sound "sound/audio/环境/鹰啼.wav"
    scene cg12-2-2 with dissolve
    with Pause(1.5)
    nrr """
    {clear}

    当白鹤展开翅膀，驮着银发黑衣的女童翩然往西边她所居之处而去时，看起来美不胜收。
    """
    play music "sound/bgm/卢小旭 - 鹧鸪天.mp3"
    nrr """
    {clear}

    然而钟明烛却望着她离去的方向扬了扬眉，而后忍不住笑起来。
    """
    scene tiantaifeng xiaowu2 with dissolve
    show zmz b miyanxiao at pos_zmz with dissolve
    zmz "是驾鹤西去呢。"
    show zmz b chijing with dissolve
    "过了一会儿她突然一拍脑门，痛心疾首地皱起眉，过了一会儿闷闷地出声："
    zmz b ganga "师父……"
    cl "何事？"
    zmz "你可知道我这个太师叔，是姓龙还是龙田？"
    "问完她突然想到长离没有姓，于是又追加了一种可能，"
    zmz "还是无姓，名龙田鲤？"
    with Pause(2.0)
    "长离沉默了一会儿，而后开口，神色如常道："
    cl "不知道，你该练剑了。"
    zmz "哦……"
    hide zmz with dissolve
    stop music
    "钟明烛干巴巴应了一声，就往外走去，快到门口时听到了长离地声音。"
    cl "五百年前，师叔炼丹时出了意外。"

    scene cg12-2-3 with tran_lf
    play music "sound/bgm/汀玄·墨姜 - 飞雪玉花 古琴版.mp3"
    with Pause(2.0)
    nrr """
    {clear}

    只此一句，说完她就落座于琴台前，单手一抚，细细聆听拨弄出几个音节，之后调节起琴弦来。

　　那张五弦琴是钟明烛炼器所得，用了桐木、鲛绡、银沙还有一点赤金，琴音蕴含灵力，可作法器，不过她们两人似乎都用不上，就在院中添了座琴台，闲暇时奏一曲以消磨时光。

{clear}

　　离开院子不久，身后便传来琴声，钟明烛却还想着长离对她说的那句话。

　　乍听之下有些莫名，她也是过了一会儿才反应过来，对方是在告诉她龙田鲤这副模样的原因，她本以为长离定然不知道的，所以根本没有想到去问她。

　　龙田鲤照顾长离到九岁，那九岁之前的长离大抵还不像后来那般冷若霜雪，可能那时候也曾好奇过，还问了。

　　没有人出生就是个冰渣子。
    """

    scene black with fade
    nrr """
    {clear}

　　还有三个月就是大会了，看着远方延绵不绝的山脉，她又想到了这茬。

　　需要在此之前炼出本命法器，时间有点紧，不过有师父在，应该没什么问题。

　　她决定练完这该死的剑就去找长离一起开炼炉，继而又想，若是没挤进前三十，到时候求师父偷偷带她下山，成功几率有多少。

　　“大概五成吧。” 她习惯性地摸了摸鼻子，感到有些遗憾。
    """

    jump story_13_1
