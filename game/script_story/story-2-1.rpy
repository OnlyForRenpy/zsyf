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

label story_2_1:

    stop music fadeout 2.0
    window hide

    image xiexiu = "images/char/其他/邪修.png"
    define daifu = Character("大夫", image = "daifu", what_size = 28, what_prefix = "『", what_suffix = "』")
    image daifu = "images/char/其他/大夫-正常.png"
    image daifu danxin = "images/char/其他/大夫-担心.png"

    image CG2-1-1 = "images/cg/CG-2-1-1.jpg"

    with Pause(3.0)
    window hide
    with fade

    play music "sound/bgm/吴欣睿 - 寒声碎.mp3"

    scene yangshan a
    with fade
    nrr """
    {clear}

        阳山，正值山雨欲来之时，云层重重压下，几乎要将整座山头吞没。
    """

    # 注意call battle之后要接一个场景转换
    $ is_in_wild = False
    $ p1 = cl_b
    $ p2 = None
    $ p3 = None
    $ fixedset = "boss1"
    call battle from _call_battle_1

    play music "sound/bgm/吴欣睿 - 寒声碎.mp3"
    scene yangshan b
    with fade

    nrr """
    {clear}

        荒僻的谷地里，嶙峋乱石围成奇怪的形状，中心为谷地最低处，五条锁链自石中伸出，缚着一个昏迷不醒的少女，而她头顶原本悬着一个药炉，此时被打翻在地，徐徐流出暗红色的液体。
    """
    show xiexiu
    queue sound ["sound/audio/被剑刺中.wav", "sound/audio/消散.wav"]
    with Shake_screen((0, 0, 0, 0), 0.4, dist=1)
    with Pause(1.0)
    show xiexiu at hide_tb(t=1.0)
    nrr """
    {clear}

一柄狭长的剑斜斜穿刺他胸口，洞穿了心脏以及元婴，身形俱灭。

　　他甚至连吃惊都来不及，魂魄便赴往轮回。
    """

    play sound "sound/audio/刀剑/拔剑.wav"
    nrr """
    {clear}

白衣女子看也没看将长剑收回剑匣，转身便想离开。
    """

    show fhl
    fhl wunaixiao "哎，小师叔！等等！"
    "随侍在女子身后的青衣少年指了指那还被锁链拴着的少女，小心翼翼道，"
    fhl wunaixiao "她还活着。"

    hide fhl with dissolve
    show cl at pos_cl with dissolve
    "女子仅是静静看着他，漆黑的眸子深若千年古潭，看得头皮一阵发麻。"

    hide cl with dissolve
    show fhl with dissolve
    fhl wunaixiao "我、我的意思是……要不小师叔你先送她去镇上医馆，这地方血气太重，我留下清理。"
    "那少年似是有些害怕女子，视线撇向一边不敢对视，声音听起来有些底气不足。"
    show fhl dark
    cl "好。"

    scene yangshan b with ImageDissolve("script_effect/common/rule/left.png", 0.8, 64)
    show zmz kunbang at objpos(y=360+100, z=0.50) with dissolve
    with Pause(1.0)
    play sound "sound/audio/碎裂.wav" volume 0.5
    transform wobbly1(x=5, y=3, t=0.1):
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
        time 0.1
    show zmz kunbang at wobbly1(x=2, y=1, t=0.05)
    with Pause(1.0)
    show zmz kunbang at hide_tb(t=1.0)
    "女子答应下来，下一瞬只听得几声脆响，五条锁链俱断，少女已被她抱入怀中，白影一晃，偌大的空地上便只剩下青衣少年。"
    play sound "sound/audio/移动呼声/布料呼声.mp3"

    scene yangshan b with ImageDissolve("script_effect/common/rule/left.png", 0.8, 64)
    show fhl with dissolve
    fhl wunai1 "好快……"
    "他喃喃道，"

    scene yangwangtiankong with ImageDissolve("script_effect/common/rule/s1.png", 0.8, 64)
    "忽地像是想起了什么一样，对着白衣女子消失的方向喊道，"
    fhl "小师叔！别忘了要用银子！"

    nrr """
    {clear}

他用上了千里传音，但还是不太确定能不能追上那女子，小师叔又是出了名的不爱说话，就算听到了也不会回个话。

{clear}

少年名为风海楼，是天一宗宗主云逸唯一的亲传弟子，而白衣女子，正是当年与千面偃一战成名的长离仙子。

　　当年她虽然重创了千面偃，第二天就因重伤再度闭关，直到前几年才出关，此次下山是奉宗主之名前往逐浪城取一些炼宝器物。

{clear}

　　长离自出生便被抱到天一宗抚养，对凡界一无所知，云逸担心她遇到麻烦，便派风海楼一道。

风海楼本以为师父小题大做，之后才发觉不无道理。

小师叔天赋太高，修为进展太快，竟连凡人要吃饭睡觉都不是很清楚，莫说付账之类了。

{clear}

　　希望小师叔不会惹事啊，风海楼轻轻叹了一口气。
    """

    scene yangshan b with ImageDissolve("script_effect/common/rule/s1.png", 0.8, 64)
    nrr """
    {clear}

    虽然很担心，但还是先清理完眼前的狼藉再说。

　　小师叔长得好看，就算没银子也不会被为难的，他如此安慰自己。

{clear}

三天前他们就办完事，返程路过阳山时察觉到邪气，立即追踪而来，不过还是迟了一步，找到那修士时，他正要对最后一个活着的少女施咒，而其他被掳来的少女都已被抽干血。

　　少女们含着怨气丧命，沾染了邪煞之气，很容易被炼成怨灵，风海楼承风逸擅符咒的衣钵，虽修为尚浅，但净化此地煞气不成问题。

    """

    image bagua = "images/effect/八卦阵.png"
    play sound "sound/audio/施法/发招.wav"
    show bagua:
        xcenter 0.5
        ycenter 0.4
        zoom 1.5
        alpha 0.0
        rotate 180
        ease 1 alpha 0.8
        ease 1 alpha 0.0

    nrr """
    {clear}

    他在五条锁链以及药炉方位贴上三清符，双手结印，口中念念有词，

    地面上以他为中心浮现出一道光纹，不多时，地上的暗血色渐渐淡去，药炉上缭绕的黑气也消失得无影无踪。

    """

    show fhl nanguo with dissolve
    fhl nanguo "入土为安吧。"
    "他轻声对那些无辜丧命的少女说道，目送尸体渐渐沉入土中，待一切结束后才轻轻吐出一口浊气，踏上飞剑往镇子方向赶去。"
    show fhl nanguo at hide_tb(y=-100, t=0.25)

    scene yaofang with fade
    with Pause(1.0)
    show daifu danxin with dissolve
    "循着长离留下的印记快速找到了医馆，进门前他用灵识一探，发现里屋一个大夫正在替那少女把脉，而长离站在床边，给大夫打下手的学徒时不时瞄一眼剑匣，看起来有些心惊胆战的。"
    "至少好好把人送到了，风海楼欣慰地踏进医馆，\n
