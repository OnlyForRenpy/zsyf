default k_dir = "down"
default m_status = "stand"

image char1_walk = ConditionSwitch(
    "m_status == 'walk' and k_dir == 'down'", renpy.easy_displayable("char1 walk down"),
    "m_status == 'walk' and k_dir == 'up'", renpy.easy_displayable("char1 walk up"),
    "m_status == 'walk' and k_dir == 'left'", renpy.easy_displayable("char1 walk left"),
    "m_status == 'walk' and k_dir == 'right'", renpy.easy_displayable("char1 walk right"),
    "m_status == 'stand' and k_dir == 'down'", renpy.easy_displayable("char1 stand down"),
    "m_status == 'stand' and k_dir == 'up'", renpy.easy_displayable("char1 stand up"),
    "m_status == 'stand' and k_dir == 'left'", renpy.easy_displayable("char1 stand left"),
    "m_status == 'stand' and k_dir == 'right'", renpy.easy_displayable("char1 stand right"),
    predict_all = True)

# image mika = "mika [k_dir]"

# define k_offset = -56

init python:
    def getFacingTile():
        if k_dir == "up":
            return (char1.x, char1.y + 1)
        elif k_dir == "down":
            return (char1.x, char1.y - 1)
        elif k_dir == "left":
            return (char1.x - 1, char1.y)
        else:
            return (char1.x + 1, char1.y)

    def mikaInteracts():
        x, y = getFacingTile()
        mika_sprite.map.triggerInteraction(x,y)

image char1 stand down = SquenceAnimator("images/rpg_wild/char_move", prefix="qks_down_00", suffix="png", begin_index=1, end_index=2, interval=0.5, loop=True)
image char1 stand left = SquenceAnimator("images/rpg_wild/char_move", prefix="qks_left_00", suffix="png", begin_index=1, end_index=2, interval=0.5, loop=True)
image char1 stand right = SquenceAnimator("images/rpg_wild/char_move", prefix="qks_right_00", suffix="png", begin_index=1, end_index=2, interval=0.5, loop=True)
image char1 stand up = SquenceAnimator("images/rpg_wild/char_move", prefix="qks_up_00", suffix="png", begin_index=1, end_index=2, interval=0.5, loop=True)
# image mika stand:
#     "images/rpg_wild/char_move/qks_[k_dir]_001.png"
# image mika walk = SquenceAnimator("images/rpg_wild/char_move", prefix="qk_[k_dir]_00", suffix="png", begin_index=1, end_index=8, interval=0.1, loop=True)
image char1 walk down = SquenceAnimator("images/rpg_wild/char_move", prefix="qk_down_00", suffix="png", begin_index=1, end_index=8, interval=0.1, loop=True)
image char1 walk left = SquenceAnimator("images/rpg_wild/char_move", prefix="qk_left_00", suffix="png", begin_index=1, end_index=8, interval=0.1, loop=True)
image char1 walk right = SquenceAnimator("images/rpg_wild/char_move", prefix="qk_right_00", suffix="png", begin_index=1, end_index=8, interval=0.1, loop=True)
image char1 walk up = SquenceAnimator("images/rpg_wild/char_move", prefix="qk_up_00", suffix="png", begin_index=1, end_index=8, interval=0.1, loop=True)

image mon1 = "images/battle/monsters/9.png"
