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

label story_5_1:

    image cg5-1-1 = "images/cg/CG-5-1-1.jpg"
    image cg5-1-2 = "images/cg/CG-5-1-2.jpg"
    image cg5-1-3 = "images/cg/CG-5-1-3.png"

    image gif_lvsehuanrao = SquenceAnimator("images/effect/绿色环绕", interval=0.1)

    play sound "sound/audio/环境/瀑布-长.wav" loop
    window hide

    scene zhulin with fade
    nrr """
    {clear}

        第四天清晨，她走了没多久就听到远处水声，
    """
    scene white with close
    show pubu:
        xoffset 0
        yoffset 0
        zoom 1.5
        alpha 0.0
        parallel:
            easein 0.8 alpha 1.0
        parallel:
            linear 2.0 yoffset -150
    with Pause(3.0)
    nrr """
    {clear}

        拨开前方几丛青竹，自山巅悬下的瀑布映入眼中，山体呈现出三层阶梯之势，水势极快，撞上石台的水流发出阵阵咆哮，溅起的水雾闪烁着银光，自上而下，好似被三朵祥云覆盖。

        那景色太美，钟明烛看了好一会儿，才动身去找那三味草药。

    {clear}

    “三迭瀑下的水潭边……”

    她念叨着几个字，循着溪畔往那边走去。

    才走了几步，她便发现此地竟还有一个人。
    """

    scene white with close
    show cg5-1-1:
        xoffset 0
        yoffset 0
        zoom 1.2
        alpha 0.0
        parallel:
            easein 0.8 alpha 1.0
            pause 2.4
            easein 0.8 alpha 0.0
        parallel:
            linear 4 xoffset -200 yoffset -150
    with Pause(4.0)
    show cg5-1-2:
        xcenter 0.5
        ycenter 0.5
        zoom 1.1
        alpha 0.0
        parallel:
            easein 0.5 alpha 1.0
        parallel:
            linear 3 zoom 1.0
    with Pause(4.0)

    nrr """
    {clear}

        瀑布之下，水潭正中，有一座圆形青石台，上面静静坐着一个人，一身素白，背影纤细，连发带都是白色。

    {clear}

    看起来正在静坐，大抵是门中前辈吧，钟明烛正犹豫是不是出声问候。
    """
    window hide

    with Pause(0.5)
    play sound "sound/audio/刀剑/拔剑.wav"
    show cg5-1-3 at CG_800_600 with tran_lf
    with Pause(0.2)
    hide cg5-1-3 with tran_lf
    with Pause(1.0)
    play sound "sound/audio/跳水落水.wav"
    with Shake_screen((0, 0, 0, 0), 1.5, dist=15)

    nrr """
    {clear}

        却见那白衣人袖子一振，挥出一道青光，没入瀑布中，片刻后，后方震了一下，一方巨石滚入水中。

    {clear}

    钟明烛看到巨石上平整的切口，不由自主地“哇”了一声，还拍了拍手。

　　她第一次，由衷地惊叹了。
    """

    scene pubu with fade
    nrr """
    {clear}

        那个白衣女子应当在她接近时就发觉了，所以听到她的声音没有表现出任何意外，待那方巨石沉入潭底，彻底安静下来后，她才施施然起身。

    {clear}

    下一瞬，人已在钟明烛面前。
    """

    play music "sound/bgm/聆溪箜篌_亦凡 - 《飞雪玉花》.mp3"
    play sound "sound/audio/移动呼声/布料呼声.mp3" volume 1.5
    show cl at appear_tb(x_c=0.5, y_c=360+160, y_o=-10, z=0.5, t=0.5)
    with Pause(2.0)
    "——绝代有佳人，幽居在空谷。\n钟明烛脑海中一瞬浮现出这样一句诗来。"
    "只见那人青丝悬瀑，白衣胜雪，面若玉……{p}