一进门就看到老板模样的人盯着柜台上一小堆银锭，一脸不知所措。"
    fhl "嘶……"
    "他当即倒抽一口冷气。"
    "整个天下，只有昆吾，云中，九幽，僬侥四城居民全部是修士，其余修士分散各地，要么是在荒山野岭中开宗立派，要么就隐居于凡人中，逐浪城便是修士与凡人混居之地，且又是交易大邦，便是凡人店铺也可能淘到好物，所以到了逐浪后他就给了小师叔一些银两以备不时之需。"
    "他记得当时一共给了二十五锭银元，如今全躺在柜台上。"
    "小师叔啊，我让你记得给银子，没让你全部给啊……{p}
一千二百五十两，纵是风海楼离开凡世几十年，仍是不可避免地感到一阵肉痛。"
    hide daifu danxin with dissolve
    show fhl wunaixiao with dissolve
    "老板，刚刚送来的是我朋友……"
    hide fhl wunaixiao with dissolve
    show daifu danxin with dissolve
    "他一开口，那老板就像被针扎了一样跳起来，结结巴巴道："
    daifu danxin "这位公子，这是那位姑娘放在这的，我可什么都还没说呢！您、要不您收回去吧……"
    "说着他似乎想起那白衣女子身上不可冒犯的凛冽之气，不禁打了个冷战。"
    "他不是不爱财，而是不敢要，能一眼不眨丢出那么多银子的人岂是他一家小小的医馆能招惹的，万一被按上欺诈的名头怕是要吃不了兜着走，而且他着实想不出那白衣女子是从哪拿出这么一堆换算起来估计百来斤的银子。"
    "说起来那姑娘算上背后的剑匣估计也差不多同重。能拿得起这等重量怎么想都不可能是常人。"
    hide daifu danxin with dissolve
    show fhl wunaixiao with dissolve
    fhl wunaixiao "不好意思，我朋友来自关外，不通此地人情风俗，老板莫见怪。"
    "风海楼抱歉地笑了笑。{p}说着便只留了一锭银两在台面，他不敢在这老板面前将那剩余银两收回储物囊，只能用布包了背到身后。"
    fhl wunaixiao "这些老板先收着，药材尽量选上好的，不够便与我说。"
    "比通常所需的诊金高了一截，却又没有高得离谱，老板见了面露喜色，便不去计较之前那些疑惑了。"

    scene yaofang with dissolve
    nrr """
    {clear}

    少女伤得不轻，来时路上长离给她服了一颗丹药，身上的伤已无大碍。

    只是对方是凡人体质，若再服丹药有可能承受不了，所以还是找凡间大夫诊断比较妥当。

    大夫把过脉后说少女只是受了刺激才昏睡不醒，好生修养几天就可以，他这才稍稍安下心。

{clear}

    担心术法留有后遗症，加上不急着赶路，风海楼稍忖度便对长离说想等那少女恢复后再离开。

　　提议的时候兢兢战战的，若问为何会对小师叔如此敬畏，一方面是因为没见过几面，另一方面是因为去年门中试炼由这位小师叔负责。
    """

    scene black with dissolve
    show yy xiao with dissolve
    nrr """
    {clear}

    “师妹她刚出关，不太熟悉新来的弟子，所以下手可能有点没轻没重，哈哈哈……”

    结束后，云逸看着哀鸿遍野的试炼场，干笑着解释。

　　修为压制在金丹中期的长离以及一柄木剑，没让参与试炼的七十八名弟子们撑到三刻钟以后。

　　当时风海楼将平时积攒的灵石全部砸了出来，辛辛苦苦布下了注重防御的玄武阵，打算龟缩一个时辰熬过试炼，没想到长离三剑就挑破阵势。

出来后他躺了三天床才能下地，之后每每见到小师叔就本能地想拔腿就跑。
    """

    scene yaofang with dissolve
    show fhl wunai1 with dissolve
    "同行那么多天后虽不至于像以前见到长离就噤若寒蝉，可终归还是有些心悸的。所以在这节外生枝的环节格外紧张，生怕被呵责。"
    fhl wunaixiao "不如小师叔您先回去？师父在等着那些器具，我把这位姑娘送回家就回去。"
    show fhl wunaixiao dark
    cl "好。"
    "出乎意料的是，长离立刻答应了。"
    "太过平淡的语气让风海楼不禁怀疑，若他提议的是把那个少女丢下，对方也会是同样的回答。"
    play sound "sound/audio/移动呼声/布料呼声.mp3"
    "说完长离片刻都没多留，一眨眼气息已远在风海楼可探范围外。"
    show fhl
    fhl "好快……"
    "他又一次感慨。"
    show fhl dark
    "这时，一声轻微的呢喃传入耳中，他看向床上的少女。"
    "只见对方修长的睫毛颤了颤，缓缓睁开了眼。"

    hide fhl with dissolve
    show zmz toutong at appear_tb(x_c=0.5, y_c=0.9, y_o=50, z=0.6, t=1.0)
    fhl "你醒了！有觉得哪里不舒服吗？要不要再找大夫看看？"
    "他高兴地丢下一连串问题，少女却只是茫然地盯着天花板，苍白的面容上缓缓出现迟疑的神色。"
    zmz toutong "……你是谁……这是哪里？"
    "她扭头看向风海楼，轻声问道，接着又迟疑地说出几个字，让风海楼当即愣住。"
    zmz toutong "我……是谁……"
    show zmz toutong at wobbly(x=2, y=1, t=0.05)
    "状况太突然，风海楼还没反应过来，下一刻却见少女突然尖叫一声坐了起来，双手死死抱住头，浑身不住颤抖，伴随着喉中溢出的破碎话语，呼吸愈发急促，浑身透漏出痛苦感。"

    fhl "气神永安！"
    play sound "sound/audio/施法/发招.wav"
    show bagua:
        xcenter 0.5
        ycenter 0.4
        zoom 1.5
        alpha 0.0
        rotate 180
        parallel:
            ease 1 alpha 0.8
            ease 1 alpha 0.0
        parallel:
            ease 1 zoom 1.8
    "风海楼急忙捻诀，点住那少女眉心，驱走她身上的狂躁惊惶之气。"
    show zmz toutong at hide_tb(y=100, t=1.5)
    with Pause(1.5)

    nrr """
    {clear}

待对方再度沉沉睡去，他试着探入对方记忆，却感受到一股斥力。

　　少女体内竟有一股浑然天成的灵气，这是修士才有的天赋。


　　他没有带测灵石，但已能笃定对方是个绝好的修真苗子。

　　念及那邪修抽干其他少女的血，却独独想在她身上施加术法的做法，风海楼恍然大悟：

　　多半是看上了这少女的根骨。

　　接下来怎么办？

    """

    show CG2-1-1 with tran_lf
    with Pause(2.0)
    nrr """
    {clear}

看向对方安静的睡颜，之前他都没好好打量过少女的模样，

如今一瞧，发现对方五官生得十分精致，便是和以容貌与剑术出名的小师叔相比，也不见得逊色多少。

　　如今门中的师妹们，好像都没有她长得好看呢，他心不在焉地如此想，片刻后忽然惊醒道：

“怎么想这些！”

    """
    play sound "sound/audio/拳击打中.wav" volume 0.25
    with Shake_screen((0, 0, 0, 0), 0.1, dist=4)
    with Pause(1.0)
    hide CG2-1-1 with tran_lf
    nrr """
    {clear}

重重给自己脑门来了一下，

思考片刻，他伸手截了少女身上半截衣袖下来，从储物囊中搬出十几颗灵石摆将那片衣料围住，捻出一道符贴了上去。

    """

    play sound "sound/audio/施法/发招.wav"
    show white:
        alpha 0.0
        easein 1.0 alpha 0.7
        easein 1.0 alpha 0.0
    nrr """
    {clear}

此乃追踪之阵，不多时便有一缕白雾自那片衣料中升起，往北方飘去，他见状立刻追了上去。

    """

    play sound "sound/audio/移动呼声/布料呼声.mp3"

    scene feiqi with tran_df
    nrr """
    {clear}

白雾所去之地就在临镇，风海楼抵达后，入目却是触目惊心的惨状。

　　偌大的府邸已是一片焦墟，官府在外贴了封条，但还没来得及清理里面，起居室的墙上还残留着干涸的血迹。

　　在废墟中转了几圈，最后在镇宅的方位布置下法阵，启动便见阵中浮现出模糊的影子，还原了当日的情景，那邪修竟是将除了少女之外的人全部杀了，临走前还放了一把火。

    """
    window hide

    scene yuanzi with fade
    with Pause(0.5)
    show zml with dissolve
    with Pause(1.0)
    nrr """
    {clear}

天明后，风海楼去了离这最近的宅子。

　　接待他的是个文士打扮的年轻男子，听到他询问有关那座府邸的事，当即吓得脸色发白，匆匆将自己所知的告诉他后便像送瘟神一样把他送出门。

　　太过惨绝人寰，寻常人谁也不愿意与之有所牵扯。

    """

    scene xiaozhen with fade
    with Pause(1.0)
    nrr """
    {clear}

十几天后，风海楼回到云浮山，却不是一个人，而是将那个少女也带了过去，他将对方安置在山脚一个镇子里，道：

　　“一个月后便是山门开放之时，以姑娘的资质，定能穿过参道，后会有期。”

　　说罢便御剑离去，身影化为一道光消失在天际。

    """

    window hide
    show zmz sikao at pos_zmz_sikao with dissolve
    with Pause(1.0)
    "少女低下头，展开手心被揉成一团的纸，比常人颜色略浅的眼眸中浮出一丝迷茫。{p}
纸上工工整整写着三个字：钟明烛。{p}
这是她的名字，是风海楼自那年轻文士口中打探来的——姓名生辰涉及人之本源，便是法力通天的修士也无法推测出来。"
    "如今，这三个字便是她与过去唯一的关联了。"


    jump story_3_1
