
default eventrunning = False
default _game_menu_screen = "preferences"
# init python:
#     if not renpy.variant("touch"):
#         config.mouse = {"default":[ ("images/cursor.png", 1, 1) ] }

label load_setup:
    # $ qiliaoshu.addSkill(a) # add new skills
    # $ zhenyuanhuti.addSkill(c)
    # $ magicswap.addSkill(y)
    call load_monsters from _call_load_monsters
    call load_items from _call_load_items
    $ party_list = [zmz_b, cl_b, a, y, c, f, r] # initial party list, including main character
    # 初始化所有小怪
    $ wild_monsters = [mon1,mon2,mon3,mon4,mon5,mon6,mon7,mon8,mon9,mon10]
    $ restorehp()
    $ restoremp()
    $ battle_players = []
    return