等等，这话怎么有点眼熟，她连忙打住，目光在女子眉心那点朱砂上落定，突然意识到面前这人的身份。"
    hide cl with dissolve

    show zmz chijing at pos_zmz with dissolve
    zmz "长、长离仙子？"
    "都怪丁灵云每次提到长离仙子都那么激动，害她不小心结巴了一下。"
    "她暗中唾弃了一声自诩为好友的家伙，轻咳了一声，笑道："
    show zmz at pos_zmz with dissolve
    zmz "虽然晚了许多，不过还是要说一句，多谢长离仙子救命之恩。"
    hide zmz with dissolve

    show cl at pos_cl with dissolve
    "对方理都没理她这番诚恳的感谢，那双漆黑的眸子里没有多余的情绪，视线在在钟明烛脸上停留了一会儿，问道："
    cl "来此地何事？"
    zmz "采药。"
    show cl at move_down(y=5, t=0.25)
    show cl at move_down(y=-5, t=0.25)
    with Pause(1.0)
    hide cl with dissolve

    "话音刚落，长离眼帘轻垂，钟明烛猜那大概是应许的意思，而后便见那袭白衣回到那块青石台上，背对她盘腿坐下，无论是位置还是姿势和此前相比都分毫不差，让她一瞬间产生对方刚刚只是甩了一抹虚影过来和自己对话的错觉。"
    scene cg5-1-2 with dissolve
    with Pause(0.5)
    nrr """
    {clear}

        她在池畔转了一圈，等候了一会儿，长离没有再和她说一个字，闭眼静静坐在瀑布前，一动不动，无声无息，仿佛下一刻就会化为一座石像。

        是寡言而冷漠的人呢。

        茂林修竹，飞瀑坠星，幽幽古潭，白衣佳人，美不胜收。

        ——只有自己是多余的。

        钟明烛摸了摸鼻子，转头去找草药了。
    """

    scene pubu with tran_lf
    nrr """
    {clear}

        水潭不大，连同附近的竹林一起，全部扫一遍都没有花费太久的时间，她几乎将那一块的地皮都翻了一遍，在夜幕降临前，她就采到了足够多的草药，甚至还挖到一株半臂长的人参。

　　干完这些后，她晃了晃塞得满满当当的储物囊，在水潭边找了块平整的石头坐下，取出一枚野果，却没立刻吃，而是盘算起这趟出门的收支来。

　　这个任务的报酬，加上多采到的草药，她大概能赚二十枚灵石。

　　而一柄飞剑据说是一百灵石，她虽然不知道修理费需要多少，但直觉告诉她，这趟绝对亏了。

{clear}

　　很好，她冷笑，恶狠狠地咬了一口野果。

　　其实她并不是很在意灵石灵药之类，风海楼评估过她的修为，说五年内筑基不成问题，对于修炼她并不是很热衷，一向是做一天和尚撞一天钟，接任务大半是出于可以出来兜风散心的缘由。

她不介意亏钱，甚至把迄今为止那点可怜的积蓄统统送人都不会皱一下眉头，但遭人暗算而导致的亏损就另当别论了。

　　那电光上的气息太明显了，她就是修为倒退一半都认得出。

{clear}

　　——有机会她一定要把南司楚脸朝下摁地上。

　　如此暗下决心后，她吞下最后一口果肉，抬眼看向长离。
    """

    with Pause(0.5)
    # play sound "sound/audio/刀剑/拔剑.wav"
    show cg5-1-3 at CG_800_600 with tran_lf
    with Pause(0.2)
    hide cg5-1-3 with tran_lf
    with Pause(1.0)

    nrr """
    {clear}

        恰好看到对方又一次朝瀑布挥出一道青光，霎时爆出的凛冽剑气便是钟明烛都感受到了。

　　又是一块巨石沉下。

　　酝酿那么久就为了这一招么，若第一次钟明烛是惊叹，第二次便觉得有些腻味了。

就在她思考这水潭能容下多少块石头时，听到长离轻轻吐了一口气。

不知为何，她似乎从中听出一丝沮丧。
    """

    scene pubu with dissolve
    show cl dazuo biyan at pos_cl_dazuo with dissolve
    zmz "你总是来劈石头吗？"
    "鬼使神差地，她朝长离喊了一句。"
    "刚喊完她就后悔了，那长离仙子冷冰冰的，看起来也不像是会搭理她的样子，更何况这问题听起来委实有些傻。{p}不料没多久她就听到对方清冽的嗓音。"
    "终归是修为深厚，无需似钟明烛那般大喊大叫，便能清晰地将声音传递过来。声音很轻，就好似来自咫尺之畔。"
    cl dazuo "我没有在劈石头。"
    "无多起伏的音调听起来颇是一板一眼，竟是很认真地在回答，这意外发现令钟明烛忍不住扬了扬眉毛，继而轻笑道："
    zmz "不是在劈石头，难道是在劈瀑布吗？"
    "她本是调笑，不料竟听到对方轻轻道了一个“是”字。"
    show cl dazuo dark at pos_cl_dazuo
    "笑容顿时僵住，钟明烛断断续续长长喘了一口气，勉强忍住险些脱口而出的质疑。"
    "心中却不以为然道，怕不是傻的，没听过抽刀断水水更流吗……{p}
