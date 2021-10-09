# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
define cl = Character("长离", image = "cl", what_size = 28, what_prefix = "『", what_suffix = "』")
image cl = "images/char/长离/长离-普通.png"
image cl dark = im.MatrixColor(
    "images/char/长离/长离-普通.png",
    im.matrix.tint(0.5, 0.5, 0.5)
)
image cl kunhuo = "images/char/长离/长离-困惑.png"
image cl kunhuo dark = im.MatrixColor(
    "images/char/长离/长离-困惑.png",
    im.matrix.tint(0.5, 0.5, 0.5)
)
image cl dazuo = "images/char/长离/长离-打坐-普通.png"
image cl dazuo dark = im.MatrixColor(
    "images/char/长离/长离-打坐-普通.png",
    im.matrix.tint(0.5, 0.5, 0.5)
)
image cl dazuo biyan = "images/char/长离/长离-打坐-普通闭眼.png"
image cl dazuo biyan dark = im.MatrixColor(
    "images/char/长离/长离-打坐-普通闭眼.png",
    im.matrix.tint(0.5, 0.5, 0.5)
)
image cl dazuo biyan tongku = "images/char/长离/长离-打坐-痛苦闭眼.png"
image cl dazuo biyan tongku dark = "dark:cl dazuo3"
image cl zhijian = "images/char/长离/长离-执剑-普通.png"
image cl zhijian dark = "dark:cl zhijian"
image cl zhijian fennu= "images/char/长离/长离-执剑-愤怒.png"
image cl zhijian fennu dark = "dark:cl zhijian fennu"
image cl zhijian blood= "images/char/长离/长离-执剑-普通-血.png"
image cl zhijian blood dark = "dark:cl zhijian blood"
image cl yingzhan= "images/char/长离/长离-迎战.png"
image cl yingzhan dark = "dark:cl yingzhan"
image cl yingzhan blood= "images/char/长离/长离-迎战-血.png"
image cl yingzhan blood dark = "dark:cl yingzhan blood"

define zmz = Character("钟明烛", image = "zmz", what_size = 28, what_prefix = "『", what_suffix = "』")
image zmz = "images/char/钟明烛/钟明烛1-普通.png"
image zmz kunbang = "images/char/钟明烛/钟明烛1-捆绑.png"
image zmz toutong = "images/char/钟明烛/钟明烛1-头痛.png"
image zmz sikao = "images/char/钟明烛/钟明烛1-思考.png"
image zmz sikao dark = im.MatrixColor(
    "images/char/钟明烛/钟明烛1-思考.png",
    im.matrix.tint(0.5, 0.5, 0.5)
)
image zmz chijing = "images/char/钟明烛/钟明烛1-吃惊.png"
image zmz xieyanxiao = "images/char/钟明烛/钟明烛1-斜眼笑.png"
image zmz miyanxiao = "images/char/钟明烛/钟明烛1-眯眼笑.png"
image zmz digu = "images/char/钟明烛/钟明烛1-嘀咕.png"
image zmz xiee = "images/char/钟明烛/钟明烛1-邪恶.png"
image zmz wugu = "images/char/钟明烛/钟明烛1-无辜.png"
image zmz ganga = "images/char/钟明烛/钟明烛1-尴尬.png"
image zmz shengqi = "images/char/钟明烛/钟明烛1-生气.png"
image zmz limaoweixiao = "images/char/钟明烛/钟明烛1-礼貌微笑.png"
image zmz tanqi = "images/char/钟明烛/钟明烛1-叹气.png"
image zmz shengqixiao = "images/char/钟明烛/钟明烛1-生气笑.png"

