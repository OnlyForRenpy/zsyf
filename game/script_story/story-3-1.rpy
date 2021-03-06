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

label story_3_1:

    image effect 3-1-1 = "images/effect/施法.png"

    stop music fadeout 2.0
    window hide
    scene black with fade
    with Pause(3.0)

    play sound "sound/audio/环境/鸟叫2.wav" volume 3.0 loop
    scene shangshan a with fade

    nrr """
    {clear}

        大半个月后，钟明烛踏上风海楼临别前指示的方向。

　　“姑娘可愿与我一道回去，修炼以踏仙途？”

　　当对方这么问的时候，她第一反应是遇到了骗子，可很快就在对方挥手招出飞剑的举动下打消了这个念头。

　　事已至此，她还有什么退路呢？

{clear}

　　自称风海楼的少年说她大抵是受到术法影响，是以失去了记忆。

　　最初尚有些许惊惶不安，很快她便冷静地接受了目前的处境，甚至可以说冷静过了头，丝毫没有身为失忆孤女该有的紧张感，脾气似乎也不算好。

　　在等候山门开启的日子里，她整日在镇上游荡，见到什么有趣的都要上去凑个热闹，放肆张扬，甚至用胡椒水对她心怀不轨的登徒子整治一番。

　　大抵是本性使然吧?听风海楼说自己本是大户千金，兴许因为见识开阔所以比常人多了一份胆识气度，这样安慰着多次，便连最后一丝不自在也消失了。

　　她不知道登上云浮山需要多久，镇子里的居民也说不上所以然，有人说三天，有人说三十天，风海楼说过这山道是第一道考验，有仙缘的人才能抵达山门。得不到所需的确切时间，她便胡乱定了个日子就发出了

——赶在那被她整治的恶少回来报复之前。
    """

    # 注意call show_wild_map之后不要接内容，直接指定story_jump_to（renpy的逻辑没搞清楚）
    $ is_in_wild = True
    $ p1 = zmz_b    # 这个地图的战斗人员
    $ p2 = None
    $ p3 = None
    $ current_char = char1_dz
    $ current_map = map_forest1
    $ story_jump_to = "story_3_2"
    $ init_map(7, 3)
    call show_wild_map from _call_show_wild_map