不过这念头转瞬即逝，因为她想到这不是凡世，这些人可都是要成仙的。\n
仙人的话，移山填海，点石成金，无所不能吧？"
    "可她刚刚并没有感受到特别强的灵力波动，也许是她修为太低没感受到，但也很可能是长离并没有动用她那元婴期的修为，她有些好奇，便试探地问："
    zmz "以仙子的修为，就是把这瀑布夷为平地也不难吧？"
    show cl dazuo at pos_cl_dazuo
    cl dazuo "这不一样。"
    "长离的语气依旧是淡淡的，并没有因为钟明烛的缪误而产生任何不满情绪，反而细细解释起来，"
    cl "此招名为断水，便是要以剑将瀑布斩断。"
    "钟明烛皱了皱眉，眸中显出一丝迟疑，探知欲却已经被勾起，继续问道："
    zmz "上源水流不绝情况下的断水？"
    cl "是。"
    zmz "唔……是否是修为不足之故？"
    cl "此为剑道，亦为心道，悟不得，便是大乘飞升，也无法斩断这流水。"
    "钟明烛凝视着清澈的潭水，潋滟波光中白衣似覆了淡淡的雾气，随水波而轻晃。{p}沉默了一会儿，她似乎有点明白了。"
    hide cl with dissolve
    show zmz sikao at pos_zmz_sikao with dissolve
    "这不就是经书上神神叨叨那套吗。"
    show zmz at pos_zmz with dissolve
    zmz "这段话是你师父教你的吗？"
    "她舒舒服服往后一靠，面上复而覆上笑意，"
    zmz "道可道，非常道，名可名，非可名诸如此类的。"
    "长离没吭声，看来是说对了。{p}
若是自己悟出来的，也不会傻乎乎在这劈石头了，钟明烛轻笑，片刻后突然意识到自己太放肆了。"
    "糟糕，太得意忘形了，那可是宗主的师妹，风海楼的小师叔，五千年来的第一天才，以及丁灵云的心之所向。\n她虽然不太清楚丁灵云对长离仙子是什么性质的心之所向，但可以肯定，若被她知道自己这么对长离仙子说话，一定会拆掉自己几根骨头。"
    show zmz wugu at pos_zmz with dissolve
    "笑容立即收敛起来，她小心翼翼瞄了一眼长离，后者看起来倒是没有计较她的失礼，而是垂下眼，再度恢复之前眼观鼻鼻观心的老僧入定状态。"
    show zmz at pos_zmz with dissolve
    zmz "咳……"
    "她也看不出长离有没有计较，不过想了想还是觉得打个圆场比较好，"
    zmz "吴长老为当世第一剑仙，必定是精于此招深有所悟方会有这番金口玉言……"
    cl "师父也没有领悟这招。"
    "钟明烛顿时想给自己一耳光，同时在心里腹诽起来。"
    show zmz ganga at pos_zmz with dissolve
    "所以吴长老那个什么大乘飞升都斩不断流水原来指的就是自己啊，自己都没会就让徒弟在这对着瀑布乱砍是不是太不负责了！"
    "感受到愈发尴尬的气氛，钟明烛扯了嘴角，勉强挤出一个笑容，敲了敲脑门，忽而想到了什么，喃喃道："
    show zmz at pos_zmz with dissolve
    zmz "方才我其实是认为以剑断水为无稽之谈，不过突然想到天地之初盘古大神开天辟地，后昊天帝分三界，连天地灵气都可分开，何况是区区流水。"
    "她又想到曾经从丁灵云口中听说过一些关于剑修的事。{p}
