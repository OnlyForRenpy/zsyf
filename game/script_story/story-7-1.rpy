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

label story_7_1:

    image cg7-1-1 = "images/cg/CG-7-1-1.jpg"

    image gif_huoyan1 = SquenceAnimator("images/effect/火焰", interval=0.1)
    image gif_huoyan2 = SquenceAnimator("images/effect/火焰", interval=0.1)
    # image gif_huoyan flip = im.Flip(gif_huoyan, horizontal=True)

    stop music fadeout 1.0
    window hide

    scene yunfushan shiliansenlin with fade

    nrr """
    {clear}

        试炼为期三天，要求穿过明镜峰下那片森林，出口在天一峰山道口，过了就直接上太乙广场等候安排。

　　三天内未能穿过森林即视为失败，只能回明镜峰再练上五年。

　　从明镜峰没有筑基期弟子的情况来看，根本无须担心通过率的问题。

　　穿过森林最快只需要一天，但途中会经过熊洞、沼泽，迷雾地等重重障碍，甚至有可能遇到山鬼。山鬼讨厌人，尤其是破坏森林的人，虽然受契约所制不能伤人，但这不妨碍他将踩坏花花草草的修行者打晕丢去林子入口或者绑到溪水里泡几个时辰。

　　还有一点，不能御剑。

{clear}

　　丁灵云很讲义气，开始之前还问钟明烛要不要和她一起。

　　“不用了，你加油。”

　　钟明烛一副胸有成竹的样子婉拒了。

{clear}

　　“真的没问题吗？你那些……符箓什么的……”

丁灵云还是有点不放心，她知道钟明烛的剑术连头熊都不见得能搞定，两人一起总好有个照应。

　　毕竟当初一见如故，又当了五年朋友，那些符箓她一剑能劈碎一打，怎么想都是不妥，非常不妥，但钟明烛仍然是拒绝。

　　“我自有分寸，最不济，沿着溪水走，三天爬也爬到了。”

　　沿溪水修有石路，此路最为安全，只不过绕的弯多，比起直行要多花一倍时间。

　　她话已至此，丁灵云便不强求，只嘱咐她多加小心。
    """
    window hide

    scene shulin b with fade
    play music "sound/bgm/芳賀敬太 - 臨戦.mp3"

    nrr """
    {clear}

        上一代元婴期门人齐聚太乙广场，对未来的宝贝徒弟们翘首以待。

　　明镜峰下，众弟子亦是摩拳擦掌，意欲一展宏图。

而就在胡清点燃森林入口两旁的火盆，示意试炼开始后，一马当先冲入林中的不是目前修为最高的南司楚和丁灵云，而是钟明烛。
    """

    window hide
    with Pause(1.5)
    play sound "sound/audio/移动呼声/消失1.wav" volume 2.0
    scene cg7-1-1 with close
    with Pause(2.0)
    nrr """
    {clear}

        只见她往腿上拍了一道符，当即足底生风，青衫化为一道虚影，眨眼就消失在树丛后，选的路径一目了然，是直行。

        不少人听到了她对南司楚的挑衅，大部分以为她只是说说，如今见了却不禁纷纷觉得说不定是真的，甚至有人惊呼出声。
    """
    scene cg7-1-1:
        xcenter 0.5
        ycenter 0.5
        easein 0.3 zoom 1.5

    scene cg7-1-1 with tran_close
    nrr """
    {clear}

        南司楚几乎在钟明烛离开的下一瞬就追了上去，心高气傲如他，怎么能容忍那番挑衅成真。

        注意到钟明烛所去的方向与自己原定之路重叠后，便盯着她的背影紧追不放。

        他自恃功法过人，决心一定要在这次试炼上脱颖而出，修为和丁灵云不相上下，剑法更胜一筹，对魁首志在必得，如今受了挑衅更是铁了心要对方好看。
    """

    scene cg7-1-1 with fade
    nrr """
    {clear}

        低阶的疾风符维持不了多久，约莫追了半日，前方那袭青衫速度终于慢了下来。
    """
    scene shulin b with dissolve
    nrr """
    {clear}

        这一路畅通无阻，没有遇到任何野兽精怪，他有些奇怪。

        但眼看钟明烛已近在咫尺，便顾不上考虑这些，手腕一转就招出长剑。
    """

    # scene gray with dissolve
    image shandian = "images/effect/闪电-小.png"
    queue sound ["sound/audio/施法/闪电攻击.wav", "sound/audio/施法/火炬  长时间.mp3"]
    show shandian:
        xcenter 0.5
        yalign 1.0
        zoom 1.0
        alpha 0.0
        easein 0.3 alpha 1.0
        # pause 1.0
        # easein 0.3 alpha 0.0
    show gif_huoyan1:
        xalign 0.1
        yalign 0.5
    show gif_huoyan2:
        xalign 0.9
        yalign 0.5
    # show gif_huoyan flip:
    #     xalign 0.9
    #     yalign 0.5
    nrr """
    {clear}

    剑风破空，卷起一道雷光朝那青衫少女奔去，而后又弹出两团火，左右夹击，钟明烛要么硬接其中一招，要么只能后退，不管怎样都会比逼退一些，而他的后招已蓄势以待。

    {clear}

        他面上已隐约浮出笑意，下一瞬，笑容却凝固了，因为钟明烛竟迎着雷光朝他扑来。

　　不知为何，她竟毫发无伤穿过了雷光，紧接着，一道纸符啪地一声被拍到南司楚的手臂上，他的手臂顿时僵住不能动弹。

之后另几道纸符跟上，贴上他的躯干四肢，将他整个人都定住。
    """
    stop sound

    window hide
    scene shulin b with dissolve
    show nsc with dissolve
    with Pause(0.3)
    play sound "sound/audio/施法/发招.wav"
    show bagua:
        xcenter 0.5
        ycenter 0.5
        zoom 1.0
        alpha 0.0
        rotate 180
        parallel:
            ease 1 alpha 0.7
            # ease 1 alpha 0.0
        parallel:
            ease 1 zoom 1.3
    with Pause(1.5)
    nrr """
    {clear}

        他很快就明白过来这是什么符，嘲讽道：“这符不过能维持一会儿，你逃不掉的。”

　　连疾风符他都能追上，这区区低阶禁锢符又能派上多少用场。

{clear}

　　“谁说我要逃。”钟明烛笑着回道。
    """

    window hide
    image bagua2_1 = "images/effect/八卦阵2.png"
    image bagua2_2 = "images/effect/八卦阵2.png"
    image bagua2_3 = "images/effect/八卦阵2.png"
    image bagua2_4 = "images/effect/八卦阵2.png"
    show bagua2_1:
        xcenter 0.2
        ycenter 0.2
        zoom 1.0
        alpha 0.0
        rotate 180
        parallel:
            ease 0.3 alpha 0.4
            # ease 1 alpha 0.0
        parallel:
            ease 0.3 zoom 1.2
    with Pause(0.3)
    show bagua2_2:
        xcenter 0.8
        ycenter 0.2
        zoom 1.0
        alpha 0.0
        rotate 180
        parallel:
            ease 0.3 alpha 0.4
            # ease 1 alpha 0.0
        parallel:
            ease 0.3 zoom 1.2
    with Pause(0.3)
    show bagua2_3:
        xcenter 0.2
        ycenter 0.8
        zoom 1.0
        alpha 0.0
        rotate 180
        parallel:
            ease 0.3 alpha 0.4
            # ease 1 alpha 0.0
        parallel:
            ease 0.3 zoom 1.2
    with Pause(0.3)
    show bagua2_4:
        xcenter 0.8
        ycenter 0.8
        zoom 1.0
        alpha 0.0
        rotate 180
        parallel:
            ease 0.3 alpha 0.4
            # ease 1 alpha 0.0
        parallel:
            ease 0.3 zoom 1.2
    show nsc fennu with dissolve
    with Pause(1.0)
    image shitou = "images/obj/石头.png"
    show shitou at appear_tb(x_c=0.5, y_c=0.5, y_o=-10, z=1.0, t=0.2)
    nrr """
    {clear}

        三十六块一人高的方石自储物囊中飞出，围成三重圆，由内至外分别八、十二、十六块，将南司楚困于中心。

　　那些都只是普通石头，是以虽然体积大却不曾被人注意。

　　之后她手起印落，在其中十二块方石上钉入石符法器。

她动作极快，看起来似是练习过很多次，不过花了半盏茶功夫就布置好一切。
    """

    window hide
    scene shulin b with tran_lf
    with Pause(0.5)
    show nsc fennu with dissolve
    nrr """
    {clear}

        就在下一刻，南司楚已挣脱束缚，怒急之下，扬手就劈向那方石，不料剑却被弹了回来。
    """
    play sound "sound/audio/刀剑/se101.wav"
    show nsc fennu:
        linear 0.3 zoom 1.5
    play sound "sound/audio/刀剑/刀剑碰撞1.wav"
    with Shake_screen((0, 0, 0, 0), 0.1, dist=3)
    show nsc fennu:
        linear 0.3 zoom 1.0
    nsc "什么？"
    "他大惊失色，沉住气试图自方石间隙里冲出去，之后就发现被无形的屏障挡住，用上全部功力都无法往前一步，面上的慌乱又重了一分，"
    nsc "这是什么？"
    window hide
    show effect 3-1-1:
        xcenter 0.5
        yalign 1.0
        zoom 1.2
        alpha 0
        easein 1 alpha 0.6
        easeout 1 alpha 0.3
        repeat
    with Pause(1.0)
    scene shulin b with dissolve
    "钟明烛席地而坐，不紧不慢地在四周撒上炼出的灵沙，在上面画出几个图案，一条细细的银线自图案下延伸出去，没入最近的方石之中。"
    stop music fadeout 1.5
    "之后她才轻轻吐了一口气，好似终于安下心来，从怀里掏出正在冒着青烟的金属器皿丢于身后，刚刚她便是用那个引走了雷击，不过低阶的果真不顶用，一次就报废了。"
    "好在如今已大功告成，她自方石间隙中看向脸色铁青的南司楚，眼中闪烁出某种恶意的神采，慢悠悠道："
    show zmz at pos_zmz with dissolve
    zmz "此乃画地为牢，南师兄，你可喜欢？对了，来的路上我稍微做了点手脚，这条路，并不是南师兄你以为的那条。"
    "这是最低阶的防御之阵演变而来，钟明烛偶然发觉可以通过改变注入灵力的次序来改变防御方位，尝试了很多次才成功布出此阵，来的路上她顺手稍稍改变树石方位，呈迷障之局，引南司楚渐渐偏离了最初的方向。"
    "她做的并不高明，但是南司楚一心要追上她，是以看的不是很仔细，轻易就被糊弄了。"
    hide zmz with dissolve
    show nsc fennu with dissolve
    show nsc fennu:
        linear 0.3 zoom 1.5
    play sound "sound/audio/刀剑/刀剑碰撞1.wav"
    with Shake_screen((0, 0, 0, 0), 0.1, dist=3)
    show nsc fennu:
        linear 0.3 zoom 1.0
    with Pause(1.0)
    show nsc fennu:
        linear 0.3 zoom 1.5
    play sound "sound/audio/刀剑/刀剑碰撞1.wav"
    with Shake_screen((0, 0, 0, 0), 0.1, dist=3)
    show nsc fennu:
        linear 0.3 zoom 1.0
    with Pause(1.0)
    "过了一会儿，南司楚又重重刺了方石几剑，见那石头纹丝不动，不可置信道："
    nsc "不可能，低阶阵法和符箓维持不了那么久。"
    play music "sound/bgm/骆集益 - 玉水明沙.mp3"
    hide nsc with dissolve
    show zmz wugu at pos_zmz with dissolve
    zmz "唉呀，师兄你没看到这个吗？"
    "钟明烛指了指那银沙，"
    zmz "如今困住你的不止是符箓，还有我的灵力。"
    "她一口一个师兄叫的亲热，可在如此境况下，无疑是火上浇油，嘲弄之意愈发浓厚，三年多来她一直处处小心谨慎，如今成功困住南司楚，自是不会放过落井下石的机会。\n看着对方被她三言两语激得暴跳如雷，心情便愈发舒畅起来。"
    "石阵和符箓法器只是辅助，她的修为虽然不如南司楚，可是在阵法加成下，就能死死困住他，那灵沙是绝佳的载物，她炼出来就是为了方便渡灵力。"
    hide zmz with dissolve
    with Pause(0.5)
    show nsc fennu with dissolve
    "南司楚愣了愣，突然笑起来："
    show nsc with dissolve
    nsc "若想困住我，你须得寸步不离，但这可是试炼啊，你能困我到几时？不如识相些放弃吧！"
    "他笃定钟明烛不会为了困住他而放弃试炼成果，态度又嚣张起来。"
    hide nsc with dissolve
    show zmz shengqi at pos_zmz with dissolve
    zmz "维持这阵法的确会消耗灵力，虽然不多，但也不是长久之计。"
    "钟明烛故作烦恼地皱了皱眉，而后忽地扬起可谓温文尔雅的微笑，柔声道："
    zmz limaoweixiao "就有劳南师兄在这陪我两天吧。"
    hide zmz with dissolve
    show nsc fennu with dissolve
    nsc "什、你不是夸口要拿第一吗？"
    hide nsc with dissolve
    show zmz limaoweixiao at pos_zmz with dissolve
    zmz "我乱说的，南师兄莫当真。"
    "钟明烛依旧笑得文雅，好似只是在与朋友谈天说地一般，"
    zmz "我区区一介凡人弟子，能当个内门弟子去扫地，便是三生有幸了。"
    "南司楚终于懂了，钟明烛这是耗上自己的前途也要叫他无法如愿以偿。"
    hide zmz with dissolve
    show nsc fennu with dissolve
    nsc "你、你为什么……我没有想害你性命，那时没多高……"
    "他语无伦次道，神情再也不似往日那般高傲，看起来就像只斗败的公鸡。"
    hide nsc with dissolve
    show zmz limaoweixiao at pos_zmz with dissolve
    zmz "我也没想害南师兄性命，而且连伤你都舍不得呢。"
    "钟明烛仍是笑。"
    hide zmz with dissolve
    "森林外设有结界，试炼过程中外界无法知晓里面的情况，为的就是杜绝徇私舞弊，当然，若真的遇到麻烦，可以用身份玉牒向外求助，这也意味着放弃此次试炼。"
    "无论哪一种南司楚都不敢，因为是他攻击钟明烛在先，所以他只能任凭摆布。"
    show nsc fennu with dissolve
    show nsc fennu at wobbly(x=3, y=2, t=0.1)
    nsc "疯子……"
    "他喃喃道，身子不由自主颤抖起来。"

    stop music
    scene black with fade
    with Pause(2.0)
    scene pubu with fade
    show cl dazuo biyan at pos_cl_dazuo with dissolve
    with Pause(2.0)
    nrr """
    {clear}

        天台峰三迭瀑下，长离依旧一身素白，独坐于青石台上。

　　飞溅的银珠四下散落，些许附上她的裙摆，留下几点转瞬即逝的水痕，而那裙摆，始终纤尘不染。

　　水声如钟，而细细聆听，却能自其中听到许多其他声音，枝叶于徐徐微风中窸窣起舞，鱼儿甩尾搅乱水波，草木丛生中时隐时现的虫声鸟鸣，清清浅浅，好似悠扬的歌谣。

　　可长离耳中却什么都没有，既没有瀑布，也没有隐匿于其后的细微声响，眸中亦什么都没有，好似她并非坐在林中瀑布之下，而是置身于虚无之中。

　　她缓缓举起手中的竹枝，不知过了多久，却又落回原处，静若止水的黑眸中似起了一丝涟漪。
    """
    window hide
    with Pause(1.0)
    show cl dazuo with dissolve
    with Pause(2.0)
    nrr """
    {clear}

        五年，她已在此山涧悟了五年，却未能有毫厘进展，好像被无形之墙阻住，死死拦在某条界限之内，用尽办法都无法往前多走一步，她应当是遇到瓶颈了。
    """
    wh "吾徒长离，可有感悟？"
    "苍老的声音传入她灵海，朴实平缓，却隐隐约约透出肃杀之意，正是她的师父，那个荡尽邪魔、无往不胜的第一剑修吴回。{p}他正以千里传音与长离交谈。"
    cl "尚无。弟子已遇瓶颈。"
    "长离据实以告。"
    "吴回沉默了很久，似乎在思考什么，良久，终于做出决定，道："
    wh "今日各峰招收弟子，你也去选一个吧。"
    cl "弟子尚未出师。"
    wh "可还记得为师曾告诉你，先入世，后出世，你去择一弟子，且当是入世磨剑罢。"
    "长离记得在她伤愈出关后，吴回就建议她出世历练，所以才会有五年前逐浪城一行，可那次出行于她而言，除却途中顺手救了一个人外，便和去宗门内其他峰没什么不同，无感无悟，加上近来宗门无事，她便不复出山。"
    "这时她突然想到了当年为她所救的少女，几年前见过一面，对方还与她论了几句剑。{p}那是她第一次与师父之外的人谈论剑道。"
    "这便是入世？"
    "她仍是不太明白师父的用意，不过既然被如此吩咐，照做便是，一直以来都是这样。"

    jump story_8_1
