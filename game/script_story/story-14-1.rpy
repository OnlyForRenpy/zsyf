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

label story_14_1:

    image cg14-1-1 = "images/cg/CG-14-1-1.jpg"
    image cg_feidan = "images/cg/飞弹2.jpg"

    stop music
    window hide
    scene black with fade
    with Pause(1.0)
    scene tiantaifeng xiaowu2 with fade
    play sound "sound/audio/环境/自然环境 （环绕）（30s版）.mp3"

    nrr """
    {clear}

        钟明烛回到重明居时，长离在插花。
    """

    show cg14-1-1 with dissolve
    with Pause(2.0)

    nrr """
    {clear}

        她手执一支含苞待放的山茶，宽袖滑落至肘间，露出一截白玉似的小臂，凝视着案上的白玉瓶迟迟没有动作。

        瓶中已经有几支茶花，有完全绽放的，也有仅是花骨朵的，疏落有致，娉婷婀娜。

　　钟明烛叫了一声“师父”，长离没有理她，一眼不眨，全部注意都放在寻找那支花的落处上，过了好一会儿终于寻好位置，缓缓地将那支花插入。

　　恰到好处，整瓶花都因此鲜活起来。

{clear}

　　师父是不是太过不务正业了一点，钟明烛突然开始思考这个问题。

弟子演武会，师伯们都密切关注着弟子们的情况，只有她师父，在插花，全然置身事外那般淡定。
    """

    scene tiantaifeng xiaowu2 with dissolve
    show zmz b tanqi at pos_zmz with dissolve
    zmz "师父，你都不关心我胜负如何，有没有受伤吗？"
    "她老大不满意地问，还献宝一样将被烧焦的下摆指给长离看。"
    show zmz b dark with dissolve
    cl "我知道。"
    show zmz b
    image gif_chuansong_lan = SquenceAnimator("images/effect/传送-蓝", interval=0.12, loop=False)
    play sound "sound/audio/施法/护盾出现.wav" volume 2.0
    show gif_chuansong_lan:
        xcenter 0.5
        ycenter 0.75
        zoom 3.5
    with Pause(0.8)
    hide gif_chuansong_lan with dissolve
    zmz b tanqi "哦……"
    "钟明烛讨了个没趣，拍了拍纤尘不染的衣衫，摸了摸鼻子开始帮长离挑拣茶花，她本来还想借此机会向长离讨些奖励。{p}——徒弟那么有出息，她当师父的也面上有光啊。"
    "结果长离似乎连半点兴趣都无，连带她也没了兴致。"
    show zmz b shengqi with dissolve
    "师父你为何如此败兴！"
    show zmz b shengqi at wobbly(x=3, y=2, t=0.1)
    "看着手中娇艳欲滴的花朵，她冷哼一声，将花瓣都揪了下来。"
    show zmz b shengqi
    with Pause(1.0)

    scene yunfushan lianwuchang with Fade(1.0, 1.0, 1.0)
    play music "sound/bgm/曾志豪 - 剑执清平.mp3"
    nrr """
    {clear}

        第二场比斗，对手依旧是金丹期的，是不语峰的一个师姐。

　　这场比试仅持续了半刻钟，钟明烛一改上一场的作风，一开始就一把符招呼过去。
    """
    play sound "sound/audio/爆炸坍塌.wav" volume 0.5
    image feidan = "images/cg/法术-技能-飞弹.png"
    show feidan:
        zoom 1.6
    with close
    with Shake_screen((0, 0, 0, 0), 5, dist=15)
    nrr """
    {clear}

        筑基级的，金丹级的，一股脑砸过去，又一次让观看的众人瞠目结舌了一回。

　　甚至有人露出痛心疾首的表情。

　　有你这样浪费的吗？

　　结果就是那位师姐连反击都没来得及就被轰到了场外，而钟明烛也用掉了手里绝大部分咒符，只剩下了三张。
    """

    scene yunfushan lianwuchang with fade
    nrr """
    {clear}

        接下来就是第三场，对她而言的最后一场。
    """
    show chengl with dissolve
    with Pause(1.0)
    nrr """
    {clear}

        对手是符咒一脉的程凌，金丹中期，是玉珑峰上除风海楼外，符咒造诣最高的那个，尤其擅防守，前两场就是占据场中位置，任凭对手怎么攻击都纹丝不动，一直撑到结束。

因为前两场表现太过惊人，这场吸引了很多人前来观看，甚至来了好几个师伯，想看看钟明烛这次又会出什么主意。

　　丁灵云也在，她已经连赢了三场，三次抽到的对手都是筑基期的，不费吹灰之力就拿到了下山资格，把钟明烛恨得牙痒痒。

　　一定是作弊了吧！把我的果脯还回来啊混蛋！
    """
    chengl "请多指教。"

    play sound "sound/audio/爆炸坍塌.wav" volume 0.5
    show feidan:
        zoom 1.6
    with close
    with Shake_screen((0, 0, 0, 0), 5, dist=15)
    nrr """
    {clear}

        两人行礼后比试正式开始，程凌起手就是五道攻击符，分别飞向钟明烛除了后方之外的五个方向，封住她的去路而后一齐爆裂。

　　他打的是先下手为强的主意，打算一开始就把钟明烛击倒或者逼到界外。
    """

    image zhumingtie = Fixed(
        Image("images/obj/朱明帖.png", xcenter=-1.0, ycenter=0.5, zoom=0.2),
        Image("images/obj/朱明帖.png", xcenter=0.0, ycenter=1.0, zoom=0.2),
        Image("images/obj/朱明帖.png", xcenter=1.0, ycenter=1.0, zoom=0.2),
        Image("images/obj/朱明帖.png", xcenter=2.0, ycenter=0.5, zoom=0.2),
    )
    scene yunfushan lianwuchang with close
    show zmz b at pos_zmz with dissolve
    show zhumingtie:
        xcenter 0.5
        ycenter 0.6
        zoom 0.2
    with dissolve
    "火光电石间，钟明烛一拂手，出现一圈金属片将她团团围住，巴掌大小，半指厚，由赤金打造，总计三十二枚，分三层，表面刻有奇特的纹路，星点辉光在纹路中缓缓流淌。"

    show zmz b dark
    dly "是那个……"
    "丁灵云一眼看出那赤金板上的辉光与那日画卷上的有些相似，"
    dly "竟然是用来炼法器了。"
    "而且还全部是赤金，即便她出身世家，都觉得钟明烛这实在是太奢侈了。"
    "筑基期的法器尚不稳定，而且容易损坏，所以大部分人到金丹期才会用贵重材料去升级法器或者重新炼造。"
    "筑基中期的钟明烛，出手就是全部由赤金打造的法器，丁灵云一眼扫过去就看到不少于二十个人正眼含羡慕以及嫉妒，甚至还有不甘和仇视，她觉得结束后需要提醒钟明烛低调一些。"
    show zmz b
    "五道灵符的威压叠加在一起，连场外的人都能感受到灵气爆发带来的巨大冲击感，钟明烛却只是退了十几丈，毫发无伤。"
    "此为折冲之阵，与当年困住南司楚的画地为牢同根而生，不过此时由法器施展起来更为方便。"
    "这些赤金板，每一块上都刻有九宫阵，注入不同的灵力可演变出成千上万种变化，受限于施术者的修为，结成的阵法威力稍弱，但用在这种场合已经足够。"

    scene black with fade
    image gif_kapai = SquenceAnimator("images/effect/卡牌", interval=0.15, loop=False)
    show gif_kapai:
        xcenter 0.5
        ycenter 0.5
        zoom 1.5
    with Pause(2.0)
    nrr """
    {clear}

        抵御住第一下攻击后，钟明烛立即转守为攻，三十二枚赤金板分向八个方向，以程凌为中心钉入石板中。
    """
    scene yunfushan lianwuchang with fade
    show chengl with dissolve
    image gif_hudun = SquenceAnimator("images/effect/护盾", interval=0.15)
    show gif_hudun:
        xcenter 0.5
        ycenter 0.6
        alpha 0.75
        zoom 1.0
    "程凌见状招出自己的法器，却是一块盾，一分为四将他周身护的严严实实。"
    "这是他的本命法器，名封岳，可承受元婴以下的任何攻击，之前一击不成他就有心以守为攻，料想筑基期弟子的攻击就算有阵法加成也破不了他这层防御，若寻不到机会，拖满两个时辰便可。"
    show chengl fennu with dissolve
    "他正欲往场地正中移动，突然发现周围的景致变了。"
    scene xueshanjiaoxia with tran_fog
    nrr """
    {clear}

        变成了葱郁的山林，一条小径出现在脚下，往前延伸，通往一座高耸的宫殿，这是玉珑峰。

　　他扫视四周，入目的景致与玉珑峰下的森林分毫不差，他好像被人移到了那里，而脚下的道路正诱他往前，去探一探发生了什么。
    """
    show chengl fennu with dissolve
    chengl "怎么可能中招。"
    "程凌眸中掠过一道凛光，他又捏出一张灵符，拍到地上，念道："
    show effect 3-1-1:
        xcenter 0.5
        yalign 1.0
        zoom 1.2
        alpha 0
        easein 0.6 alpha 0.6
        easeout 0.6 alpha 0
    with Shake_screen((0, 0, 0, 0), 2, dist=8)
    chengl "破！"

    scene yunfushan lianwuchang with tran_water
    nrr """
    {clear}

        而后便见灵气水波般扩开，不多时便听得几声轻响，眼前又变回演武场，而钟明烛正在将被击飞的赤金板收回来，面上似有恼意。

　　雕虫小技，他不以为然地心想，然后一个闪身便移动到场地正中，封岳钉入地中，结成牢不可破的屏障。
    """

    show chengl with dissolve
    show huzhao:
        xcenter 0.5
        yalign 1.0
        zoom 3.5
        alpha 1.0
        ease 1 alpha 0
        ease 1 alpha 1.0
        repeat
    with Pause(2.0)
    play sound "sound/audio/刀剑/se101.wav"
    scene cg_feidan with tran_lf
    with Pause(0.5)
    scene yunfushan lianwuchang with tran_lf
    show chengl with dissolve
    show huzhao:
        xcenter 0.5
        yalign 1.0
        zoom 3.5
        alpha 1.0
        ease 1 alpha 0
        ease 1 alpha 1.0
        repeat
    play sound "sound/audio/爆炸坍塌.wav" volume 0.5
    with Shake_screen((0, 0, 0, 0), 2, dist=10)
    nrr """
    {clear}

        两张金丹期灵符飞来，在盾上炸裂，巨大的冲击在场地上回荡，他却丝毫没有受影响，甚至连衣摆都没有晃。

　　就这样坚持到结束就好，他稍稍松了一口气，露出一丝笑容。
    """

    scene black with tran_lf
    scene yunfushan lianwuchang with tran_lf
    show zmz b shengqi at pos_zmz with dissolve
    with Pause(1.0)

    show zmz b shengqi:
        linear 0.3 zoom 0.6
    play sound "sound/audio/刀剑/刀剑碰撞1.wav"
    with Shake_screen((0, 0, 0, 0), 0.1, dist=3)
    show zmz b shengqi:
        linear 0.3 zoom 0.4
    with Pause(1.0)
    show zmz b shengqi:
        linear 0.3 zoom 0.6
    play sound "sound/audio/刀剑/刀剑碰撞1.wav"
    with Shake_screen((0, 0, 0, 0), 0.1, dist=3)
    show zmz b shengqi:
        linear 0.3 zoom 0.4
    with Pause(1.0)

    nrr """
    {clear}

        之后，钟明烛围着他试图寻出破绽，以赤金板接连砸上去，同时不断构筑幻象诱他出来，可诸般努力都不见丝毫成果，最后气急之下拔剑砍过来，却被震得剑险些脱手，可就算这样她都没有放弃，不断想新花招试图破除那层障碍。

　　没用的，程凌满意地想。
    """

    hide zmz with dissolve
    nrr """
    {clear}

        就在这时候，他感觉到结界消除了，外界的声音传入耳中，比试结束了，这时还不足两个时辰。

　　难道是钟明烛自己出界了？他略迟疑地收了法器，然后听到了结果：\n\n\n

　　“天台峰，钟明烛胜。”
    """

    stop music
    scene yunfushan lianwuchang with fade
    show chengl shoushang with dissolve
    chengl "什、什么？"
    "程凌惊呼起来，只是片刻后就明白了原委。"
    hide chengl with dissolve
    show zmz b at pos_zmz with dissolve
    show zhumingtie:
        xcenter 0.5
        ycenter 0.6
        zoom 0.2
    with dissolve
    "钟明烛盘腿坐在飞剑上，张开手，空中又浮现出三十二块赤金板，而那个位置——程凌看清了——{p}——正是场地正中。"
    zmz "师兄应该多动一下才行。"
    hide zhumingtie with dissolve
    "钟明烛收回六十四块法器，留下这句话就绝尘而去。"
    play sound "sound/audio/移动呼声/布料呼声.mp3"
    show zmz b at hide_rl(x=-100)
    nrr """
    {clear}

        她在布下两重幻阵，一重破绽较多，是程凌察觉到的那些，另一重却是幻化为演武场的模样，只不过中心偏移了十几丈，而那一重才是真正的幻阵，钟明烛耗费了大量精力维持，即便是金丹期修为，不仔细分辨也难以窥破真相，程凌被她百般干扰，又早早就笃定自己能胜，所以被她糊弄过去了。

　　若程凌主动进攻，钟明烛需要分神防守，就无力维持那重幻阵，这样的话这场比试的结果还不得而知。

　　其实钟明烛听闻程凌前两场比试的作派后抱着姑且一试的心态想了这个办法，打算若是行不通，就把那六十四块法器全部用来防身，能对拖延一刻就是一刻，却没想到会那么顺利。
    """

    scene tiankong b with fade
    nrr """
    {clear}

    “那么喜欢缩龟壳里就别参加什么演武会啊……”

    她不屑一顾地念叨，原本是想当面说给程凌听的，不过因为精力不济的原故作罢了，结束后立刻就走而不是留下来找丁灵云耀武扬威一番也是因为这个。

　　为了维持那法阵同时做戏扰乱对方注意力，她几乎耗尽了精力，只剩下御剑飞回去的力气了。

　　感觉快晕过去了，她揉了揉脸，觉得连笑的力气都没有了。

　　不过总算是结束了呢，她心满意足地想。

    {clear}

    很快，钟明烛就发现她心满意足地太早了。
    """
    play music "sound/bgm/芳賀敬太 - 暗雲を払え.mp3"
    show zmz b shengqi at pos_zmz with dissolve
    zmz "什么事？"
    "她还是坐在飞剑上，仰头打量着拦住去路的几道身影，之后又觉得兴味阑珊只想回去休息，便垂下脑袋道，"
    zmz "算了，有什么事从长计议吧，我先告辞。"
    hide zmz with dissolve
    "说完她想绕道，然而还是被挡住去路。"
    show ptdz:
        xalign 0.0
        yalign 1.0
        easein 0.3 xalign 0.05
    show jty:
        xalign 0.2
        yalign 1.0
        easein 0.5 xalign 0.3
    show ptdz3:
        xalign 0.4
        yalign 1.0
        easein 0.5 xalign 0.55
    show ptdz4:
        xalign 0.8
        yalign 1.0
        easein 0.5 xalign 0.8
    with Pause(1.0)
    "一共四个人，三个金丹期，一个筑基期，都是不认识的。"
    "这才离开主峰地界呢……{p}她揉了揉鼻子，往下瞅了一眼，只能看到深浅不一的绿色。"
    "为首那人拱了拱手，笑道:"
    jty "久闻钟师妹得长离师叔真传，英姿……"
    zmz "少废话。"
    "钟明烛一脸不耐烦地打断他，"
    zmz "对了，名字也别报了，我没兴趣。"
    show jty yansu with dissolve
    "被她的态度激怒，那人脸色沉下来，语气也凌厉起来："
    jty "师妹连胜三场，实力不凡，我等欲与师妹切磋。"
    scene tiankong b with dissolve
    show zmz b xiee at pos_zmz with dissolve
    zmz "呵……"
    "钟明烛冷笑，"
    zmz "切磋，说得好听，眼红就直说，不会因此更看不起你们。"
    "仅仅是筑基中期修为，却有不少金丹期灵符，赤金打造的法器，在比斗大会中连胜三场大出风头。必然有弟子会将她胜出的原因归结于法宝道具，然后生出怨气，他们自然是不敢去找长离的麻烦，于是就找上了钟明烛。"
    "因为她接连胜过三位金丹期前辈，所以想与她切磋，多么冠冕堂皇的理由。反正修正之人体格强，受点小伤也不碍事，就算去师长那告状最多也就思过几个月。"
    "能出一口气，思过几个月算得了什么呢？"
    hide zmz with dissolve
    show jty yansu with dissolve
    "被她拆穿，那人有些恼羞成怒，刷地抽出剑，道："
    jty "同门切磋只是稀松平常的事，师妹休得以小人之心相度。"
    hide jty with dissolve
    show zmz b xiee at pos_zmz with dissolve
    zmz "好啊。"
    "钟明烛眸光一沉，吞下几颗救急的灵药，缓缓站起，拍了拍外衫，"
    zmz "请……"
    show zmz b xiee:
        linear 0.3 zoom 0.6 alpha 0.0
    with Pause(0.6)

    play sound "sound/audio/刀剑/se101.wav"
    image zongqie = "images/cg/纵切.png"
    show zongqie:
        xalign 0.0
        yalign 1.0
        zoom 1.6
    nrr """
    {clear}

        然后在“请”字出口的一瞬就冲了过去，在那人毫无防备时一剑劈下，同时将脚下飞剑踢出。
    """
    hide zongqie with tran_uf
    play sound "sound/audio/刀剑/se104.wav"
    show jty:
        xcenter 0.5
        yalign 1.0
        zoom 1.5
        alpha 0.3
        easein 0.3 zoom 1.0 alpha 1.0
    with Pause(1.0)
    "又是出乎意料的做法，不过那人好歹修为高一层，将两招都防住。"
    show jty yansu dark
    zmz "列阵！"
    "感觉身子已有下坠之势，钟明烛大喊一声，见对方分神去寻她的法器，扬手就把剑往他脸上摔去。"
    play sound "sound/audio/击打.wav"
    show jty at wobbly(x=5, y=3, t=0.05)
    with Pause(0.15)
    hide jty
    show jty
    "她想这么做很久了，下手格外重，一下把对方鼻子砸出了血。"
    hide jty with dissolve

    scene black with fade
    play sound "sound/audio/环境/寒风2.wav" loop
    show fastwork_ud:
        alpha 0.5
    nrr """
    {clear}

        一切发生得太快，旁边三人竟没能插得上手，待他们反应过来，钟明烛已往下坠去。

　　“哈哈哈…”听着在耳畔凄厉咆哮的风，钟明烛狂笑起来。

而后，灵符在上方爆裂，她跌落的那一瞬，将最后那道金丹级灵符抛了出去。
    """
    play sound "sound/audio/爆炸坍塌.wav" volume 0.5
    with Shake_screen((0, 0, 0, 0), 3, dist=15)
    nrr """
    {clear}

就算没能伤得了他们，把他们吓个灰头土脸也好。

　　灵药的效力已经消失了，她费力地勾了勾手指，试图把飞剑召回来，然而未感觉到飞剑的回应，耳畔的风声忽然停止了。
    """
    stop sound
    stop music
    hide fastwork_ud with dissolve
    nrr """
    {clear}

——被接住了。
    """

    scene tiankong b with tran_close
    nrr """
    {clear}

急速远去的天幕定格，然后再度缓缓拉近。

　　她抬起头，看到了长离。
    """

    scene cg12-2-1 with close
    nrr """
    {clear}

        所谓流年不利大抵就是如此吧。

　　四人挡的挡，躲的躲，手忙脚乱撑过钟明烛那道灵符，还没来得及说一个字——为首那人的鼻血还在滴滴答答落下来——就被出现在前方的白衣慑得脑子乱作一团。

　　长离看着他们，漆黑的眸子里分明没有任何情绪，却叫他们如坠冰窟似的惶恐。

　　他们忍不住后悔去挡那道灵符了，被炸晕炸伤也好过现在，与面无表情的长离仙子相对而立。

　　虽然长离仙子从来都是面无表情的，可此刻不知为何看起来格外可怕。

{clear}

　　钟明烛抓着长离的手，疲倦感在对方渡来的灵力中渐渐消散后，她抬起下巴，挑衅地嗤笑了几声，颇有几分小人得志的味道。

　　追究起来其实也是钟明烛自己种下的因。

　　她因为长离对她的比试毫不在意的态度而气恼，然后借着第二场比试把怨气全发泄出来了，她虽是胜了，但靠师父帮她炼的一堆灵符取胜委实有些难以服众。那位输了的师姐难免会委屈，她一难过，在意她的人自然是心中不平。

　　前来滋事的人中，为首那个正是那位师姐的道侣，他本想等钟明烛落败然后好生嘲弄一番替自己心上人出口气，没想到钟明烛又赢了，还亮出了纯赤金打造的法器。怒气与嫉恨交叠，于是脑子一热就喊上好友追了上来。

　　并没有想下狠手，只是想挫挫她的锐气，看到她踢了飞剑掉下去还慌了一下，结果转头就看到了长离。

{clear}

　　谁都知道天台峰长离仙子对门中事务毫无兴趣，今年祭天大典也只在开始露了个面，亲传弟子三场比试皆是以弱敌强，她却一眼都没来瞧过。

四人见钟明烛比试已结束，料想长离也不会过来了，事后追究，顶多关一阵子禁闭，没想到她竟然在这个时候出现。

　　被抓了现形，师长亲自动手教训是常有的事。

　　有几个回过神后下意识想逃，然而飞剑还未掉头，就觉一股冷冽的剑气封住了去路，眼前明明什么都没有，可潜意识却有个声音在警告——再进一步就会万剑穿心。

{clear}

　　会死吗？

　　他们心中竟不约而同浮现出这个念头。
    """

    scene tiankong b with fade
    show yy with dissolve
    yy "你们在做什么？"
    "拯救了他们的是云逸，他察觉到那道灵符以及长离的气息，立即赶过来了。他修为超过长离许多，且性子温润，有他镇场，那股剑气终于不至于吓得人说不出话来了。"
    jty "弟子知错！恳请宗主责罚！"
    "一恢复行动能力，那几人马上拜下认错。"
    nrr """
    {clear}

长离天赋虽高，但受限于年龄，修为是几个峰主中最弱的，可她背后有三大长老袒护，那几个元婴末期只差一步就能踏入化神行列的师兄师姐见到她都要避让三分。

　　追截钟明烛是一时脑热，此时再嘴硬就真的是找死了，说谎也不可能，云逸最擅长追踪现形之术，手指一动就能以虚像再现此前发生的事，剩下的路只有一条。
    """
    show yy biyan with dissolve
    "云逸问明情况，沉吟片刻后念道："
    show yy with dissolve
    yy "尔等欺凌同门，触犯门规，这便留下名字，向钟师侄道歉，而后自行去刑堂领罚吧。小师妹你看如何？"
    "违规弟子的惩罚由刑堂定夺，他身为宗主亦不能擅作主张，叫他们留下名字则是提防有人逃脱，这决定遵循门规，合情合理，不存在任何偏袒。"
    "钟明烛不乐意了，当初她阻止风海楼去警告南司楚便是出于这种理由。"
    "交给门规处置哪有自己亲手报复来得愉快。"
    "可此时，云逸和长离都在，对方又很识抬举地服了软，她想找事反而显得理亏了。"
    hide yy with dissolve
    show zmz b wugu at pos_zmz with dissolve
    zmz "师父……"
    "她扯了扯长离的袖子——她恢复力气后对方就松开了手，"
    zmz "如果你没来，弟子就要被他们欺负去了。"
    "听到这话，那几人表情都有些微妙。"
    "事实上他们还什么都没来得及做，反而白白受了一道灵符，领头的还被砸断了鼻梁。{p}怎么看也不是她被欺负了。"
    hide zmz with dissolve
    show cl b at pos_cl with dissolve
    cl "嗯。"
    "长离就像没听到钟明烛的话一样，轻轻应了一声。"
    hide cl with dissolve
    show zmz b shengqi at pos_zmz with dissolve
    "钟明烛冷哼了一声，抓着袖子的手愈发用力，恨不得把那袖子扯下来。"
    "——我就知道！这铁石心肠的女人！根本不懂什么叫师徒情深！"
    show zmz b tanqi dark with dissolve
    "就在她决定回去就把长离腰间那串玛瑙抠下来时，却听她再度开口，嗓音清冷如霜："
    cl "你学艺不精，才会被欺负了去。"
    zmz b shengqi "你？！"
    "钟明烛脸都青了，她张了张嘴，正想呛声，却听得一声剑吟。"
    play sound "sound/audio/刀剑/拔剑.wav"
    hide zmz with dissolve
    show cl yingzhan at pos_cl_yingzhan with dissolve
    "那是她的飞剑，不知何时落在了长离手中，她握着剑，手臂垂在身侧，看起来仅仅是握着剑而已，没有用半分力气。"
    play sound "sound/audio/刀剑/破风剑光.wav"
    "隐约中似有一道清光扬起，一瞬间，她感受到了剑意的寒气，但去细看时，却什么都没有，长离的手还是在原来的地方，没有剑气，没有灵力波动，看起来什么都没发生。"
    hide cl with dissolve
    nrr """
    {clear}

    紧接着，张皇失措的惊叫声响起，她往那边看去，不觉“哇”地叹了一声。

　　那几人脚下的飞剑齐刷刷一分为二，从剑柄到剑尖被对半剖开，可是没有伤及上面的飞行阵术，还稳稳当当停在空中，只是因为这徒然变故，上面几人歪歪扭扭的站姿显得很滑稽。

　　云逸呆住了。
    """

    show cl b at pos_cl with dissolve
    cl "你可看清？"
    "长离瞥了钟明烛一眼，不动声色地问道。"
    hide cl with dissolve
    show zmz b chijing at pos_zmz with dissolve
    with Pause(1.0)
    zmz b miyanxiao "没、不，有有有！"
    "钟明烛笑得那个叫猖狂。"
    "看起来愈发小人得志了。"



    jump story_15_1