据传曾经修得大成的那剑修，曾偶然得上古剑谱，又观得残留于玉壁上的舞剑之姿，后方有所感悟，那舞剑之人却是个凡人。其后人开创荒连剑宗，传承上古剑谱，然于剑道上的造诣却远不及先祖万分之一，勿论在玉璧上留下残影的凡人了。"
    show zmz sikao at pos_zmz_sikao with dissolve
    "听的时候她其实没多大留心，如今随口胡诌上古传说时偶然想到，忽然就觉得此前的嘲笑倒是显得自己无知了，这么想着，口气不觉认真起来："
    zmz "这么说来我倒是听闻凡世有宝刀，名为断水流，想来悟此道的确不分修为。"
    show zmz sikao dark at pos_zmz_sikao
    cl "何以悟得此道。"
    "长离若有所思地开口。"
    show zmz at pos_zmz with dissolve
    zmz "不知道，我对剑道其实一窍不通。"
    "钟明烛又摸了摸鼻子，这是她感觉不自在时候惯有的小动作，大概是以前的习惯，虽然失忆了，但身子还记得，"
    "若长离仙子以后有所领悟，不妨赐教一二。"
    hide zmz with dissolve
    show cl dazuo at pos_cl_dazuo with dissolve
    cl "可以。"
    show cl dazuo biyan at pos_cl_dazuo with dissolve
    "说完这两个字，长离便重归于沉默。"
    "钟明烛伸了一个懒腰，她也觉得有点累了，索性闭上了眼。"

    scene black with close
    nrr """
    {clear}

        风海楼偶然提到过几次这位小师叔，自他口气中很明显能感受到恭敬、倾佩以及战战兢兢，刚见面时候长离的确给人一种不近人情的感觉，她几乎要对风海楼感同身受了。

        可刚刚那番对话又让她觉得并不尽然。

　　冷漠倒是真的，却非拒人于千里之外那种。

　　似乎是挺有趣的人啊。
    """

    stop music fadeout 3.0
    play sound "sound/audio/环境/鸟叫2.wav" loop
    play sound "sound/audio/环境/瀑布-长.wav" loop
    scene pubu with close
    show cl dazuo biyan at pos_cl_dazuo with dissolve
    "睁眼已是天明，长离还坐在那块青石上。"
    show cl dazuo biyan dark at pos_cl_dazuo
    "不愧是元婴修为，钟明烛懒洋洋打了个哈欠，起身走到潭水边上，捧起水往脸上泼了泼，冰冷的水激得她打了个激灵，然后彻底清醒了。"
    "醒了就该打算回程的事了，她心道天台峰应该有传送阵吧，不过为了保险起见，还是问了一句："
    zmz "天台峰顶有传送法阵吗？"
    show cl dazuo biyan at pos_cl_dazuo
    cl "没有。"
    "答案竟出乎意料，该先说一句幸亏问了还是直接开始哀嚎？"
    "钟明烛一下露出头疼的表情，一边习惯性去摸鼻子，一边开口，听起来有点瓮声瓮气的："
    show cl dazuo biyan dark at pos_cl_dazuo
    zmz "不知不语峰在哪个方向，可否给我指个路？"
    show cl dazuo biyan at pos_cl_dazuo
    cl "顺着溪水往下游即可。"
    "长离仍是一板一眼的调子，有问必有答，但除却回答外，不会多说半个字。"
    "钟明烛本来还等着她问自己为什么不御剑，然后就好顺水求个人情，结果等了个自讨没趣。她心里本就不痛快，见长离这般不冷不热半点关爱同门的意图，便愈发不痛快起来。"
    "难道不应该稍微多关心一下未来的师侄吗？亏得丁灵云那么崇拜你，却是个不顾别人死活的，亏我昨天还和你扯什么剑道！她心里抱怨道。"
    "这般不闻不问也太过不合常理了——{p}念及“常理”二字时思绪骤然顿住，她皱了皱眉，心中忽地浮起一个念头。"
    "——莫非当真是不通俗事？"
    "她收起面上愤懑之色，将那柄剑自储物囊中拿出往前一递，笑道："
    zmz "长离仙子，我的飞剑被雷劈坏了，不语峰路途遥远，我着急回明镜峰将药材交给龙田鲤大长老，不知……"
    show cl dazuo at pos_cl_dazuo with dissolve
    "话至此，换个人早该明白她的言下之意，无需她亲自说出口就该有所回应，长离却还是一声不吭，而是回身看着她，安静地等她说完。"
    "真是个怪人，钟明烛摸了摸鼻子，老老实实把话说完："
    zmz "还请长离仙子助我回明镜峰。"
    cl "好。"
    hide cl with dissolve
    image feijian = "images/obj/飞剑.png"
    show feijian:
        xcenter 0.0
        ycenter 0.5
        alpha 0.0
        zoom 0.5
        parallel:
            easein 0.6 alpha 1.0
        parallel:
            easein 1.0 xcenter 0.5
    with Pause(1.5)

    "钟明烛还以为要等上老半天才能听到长离的答复，没料到才说完对方就应许了，下一瞬她眼前就多了一柄明晃晃的灵剑。"
    zmz "咦？这是？"
    "她愣住了。{p}这也太干脆了。"
    cl "飞剑上的飞行符阵已彻底损坏，我没法帮你修好，就用这个回去吧。"
    "长离如此解释。"
    "这把飞剑成色比自己那把不知好上多少，钟明烛接来比划了一下，轻便灵巧，而后一松手，那把剑便稳稳停在半空。"
    zmz "送给我的？"
    "她挑眉，还是有些不相信。"
    cl "可以。"
    "长离没有纠结送还是借的问题，钟明烛觉得如果自己问的是借，对方的回答说不定一点都不会变。{p}
