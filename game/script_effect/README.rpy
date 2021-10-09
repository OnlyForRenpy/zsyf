#### 1、基础角色动画
## 使用 at + 动画函数名称

# 个人使用习惯，x用xcenter，y看情况用yalign或ycenter

########### 出现效果 ####################
# 扩张出现在中央：at appear_center_extend
# x_c=xcenter, y_a=yalign, z=zoom, t=time

# 溶解出现在中央(靠近效果，上下)：at app_tb 或 appear_tb
# y_c=ycenter
# 溶解出现多个人(靠近效果，上下, 主要是方便排位置，不推荐使用，建议直接使用app_tb调参数)：at app_tb21、at app_tb22 等

# 溶解出现在中央(靠近效果，右左)：at app_rl 或 appear_rl
# y_c=ycenter
# 溶解出现多个人(靠近效果，右左, 主要是方便排位置，不推荐使用，建议直接使用app_rl调参数)：at app_rl21、at app_rl22 等


########### 移动效果 ####################
# 走路效果 walk
# x_c_b——开始位置, x_c_e——结束位置, y_c, y_o——走路颠簸幅度, z, t

# 上下移动，可模拟蹲下 at move_down
# y——yoffset，正为向下，负为向上, t

# 左右移动 at move_right
# x——xoffset，正为向右，负为向左, t

# 重复性上下移动，可模拟点头和跳跃 at nod
# y——yoffset，正为向点头，负为跳跃

# 重复性左右移动，可模拟摇头 at shake_head
# x——xoffset, t

# 重复性左右移动(repeat)， at shake_head_r
# x——xoffset, t

# 重复性上下移动(repeat)， at nod_r
# y——yoffset, t


########### 隐藏效果 ####################
# 放大隐藏并略向上移动 at hide_extend
# z, y——yoffset

# 从右侧溶解隐藏,注意zoom要对应 at hide_rl,上下是 hide_tb
# x=100，t=0.25 正向右，负向左


########### 表情效果 ####################
## 使用 show
# 疑问 show why_icon
# 汗 show sweat_icon
# 混乱 show dizzy_icon
# 慌张 show panic_icon
# 惊讶 show amazing_icon
# 高兴 show happy_icon
# 愤怒 show angry_icon
# 生气 show show_sign
# 微妙 show subtle_icon
# 哼歌 show munote11


########### 其他动画 ####################
## 使用 at + 动画函数名称
# 闪烁 flicker
# 较慢较浅的闪烁 layerflicker
# 立绘摇晃 wobbly
# x=5, y=3, t=0.1,摇动范围和快慢
# 立绘摇晃上升 wobbly_stand
# x=5, y=3, y_c_b=0.8, y_c_e=0.65, t=0.1, tmove=2.5摇动范围和快慢，起止位置。如果站起来后还需继续摇晃，可把最后一句 time 2.5 删掉

########### 场景转换 ####################
## 使用 with + 动画函数名称
# 第二个参数是时间
# close_eyes 闭眼
# open_eyes 睁眼
# push_left 左侧推出
# push_up 上侧推出
# clockwise 顺时针
# anticlockwise 逆时针
# close 扩张
# tran_close 扩张变黑再扩张到新场景
# tran_clockwise 顺时针变黑再顺时针到新场景
# tran_lf、tran_rf、tran_uf、tran_df 从左、右、上、下侧溶解
# tran_water、tran_light、tran_fog、tran_fast、tran_updown 几种转场效果

#### 5、图像
## 使用 show
# black 黑色
# white 白色
# red 红色
# movietext 电影效果
# snow_white 白色雪花
# snow_yellow 黄色光斑
# snow_blood 红色飚血
# blood 血
# blood_thorn、blood_boom、blood_shed 几种血效果
# noise 雪花屏
# linework 集中线
# fastwork 速度线

#### 6、特殊文本
## 使用 show + 效果 + 文本
# credits_text 中间文本
# credits_text_up 中间文本偏上
# credits_text_down 中间文本偏下
# credits_text_big 中间大文本



#### 7、其他音轨
# 音效 second_sound、third_sound
# 音乐 second_music、third_music

#### 8、获得时间
# getTime()

### 禁止选项回滚
# define config.rollback_enabled = False

### 强制自动存档
# $ renpy.force_autosave()

### 让Ren’Py重启，将用户带会到主菜单。
# $ renpy.full_restart(transition=False, label='_invoke_main_menu', target='_main_menu')

### 返回一个(x, y)元组，表示鼠标指针或当前触摸位置的坐标。
# $ renpy.get_mouse_pos()

### 返回物理窗口的尺寸。
# $ renpy.get_physical_size()

### 让Ren’Py暂停
# $ renpy.pause()
