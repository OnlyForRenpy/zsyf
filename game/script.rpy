# 游戏的脚本可置于此文件中。

# 全局设置
define config.say_attribute_transition = dissolve
define nrr = nvl_narrator  # 旁白用NVL模式，即大对话框

# 开始脚本
label start:
    jump story_12_1
