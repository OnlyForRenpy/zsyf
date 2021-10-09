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

label story_3_2:

    image effect 3-1-1 = "images/effect/施法.png"

    stop music
    scene black with fade
    with Pause(1.0)

    scene shangshan b with tran_close

    nrr """
        {clear}

        山道算不上陡峭，两畔树木葱郁，花香袅袅，缭绕不散的淡雾令一切都胜似泼墨画卷一般带着几分朦胧，美不胜收。

　　她不紧不慢地走着，累了就休息，休息够了就继续往前走，路上一个人都没碰到，不管往前还是往后看，景色总是一个样子。

就这样过了七天，雾气突然散开。
    """
    stop sound fadeout 1.5

    scene shanmen with MultipleTransition([False, close ,Solid("#fff"), close ,True])
    window hide
    with Pause(1.5)
    scene white with close
    play sound "sound/audio/环境/风-自然.mp3" volume 5.0 loop
    show yunfushan quanjing:
        xoffset 0
        yoffset 0
        zoom 1.5
        alpha 0.0
        parallel:
            easein 0.8 alpha 1.0
            pause 1.4
            easein 0.8 alpha 0.0
        parallel:
            linear 3 xoffset -200 yoffset -150
    with Pause(3)
    show yunfushan quanjing:
        xalign 1.0
        yalign 1.0
        xoffset 0 yoffset 0
        zoom 1.5
        alpha 0.0
        parallel:
            easein 0.8 alpha 1.0
            pause 1.4
            easein 0.8 alpha 0.0
        parallel:
            linear 3 xoffset 200 yoffset 150
    with Pause(3)

    scene yunfushan quanjing with close

    nrr """
        {clear}

        飞檐斗拱，巍峨描画的轮廓显得威严不可逼视，正中“天一宗”三字潇洒飘逸，细看之下似化作金蛇狂舞，其后是青石板铺成的台阶，笔直往上插入云端，云后隐隐显出宫殿的影子。

　　钟明烛轻轻吐了一口气，心跳不由加快了起来。

　　这就是仙门。

　　若说路上她还抱着可有可无的心态，当看到延绵数万里的山峦时，她已没了回头的打算。

　　甚至胸中浮现出一种近乎盲目的自信，自己一定能跨进那道石门。
    """
    stop sound fadeout 2.0

    scene yunfushan qiandian with MultipleTransition([False, close ,Solid("#fff"), close ,True])
    nrr """
        {clear}

        及走近，才发现门前已有不少人。数了数，足足有一百多人。

　　这一路上她都没见到其他人，想是这山道被布下了什么法术吧。

　　队伍中大部分是十几岁的少男少女，也有几个三十多岁的中年人。

{clear}

　　——我今年多大？

　　突然想到这个问题，脑海浮出梳妆时铜镜中映照的脸庞。

　　十五？还是十六？

　　不知为何她隐约觉得自己没那么年幼。

　　难道自己是那种长得比较嫩的类型？

　　疑惑地摸了摸脸，可继续想下去头便疼了起来，遂打住，慢吞吞向队伍末尾走去。
    """

    play music "sound/bgm/曾志豪 - 少年游.mp3"
    show zmz at pos_zmz with dissolve
    "在队尾站定后，前面的人转过头来瞧了瞧她，钟明烛立即报以无可挑剔的微笑，点头道："
    zmz "你好。"
    hide zmz with dissolve
    show dly with dissolve
    with Pause(1.0)
    "那是一个穿白衣的少女，料子剪裁很精致，大抵也是世家出身。脸圆圆的，眼睛也圆圆的，长得很可爱，见钟明烛向自己问好，便细声细气地回道："
    dly "你好，我叫丁灵云。"
    zmz "钟明烛。"
    "礼尚往来，钟明烛也给出了自己的名字，说完后她就踮脚往前看去。"

    scene yunfushan qiandian with tran_lf
    image threepeople = Fixed(
        Image("images/char/其他/木丹心.png", xcenter=0.8, ycenter=0.75),
        Image("images/char/其他/云逸-普通.png", xcenter=0.5, ycenter=0.65),
        Image("images/char/其他/风海楼-正常.png", xcenter=0.25, ycenter=0.7),
    )
    show threepeople with dissolve

    "山门后有站着一排人，为首是个紫袍玉冠的年轻男子，\n