image zmz b = "images/char/钟明烛/钟明烛2-普通.png"
image zmz b flip = im.Flip("images/char/钟明烛/钟明烛2-普通.png", horizontal=True)
image zmz b chijing = "images/char/钟明烛/钟明烛2-吃惊.png"
image zmz b shengqi = "images/char/钟明烛/钟明烛2-生气.png"
image zmz b miyanxiao = "images/char/钟明烛/钟明烛2-眯眼笑.png"
image zmz b sikao = "images/char/钟明烛/钟明烛2-思考.png"
image zmz b sikao dark = im.MatrixColor(
    "images/char/钟明烛/钟明烛2-思考.png",
    im.matrix.tint(0.5, 0.5, 0.5)
)
image zmz b ganga = "images/char/钟明烛/钟明烛2-尴尬.png"
image zmz b xiaqi = "images/char/钟明烛/钟明烛2-下棋.png"
image zmz b tanqi = "images/char/钟明烛/钟明烛2-叹气.png"

define yy = Character("云逸", image = "yy", what_size = 28, what_prefix = "『", what_suffix = "』")
image yy = "images/char/其他/云逸-普通.png"
image yy dark = im.MatrixColor(
    "images/char/其他/云逸-普通.png",
    im.matrix.tint(0.5, 0.5, 0.5)
)
image yy xiao = "images/char/其他/云逸-笑.png"
image yy biyan = "images/char/其他/云逸-闭眼.png"
image yy chensi = "images/char/其他/云逸-沉思.png"
image yy fennu = "images/char/其他/云逸-愤怒.png"

define fhl = Character("风海楼", image = "fhl", what_size = 28, what_prefix = "『", what_suffix = "』")
image fhl = "images/char/其他/风海楼-正常.png"
image fhl dark= im.MatrixColor(
    "images/char/其他/风海楼-正常.png",
    im.matrix.tint(0.5, 0.5, 0.5)
)
image fhl fennu = "images/char/其他/风海楼-生气.png"
image fhl nanguo = "images/char/其他/风海楼-难过.png"
image fhl wunaixiao = "images/char/其他/风海楼-无奈笑.png"
image fhl wunaixiao dark = im.MatrixColor(
    "images/char/其他/风海楼-无奈笑.png",
    im.matrix.tint(0.5, 0.5, 0.5)
)
image fhl wunai1 = "images/char/其他/风海楼-无奈1.png"
image fhl wunai2 = "images/char/其他/风海楼-无奈2.png"

define zml = Character("竹茂林", image = "zml", what_size = 28, what_prefix = "『", what_suffix = "』")
image zml = "images/char/其他/竹茂林-正常.png"

define dly = Character("丁灵云", image = "dly", what_size = 28, what_prefix = "『", what_suffix = "』")
image dly = "images/char/其他/丁灵云-普通.png"
image dly dark = im.MatrixColor(
    "images/char/其他/丁灵云-普通.png",
    im.matrix.tint(0.5, 0.5, 0.5)
)
image dly shengqi = "images/char/其他/丁灵云-生气.png"
image dly wunai = "images/char/其他/丁灵云-无奈.png"
image dly lianhong= "images/char/其他/丁灵云脸红.png"

define ltl = Character("龙田鲤", image = "ltl", what_size = 28, what_prefix = "『", what_suffix = "』")
image ltl = "images/char/其他/龙田鲤.png"

define mdx = Character("木丹心", image = "mdx", what_size = 28, what_prefix = "『", what_suffix = "』")
image mdx = "images/char/其他/木丹心.png"

define qmy = Character("千面偃", image = "qmy", what_size = 28, what_prefix = "『", what_suffix = "』")
image qmy = "images/char/其他/千面-正常.png"
image qmy fennu = "images/char/其他/千面-愤怒.png"
image qmy yinchen = "images/char/其他/千面-阴沉.png"
image qmy jianxiao1 = "images/char/其他/千面-奸笑.png"
image qmy jiaoxiao2 = "images/char/其他/千面-奸笑2.png"

define nsc = Character("南司楚", image = "nsc", what_size = 28, what_prefix = "『", what_suffix = "』")
image nsc = "images/char/其他/南司楚-普通.png"
image nsc fennu = "images/char/其他/南司楚-愤怒.png"

define wh = Character("吴回", image = "wh", what_size = 30, what_color = "#000", what_prefix = "『", what_suffix = "』")
