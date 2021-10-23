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

label story_16_1:

    stop music
    window hide
    scene black with fade
    with Pause(1.0)

    play music "sound/bgm/剑网3 - 情缘·一见千年.mp3"
    scene yunfushan guangchang with fade

    nrr """
    {clear}

        宗门大典结束后，下山的日子便定了下来。

        同去的还有两位元婴期前辈，分别是回廊峰主卢忘尘和不语峰肖月。

        待出发那天，前往主峰集合的弟子发现卢忘尘和肖月身后还跟了一人，竟然是长离。
    """

    show cl c at pos_cl with dissolve
    with Pause(2.0)

    nrr """
    {clear}

        她背着古朴的剑匣，依旧是一袭白衣，然而眼尖的人却发现这身白衣与以前不同了。

        剪裁不一样，前襟和裙摆左侧以银丝绣了花纹，乍眼一看依旧是素白一片，仔细一瞧却能看到其上隐有流光浮动，尤其是裙摆，仿佛夜昙绽放。

        不过最显眼的还是腰间那串红色玛瑙，好似流火，鲜明夺目。

　　这串玛瑙长离挂了有些时日，只是她鲜少在人前走动，门中大半弟子都无从得知。
    """

    play sound "sound/audio/众人谈话.wav" loop
    with Pause(2.0)
    "“小师叔怎地来了？她也去吗？”立即有人交头接耳起来。"
    "“我怎么知道，没想到百年不见，小师叔竟然会打扮了。”接话的是当初和风海楼一同参加试炼的弟子。{p}比起长离为何出现在此，他更在意的是长离竟然会佩戴腰坠，还是那么显眼的红色。"
    "毕竟世间对长离样貌的形容永远都是一身素白，不施粉黛，无任何装饰等等。"
    "如今这个虽仍是素衣却不失精细考究的人，这还是那个头发随意用布条一绑了事的小师叔吗？"
    "他如此想着，然后便发现长离头上的发带也换了，与衣服一样是白底银线，初看平平无奇，细看却是精巧绝伦，窄窄一条上竟是绣了延绵不绝的山石草木。"
    "“这……”他瞪大了眼，“还真是不得了了……”"
    hide cl with dissolve
    show zmz b miyanxiao at pos_zmz with dissolve
    stop sound
    "钟明烛听到这些窃窃私语，心里偷笑。"
    "这些都出自她之手，之前用来炼器的鲛绡还剩下几卷，她便给长离做了衣裳，此前一直在炼炉里，前几日才大功告成，原先是想作为饯别礼留给长离的。"

    scene black with fade
    with Pause(1.0)
    scene tiantaifeng xiaowu2 with fade
    play music "sound/bgm/阿鲲 - 萧 Xiao.mp3"
    nrr """
    {clear}

        诛妖之事，少则数年，多则数百年，听闻当年孤鸿尊者在东海与海妖斗法，一斗就是三百七十四年，这一下山也不知要过多久才能回来。

　　她曾问过长离为何不下山游历。

　　几次灭门之祸后天一宗弟子只有遭逢大事时才会持宗主令外出走动，但也没有明令弟子不得出山，自行外出寻找机缘的人不少。不过若是自行下山历练，在外期间不得依仗天一宗的名号，等同于散修，生死祸福皆看自己的造化，与宗门无关。

　　长离答道因她修为尚浅所以师父不许，把钟明烛听得一头雾水。

　　要长离入世，又不准她下山历练，光收个徒弟，偶尔下山跑个腿，那顶多叫和世间有了一缕牵系，和入世差了十万八千里，这老头子真是莫名其妙，活得太久了脑子也会不正常么。

　　钟明烛亲近长离，却对自己名义上的太师父没有好感，心里对他从没有过半点尊敬，称呼他不是“老头子”就是“老不死”，若旁人有读心术，恐怕要被她吓死。

{clear}

　　临行前几日，她一边为诛妖之事而兴奋，一边又因要与长离分别而不舍。

　　相伴百年，如她这般薄凉的性子，也不能否认二人之间或许真的有那么点师徒情谊。

　　毕竟长离从没亏待过她，除了态度冷淡些以及逼她练剑外可以说是挑不出毛病的好，物资上任她索求，授业毫无保留，还从不摆长辈架子，任她如何挑衅滋事都不动怒。

　　对于自己的脾气，钟明烛还是有点自知之明的，能朝夕相对而不给她脸色看的，大抵只有长离了。当年在明镜峰五年，丁灵云可好几次都与她动了手。

　　下山之后，哪里去找这么好的师父啊，况且没长离护着，她若想安然无恙怕是需得夹着尾巴做人，想想就万分憋屈。

{clear}

正当她半真半假感伤时，长离却说此次她会一同前往。

　　“当日师叔前来便是吩咐此事。”

　　听到这句话，好不容易挤出的愁绪一下子散得干干净净，钟明烛径直将手里放着那套鲛绡衣的木盒掷了过去，对准了长离的脸。
    """

    play sound "sound/audio/移动呼声/落地-重.wav"
    image muhe = "images/obj/木盒.png"
    show muhe:
        xcenter 0.5
        ycenter 0.5
        alpha 1.0
        zoom 2.0
        parallel:
            linear 0.7 zoom 0.6
        parallel:
            linear 0.7 rotate 720
        parallel:
            pause 0.5
            linear 0.2 alpha 0.0
    with Pause(1.5)
    show zmz b shengqi at pos_zmz with dissolve
    zmz "不早说！"
    "又变回了那个目无尊长的钟明烛。"
    hide zmz with dissolve
    show cl b at pos_cl with dissolve
    cl "你没有问。"
    "长离接住木盒，打开，问道，"
    cl "这是什么？"
    hide cl with dissolve
    show zmz b shengqi at pos_zmz with dissolve
    zmz "原本是饯别礼，现在么，唉……算了算了。"
    "钟明烛挥了挥手，眉宇间怨气未消，"
    zmz b tanqi "总之是弟子一片心意。"
    show zmz b tanqi dark
    cl "谢谢。"
    "云淡风轻，听不出半分诚意。"
    show zmz b tanqi
    show zmz b shengqi with dissolve
    "钟明烛不以为然冷哼，她以为接下来长离会将木盒收起，当初她收下那串玛瑙后转手就想丢进储物戒，若非钟明烛快一步夺回来给她佩上，那玛瑙估计没机会见得天日了。可这回是衣裳，她总不能强行替长离更换。"
    "大概要过个几百年才会见她穿上吧，她愤懑地想。"
    show zmz b chijing with dissolve
    "不料转头就见长离已经换上了，原本的衣裳折叠好摆在了一边，见状她不禁啧啧了几声。"
    "——修为高了就是方便啊，手指勾一勾身上衣服就换过了。"
    hide zmz with dissolve
    show cl c wuyaozhui at pos_cl with dissolve
    "她打量着长离，看起来仍是一袭白衣，神情淡漠，却不知为何有种焕然一新的感觉。"
    "大概是衣裳好看的缘故吧，果然是我的手艺太好了，她暗暗将自己天花乱坠夸奖了一通，神色缓和下来。"
    "总是这样，脾气来得急去得也快，翻脸比翻书还快，说的就是她这种人。"
    "她走过去拾起那串琉璃，再一次将其绑到长离腰带上，语重心长道："
    show cl c with dissolve
    zmz "师父，我要下山，你若也要下山，这便是与我有关之事，与我有关的，就算我不问，你也应当告诉我。"
    "完全是歪理，照她这么说，长离岂不是要与那三十名弟子一个个打招呼，长离竟是也考虑到这层，反问道："
    cl "那其他人呢？"
    hide cl with dissolve
    show zmz b ganga at pos_zmz with dissolve
    "钟明烛一时语塞，撇了撇嘴心想师父不如以前好骗了，随即凶巴巴扯了一下那串腰坠，道："
    zmz b shengqi "我们师徒情深，他们算什么东西，只要和我说便好。"
    show zmz b with dissolve
    "她半跪在长离身边，没有留心落在自己头上，似若有所思的眼神，片刻后便听到了一如既往的纵容。"
    show zmz b dark
    cl "嗯。"

    scene black with fade
    with Pause(1.0)

    play music "sound/bgm/剑网3 - 情缘·一见千年.mp3"
    scene yunfushan guangchang with fade
    nrr """
    {clear}

        出发前必不可少的一环是宗主讲话，卢忘尘等人立于弟子侧畔，而云逸则在主殿前长篇大论。

　　在他不厌其烦讲着诸如修道之人心念苍生、妖兽作乱天理不容之类的废话时，钟明烛四下张望起来。

　　三十名弟子中，她只认识三个，丁灵云，风海楼，以及被她戏称为清江使的程凌。

　　清江使，神龟也，他虽然输了，不过因为在场时间足够久，是以也得到了机会。

　　除了她和运气极好的丁灵云，其余都是金丹修为，其中最惹人注目的不是风海楼，而是他符咒一脉的师姐柳寒烟，此刻站在钟明烛右前方，目不斜视，风姿凛然。
    """
    show lhy with dissolve
    with Pause(2.0)
    nrr """
    {clear}

        柳寒烟资质普通，五百年才金丹中期，能否踏入元婴期还不得而知，此前一直名不见经传，当年随三大长老赴须弥之海后一直云游在外，几年前才回来。

        她为人低调，回来后就在藏书阁修书，此次比试却一鸣惊人，接连挫败资质和修为最拔尖的数位弟子夺得魁首，其中包括几个金丹末期以及资质最优的风海楼。

　　同在金丹中期的风海楼在第四轮对上了她，一刻钟就败下阵来。

符咒一脉以花样百出的灵符见长，她却鲜少借用灵符辅助，仅凭一把剑从头赢到尾，看了那几场比试的人都觉得那剑气俨然是剑修才有的。

{clear}

　　一剑破万法。

　　相比起来，钟明烛这个天台峰亲传的剑术只能用“丢人”两个字来形容。

　　她站得笔直，好似一把利剑，容姿秀丽，却面若冰霜，一副生人勿近的模样。

据说她还是外门弟子时就有心拜入天台峰，只可惜当时天台峰一脉死的只剩吴长老一人，而吴长老早已不再招纳门人，入了玉珑峰后的几百年一直默默无闻，之后约莫是在外得了什么机缘，练成无双剑法。
    """
    hide lhy with dissolve
    "“若柳师姐晚生几年，如今说不定就是长离仙子的亲传弟子啦。”"
    show zmz b shengqixiao at pos_zmz with dissolve
    "这样的窃窃私语传入钟明烛耳中，她挑了挑眉，冷笑。"
    zmz "几年？那个柳什么比我师父年长了两百……"
    hide zmz with dissolve
    "她话还没说完就被丁灵云捂住了嘴。"
    show dly shengqi with dissolve
    dly "你想被她削吗！"
    "丁灵云压低声音警告道，"
    dly "前几日我师兄无意冲撞到她，最后是被抬回来的。"
    hide dly with dissolve
    show zmz b ganga at pos_zmz with dissolve
    zmz "哇这么凶……"
    "钟明烛缩了缩脖子，"
    zmz "看起来冷冰冰的，怎么脾气那么爆。"
    hide zmz with dissolve
    show dly shengqi with dissolve
    dly "你顶着张话本女主角的脸，不一样是烂脾气！"
    "丁灵云斜了她一眼，而后若有所思道，"
    dly wunai "话说，你不觉得柳师姐和长离仙子有点像吗？"
    "也不知道她什么心态，不喊师叔，非得继续称长离仙子。{p}钟明烛觉得她可能是觉得师叔两个字配不上长离，仙子才够格。"
    hide dly with dissolve
    show zmz b digu at pos_zmz with dissolve
    zmz "才不像。"
    "钟明烛想也不想就摇头。"
    hide zmz with dissolve
    nrr """
    {clear}

        别人看不清楚，她却是知道的，长离是因为淡漠而导致看起来很冷，与其说是冷，不如说是空；

        而柳寒烟的冷则是来自骨子里，散发着危险的气息。

　　而且还带着一股煞气，这才是在杀戮中往前的剑修应当有的样子，长离那般透彻干净反倒是异类。
    """
    show zmz b ganga at pos_zmz with dissolve
    zmz "反正我暂时是不敢往她脚下摔剑的。"
    "她想了想，又补了一句。"
    "发脾气和命相比，还是后者更重要。"
    "最初敢顶撞长离是因为知道顶多被打一顿，可柳寒烟的话，她觉得可能真的会闹出人命。"
    "然后就被丁灵云抓住了关键。"
    play music "sound/bgm/卢小旭 - 鹧鸪天.mp3"
    hide zmz with dissolve
    show dly shengqi with dissolve
    show dly shengqi at wobbly() with dissolve
    dly "什么？"
    "她指着钟明烛的指尖不住颤抖，声音也在抖，"
    dly "你、你竟往长离仙子脚下摔过剑？！"
    "她说着就撩起衣袖，在旁听了许久的风海楼连忙帮她把袖子拉回去。"
    transform wobbly_move(x=5, y=3, t=0.1):
        yalign 1.0
        xcenter 0.5
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
            linear 2.0 xcenter 0.4
    show fhl wunaixiao:
        yalign 1.0
        xcenter 0.3
        linear 2.0 xcenter 0.2
    with dissolve
    show dly shengqi at wobbly_move()
    with Pause(2.0)
    fhl "丁师妹，冷静。"
    dly "是姓钟的不知好歹！"
    show fhl wunaixiao:
        yalign 1.0
        xcenter 0.2
        alpha 1.0
        linear 0.5 xcenter 0.0 alpha 0.0
    with Pause(0.5)
    show dly shengqi:
        yalign 1.0
        xcenter 0.4
        linear 0.5 xcenter 0.5
    with Pause(0.5)
    "丁灵云拍开他，继续撩袖子。"
    show dly shengqi:
        xcenter 0.7
    with dissolve
    show zmz b ganga flip at objpos(x=0.3, y=0.6, z=0.4) with dissolve
    zmz "骗吃骗喝时候亲热地叫人家阿烛，现在就是姓钟的了。"
    "钟明烛不怕死地对她做了个鬼脸，"
    zmz "丁大小姐负心薄幸，我心戚戚啊。"
    show dly shengqi:
        xcenter 0.7
        linear 0.3 xcenter 0.80
    show zmz b ganga flip:
        linear 0.3 xcenter 0.2
    show fhl wunaixiao:
        yalign 1.0
        xcenter 0.5
        alpha 1.0
    with dissolve
    "风海楼当机立断插到两人中间，一手一个，他好歹金丹中期，制服两个筑基修为的绰绰有余。{p}同时庆幸是自己被师父派来照顾这两个修为最弱的师妹。"
    "在师父正在慷慨激昂念诛妖檄文时，下面若是突然有人打起来，他老人家的面子不知要往哪搁。"

    stop music
    scene yunfushan guangchang with dissolve
    nrr """
    {clear}

        这时，钟明烛注意到柳寒烟看了一眼长离。
    """

    show lhy yansu with dissolve
    with Pause(2.5)

    nrr """
    {clear}

        看长离不奇怪，大半弟子的视线都黏在她身上，毕竟那是不足两百年就结成元婴的人，前无古人，就算是长得平平无奇也有大把人争着要看一眼。

        引起她注意的不是柳寒烟看了长离，而是她的眼神。

　　其他弟子在看长离时，就算不喜，也带着一丝敬畏，而柳寒烟那一瞥不含感情，冰冷至极，好似利剑，要将人刺穿。

　　看来这天一宗还有其他不怕师父的人呢。

　　是叫柳寒烟吧，钟明烛意味深长地眯了眯眼，记下了这个名字。
    """

    play music "sound/bgm/剑网3 - 情缘·一见千年.mp3"
    scene yunfushan qiandian with fade
    nrr """
    {clear}

        云逸说完后，便亲手给诸位弟子发了宗主令，这是天一宗弟子以宗门之名外出行事的凭证，凭此令可以利用天一宗设于外界的各种资源，必要时亦能求得其他正道宗门的援护。只有遇到大事需弟子集体出山时才会发放。和自行外出历练相比安全许多，不过也因为需得听从为首前辈调遣的缘故，不怎么自由便利，就算途中偶遇灵宝现世之类福缘也只能忍痛视而不见。

　　宗主令实际上附加于身份玉牒上的一道符，云逸拿出一个匣子，念了几句法诀，便见几十道光自匣中飞出，没入众人的玉牒，钟明烛拿起玉牒一看，发现上面多了一圈暗纹。
    """

    show fhl with dissolve
    fhl "有这个，天一宗在九州四海的产业和盟友都会予以庇护。"
    "风海楼说。"
    zmz "在其他地方还有产业？"
    "钟明烛惊了，她一直以为这种修仙宗门应该和产业之类市侩的词没关系才对。"
    hide fhl with dissolve
    show dly shengqi with dissolve
    dly "不然你以为你每个月的月钱哪来的。"
    "灵云没好气道，很显然她还耿耿于怀钟明烛对长离仙子不敬的事，声音格外冷，"
    dly "天一宗人少，可是金丹以上的修士是所有正道宗门里最多的，还有三个化神期以及一个洞虚期，随便吐纳几下就是一大把灵石，没有海量的灵石灵药根本供不起，普通小门派可是连一个化神期修士都养不起，偶尔出一个，也是撞了天大的好运捡到天大的机缘才得来的。"
    zmz "那邪道呢？有什么门派有很多金丹期以上修士吗？"
    "钟明烛的重点又转到了奇怪的地方。"
    dly wunai "这我也不清楚，云中城是正道的地界。"
    "丁灵云皱了皱眉，"
    dly "听说昆吾城高手众多，不过各自为营也算不了一个门派，哦，我还听说，当世三个洞虚期修士，其中之一是妖修，和昆吾城主交情匪浅，所以云中城才一直拿昆吾没办法，可恶啊，赤金三分之一都是那里产的。"
    "身为正道后人，丁灵云对邪道可谓深恶痛绝。"
    hide dly with dissolve
    show zmz b sikao at pos_zmz_sikao with dissolve
    zmz "昆吾城。"
    "钟明烛却想到了别的。"
    "当年想夺取苍梧剑结果败在四灵诛邪阵下的陆离便是昆吾城二城主，同样想夺苍梧剑的千面偃可能是陆离传人，而此次妖兽作乱之地与昆吾城离得很近。"
    zmz "倒是挺巧。"
    "她喃喃道。"

    scene yunfushan qiandian with fade
    nrr """
    {clear}

        发完宗主令，云逸又给每人发了一千灵石、上品和中品灵药各二十瓶还有救伤药丸若干，这才开启了传送阵。
    """
    image fazhen = SquenceAnimator("images/effect/法阵", interval=0.15, loop=True)
    show fazhen:
        xcenter 0.5
        yalign 1.0
        zoom 3.0
    nrr """
    {clear}

        将这些收入储物戒里，钟明烛感慨第一仙宗果然家大业大。

　　外门弟子时发放的储物囊容量较小，正式拜师后的弟子们做的第一件事通常是给自己买一个储物戒，钟明烛的是长离给她灵石和材料时一并送给她的，好像是当年龙田鲤给的那枚，她在里面找到了不少灵草。

　　为了应付那三场比试，她的储物戒里的东西差不多被掏空了，将得来的灵石灵药放进去后总算充实了点。

{clear}

　　前面的弟子陆续踏入传送阵，已经走了一大半。

　　钟明烛跟上去，发现长离还没离开，正站在阵外看着她。
    """

    show zmz b flip at objpos(x=0.3, y=0.6, z=0.4) with dissolve
    zmz "师父在等我吗？"
    "她立即将囊中羞涩的忧郁抛到脑后，几步跨到长离身边，笑逐颜开拽住她的袖子扯了扯。"
    show cl c at objpos(x=0.7, y=360+100, z=0.38) with dissolve
    show cl c at nod(y=10, t=0.24)
    "长离移开视线，轻轻应了一声。"
    "看得丁灵云恨不得一套流云剑招呼上去，风海楼干笑了两声连忙拉起她走了，他怕再留下丁灵云，两人下一刻就要打起来。"
    "只留钟明烛和长离两人了。"
    zmz b miyanxiao flip "师父，我们走吧。"
    "她笑的时候，眼中好似有火光在跳动。"
    cl "嗯。"
    "两人一起踏入阵中，身影转瞬消失在光中。"
    show white:
        alpha 0.0
        linear 5 alpha 1.0
    with Pause(5.0)
    show credits_text_big "未 完 待 续"
    with Pause(4.0)


    # jump story_15_1