风海楼捧玉盘站在那男子身边，同样是紫衣，之前她印象中风海楼一直是和和气气的模样，如今正式而华丽的穿著，让他倒有几分不怒自威的感觉。\n
无名紫衣男子斜后方是一个须发皆白黑袍老者，目含精光，地位应该很高，他身后是十几个青衫人，男女各半。"
    "入门测试已经开始，据风海楼说就是灵力测试，钟明烛看不到是怎么个测法，只能看出很严格，排在前头的，约莫有三分之二被挡在了山门外。"

    scene yunfushan qiandian with tran_lf
    show zmz sikao at pos_zmz_sikao with dissolve
    zmz sikao "嘶……感觉很苛刻啊……"
    "她自言自语道。"
    hide zmz with dissolve
    show dly with dissolve
    "这话被丁灵云听到，她立刻附和地猛点头，"
    transform nod2(y=20, t=0.24):
        easein t yoffset y
        easeout t yoffset 0
        easein t yoffset y
        easeout t yoffset 0
    show dly at nod2(y=10, t=0.2)
    dly "毕竟是第一大仙宗，不像有些广罗门徒的宗派，天一宗招收弟子一向是宁缺毋滥。"
    show dly dark
    zmz "感觉很厉害……"
    show dly
    show dly at nod(y=10, t=0.2)
    dly "是啊！"
    "丁灵云继续点头，"
    dly "能进入天一宗内门修炼的弟子，各个都是人中龙凤！"

    scene yunfushan qiandian with tran_lf
    show fhl
    "人中龙凤？钟明烛往风海楼的方向瞥了一眼，心想那少年原来那么厉害。"
    "丁灵云性子热络，她见钟明烛的打扮不似出自修真世家，便没想过她会认识风海楼，见她往那边看去，立刻给她介绍起来："
    dly "那个紫衣少年叫风海楼，是宗主云逸唯一的亲传弟子，百岁出头便已结丹，是年轻一辈中当之无愧的佼佼者，不过比起长离仙子还差了点。"
    hide fhl with dissolve
    show zmz sikao at pos_zmz_sikao with dissolve
    zmz sikao "长离仙子？"
    show zmz sikao:
        linear 0.6 xcenter 0.75
    show cl at objpos(x=0.3, y=360+160, z=0.5, a=0.5) with dissolve
    "钟明烛眯了眯眼，她听过这个名字，是风海楼的小师叔，也是自邪修手中救下了自己的人，她半昏半醒时的印象里的确有个模模糊糊的白色身影，也不知道是不是错觉，心中一边计较这结丹是什么以及风海楼那厮原来那么老了，一边下意识脱口而出问道，"
    show zmz at objpos(x=0.75, y=0.6, z=0.4) with dissolve
    zmz "她也很厉害吗？"

    scene yunfushan qiandian with dissolve
    show dly shengqi with dissolve
    dly "岂止是厉害！"
    "丁灵云听到她不咸不淡的口气，一下子竖起眉毛，眼中掠过一丝不快，好似受到了无礼冒犯。若非无知者无罪，她说不定要动手打人了，"
    dly "长离仙子可是几千年来首屈一指的天才，你可知她几岁便修得元婴？"
    with Shookhead_screen((0, 0, 0, 0), 0.5, dist=10)
    "钟明烛摇了摇头，心里嘀咕着元婴又是什么东西，但又不好问出口，她隐约觉得，既然能走到这山门口，若连这个都不知道，一定会为人耻笑。"
    "她不免埋怨起风海楼来，既然哄骗了她过来，不该多告诉她一些修炼相关的事吗！"
    show dly with dissolve
    dly "长离仙子三十四年前修炼出元婴，当时才一百八十三岁！"
    "丁灵云得意地抬起下巴，骄傲得像只开屏的孔雀，"
    dly "要知道，之前被奉为当世无双、天纵奇才的逐浪城主江临照，从入门到元婴，都花了三百多年。"
    show dly dark
    zmz "原来如此……"
    "钟明烛轻声应了一句，她还在计较之前的疑惑，又被几个陌生的字眼甩了一脸，着实有些稀里糊涂的，能够真切体会到的只有两点:{p}
修仙人的看起来年轻，实际上都是些老不死的，动不动就几百岁。{p}
以及——"
    play sound "sound/audio/星星棒.wav"
    show dly lianhong with dissolve
    "丁灵云一定是那个长离仙子的仰慕者，谈及长离仙子时，那双圆圆的眼睛里闪烁着异常明亮的光泽，甚至脸上还浮现出淡淡的红晕。"
    "若是告诉她，长离仙子救了自己一命、亲手喂了自己一颗保命的丹药还亲自送自己去了医馆，她会是什么表情呢？"
    hide dly with dissolve
    show zmz xieyanxiao at pos_zmz with dissolve
    "一定会很有趣，钟明烛勾起嘴角，心中忽地泛起一丝难耐的冲动。"

    scene yunfushan ceshi with tran_lf
    "不过她没能来得及说出来，因为这时候她们已挪到山门前，轮到丁灵云进行灵力测试了。"
    show dly with dissolve
    with Pause(1.0)
    show effect 3-1-1:
        xcenter 0.5
        yalign 1.0
        alpha 0
        easein 1 alpha 0.4
        easeout 1 alpha 0
        repeat
    with Pause(2.0)
    "钟明烛注意到山门左侧有个人双手捧着一块透明的石头，丁灵云走过去将手按到那石头上，而后那石头便发出柔和的光芒，那个人点了点头，对她做了个请的手势。"
    scene yunfushan ceshi with dissolve
    "看来是通过了呢，原来就是摸一下那块石头么……"
    "轮到自己了，钟明烛快步走到青衣人面前，如法炮制地将自己的手按上去，下一瞬便感到有什么自体内抽出，通过掌心流入那石头中。"
    zmz "咦？"
    show effect 3-1-1:
        xcenter 0.5
        yalign 1.0
        zoom 1.2
        alpha 0
        easein 1 alpha 0.6
        easeout 1 alpha 0
        repeat
    with Pause(2.0)
    "她惊讶地睁大眼，看着石头中迸发出近乎耀眼的光芒。"
    "看起来好像很了不起的样子？"

    scene yunfushan guangchang with tran_close
    show fhl with dissolve
    fhl "果然不出我所料，恭喜钟姑娘……"
    "穿过山门，钟明烛对上风海楼掩不住欣慰的笑容，"
    "啊，现在该叫师妹了。"
    hide fhl with dissolve
    show zmz at pos_zmz with dissolve
    "她挑了下眉，有些心不在焉地应了一声，从风海楼捧着的玉盘中拿起一枚方形木牌，按照指示挂在了腰带上。"
    "如今她便是这天下第一仙踪的弟子了，也算是半个人中龙凤了吧。\n想到丁灵云的话，她不禁轻笑出声。"
    show zmz miyanxiao with dissolve
    "——看来有机会再和她聊一下长离仙子的事了。{p}
她如此想着，愉快地眯了眯眼。"

    jump story_3_3