那人对这些都毫不在意。"
    "还真的是不能用“常理”忖度，她这般寻思着。{p}突然瞥见长离右手正握着一根细长的竹枝，看起来是随手折来的，约莫三尺多长，上面还缭绕着丝丝剑气。"

    scene pubu with tran_lf
    show cl dazuo biyan at pos_cl_dazuo with dissolve

    # show image gif_1.pop(0)
    # $ count = 10
    # while gif_1.png_list:
    #     # image gif1:
    #     #     gif_1.png_list.pop(0)
    #     #     pause gif_1.t_interval
    #     show image gif_1.png_list.pop(0):
    #         # gif_1.pop(0)
    #         xcenter 0.33
    #         ycenter 0.75
    #         zoom 1.2
    #         alpha 0.5
    #         pause 0.5

    show gif_lvsehuanrao:
        xcenter 0.33
        ycenter 0.75
        zoom 1.2
        alpha 0.5
    with Pause(2.0)

    "昨晚她就是用这个劈开岩石的吗？"
    "顿时明白为何看到的是青光，钟明烛不禁缩了缩脖子，若她一早知道对方手里的只是竹条，打死也不会那般口出狂言。{p}
她竟然还暗中嘲笑对方傻乎乎的，幸好没说出来，不然指不准要被这竹条抽。"
    "长离没发觉钟明烛看到竹枝后汹涌而起的复杂情绪，给了灵剑后，见钟明烛没说什么，便回去继续静坐。"
    "钟明烛稍加思忖，心道对方有吴回长老倾囊相授，区区一把飞剑不足挂齿，又见长离已开始闭目运功，于是索性连客套都省了，留了句：“那就多谢啦。”便跳上灵剑离开了天台峰。"

    stop sound
    scene yunfushan guangchang with fade
    with Pause(1.0)
    play music "sound/bgm/曾志豪 - 少年游.mp3"
    nrr """
    {clear}

        她没有立刻回明镜峰，而是先去主峰找了风海楼，问这把剑是否能归她所用。

        她觉得以长离不通俗事的程度，极有可能不清楚外门弟子的条条框框，还是找靠谱的人问清楚比较好。她可不想因为违反门规再被参一本。

　　风海楼正好在，听了她这几天的经历，先是愤愤不平扬言要找南司楚问清楚，不过被钟明烛阻住，说自己有分寸若他出面反而给人留话柄，之后，听闻他小师叔送了一把飞剑给钟明烛后，顿时露出半是惊奇半是羡慕的神情。

　　看钟明烛招出那柄剑后，更是露出了眼馋的表情。
    """
    show fhl with dissolve
    fhl wunaixiao "这可是金丹级的飞剑，还是上品。"
    "他抚过剑身，感叹道，"
    "我现在那把也就差不多品质，可能还要差一点。"
    zmz "那送给你？我离金丹期还早。"
    "反正是白来的，钟明烛在心里补了一句。"
    show fhl with dissolve
    fhl "这倒不用。法器也要讲机缘，那日小师叔救了你，这次又助了一把，这剑就是你与她的机缘。"
    "风海楼将剑推还给她。"
    zmz "那门规？"
    fhl "无碍，门规限制的只是灵药灵石等有助于快速提升修为的东西，对于法器没有限制。"
    zmz "若有人带了厉害的法器岂不是能横着走？"
    fhl "法器受制于主人修为，就像这把剑，在你手中至多发挥出炼气程度的水平。"
    zmz "那我就收下了。"
    "钟明烛放心了，开开心心地跳上剑打算飞回了明镜峰，临走前她问了风海楼一个念念不忘的问题。"
    zmz "你那太师叔，龙田鲤长老，是姓龙，还是龙田？"
    stop music fadeout 0.01
    show fhl wunaixiao with dissolve
    with Pause(1.0)
    "风海楼沉默了。"
    "过了好一会儿，声音才再度响起。"
    zmz "那我先走了？"
    fhl "嗯……你走吧。"

    jump story_6_1
