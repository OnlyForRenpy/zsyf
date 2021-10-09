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

label story_11_1:

    image cg11-1-1 = "images/cg/CG-11-1-1.jpg"
    image cg11-1-2 = "images/cg/围棋2.jpg"

    stop music
    window hide
    scene black with fade
    with Pause(1.0)
    scene yunfushan guangchang with fade
    play music "sound/bgm/剑网3 - 情缘·一见千年.mp3"

    show yy dark with dissolve
    cl "师兄，恭贺出关。"
    show yy
    nrr """
    {clear}

        云逸刚从闭关到石室踏出，就听到一道熟悉的嗓音。

　　恍若濯清涟而不妖的水芙蓉，又若空山新雨初歇之后的青石，美则美，却也因为太过不沾人气的缘故显得冷漠疏离。

　　这声音，莫非是——

　　他一个趔趄险些撞在石室外那棵歪脖子老槐树上，抬眼就瞥见不远处那袭白衣。
    """
    hide yy with dissolve
    window hide
    show cl at pos_cl with dissolve
    with Pause(2.0)
    hide cl with dissolve
    show yy biyan with dissolve
    with Pause(1.0)
    nrr """
    {clear}

        先是一怔，而后立即闭眼默念起清心诀来。

        稍后才反应过来他闭的不过是为期七七四十九天的护气养身关，不可能遇到心魔，这才定了定心，再度往那瞧去。
    """
    show yy with dissolve
    nrr """
    {clear}

        发现的确是长离本人在问候他，她身前是引路的风海楼，后面还跟了个青衫少女。

        正是她前不久收的徒弟，手里还捧着一个紫檀盒，像是礼物的样子。

　　小师妹竟然过来给自己请安，还带了礼物？
    """
    show yy chensi with dissolve
    nrr """
    {clear}

        纵是他已九百多年道行，仍是难以保持淡然，下意识就往西边看去。

　　这事出反常必有妖，难道是日头打西边出来了？
    """
    hide yy with dissolve
    show fhl wunaixiao with dissolve
    fhl "师父，别看了。"
    "风海楼有点看不下去了，小声提醒道，"
    fhl "听闻您今日破关，小师叔特地来看望。"
    "好歹是堂堂第一仙门的宗主，他这个当徒弟的还是要脸面的。"
    hide fhl with dissolve
    nrr """
    {clear}

        其实风海楼自己也没好到哪里去。

        十几天前，他见一抹白衣御剑而来，轻飘飘落在玉珑峰主殿前，而后传音道欲拜访云逸，顿时像中了定身咒一样瞪大眼张着嘴一句话都说不出，直到钟明烛过来轻轻把他下巴往上一推，他才回过神。

　　长离不是没来这找过云逸，之前来过一次，直奔云逸所处之地，第一句话就开门见山说明来意，就像择徒那天一样，来去如风，从未考虑过礼节，而今却规规矩矩站在门口求见。

　　\n怕不是个假的！

{clear}

“我师父来拜访宗主，你这什么态度！”

最后还是钟明烛的声音令他安下心。

　　这么嚣张的口气，至少这个钟师妹是真的，不过他没来得及细想，禀明师父正在闭关后，那对师徒问了出关时间就离开了。

{clear}

之后，他不断听闻长离前往其他几峰拜访的事，一时流言四起，有几位师叔甚至亲自过来问他是不是发生了什么不得了的事，一个个都是白日撞鬼的表情。

　　毕竟只要不是新入门的弟子，都知道长离仙子与世隔绝，见她一面比见那三位化神期长老都难，连门派百年祭典这种事都不露面。和风海楼一辈的弟子，大部分只在当年的试炼中和长离接触过，而这大部分中的七成连她的脸都没看清就晕过去了。

　　所以长离此举无疑在门中掀起一番波澜，风海楼无意中还听到有弟子偷偷讨论长离仙子是不是被夺舍了。

{clear}

夺舍当然是无稽之谈，天一宗能存活那么久，全是得益于天一道人留下的大小结界和阵法，门人以外，所有不是从山门进入的人都会被发觉，即使是一缕幽魂都不例外，门人则是因为入门时已经过山门的考验，以后出入才能省略这一步。要在天一宗境内对长离仙子夺舍是不可能的。

不过长离仙子一改往日作风，却也是事实。

　　今天一大早，长离又带了钟明烛一起过来，风海楼有了心理准备，所以这次没有露出下巴都惊掉的表情，顺带还提醒了自己师父一下。
    """

    scene yishiting with close
    show fhl wunai2 with dissolve
    "等云逸将长离引入茶室，风海楼便将本打算一起进去的钟明烛扯到一边，有些紧张地问道："
    fhl "小师叔怎么了，是、是病了吗？"
    hide fhl with dissolve
    show zmz b shengqi at pos_zmz with dissolve
    zmz "你才病了！"
    "钟明烛立刻甩过去一个白眼，"
    zmz "我师父诚心拜访，交流一下同门情谊，你的想法能不能不要那么阴暗！"
    hide zmz with dissolve
    show fhl wunaixiao with dissolve
    fhl "是我失言了，抱歉。"
    "风海楼尴尬地拱手道歉，但仍是不死心，"
    fhl "师妹可否告诉我，小师叔为何突然拜访起其余各峰来？"
    show fhl wunaixiao dark
    zmz "这不是应有的礼数吗？"
    show fhl wunaixiao
    fhl wunai1 "话虽如此，但……"
    "风海楼叹了一口气，门中互相走动很正常，师叔们经常来寻云逸议事或者单纯过来喝茶，但这事放在长离身上就不正常了，"
    fhl "小师叔从不与人来往，突然改变作风，门中难免有诸多揣测。"
    hide fhl with dissolve
    show zmz b sikao at pos_zmz_sikao with dissolve
    zmz "这是我的主意，毕竟是同门，师父这样索然独居才是太奇怪了。{p}我倒是不解，为何师父会与诸位师伯生分至此。"
    show zmz b sikao dark
    fhl "这……我也不清楚。听说是太师伯的主意，说小师叔体质特殊，须得心无旁骛。"
    show zmz b sikao
    "如今遇到瓶颈了就想到要她入世了呢——"
    show zmz b at pos_zmz with dissolve
    "钟明烛眸中闪过不以为然的神色，但也仅是告诉长离要入世历练，至于具体该做些什么却没有任何交代，只道一切都由长离自己决定，仿佛有意要让她自行探索。"
    "——若非机缘巧合选到我这么个机灵的徒弟，师父这会儿怕还是在天台峰闭门造车吧。{p}钟明烛如此想着，抿嘴勾起一个浅笑，心里又把自己夸了一通。"
    "她如此建议其实有自己的考量，什么助师父历练，只是顺带而已。{p}剑修一道对她来说无异于镜花水月，而唯一感兴趣的事却需要其他各脉辅助，叫长离携礼前往各峰拜访，便是给自己以后谋些便利，刷个脸熟后即可自行登门求教。"
    "这不，丹药炼器术法等三脉的峰主收了长离的礼物后，听闻长离的弟子有心博采众家，便都传了些功法玉牒给她，虽说这些并不是秘密，但若是钟明烛自己前去，必然无法这般顺利的。"
    hide zmz with dissolve
    show fhl wunaixiao with dissolve
    fhl "钟师妹，你……"
    "风海楼看着她不觉流露出得意的模样，欲言又止。"
    zmz "嗯？"
    fhl "你就不怕惹小师叔生气吗？"
    "还是忍不住说了。"
    "他可是见到小师叔就想逃跑呢，和他一起参加试炼的弟子也都差不多，便是对小师叔仰慕有加的新弟子，也仅仅是抱着仰慕之心远观而已。"
    scene yunfushan qiandian with dissolve
    show cl at pos_cl with dissolve
    nrr """
    {clear}

        长离在主殿前等候时，不少人驻足观望，却无一人敢于上前问候，至多只是一边窃窃私语一边投以热切的目光。

        要风海楼说的话，他完全能体会那些弟子的感受，毕竟小师叔那副遗世独立的清冷模样即使不做什么也足以叫人心生畏惧，就像是一尊绝美的冰雕，远观即可，接近的话就太冷了。

　　钟明烛竟然敢给长离出主意，而长离竟然照做了，风海楼都不知这两件事里哪一件更叫人吃惊一些了。
    """
    scene yishiting with dissolve
    show zmz b at pos_zmz with dissolve
    zmz b ganga "这……"
    "钟明烛其实想告诉风海楼，你小师叔一点都像你所想的那样吓人，可话到嘴边，可瞥见风海楼那副疑惑的样子便改了主意，转而假装糊涂，"
    show zmz b with dissolve
    zmz "我也不清楚，师父她必然有自己的考量吧。"

    scene cg5-1-2 with Fade(1.0, 1.0, 1.0)
    play music "sound/bgm/阿鲲 - 萧 Xiao.mp3" volume 1.5
    nrr """
    {clear}

        第一次见面时，她其实和风海楼一样，觉得那位长离仙子是拒人于千里之外的高傲性子，若要寻个具体一些的形容，那便是大抵是浑身结着冰棱，一接近就会被刺伤。

        与她短暂交谈后虽稍有好转，甚至觉得对方有趣，只是事后忆起那白衣女子，却还是有种霜雪扑面而来的冰冷之意。

　　钟明烛没有惧怕，甚至敢于和她讨价还价，只是因为本性如此，这天不怕地不怕的性子连她自己有时都要嘀咕上几句。
    """
    scene tiantaifeng xiaowu2 with fade
    nrr """
    {clear}

        但经过大半年的相处，她差不多已摸清长离的脾气。

　　长离根本就没有脾气。

　　就算是练剑时候把剑摔她脚下都不会显出气恼的神情，顶多罚她抄几遍门规罢了，会惩罚也不是因为生气，而是因为这样对师父不敬的确有违门规——

———那也是在钟明烛影响下记住门规内容后才这样的。


{clear}

　　长离寡言，鲜少主动说话，若钟明烛有事相问，却是知无不言，从功法到剑招，甚至天台峰上的一草一木，只要她知道，都会如实告知，从不会不耐烦。

　　有一次钟明烛练剑练一半突然问她：“师父你多高啊？”

　　明显是闲得无聊没话找话，换个人必定要呵斥几句，脾气差的说不定会责罚。而长离连眼神都没变，平静地报出一个尺码，然后继续看钟明烛练习她新教的剑招。

　　发觉这点后钟明烛有事没事就去逗长离说话，一问一答，这时候长离从不吝啬，纵然是长篇大论也会一字不漏地说与她听。

　　钟明烛觉得很好玩，日复一日变本加厉，她以为总有一天长离会不耐烦，甚至可能会恼羞成怒，可最终还是她先腻味了，之后连着十几天没和长离搭话，对方也没有任何反应。仿佛根本没有察觉到变化，这让她挫败了一阵子，不过很快就自我安慰起来，其他人两百多年来听到长离仙子说的话都不如她一天来得多，这么一想便又神气活现了。
    """

    window hide
    scene cg11-1-1 with fade
    with Pause(2.0)
    nrr """
    {clear}

    在听过她那套入世理论后，长离便不再整日枯坐冥想，除了偶尔指点剑招，余下的时间便是看书练字，栽培花苗，垂钓采药，有时候甚至会在她做饭时候打打下手，颇有几分不务正业的架势————

    ————当然，这些可做的事都是在钟明烛告诉她的。

    天一宗藏书颇多，除却修炼之外各艺皆有涉猎，平时无人问津，钟明烛随便找找就捧了一堆回来。

　　一开始她还担心会被太师父找上门，过了一阵子见无人来兴师问罪，便也放下了心，有人和自己一起玩，何乐不为。

{clear}

　　而符咒炼器一类的修行在长离的帮助下愈发顺风顺水，长离修为深厚，刻符篆的成功率比钟明烛高了许多，替她刻了不少金丹级别的符箓，若钟明烛的灵力不足以催动阵法，便以自身灵力相辅助。是以钟明烛虽然仅是筑基修为，却能琢磨远高于自身修为的阵法。天台峰有炼炉，只是长久未开启，接下来钟明烛就打算让长离帮自己炼几套法器。

若被其他几峰的弟子知道这等待遇，估计要羡慕得红了眼，自古长幼有别，师父对于弟子向来是教导提点，即便是对待亲传弟子也不会像长离那样有求必应。顶多偶尔赠弟子一些符咒法器防身，哪里会直接帮弟子刻符炼器。

而钟明烛倒好，丝毫没有僭越的自觉，满脑子都是怎么从长离讨更多便利。

毕竟得来全不费工夫，不用白不用。
    """

    scene black with fade
    nrr """
    {clear}

    这些事她都没有告诉风海楼，她觉得那就像是自己私藏的点心，放在只有自己知道的地方，只有自己才能品尝，并为这份属于自己的独一无二开心不已。

　　若被其他人知道师父那么好说话，说不定会打消先前的顾虑一窝蜂涌上来，长离的声望何其高，仰慕者何其多，她可是一清二楚。

　　—————那么好的师父是她一个人的。想来分一杯羹，这可不行。

　　既然选择了远观，那就继续远远看着吧。
    """

    scene yishiting with tran_fog
    show fhl wunaixiao with dissolve
    nrr """
    {clear}

    风海楼看着钟明烛唇角若有若无的笑意，不禁打了个冷战。

　　救回钟明烛那会儿他还以为自己会添一个乖巧可人的小师妹，毕竟有着那么一张写满了柔弱无助的脸。

不过这样的遐想很快在对方用聊天气的口气和自己商量“我是不是该表现得愁苦一些”之类的问题后被击碎，而后很快就认识到钟明烛身上能称得上乖巧的只有那张脸而已，他身为宗主唯一的亲传弟子，其他弟子见了都要露出恭敬的神色，唯有钟明烛半分畏缩之意都无，待他与外门弟子没有任何区别。

他性子宽厚，加上钟明烛于阵法一道天分很高又是自己引入门中的缘故，所以还挺喜欢这个小师妹的，也知道对方张扬的性子容易结仇，总会提醒她注意些。

    {clear}

这不又来了。

　　师妹，还请你收敛一下眼里的得意和算计啊。
    """

    scene tiantaifeng xiaowu2 with Fade(1.0, 2.0, 1.0)
    nrr """
    {clear}

    回天台峰后，钟明烛就去料理食材了。

　　她七天煮一次饭，雷打不动，林中物产丰厚，足够她尝试诸般花样。

当热腾腾的饭菜摆上石桌时，长离已经入座，等着开饭。

　　若被那些个师兄师姐们知道自家小师妹进食比普通弟子还勤，怕又是一阵惊涛骇浪。

    {clear}

　　自从长离听了钟明烛的建议开始尝试其他事后，就不再拒绝她一同吃饭的邀请。

起初还要钟明烛唤一声，后来看到钟明烛去厨房她就先行去坐好，如今执筷已非常熟练，对于吃食的讲究也了解了不少。

　　她不挑食，问她喜欢什么总是说都可以，不过时间久了钟明烛还是发现自家师父比较偏好糕点甜食，会稍微多吃一点，想来是本性使然，只是她自己还没发觉。

　　——这些都是钟明烛觉得有意思的地方，这样的长离才像个活生生的人，而不是雕像之类的。
    """

    scene cg11-1-2 with close
    nrr """
    {clear}

    吃过饭，长离就回房，继续研究桌上那局棋。

　　那天钟明烛兴冲冲抱着棋盘过来，最终却还是没能下成，因为长离说她不会。叫钟明烛手一抖险些把棋盘摔了。

　　都说修道之人六艺精通，放凡世那可都是风流无双的人物，就像风海楼，琴棋书画无不出彩，钟明烛之前以为长离只是不感兴趣，那时候才知道她对剑术之外的事当真是一无所知。

　　哭笑不得之下她只能自己与自己对局，一边落子一边将规则告诉长离，心中念叨着不知道师父何时才能摸出门道。

　　她可不想和初学者对弈，一会儿就可以将对方杀得片甲不留那多无趣，可念及长离说个话都一字一顿的样子，她就觉得自己怕是要等很久才行。

{clear}

　　然而很快钟明烛就发现，她小看了长离，抛开剑灵之体这点，她师父本身就极其聪慧，对那些从未接触过的事，一点就通。

　　没多久就能试着去解棋谱上的残局了，她们隔三差五对上几盘，起初钟明烛几乎闭着眼睛都能赢，如今虽还是她赢面更大，不过落子前已需要好好考虑一番了。

　　这样日子比之前不知道有趣多少。

　　虽然剑法还是没长进就是了。
    """

    scene yunfushan_far with Fade(1.0, 1.0, 1.0)
    with Pause(1.0)
    scene yunfushan_far b with dissolve
    with Pause(1.0)
    scene yunfushan_far c with dissolve
    with Pause(1.0)
    scene yunfushan_far with dissolve
    with Pause(1.0)
    nrr """
    {clear}

    春去秋来，起初钟明烛还能记得一年一月的变化，时间久了便渐渐看淡了。

　　吐纳的时间从最初的几个时辰变成几天，十几天，甚至数月。

　　天一宗功法包罗万象，她沉浸于其中，又有长离相伴，不觉时日枯燥，反而寻得诸多乐趣。
    """
    stop music fadeout 3.0
    scene black with fade
    nrr """
    {clear}

    时光荏苒，弹指便是百年。
    """
    scene yunfushan quanjing with fade
    nrr """
    {clear}

    当钟明烛将不少中高阶的阵法都摸索透，并且能勉强将长离传授的几百套剑法比划得足以糊弄外行人时，传来西南有妖兽作祟的消息，天一宗欲派弟子下山，与正道其余宗门合作诛妖。

　　在此之前，是天一宗百年一度的宗门大会，两件事合一起，云逸便决定以比斗的方式选出下山诛妖的人选。

　　毕竟诛妖这种事，虽可以有机会扬名立万，但稍有不慎便会落得身死道消的下场，有人想去，也有人不想去，而想去的人也不见得有足够实力，万一派出的弟子还没走几步就被妖兽叼走了，天一宗难免颜面无光，于是就想了个妥善的主意，欲前去诛妖的弟子自行报名参加比斗，前三十名方可下山。

{clear}

　　钟明烛想也没想就报了名，此前偶尔下山过几次，都是在附近城镇，至多去送个信什么的，记忆最深一次是随长离去了一趟逐浪城，好像是城主诞辰，对方亲自送来了请帖。

　　都是平平无奇的经历，钟明烛连去回想都嫌麻烦。

　　这次，终于让她盼来了值得期待的。\n\n

　　——这可是讨伐妖兽，多么令人热血沸腾啊。
    """
    window hide
    show zmz b miyanxiao at pos_zmz with dissolve
    with Pause(2.0)
    nrr """
    {clear}

    她勾起嘴角，仿佛看到血之花在眼前绽放。
    """

    jump story_12_1
