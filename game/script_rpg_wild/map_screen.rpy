


screen map_screen(aMap):

    add "#000"

    $ offset_x = 640 - (80 * aMap.center_x) - 40
    $ offset_y = 360 - (80 * aMap.center_y) - 80
    add aMap.img:
        pos(offset_x, offset_y)

    for i in range (len(aMap.map)):
        $ row = aMap.map[i]
        for j in range(len(row)):
            $ tile = row[j]
            # 如果被占用了(人物或其他物品)
            if not tile.occupant is None and isinstance(tile.occupant, MapDenizen):
                $ offx, offy = tile.occupant.getOffset()    # occupant的坐标
                $ tile_lc_x = 80 * j + offset_x         # 应该显示到屏幕的坐标
                $ tile_lc_y = 80 * i + offset_y
                add tile.occupant.img:
                    pos(tile_lc_x + offx, tile_lc_y + offy)
    key "K_UP" action [Function(aMap.moveDenizen, current_char.x, current_char.y, 0, -1), SetVariable("k_dir", "up"), SetVariable("m_status", "walk")]
    key "keyup_K_UP" action [Function(aMap.moveDenizen, current_char.x, current_char.y, 0, 0), SetVariable("k_dir", "up"), SetVariable("m_status", "stand")]
    key "repeat_K_UP" action [Function(aMap.moveDenizen, current_char.x, current_char.y, 0, -1), SetVariable("k_dir", "up"), SetVariable("m_status", "walk")]
    key "K_DOWN" action [Function(aMap.moveDenizen, current_char.x, current_char.y, 0, 1), SetVariable("k_dir", "down"), SetVariable("m_status", "walk")]
    key "keyup_K_DOWN" action [Function(aMap.moveDenizen, current_char.x, current_char.y, 0, 0), SetVariable("k_dir", "down"), SetVariable("m_status", "stand")]
    key "repeat_K_DOWN" action [Function(aMap.moveDenizen, current_char.x, current_char.y, 0, 1), SetVariable("k_dir", "down"), SetVariable("m_status", "walk")]
    key "K_LEFT" action [Function(aMap.moveDenizen, current_char.x, current_char.y, -1, 0), SetVariable("k_dir", "left"), SetVariable("m_status", "walk")]
    key "keyup_K_LEFT" action [Function(aMap.moveDenizen, current_char.x, current_char.y, 0, 0), SetVariable("k_dir", "left"), SetVariable("m_status", "stand")]
    key "repeat_K_LEFT" action [Function(aMap.moveDenizen, current_char.x, current_char.y, -1, 0), SetVariable("k_dir", "left"), SetVariable("m_status", "walk")]
    key "K_RIGHT" action [Function(aMap.moveDenizen, current_char.x, current_char.y, 1, 0), SetVariable("k_dir", "right"), SetVariable("m_status", "walk")]
    key "keyup_K_RIGHT" action [Function(aMap.moveDenizen, current_char.x, current_char.y, 0, 0), SetVariable("k_dir", "right"), SetVariable("m_status", "stand")]
    key "repeat_K_RIGHT" action [Function(aMap.moveDenizen, current_char.x, current_char.y, 1, 0), SetVariable("k_dir", "right"), SetVariable("m_status", "walk")]
    key "K_RETURN" action Function(mikaInteracts)


default sprite1 = "mika"
default sprite1_walk = "k_walk"
default sprite1_x = 6
default sprite1_y = 6
