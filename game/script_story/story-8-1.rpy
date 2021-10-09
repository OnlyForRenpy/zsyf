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

label story_8_1:

    image cg8-1-1 = "images/cg/CG-8-1-1.jpg"

    stop music fadeout 1.0
    window hide
    scene black with fade
    with Pause(1.0)
    scene yunfushan guangchang with fade
    play sound "sound/audio/嘈杂.wav" loop
    with Pause(4.0)
    show cl at appear_tb(x_c=0.5, y_c=360+100, y_o=-30, z=0.38, t=0.75)
    stop sound fadeout 1.0
    with Pause(2.0)
    "到了太乙广场，原本人声鼎沸的地方霎时安静下来，好像被冻住了一样。大家的反应惊人地一致，论是各峰峰主还是在等候的下一代弟子都不约而同将目光落在那抹纤白的身影上。"
    hide cl with dissolve
    show yy with dissolve
    "最先反应过来的是云逸，立即笑容可掬迎上来，道："
    yy xiao "师妹，许久不见，今日过来，莫非也是要择徒？"
    show yy with dissolve
    nrr """
    {clear}

        他知道长离尚未出师，此话不过是缓和一下气氛。因为是宗主，在所有平辈门人中他是唯一能与长离说上几句话的。

　　当初看到襁褓中粉雕玉琢的女婴时，大家其实都很欢喜，甚至有人当天就开始琢磨该给这位师妹准备什么礼物，只是没几天长离就被吴回带去了天台峰，还下了禁令，三大长老以外的人都不得擅入，连他这个宗主，也是在长离结丹后才再一次见到她。

曾经的喜爱再强烈，也早就在那么长时间的毫无交集里烟消云散，加上吴长老在与长离相关的事上屡屡破例，招致不少门人心有不满，然那个第一剑修要偏袒他的弟子，另外两大长老亦睁一只眼闭一只眼，纵是有怨言又能如何？

久而久之，天台峰就像是被剔出了天一宗一样，无人过问，即使当年长离逼退千面偃立下大功，同门也只是对她多了几分敬意，而非亲近。
    """
    play sound "sound/audio/嘈杂.wav" loop volume 0.5
    "云逸一开口，气氛终于活络了一些，大抵也是因为刚结束修炼的弟子终于从亲眼见到长离仙子的震惊中缓过来了。"
    "“真的是长离仙子？”"
    "“你看那颗朱砂痣，准没错。”"
    "“谁来扶我一把，我要站不住了……”"
    "此起彼伏的惊叹传入云逸耳中，他不由得干笑了两声，还注意到而站在最前面，第一个结束试炼的圆脸少女，那个丁家的小女儿，激动到眼角都红了。"
    hide yy with dissolve
    show dly lianhong with dissolve
    transform nod2(y=10, t=0.24):
        easein t yoffset y
        easeout t yoffset 0
        easein t yoffset y
        easeout t yoffset 0
    play sound "sound/audio/星星棒.wav"
    show dly lianhong at nod2(y=10, t=0.2)
    with Pause(1.5)
    hide dly with dissolve
    show yy biyan with dissolve
    "不愧是小师妹……他如此感慨，接着就听到了意料外的答案。"
    scene yunfushan guangchang with tran_lf
    show cl at pos_cl with dissolve
    cl "是，我修行遇瓶颈，师父吩咐我来选一个弟子，为入世之历练。"
    "长离好似完全没注意到那边的骚动，坦然作答，声音并不是很响，却也足以传入在场所有人耳中。"
    play sound "sound/audio/嘈杂.wav" loop volume 2.0
    "然后广场瞬间炸开了锅，甚至还传出几声尖叫。"
    hide cl with dissolve
    show yy with dissolve
    yy xiao "呃……"
    "云逸心想既然是吴长老的吩咐，他也不好反对，便问，"
    show yy with dissolve
    yy "不知师妹可有人选？"
    nrr """
    {clear}

        ——必定是没有的，云逸敢肯定小师妹之前估计连试炼的事都不清楚，问完后一边告诉她此次试炼的情况，一边思考起该给她推荐哪些人。

　　优秀的显然是不行的，在座不少师弟师妹可是眼巴巴地盼了宝贝徒弟好多年。况且从长离话里的意思来看，收弟子为的是突破瓶颈，这本就是有悖师道之事，将好苗子丢给她很可能误了他们修行。

　　差的也不行，那岂不是不给吴长老面子，而且小师妹天赋过人，给她资质差的估计两人都没法交流。

　　思来想去，云逸打算给长离推荐几个资质中庸，能自食其力，无论拜入何人门下影响都不大的人。
    """

    hide yy with dissolve
    show cl at pos_cl with dissolve
    "他在想的时候，长离也在思考需要怎样的弟子。"
    "不过她想的比云逸简单多了，她初为人师，此前修行多为自行领悟，可以说对教习二字一无所知，而且师父也没有交代需要怎样的弟子，于是很快拿定主意，问道："
    cl "试炼结束了吗？"
    yy "尚有两人未出来，不过时间快到了……"
    "云逸话还没说完，就察觉森林出口处传来一阵灵力波动，微微一笑道，"
    yy "来了。"
    stop sound
    scene shulin b with tran_lf
    show zmz xiee at objpos(x=0.3, y=0.6, z=0.4) with dissolve
    show nsc fennu:
        xcenter 0.7
        yalign 1.0
    with dissolve
    with Pause(2.0)
    "话音刚落，两道青灰色的身影自山道那出现，一前一后奔入太乙广场。"

    scene yunfushan guangchang with tran_lf
    show cl at pos_cl with dissolve
    "与此同时，长离向众人宣告了她的决定。"
    window hide
    scene cg8-1-1 with dissolve
    with Pause(2.0)
    nrr """
    {clear}

        “师兄，我欲收此人为徒。”

        她看也不看就一指最后抵达广场的那道身影，平静地说道。
    """

    scene yunfushan guangchang with dissolve
    hide cl with dissolve
    show zmz xiee at pos_zmz with dissolve
    "钟明烛看起来有些狼狈，衣服上沾了不少泥尘，头发也有些乱，可却笑得春风得意，好似在试炼中撞了天大的好事一般。"
    hide zmz with dissolve
    nrr """
    {clear}

        事实上的确如此，成功报了当年的一箭之仇，可不是天大的好事吗。甚至还换来了南司楚的苦苦哀求和指天划誓再不冒犯。

　　起初南司楚还憋着一股傲气不与她说话，可熬了一天后终是屈服于试炼失败的恐惧下，晓之以理动之以情，恳求钟明烛早些放了他。

　　鬼才信你，钟明烛面上一直笑眯眯的，心里却暗骂，她知道以南司楚的气量，若放早了一定会翻脸对她发难，所以算好了时间，在还剩大半天试炼就结束的时候从方阵前撤离了。

{clear}

　　南司楚花了一柱香多一点的时间击碎了挡路的方石，他以为钟明烛先行一步，便发了疯似的往出口冲，一路上劈坚斩锐，以所向披靡之势杀出一条路，连山鬼都被他吓得躲远。

　　怎料到钟明烛根本没走远，而是藏匿于不远处，在他大杀四方开路的时候偷偷跟在他后面，一路畅通无阻，直到即将出森林才加快速度。

　　南司楚发现身后突然出现的钟明烛，才知道自己又被摆了一道，脸色不知有多难看，然而顾忌试炼结果，只能强忍住脾气。

{clear}

　　去太乙广场的路上，钟明烛一直在回味南司楚那青一阵紫一阵的脸色，根本没注意广场上的动静。

反正她是最后一个，也没有什么好在意的。

　　待她察觉到气氛似乎有些不对劲时，长离那番话已传入所有人耳中。
    """

    show zmz wugu at pos_zmz with dissolve
    zmz "嗯？"
    "发觉那些恨不得化为利刃将自己戳穿的眼神，钟明烛的笑容终于有些挂不住了，她茫然地扫视四周，最终目光在一只纤纤玉手上落定。"
    hide zmz with dissolve
    show cl at pos_cl with dissolve
    "那是长离仙子的手，正在指着自己。"
    "发生什么了？为何那么安静？我做了什么吗？"
    "她第一反应是林中的事被发觉了，可很快就推翻了这个猜测，就算被发觉，也不会是被那个连天台峰都没出过几次的长离仙子发觉。{p}天之骄子如她，根本不知道筑基试炼是什么吧！"
    "百思不得其解之下，她一头雾水地摸了摸脸，随后求助地看向了最前面的丁灵云。"
    hide cl with dissolve
    show dly shengqi with dissolve
    play music "sound/bgm/卢小旭 - 鹧鸪天.mp3"
    "——挚友啊，请告诉我发生了何事？"
    show dly shengqi at wobbly(x=3, y=2, t=0.1)
    "而丁灵云回了一个非常不友好的手势，以她的大小姐身份来说，那手势可以说相当粗暴了。"
    scene black with tran_lf
    scene yunfushan guangchang with tran_lf
    "摸了摸鼻子，钟明烛迅速收回视线，她有一种强烈的感觉，如果此刻发问的话，很可能会陷入万劫不复的境地。"
    "单是随意一瞥她就看到不少把拳头捏的咯咯作响的人，有些人脑袋上甚至迸发出星点火花，太吓人了，她决定装死。"
    show nsc fennu with dissolve
    show nsc fennu at wobbly(x=3, y=2, t=0.1)
    "在此之前，她特地瞄了南司楚一眼，见到他那显然已经无法用难看来简单形容的脸色后，确定他应当是知道发生了什么，而且对他来说肯定不是什么好事。"
    hide nsc with dissolve
    show zmz limaoweixiao at pos_zmz with dissolve
    "敌人的痛苦即是我的快乐，钟明烛当即勾起嘴角朝他露出一个比之前更为灿烂的笑容，这才垂下眼做出一副听凭处置的乖巧样。"

    hide zmz with dissolve
    with Pause(1.0)
    nrr """
    {clear}

        比起后辈中滔天的不满，长辈们倒是心照不宣交换了个宽慰的眼神，放松下来。

　　没有去抢最优秀的那几个，甚好。

　　云逸看了一圈，见无人反对，便立刻答应下来：“就按师妹的意思来。”

　　期间风海楼好几次都想说什么都被他阻住了。凡事须以小师妹为先，不然那个吴长老拉下脸来，可不是闹着玩的。

　　那个最后结束试炼的弟子的确是合适的人选，虽然是最后一位，但却是在五年内就成功筑基的，表现不算拔尖，却也不是很差，既不会抢了诸位师弟师妹心仪的人选，又不会拂了吴长老面子。

　　宗主一开口，广场陷入了更深的死寂。
    """

    window hide
    show cl at pos_cl with dissolve
    "长离则是倘若未闻般，对那些黏在自己身上得眼神视而不见，快步向即将成为自己弟子的人走去。"
    scene yunfushan guangchang with tran_lf
    show zmz at pos_zmz with dissolve
    "她这才发现竟又是那个少女，若是其他人，说不定会觉未免太过巧合，她却半点未多想，走到对方面前站定，漆黑的眸子里倒映出对方好似不堪一折的脆弱轮廓。"
    cl "可愿入我门下？"
    zmz wugu "啊？"
    "钟明烛后知后觉地反应过来，为何那些同门一个个都那么凶神恶煞看着她。{p}原来是长离仙子要收她为徒，而她剑术有多糟糕大家也都心知肚明，二者加起来，几乎占了七成人数的长离仙子仰慕者会多愤怒，可想而知。"
    show zmz tanqi with dissolve
    "纤细修长的眉稍稍皱起，她觉得有些为难。"
    "虽然之前说了去哪扫地都无妨，事实上她还是有打算的，想借风海楼的关系入驻天一峰，以她的试炼结果，亲传自是指望不上，但只要拜入符咒一脉，以后自然有机会学习更多阵法，她目前也只对那个稍微多一点兴趣。"
    "却没想到长离仙子会突然杀出来。可惜剑术对她而言，委实没什么吸引力。"
    show zmz digu with dissolve
    "不是说了小师叔未出师不收徒么，风海楼你个骗子。"
    show zmz miyanxiao with dissolve
    "她心中暗暗抱怨起来，面上却做出恭敬的样子，正打算以自己剑术不精为由推脱，不知为何又有点舍不得。"
    "她承认她心动了，虽然她对练剑不感兴趣，虽然长离仙子的口气淡漠的听不出半点诚意，可看着周围门人几乎要从眼中溢出的强烈羡慕，以及南司楚气到发抖的模样，不得不说当真是心情大好，叫人飘然欲仙。"
    "被天上掉下的馅饼砸到，她为何不吃了再做打算？"
    zmz wugu "亲传吗？"
    "她眨了眨眼问道，下一瞬就听到四周一片抽气声。"
    "这家伙还敢讨价还价？长离仙子的亲传？做梦吧！"
    "门人眼中的愤懑几近实体化，然而顷刻便因长离仙子的回答碎成粉末随风而散。"
    cl "可以。"
    "那个拥有几千年来最高天赋的白衣剑修，想也没想就答应了。"
    zmz miyanxiao "好，我愿入你门下。"
    "钟明烛轻轻笑了起来，眼中透出飞扬的神采，连眉梢都似挂上了笑意。"

    scene black with fade
    with Pause(1.0)
    scene yunfushan guangchang with fade
    show yy biyan with dissolve
    "目送长离携她新收的小徒弟离开后，云逸心中一块大石终于落定。"
    "既然解决了小师妹的问题，那接下来就该轮到他们好好挑选徒弟了。"
    "他转过身，笑眯眯地问风海楼："
    yy xiao "徒儿，上次你说的那个对阵法颇有造诣的师妹在哪？"
    hide yy with dissolve
    show fhl wunai1 with dissolve
    "而风海楼还目瞪口呆看着长离离去的方向，待云逸第二遍发问，才哭丧着脸说："
    fhl wunaixiao "师父……就是被小师叔带走那个……"
    "为了避免有偏袒之嫌，他此前只和师父提过有这么一个师妹，却没有讲她的名字，现在肠子都悔青了。"
    "钟明烛擅长阵法，剑法却是糟糕透顶，去当小师叔的徒弟，不是闹笑话吗。"
    stop music fadeout 0.01
    hide fhl with dissolve
    show yy xiao with dissolve
    yy "什么？"
    "云逸的笑容僵住了，一时不知该惋惜自己一脉丢了个好苗子，还是该忧心给长离塞了个不谙剑术的弟子会招来吴长老的不满，大概两者都有吧。"
    "可木已成舟，他身为一宗之主岂能出尔反尔，只得安慰自己道小师妹还年轻，以后大可再收几个能继承衣钵的弟子，而那位擅长阵法的弟子，他个人可以给她些指导。\n所谓五脉，指的只是专精，若有心，什么都可以学。"


    scene black with fade
    with Pause(2.0)
    play music "sound/bgm/剑网3 - 情缘·一见千年.mp3"
    scene yunfushan quanjing with fade
    nrr """
    {clear}

        通常弟子拜入各峰后，会由内门的师兄师姐引领前往住处，办理名牒更替，并发放内门弟子服饰以及更高阶的物品，并予以修炼安排。

　　天台峰却是例外，只有长离一人，连个服侍的小童都没有。

　　一开始钟明烛沉浸在巨大的成就感中未曾想到这一层。

　　离开太乙广场时她提出要长离载她一程——在其他人看来简直厚颜无耻胆大包天，然而后者没有反对。

这一出令同门对她的怒火燃到了空前的高度，也令她的得意翻了数倍，只顾着高兴了将其他都抛到了脑后。待冷静下来时，已稀里糊涂跟着长离一起到了天台峰。

{clear}

　　天台峰和其他几峰格局相似，自南向北分别是前门，广场，主殿，演武场以及居室。

看得出曾经的辉煌，而如今却只剩冷清萧索。

曾经天台峰武尊一脉下有好几分支，剑修只是其中之一，但兴许是运气不好，云逸一代的武尊弟子不是寿元耗尽就是战死，在长离入门前，便只余吴回长老一人。

前山的建筑被结界封起，约莫是太久无人往来，索性封起来也好省去维护的功夫。

　　长离直接将钟明烛带到了后山的住处。
    """

    scene tiantaifeng xiaowu1 with fade
    nrr """
{clear}

    那是一所竹制的阁楼，和前山的建筑比起来成色尚新，看起来应是专门建了给长离住的，西傍一池碧波，不远处就是天台峰峰巅，往下可见渺渺云海。

　　竹篱围起的小院里有几块青石，几株翠竹，门外一棵雪松，除此之外，空无一物，门前牌匾上书有“重明”二字。

　　明明是竹屋，却起这样的名字，也不怕不吉利。

　　钟明烛看着那沉稳大气的两个字，隐隐约约察觉到那并非简单书写而成，而是刻下的符篆，心中不免浮现出一股怪异感，继而她又想到长离和自己的名字，倒是有些可怜起这屋子来。

　　一座竹阁，却是外火内火，倒是滑稽。

她想进去好好观望一番，可前面长离却驻足不前。
    """
    show cl kunhuo at pos_cl with dissolve
    "只见那白衣女子一言不发，凝眸沉思，看起来就好像庙堂里供奉的神女像一般凛然不可侵犯。"
    "上下打量了长离一番，钟明烛无奈地摸了摸鼻子。"
    "她就知道……刚刚，终究是太过得意忘形了。"
    "长离仙子知道如何替弟子更替名牒吗？{p}或者说，她知道需要先给弟子换上内门弟子的身份玉牌吗？{p}显然，是不知道的。"
    "虽然对方看起来在很认真地思考，可光这么想能想出来个鬼。"
    "丝毫没意识到心中的嘀咕已算得上目无尊长，钟明烛叹了口气道："
    zmz "师父？"
    show cl with dissolve
    cl "何事。"
    "其实钟明烛还未正式拜师，在三叩六拜奉上拜师茶之前还不能直接喊师父，不过她笃定长离没那么讲究，便也懒得计较这些细节，再者，抢先一步喊上了，以后对方也不好反悔。"
    zmz "弟子尚未更换名牒，交接之事，师父若不清楚，不妨寻宗主一问？"
    "钟明烛本想说由自己去，但转念一想以自己的身份，直接去找师伯们大抵是僭越了，于是话头一转便全部推给了长离，再说，她这个师父是该去了解一下为人师者该做些什么。{p}看，她这弟子多贴心。"
    cl "也好，你且在此等候。"
    play sound "sound/audio/移动呼声/布料呼声.mp3"
    show cl at hide_tb(y=-100, t=0.5)
    nrr """
    {clear}

    说罢长离便离开了，钟明烛只来得及瞥见一道残影，之后，这空空荡荡的山头便只剩下她一人，正午刚过，阳光正烈，她却莫名感到一股寒意。

　　大抵是山顶的风太大了，如此叹道，她抬手在竹扉上磕了三下，而后推门而入。

　　院中便是她在外所见的那样，几块石头和几棵竹子，连杂草都没几根，衬着偌大的院子，显得可怜巴巴的，钟明烛挑了下眉，一边寻思着以后是不是该种点花花草草改善一下，一边顺着竹木铺成的小径往里走。

　　小径通往正北的阁楼，看起来约莫有三层，除此之外，湖畔还有一座小屋，仅一层，和那阁楼相比显出几分简陋来。

　　钟明烛觉得那大抵是堆放杂物的地方，可又觉得依水而筑有些浪费，便先往那走去想探个究竟。
    """

    scene tiantaifeng fangjian with tran_close
    with Pause(2.0)
    nrr """
    {clear}

    门未上锁，她进门一看，发现里面看起来倒像是起居室，但是东西很少，仅一张竹塌，一套桌椅，床上连枕头都没有，明明屋子不大，却还显得空空荡荡的。

　　难道这其实是长离仙子住的地方？

　　她寻思道，心里还没习惯称对方为师父。

　　就位置来看没什么问题，湖畔风景好，若是她也会乐于住在这，可这屋里又太过空旷，根本不像有人居住的样子。

虽说修道之人清心寡欲，但这未免也太过了。

　　她记得风海楼说他曾炼了个熏香炉送给师父当贺礼，云逸很喜欢，立刻放置在屋中，由次可推测像云逸那般修为的人屋里也是有点摆设的。

{clear}

　　也许这里曾经有人住，只不过现在废弃了，她找了一个看起来比较合理的解释，接着便去了正北的阁楼。
    """

    scene sword-1-2 with tran_close
    with Pause(2.0)
    nrr """
    {clear}

    随即闯入眼帘的景象令她不由得惊了一惊。

　　剑、满眼都是剑，阁楼为分层，八面墙壁直通到屋顶，每一面墙上都挂满了剑，足足有上千把，剑为杀器，那么多柄聚集一处，单是剑气就会对人造成不小的损伤。

寻常人收藏剑都是收入鞘中的，而这些剑都是剑刃朝外，倒是御敌之态。

最叫人奇怪的时，那些剑看起来皆品相不俗，偏偏都黯淡无光，看起来就像是破铜烂铁似的。

　　她随意捡了一把，只见剑刃极其锋利，足以吹毛断发，然而一丝神采都无，就是将手指贴到剑刃上，都不会感受到丝毫威慑。

{clear}

　　这是已经毁了吗？

　　她挥了挥手里那把，只觉迟缓如朽木，心道：

那个长离仙子已经够奇怪了，没想到住的地方更奇怪，收纳了一堆宝剑偏偏都是破铜烂铁，也不知是什么癖好。

　　乱七八糟的念头此起彼伏，她揉了揉脑门，无心再看那些剑，退了出去，回到湖畔的木屋里。
    """

    scene tiantaifeng fangjian with tran_close
    nrr """
    {clear}

    至少有一点确认了，钟明烛幽幽叹了一口气。

　　这破屋子的确是长离仙子的起居室。

　　那我该住在哪？

　　她看着空空荡荡的山头，眼中难得出现茫然之色，最后还是决定乖乖回那小屋里等长离回来。\n\n\n\n\n\n

　　——没想到，一等就是三个月。
    """

    jump story_9_1
