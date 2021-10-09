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

label story_12_1:

    stop music
    window hide
    scene black with fade
    with Pause(1.0)
    scene yunfushan quanjing with fade
    play music "sound/bgm/剑网3 - 情缘·一见千年.mp3"

    nrr """
    {clear}

        自山脚看，云浮山不过长数百里，即地处平原之地，也算不得什么名山。

　　名为“云浮”，只是因为山中多雾，似浮云缭绕。

　　山上无庙宇，无宗祠，山下居民欲入山打猎采摘，往往都会止步于山腰，再往前便是山道奇诡，雾气蔽日，难以辨明方向，极易走失。外来有求索者入山，返者仅五成。

　　有人道山中有仙人，也有人道那哪里是仙人，分明是妖，食人精魄。

　　天一宗山门百年一开，人间已过三世，传下的也只有些无稽之谈。

{clear}

又有哪个凡人能想到，他们眼中的小山丘，实则延绵数千里，拥峰峦无数，云海之上还盘踞着今世第一大仙宗。

　　自山道起雾开始，就已经进入护山大阵范围了。

　　无仙根，或者心怀叵测者，就算在山道上徘徊一辈子，都无法到达山门前。
    """

    scene tiankong b with fade
    show zmz b xiaqi at pos_zmz_xiaqi with dissolve
    "钟明烛盘腿坐在飞剑上，飞剑放大了数倍，还垫了个蒲团，是以久坐也不会嫌不舒服，她手里抱着一大罐蜜渍果脯，嘴里叼着一片，眼睛却专注地望着眼前飘浮着的空白画卷，眉头微蹙，不时扬手，将几点辉光打入画卷中。"
    image juanzhoubi = "images/obj/卷轴闭.png"
    image juanzhoukai = "images/obj/卷轴开.png"
    window hide
    show juanzhoubi:
        xcenter 0.5
        ycenter 0.5
        zoom 0.6
    with dissolve
    with Pause(1.0)
    hide juanzhoubi with dissolve
    play sound "sound/audio/纸张摇动.mp3"
    show juanzhoukai:
        xcenter 0.5
        ycenter 0.5
        zoom 0.6
    with dissolve
    with Pause(1.0)

    "那其实并非空白画卷，若用灵识探寻，便可发现上面已经布满了光点，颜色不一，细小的纹理在其中慢慢流淌，因为太多了，乍一看显得杂乱无章。"
    hide juanzhoukai with dissolve
    show zmz b xiaqi:
        xoffset 0
        linear 1.0 xoffset -200
    show dly:
        yalign 1.0
        xoffset 1280
        linear 1.0 xoffset 680
    dly "阿烛，你在做什么？"
    "丁灵云说着毫不客气地在她身边坐下，捏了片果脯，往画卷上那浩瀚星辰似的光点上瞄了一眼，顿时觉得一阵眼花缭乱。"
    "她的脸不像当年那么圆了，下巴尖尖的，退去了小孩子的稚气，不过眼睛还保留有当初的可爱。"
    "她如今是回廊峰主卢忘尘的亲传弟子，回廊峰为术法一脉，丁灵云的五行之法已有小成，筑基后期，被认为是新一代弟子中仅次于风海楼的人物。"
    nrr """
    {clear}

    当年钟明烛被长离挑走，又三个月不见踪影，丁灵云觉得自己的友情被背叛，一度想将她从自己好友名单上除名，再见面，已经是大半年后。

        先是听她绘声绘色讲了被长离困在天台峰整整三个月的悲惨遭遇，又听她讲了长离收她为弟子的原委，最后从她那拿到了几套“长离仙子亲赐的剑谱”，两人即刻冰释前嫌。

        丁灵云还告诉她，南司楚回了老家，临走前发誓有朝一日要将钟明烛挫骨扬灰。对此钟明烛只懒洋洋摊手，然后嘿嘿一笑，道：“我师父是长离仙子，他敢吗？”

　　看得丁灵云差点又想揍她了，最后看在那几套剑谱的份上放过了她。

长离的剑谱皆是自吴回长老那得来，其他几峰没有复本，修士施法，以法器为媒介，她的法器则是剑，学了那几套剑法后无异于如虎添翼。

作为交换，她偶尔会在钟明烛炼阵时施以援手。
    """
    zmz "杀手锏！"
    play sound "sound/audio/纸张摇动.mp3"
    "钟明烛点了画卷一下，将其收了起来，"
    show zmz b flip at objpos(x=0.4, y=0.6, z=0.4) with dissolve
    zmz "啊说起来太麻烦了，到时候你就知道了！"
    dly "那你多小心，这次有一百五十多人参加呢，其中有七十多金丹修为的。"
    play sound "sound/audio/移动呼声/布料呼声.mp3"
    show dly at nod(y=5, t=0.1)
    play sound "sound/audio/移动呼声/布料呼声.mp3"
    with Pause(0.3)
    show dly at nod(y=5, t=0.1)
    "丁灵云抿了抿嘴，吃完那片果脯后又瞄上了罐子里剩下的，也不和钟明烛客气，伸手就去拿，一边还要落数她，"
    dly wunai "唉，若你能得长离仙子真传就万无一失了，筑基期的剑修可与金丹期的其他修士持平，长离仙子的话，大概筑基初就能对战金丹末期了。"
    "一天不夸我师父会死吗？"
    zmz b tanqi "走了走了，比斗不要让我遇到你。"
    show zmz b with dissolve
    "钟明烛冷哼了一声，将手里的罐子丢给丁灵云，踏着飞剑就回天台峰了。"
    play sound "sound/audio/移动呼声/咻.wav"
    show zmz b at hide_tb(y=-100)
    with Pause(1.5)
    show dly at nod(y=5, t=0.1)
    with Pause(0.3)
    show dly at nod(y=5, t=0.1)
    "丁灵云一脸满意将那罐果脯收了起来。"
    "同为外门弟子的时期，她有幸尝过钟明烛的手艺，这么一大罐，赚了。"

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
