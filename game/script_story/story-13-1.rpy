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

label story_13_1:

    stop music
    window hide
    scene black with fade
    with Pause(1.0)
    scene yunfushan lianwuchang with fade
    play music "sound/bgm/剑网3 - 情缘·一见千年.mp3"

    image gif_jianying = SquenceAnimator("images/effect/剑影", interval=0.3)
    with Pause(1.0)
    play sound "sound/audio/施法/se414.wav" loop
    show gif_jianying:
        xcenter 0.5
        yalign 1.0
        zoom 3.5
        alpha 0.0
        linear 1.0 alpha 1.0

    nrr """
    {clear}

        祭天大典，百年一次，是天一宗各峰切磋论道的盛典。

　　先是拜祭天一道人，而后宗主授道，继而是四灵诛邪阵的演示，云逸分二十八虚影，据四方之位，长剑齐舞，万般变化俱在此阵中。

　　当年四灵诛邪阵被千面偃所破，百年来云逸一直致力于完善此阵，演示亦是希望门人观之能有所感悟。

    {clear}

　　上一次大典时，钟明烛尚是外门弟子，没有资格上天一峰，而这次，她凭借长离仙子亲传这层身份，占据了个好席位。

每一脉师长都会择一弟子侍于左右，有点类似凡间的书僮，天台峰只她一人，便当仁不让担起了给长离端茶倒水的工作。

相比起来，长离仙子竟会出席这一点更叫人吃惊，素衣清颜，往那一坐，就吸引了大半目光。

　　她本没打算来，不过钟明烛说想来观摩这套阵法，便依了她。

{clear}

　　四灵诛邪阵是天一道人观星辰演变有感而作，蕴含万物苏生之理，钟明烛看了一会儿，却觉得那阵法虽精巧，却非攻亦非守，看起来单纯只是依据星宿变化踩位而已。
    """

    hide gif_jianying with dissolve
    stop sound
    show zmz b at pos_zmz with dissolve
    zmz "师父，你能破阵吗？"
    "她低声问长离。"
    hide zmz with dissolve
    show cl b kunhuo at pos_cl with dissolve
    "长离闻言看向那套阵法，沉吟半晌，答道："
    show cl b with dissolve
    cl "尚无破解之法。"
    hide cl with dissolve
    show zmz b sikao at pos_zmz_sikao with dissolve
    zmz "何故？"
    "钟明烛不解，她觉得上次长离用来和龙田鲤对峙的剑阵威慑力都要强一些。"
    hide zmz with dissolve
    show fhl with dissolve
    fhl "钟师妹稍安勿躁。"
    "出声的却是风海楼，云逸在演示阵法，他闲来无事就来找钟明烛打算与她探讨一番，刚过来就听到她的提问，这次换他露出得意的表情了，向长离行过礼后就在钟明烛边上坐下，示意她继续看。"
    hide fhl
    image baota = "images/obj/宝塔.png"
    show baota:
        xcenter 0.5
        ycenter 0.5
        zoom 1.2
        xoffset 200
        yoffset -100
        alpha 0.0
        easein 1.5 xoffset 0 yoffset 0 alpha 1.0
    with Pause(0.6)
    nrr """
    {clear}

        没过多久，忽然有一物飞入那虚影所化的阵法中，钟明烛眼尖地看出那是一尊塔形法器，由赤金打造。

　　塔可镇万物，擅守，若是以赤金炼就，便是防御最强的法器，下一瞬，便见阵中爆发出摄人的威压，只一瞬就将那塔形法器碾得粉碎。
    """
    play sound "sound/audio/碎裂.wav"
    hide baota with tran_crystal
    with Pause(2.0)
    nrr """
    {clear}

        在场门人无不动容。

　　之后，那阵又恢复了此前的平静。
    """
    show zmz b chijing at pos_zmz with dissolve
    with Pause(1.0)
    "钟明烛似乎也看呆了，眸中浮现出异样的神采，过了很久才悠悠吐了一口气，道："
    zmz "我懂了，是……天道吧。"
    hide zmz with dissolve
    "上古有天演者，观星象推演天下之势，而星象即天道之相，那四灵诛邪阵排的是井然有序的天象，若有外来者，即是扰乱秩序，为天道不容。"
    show fhl with dissolve
    fhl "哈哈，我就知道钟师妹于此道有天赋。"
    "风海楼笑了起来，"
    fhl "此阵威力不可估量，屡次助我天一宗驱除强敌。"
    hide fhl with dissolve
    show zmz b ganga at pos_zmz with dissolve
    zmz "哦？我倒是听说上次那个千什么的破了阵大摇大摆到了主峰后山。"
    "——多亏我师父，不然这天一宗怕是已经完蛋了。"
    "后半句她没说出来，毕竟是大典上，她不想再遇到一个龙田鲤。"
    hide zmz with dissolve
    show fhl nanguo with dissolve
    "被她这么一呛，风海楼面上露出几分黯然，当年他尚未结丹，没能亲眼见一见千面偃，只知道那一战危急之际，师父险些自爆元婴。"
    "不过他很快又再度打起精神，带着几分强势的口气说："
    fhl fennu "当时是准备仓促，列阵弟子中有不少还不熟悉步法，才会被那厮破了阵。"
    hide fhl with dissolve
    show zmz b at pos_zmz with dissolve
    zmz "就算是未准备周全，也不至于被初见之人破了去吧？"
    "钟明烛玩味地一挑眉，反驳道，"
    zmz "我倒觉得是一山还有一山高，师父你说是不是？"
    hide zmz with dissolve
    show cl b at pos_cl with dissolve
    "他们讨论时，长离始终一副游离事外的表情，这时被钟明烛的问题拉回注意，她看了那神色张扬的少女一眼，没有承认，也没有反对，而是回想起当年的事来。"
    show cl b kunhuo with dissolve
    with Pause(1.0)
    "千面偃离开后，师父和两位师叔找了她询问当时的情况，还做出了一些推测，她当时对什么都不在意，是以没有刻意去记，但终归是听到了的，思考了一会儿就回想起来。"
    show cl b with dissolve
    cl "木师叔说，千面偃可能是昆吾城陆离的传人。"
    "当时木丹心只是随口推测，并无实据，后来千面偃销声匿迹，便更加无从追查。"
    hide cl with dissolve
    show fhl with dissolve
    fhl "那就是了。"
    "风海楼一捶掌，声音精神了不少，"
    fhl "七百年前祭天大典之时，昆吾城二城主陆离率众多高手攻入云浮山，欲夺本门至宝苍梧剑，最后溃败于四灵诛邪阵下。"
    hide fhl with dissolve
    show zmz b at pos_zmz with dissolve
    zmz "陆离是谁？"
    hide zmz with dissolve
    "风海楼清了清嗓子，细细与她说起当年的事。"

    scene kunwucheng with fade
    nrr """
    {clear}

　　西南有山名{size=30} 昆吾 {/}，山下多赤金，两千年前魔尊陆临于昆吾山巅筑城，名即昆吾，毗邻妖之国，如今是邪道最猖獗的地带。

陆离即陆临之弟，七百年前就已是化神修为，当时孤鸿尊者远赴东海寻机缘，陆离伺机来犯，当时宗主还是木丹心，在宗门外十里布四灵诛邪阵，击溃了来犯的邪修，陆离本人亦在此战中受重伤，如今不知存活。

　　多半是死了吧，钟明烛心想。
    """

    scene yunfushan lianwuchang with fade
    zmz "为什么他们都想夺苍梧剑？那剑很厉害吗？"
    show fhl with dissolve
    fhl "苍梧剑是当世第一利器。"
    "风海楼很是自豪地说，"
    fhl "遭人觊觎很正常。"
    hide fhl with dissolve
    show zmz b sikao at pos_zmz_sikao with dissolve
    zmz "你见过吗？"
    "钟明烛记得那苍梧剑是一把木剑，一把木剑却是世上最锋利的武器，她觉得有些稀奇。"
    show zmz b sikao dark
    fhl "没有，此剑存于后山宝库，即便是三大长老亦不得擅动，若想动用此剑，需宗主以及各峰主首肯，非危难之际不现。"
    show zmz b at pos_zmz with dissolve
    zmz "希望能有缘一见。"
    "钟明烛惋惜地轻叹。"
    show zmz b miyanxiao with dissolve
    "比如说在有生之年宗门再造些祸事之类的，当然，这句话也被她藏在心里了。"

    scene yunfushan lianwuchang with fade
    nrr """
    {clear}

        接着又和风海楼探讨了些符箓以及风水之事，大典第一天就过去了。

　　次日便是众目所盼的弟子演武。

　　参与者总计一百五十二名，抽签决定对手，胜者进入下一轮，以此类推。

　　因为时间紧张，担心出现双方势均力敌只守不攻导致耗时数月才决出胜负的情况，云逸想了一个办法，在比斗开始后场地会渐渐缩小，两个时辰后收束至仅能容一人，先出边界者即落败。

　　最后第三轮的胜者以及败者中坚持时间较长的十一位可下山诛妖。

　　至于因为抽签导致的强者提前会面，弱者反而得到机会进入下一轮这样的情况，云逸轻描淡写道机运亦是实力的一环。

　　“一切皆是机缘。”

　　钟明烛总算是知道风海楼那开口闭口就是机缘的习惯是从哪来的了，她算了一下，需要赢三场，或者第三场坚持足够多的时间才能有下山机会。
    """
    show zmz b sikao at pos_zmz_sikao with dissolve
    zmz "希望是筑基期的好伙伴。"
    "她按住抽签用的法印，同时口中念念有词道，然后就看到了自己对手的名字。"
    window hide
    play sound "sound/audio/碰撞 树枝 打在混凝土上 02.mp3"
    # show zmz b at pos_zmz with dissolve
    show zmz b sikao at nod(t=0.15)
    with Pause(2.0)
    show zmz b at pos_zmz with dissolve
    "——季彤崖。"
    show zmz b flip with dissolve
    show zmz b flip:
        xoffset 0
        linear 1.0 xoffset -200
    show dly:
        yalign 1.0
        xoffset 1280
        linear 1.0 xoffset 680
    with Pause(1.5)
    dly "那是和我一脉的师兄，金丹初期。"
    show zmz b tanqi flip with dissolve
    "丁灵云路过，瞄了一眼，毫不留情打碎了钟明烛的期冀。"

    stop music
    scene tiantaifeng xiaowu2 with Fade(1.0, 2.0, 1.0)
    play music "sound/bgm/阿鲲 - 萧 Xiao.mp3"
    show zmz b at pos_zmz with dissolve
    zmz "师父，你在筑基中期能打败金丹期的吗？就门中普通水平的金丹期。"
    "她那场时间很靠后，嫌现场人太多，便索性回天台峰等候，见长离正在廊下闭目养神，就往她身边一卧，视线漫无目的地扫过竹阶，湖面，天空，最后落在长离眉心的朱砂痣上，瞧了很久后懒洋洋如此问。"
    hide zmz with dissolve
    show cl b dazuo biyan at pos_cl_dazuo with dissolve
    cl "可以。"
    "长离没有睁眼，她能够察觉落在自己脸上的眼神，对此已习以为常。"
    hide cl with dissolve
    "过了好一会儿，钟明烛才收回目光，翻了个身，瞥见长离腰带上那串南红玛瑙，眸底不觉掠过一丝笑意，抓起把玩起来。"
    image manao = "images/obj/玛瑙.png"
    show manao:
        xcenter 0.5
        ycenter 0.5
        zoom 1.0
    with dissolve
    with Pause(1.0)
    nrr """
    {clear}

        那是她在逐浪城街头偶然所见，一眼便被那火一样的成色吸引，便买了下来，后来见长离一身素白，觉太过单调就转手赠给了她，还亲手替她挂到了腰带上。

　　和她眉心那点朱砂一样，是空寂中唯一的色彩，仿若雪中绽放的梅花，绮丽异常。

当时那个江城主发觉后还赞美了一大通，叫钟明烛愈发得意。
    """
    hide manao with dissolve
    show zmz b tanqi at pos_zmz with dissolve
    zmz "那我呢？"
    "隔了许久，她松开那串玛瑙，望向主峰所在的方向，幽幽问。"
    hide zmz with dissolve
    show cl b at pos_cl with dissolve
    with Pause(1.0)
    "长离沉默，不知是不是错觉，钟明烛觉得她似乎轻轻叹了一口气，等了一会儿才听她缓缓道出“尽力而为”四个字。"
    hide cl with dissolve
    show zmz b ganga at pos_zmz with dissolve
    zmz "啊……师父你就不知道有时候坦诚很伤人的……"
    "她叽叽咕咕数落起来，看上去哀怨极了。"
    hide zmz with dissolve
    "长离不理她，任凭她碎碎念念说了一大通废话都一声不吭。"
    "午后的阳光过于舒适，很快她就被睡意缠住，半睡半醒之际，隐约听到长离对她说了什么。"
    cl "……为师等你捷报。"
    "似乎是思考了很久才想到的，依旧带着几分不确定和犹豫。"
    "真的假的啊？"
    "她来不及多想，就睡着了。"

    scene yunfushan lianwuchang with Fade(1.0, 1.5, 1.0)
    stop music
    show jty with dissolve
    with Pause(1.5)

    nrr """
    {clear}

        季彤崖和风海楼同一批入门，看起来年纪却大很多，约莫二十六七岁的模样。

　　看着比师父还老，钟明烛撇了撇嘴，和修为高出一阶的前辈相对立于演武场上，她竟然还有心思想别的。

　　很快，她就修正了自己的想法。

　　——师父的话，还不至于用老来形容，看起来还不满二十岁，混在一干师伯里简直就像他们的女儿，不过的确是差了好几百岁，若师伯们有孩子，说不定比师父年纪还大。

　　不但有心思想别的，甚至还很认真地越想越远。
    """
    jty "师妹，请多指教。"
    "直到季彤崖洪钟似的的声音响起，她才止住进一步去思考师伯们有没有孩子这个问题。"
    hide jty with dissolve
    show zmz b at pos_zmz with dissolve
    zmz b wugu "师兄，请多指教。"
    "她勾起一个柔柔的微笑。"
    "柳眉舒展开，却驱不散那股似是与生俱来的脆弱感，略浅的眸中含着雾气，愈是笑，愈让人产生一种稍用力就会碎掉的感觉。"
    "好一个柔弱无助的小师妹啊。"

    play music "sound/bgm/曾志豪 - 剑执清平.mp3"
    hide zmz with dissolve
    "她注意到季彤崖的呼吸顿了一顿，眼微微眯起，笑得愈发温柔，扬手招出长剑，下一瞬便挥出漫天剑光。"
    window hide
    image gif_mantianjianguang = SquenceAnimator("images/effect/漫天剑光", interval=0.15)
    play sound "sound/audio/刀剑/连续唰唰声.mp3" loop
    show gif_mantianjianguang:
        xcenter 0.5
        ycenter 0.5
        zoom 5
        alpha 0.0
        easein 0.5 alpha 1.0
    with Pause(2.0)
    play audio "sound/audio/鞋摩擦.mp3" volume 5.0
    show jty yansu:
        xcenter 0.5
        yalign 1.0
        zoom 1.5
        easein 0.3 zoom 1.0
    with dissolve
    "季彤崖还没完全从怜香惜玉的情绪中抽离出来，就被这眼花缭乱的剑法震慑住，接连后退至边界。"
    play audio "sound/audio/移动呼声/se115.wav" volume 2.0
    scene black with tran_lf
    scene yunfushan lianwuchang with tran_lf
    play audio "sound/audio/鞋摩擦.mp3" volume 5.0
    show jty yansu:
        xcenter 0.5
        yalign 1.0
        zoom 1.5
        easein 0.3 zoom 1.0
    with dissolve
    "这是她学过的剑法中招式最繁复的一套，名为繁花，意在表达出百花斗艳的浮世繁华，她在剑中注入了灵力，刹那间流辉耀目，将大半演武场都纳入其中，倒真的演绎出了几分繁华的感觉。"
    "但也仅仅是看起来而已，钟明烛这套剑法说白了就是花架子，遇到金丹期的，很快就会被看出底细。那边季彤崖已经在最初的冲击中冷静下来，会被唬住的主要原因也是因为钟明烛的师父是长离仙子。{p}若没有这层关系，他估计连最初那一丝慌乱都不会有。"
    hide gif_mantianjianguang with dissolve
    show jty yansu with dissolve
    "看出这师妹身手不过如此，他立即展开攻势，祭出法器，也是剑，他驱剑画了一个圈，然后轻轻一推，一条火龙当即自剑尖跃出，咆哮着向钟明烛奔去。"
    hide jty with dissolve
    image gif_huolong = SquenceAnimator("images/effect/火龙", interval=0.3)
    play sound "sound/audio/龙咆哮.wav"
    show gif_huolong:
        xcenter 0.5
        ycenter 0.5
        zoom 3.5
        alpha 0.0
        easein 0.5 alpha 1.0
    with Pause(3.0)
    scene black with tran_lf
    scene yunfushan lianwuchang with tran_lf
    show zmz b shengqi at pos_zmz with dissolve
    "钟明烛当即御剑而起，她剑法不行，御剑之术倒是不错。"
    play sound "sound/audio/移动呼声/咻.wav"
    show zmz b at hide_tb(y=-100)
    "用她的话来说，若御剑不行，万一遇到危险岂不是逃命都来不及，不行，一定要精通。"
    scene black with tran_lf
    scene yunfushan lianwuchang with tran_lf
    play sound "sound/audio/龙咆哮.wav"
    show gif_huolong:
        xcenter 0.5
        ycenter 0.5
        zoom 3.5
        alpha 0.0
        easein 0.5 alpha 1.0
    "她用了疾风符，速度极快，游刃有余地在边界范围内与那火龙斡旋，试过结印抵御，但是一下子就被冲破了。"
    image gif_shuilong = SquenceAnimator("images/effect/水龙", interval=0.3)
    play sound "sound/audio/施法/闪电攻击.wav" loop
    show gif_shuilong:
        xcenter 0.5
        ycenter 0.5
        zoom 1.5
        alpha 0.0
        easein 0.5 alpha 1.0
    "季彤崖御剑追了她一会儿，发现追不上便索性停下，长剑一点又挥出一条雷龙，然后在场中设下重重石障碍。"
    "多了一条龙，还须得绕开或击碎石障，情况立即危险了数倍，钟明烛的兴致却愈发高昂起来，眼底眉间均是兴奋，她手里有不少金丹级别的符箓，不过打算留到之后再用，万一砸完了后面遇到高手就无计可施了。"
    stop sound
    scene black with tran_lf
    scene yunfushan lianwuchang with tran_lf
    show zmz b xiee at pos_zmz with dissolve
    "好在这季彤崖比较蠢，她瞥了眼专心驾驭那两条龙的人，嘲弄地冷哼了一声，忽然一转身，向季彤崖冲过去。"
    play sound "sound/audio/移动呼声/咻.wav"
    show linework
    show zmz b xiee:
        linear 0.3 zoom 0.8
    with Pause(0.3)
    scene black with tran_lf
    scene yunfushan lianwuchang with tran_lf
    show jty yansu with dissolve
    show huzhao:
        xcenter 0.5
        yalign 1.0
        zoom 3.5
        alpha 1.0
        ease 1 alpha 0
        ease 1 alpha 1.0
        repeat
    "对方见她来势汹汹，结起屏障的同时下意识后退了一段距离。"
    scene tiankong xialuo with tran_lf
    show fastwork_ud:
        alpha 0.5
    "钟明烛在即将撞上屏障的时候忽地拔高位置，眼看那两条龙要撞上去，季彤崖立即双手结印，同时降低高度回避，口中喝道："
    scene yunfushan lianwuchang with tran_lf
    show jty with dissolve
    jty "起！"
    play sound "sound/audio/移动呼声/布料呼声.mp3" volume 1.5
    show jty at nod()
    "两龙随即贴着屏障往上奔去。"
    hide jty with dissolve
    show gif_huolong:
        xcenter 0.5
        ycenter 0.5
        zoom 3.5
        alpha 0.0
        easein 0.5 alpha 1.0
    show gif_shuilong:
        xcenter 0.5
        ycenter 0.5
        zoom 1.5
        alpha 0.0
        easein 0.5 alpha 1.0
    with Pause(1.0)
    play sound "sound/audio/龙咆哮.wav"
    show gif_huolong:
        easein 1.0 alpha 0.0 zoom 5.0
    show gif_shuilong:
        easein 1.0 alpha 0.0 zoom 3.0
    with Pause(1.0)
    scene tiankong xialuo with tran_lf
    show zmz b xiee at pos_zmz with dissolve
    zmz "啊，是时候了。"
    play sound "sound/audio/移动呼声/咻.wav"
    show linework
    show zmz b xiee:
        linear 0.3 zoom 0.8 alpha 0.0
    with Pause(0.3)
    "钟明烛扫了眼场地，身子在空中绕了个圈，再度向季彤崖冲去，场地和之前相比缩小了一些，她险些转身时险些被火龙扫到，下摆都被烧了一块。"
    scene yunfushan lianwuchang with tran_lf
    show jty yansu with dissolve
    "看着再一次冲过来又在极近处改变方向的钟明烛，季彤崖这次冷静了许多，没有回避，而是试图提前驱动那两条龙改变方向，不料他还没来得及念完咒就觉得那两条龙上的灵力被放大了。"
    hide jty with dissolve
    play sound "sound/audio/龙咆哮.wav"
    show gif_huolong:
        xcenter 0.5
        ycenter 0.5
        zoom 3.5
        alpha 1.0
        linear 1.5 zoom 5.0
    with dissolve
    show gif_shuilong:
        xcenter 0.5
        ycenter 0.5
        zoom 1.5
        alpha 1.0
        linear 1.5 zoom 3.0
    with dissolve
    with Pause(2.5)
    "身形瞬间暴涨，连咆哮声都大了许多，竟是有人在上面灌注了更多灵力，灵力多了后驾驭起来更加困难，季彤崖竟没能让它们慢下来。"
    scene yunfushan lianwuchang with dissolve
    show jty yansu with dissolve
    jty "怎么回事？"
    show jty nanguo with dissolve
    "他惊讶地睁大眼，连忙想收回所施之法，而后，眼里却浮现出更多的震惊，甚至慌乱。"
    transform shake_char(x=5, y=3, t=0.06):
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
        parallel:
            yoffset 0
            ease t yoffset y
            ease t*2 yoffset -y
            easein t yoffset 0
    show jty nanguo at shake_char(x=5, y=3, t=0.1)
    with Pause(1.5)
    show jty nanguo at shake_char(x=5, y=3, t=0.1)
    with Pause(1.5)
    "他发现他动不了。"
    hide jty with dissolve
    play sound "sound/audio/龙咆哮.wav"
    show gif_huolong:
        xcenter 0.5
        ycenter 0.5
        zoom 3.5
        alpha 1.0
        parallel:
            linear 0.5 zoom 5.0 alpha 0.0
        parallel:
            linear 1.5 alpha 0.0
    with dissolve
    show gif_shuilong:
        xcenter 0.5
        ycenter 0.5
        zoom 1.5
        alpha 1.0
        parallel:
            linear 0.5 zoom 3.0 alpha 0.0
        parallel:
            linear 1.5 alpha 0.0
    with Pause(2.0)
    "下一瞬，他亲手放出的两条巨龙咆哮着将他吞没。"

    stop music
    scene yunfushan lianwuchang with fade
    show zmz b at pos_zmz with dissolve
    with Pause(0.6)
    play sound "sound/audio/移动呼声/落地.wav"
    show zmz b at nod(y=-20, t=0.12)
    with Pause(1.5)
    "待那两条龙消失后，季彤崖已经晕了过去，钟明烛从飞剑上跳下来，笑嘻嘻对他作了个揖，故作谦虚道："
    show zmz b at nod()
    zmz "多谢师兄手下留情。"
    "与此同时，负责裁夺的卢忘尘给出了结果——天台峰钟明烛胜。"
    hide zmz with dissolve
    nrr """
    {clear}

        而围观的弟子大部分还沉浸在不可置信中，当钟明烛暴露出她的剑法水平后，他们以为她输定了，就算再能跑，场地一缩再缩，迟早要被追上或者自行出界的。却没想到季彤崖会被自己的灵力反噬。

　　可能是还不能熟练驾驭吧，才会失手，多数人都这么认为，只有修为较高的一些人才知道发生了什么，他们同样表现出了惊讶，不过是惊讶于钟明烛的大胆或者说那前所未有的方法。

{clear}

　　起手那套剑法的根本目的是在场中留下灵气，那些灵气微弱且毫无章法，很容易就被忽视，实际上却是补下了一张网。

她将季彤崖诱入其中后，引火雷二龙追逐，在接近季彤崖的时候挥出两道符，在短时间内将那两条龙的威力提高了一倍，好令季彤崖控制不住，然后在他试图防御的时候以先前部下的灵气为引，结阵将他定住。

钟明烛只有筑基期修为，无论是提高那两条龙的威力，还是定住金丹期修士，都只能维持片刻，可能只有几个眨眼的功夫，稍有偏差便会功亏一篑。

可她却做到了，即便是金丹期修士也鲜少有人能将时机把控得如此精准。
    """
    show yy with dissolve
    with Pause(1.0)
    nrr """
    {clear}

        云逸同样注意到了这场比斗。

        他已经很久没见过能将阵法、符咒等等天衣无缝融合到战斗中的人了。

        心思缜密且敢于以身犯险，增强对手灵力之类的举措简直匪夷所思。

　　之前他只知道钟明烛在阵法一道天赋很高，这时候却发现，她在战斗上的天赋可能更高。

明明不是剑修，却能运用策略胜过高一级的敌手。
    """
    yy biyan "后生可畏，后生可畏。"
    "他感叹道。"


    jump story_14_1
