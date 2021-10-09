define tile_size = 80
# map: 3000 X 2000 pix, 37.5 X 25 grid
define story_jump_to = ""
define current_char = None
define current_map = None
define current_dx = 0
define current_dy = 0
define is_in_wild = False

init python:


    class TestMap:
        def __init__(self, img, grid_x, grid_y, start_x=0, start_y=0):
            self.img = img
            self.grid_x = grid_x
            self.grid_y = grid_y
            self.center_x = start_x
            self.center_y = start_y

        def set_map_grid(self, map_grid):
            self.map = map_grid

        def isEmpty(self, x, y):
            return self.map[y][x].occupant is None

        def occupy(self, x, y, denizen):
            if not self.isEmpty(x, y):
                return
            self.map[y][x].occupant = denizen
            denizen.x = x
            denizen.y = y
            denizen.map = self

        def unoccupy(self, x, y):
            self.map[y][x].occupant = None

        def overlayimg(self, image):
            self.image = image

        # 人物移动时背景地图移动，人物固定在中央不动。还有一种方式是背景不动人物移动
        def moveDenizen(self, x, y, offx, offy):    # x, y, offx, offy表示格网数
            if self.isEmpty(x,y):
                return
            if x + offx >= len(self.map[0]) or x + offx < 0:    # 移动距离大于map的范围，直接返回
                return
            if y + offy >= len(self.map) or y + offy < 0:
                return
            if not self.isEmpty(x + offx, y + offy):
                if self.map[y + offy][x + offx].occupant.name == "wall":     # 如果目的地是墙，直接返回（走不动）
                    return
                elif self.map[y + offy][x + offx].occupant.name == "exit":  # 如果目的地是出口，jump到对应的故事剧本
                    renpy.hide_screen("map_screen")
                    renpy.jump(story_jump_to)
                # elif self.map[y + offy][x + offx].occupant.name == "exit2":  # 如果目的地是出口，jump到对应的故事剧本
                #     init_map(11, 8)
                #     renpy.call("show_wild_map")
                elif self.map[y + offy][x + offx].occupant.name == "monster":
                    fixedset = None
                    # is_in_wild = True
                    renpy.hide_screen("map_screen")
                    self.map[y + offy][x + offx].occupant.alive = False
                    current_dx = x + offx
                    current_dy = y + offy
                    init_map(current_dx, current_dy)
                    renpy.call("battle")
                    # init_map(11, 8)
                    # renpy.call("show_wild_map")
                else:
                    return

            denizen = self.map[y][x].occupant
            self.map[y][x].occupant = None
            self.map[y + offy][x + offx].occupant = denizen
            denizen.x += offx
            denizen.y += offy

            if denizen.x > 8 and denizen.x < self.grid_y - 8:
                self.center_x = denizen.x   # 地图跟着一起移动

            if denizen.y > 3 and denizen.y < self.grid_x - 6:
                self.center_y = denizen.y


        def triggerInteraction(self, x, y):
            if x < 0 or x >= len (self.map[0]):
                return
            if y < 0 or y >= len(self.map):
                return
            if self.isEmpty(x,y):
                return
            self.map[y][x].occupant.interact()




    class MapTile:
            def __init__(self, occupant=None):
                self.occupant = occupant


    class MapOccupant:
        def __init__(self, x, y, name="", map=None):
            self.x = x
            self.y = y
            self.name = name
            self.map = map

        def interact(self):
            pass

        def unoccupy(self):
            if self.map:
                self.map.unoccupy(self.x, self.y)
                self.map = None



    class MapDenizen(MapOccupant):
        def __init__(self, x, y, img, width, height, name="", alive=True, interaction=None):
            super(MapDenizen, self).__init__(x,y)
            self.img = img
            self.width = width
            self.height = height
            self.name = name
            self.alive = alive
            self.interaction = interaction

        def getOffset(self):
            return(tile_size - self.width / 2, tile_size - self.height / 2)

        def interact(self):
            self.interaction(self)

    # 人物
    char1_dz = MapDenizen(0, 0, "char1_walk", 100, 168, name="player", interaction=no_op)
    # 怪物
    mon1_wild = MapDenizen(0, 0, "mon1", 192, 192, name="monster")
    # 方格类型定义
    wall = MapOccupant(0, 0, "wall")
    exit = MapOccupant(0, 0, "exit")
    # exit2 = MapOccupant(0, 0, "exit2")

    map_forest1 = TestMap("images/rpg_wild/map_forest.jpg", 26, 38)




    def init_map(char_x, char_y):
        grid_map = []
        for i in range(map_forest1.grid_x):
            new_row = []
            for j in range(map_forest1.grid_y):
               new_row.append(MapTile())
            grid_map.append(new_row)
        map_forest1.set_map_grid(grid_map)

        map_forest1.occupy(0, 0, wall)
        for uw in range(37):
            map_forest1.occupy(uw, 1, wall)  #up wall
        for lw in range(25):
            map_forest1.occupy(0, lw, wall)  #left wall
        for rw in range(25):
            map_forest1.occupy(37, rw, wall) #right wall
        for dw in range(37):
            map_forest1.occupy(dw, 23, wall)   #down wall
        for dw in range(4, 37):
            map_forest1.occupy(dw, 22, wall)
        map_forest1.occupy(4, 2, wall)
        map_forest1.occupy(3, 2, wall)
        map_forest1.occupy(2, 3, wall)
        map_forest1.occupy(1, 4, wall)
        for i in range(6):
            map_forest1.occupy(1+i, 5+i, wall)
        map_forest1.occupy(6, 11, wall)
        for i in range(4):
            map_forest1.occupy(6-i, 12+i, wall)
        for i in range(3):
            map_forest1.occupy(3, 16+i, wall)
        for i in range(4):
            map_forest1.occupy(3-i, 19+i, wall)
        map_forest1.occupy(9, 13, wall)
        for i in range(10):
            map_forest1.occupy(8, 14+i, wall)
        for i in range(4):
            map_forest1.occupy(7, 20+i, wall)
        map_forest1.occupy(6, 22, wall)
        map_forest1.occupy(6, 23, wall)
        map_forest1.occupy(5, 23, wall)
        map_forest1.occupy(12, 2, wall)
        map_forest1.occupy(13, 3, wall)
        map_forest1.occupy(12, 4, wall)
        map_forest1.occupy(11, 4, wall)
        map_forest1.occupy(10, 5, wall)
        map_forest1.occupy(9, 5, wall)
        map_forest1.occupy(8, 6, wall)
        map_forest1.occupy(7, 7, wall)
        map_forest1.occupy(7, 8, wall)
        map_forest1.occupy(8, 8, wall)
        map_forest1.occupy(9, 9, wall)
        map_forest1.occupy(10, 9, wall)
        map_forest1.occupy(11, 8, wall)
        map_forest1.occupy(12, 7, wall)
        map_forest1.occupy(13, 7, wall)
        map_forest1.occupy(14, 6, wall)
        for i in range(7):
            map_forest1.occupy(15+i, 5, wall)
        map_forest1.occupy(22, 6, wall)
        for i in range(3):
            map_forest1.occupy(22-i, 7+i, wall)
        map_forest1.occupy(19, 9, wall)
        map_forest1.occupy(18, 10, wall)
        map_forest1.occupy(16, 11, wall)
        for i in range(3):
            map_forest1.occupy(15-i, 12, wall)
        map_forest1.occupy(12, 13, wall)
        for i in range(10):
            map_forest1.occupy(12+i, 14, wall)
        map_forest1.occupy(16, 15, wall)
        map_forest1.occupy(17, 15, wall)
        map_forest1.occupy(18, 16, wall)
        map_forest1.occupy(19, 16, wall)
        map_forest1.occupy(16, 17, wall)
        # for i in range(3):
        #     map_forest1.occupy(16+i, 18, wall)
        # for i in range(5):
        #     map_forest1.occupy(17+i, 19, wall)
        # for i in range(4):
        #     map_forest1.occupy(19+i, 20, wall)
        # for i in range(3):
        #     map_forest1.occupy(23, 21+i, wall)
        # map_forest1.occupy(22, 15, wall)
        # map_forest1.occupy(23, 16, wall)
        # for i in range(6):
        #     map_forest1.occupy(24+i, 17, wall)
        # map_forest1.occupy(30, 16, wall)
        # for i in range(3):
        #     map_forest1.occupy(31, 16-i, wall)
        # for i in range(4):
        #     map_forest1.occupy(30-i, 14, wall)
        # map_forest1.occupy(26, 15, wall)
        for i in range(4):
            map_forest1.occupy(25-i, 15-i, wall)
        map_forest1.occupy(22, 11, wall)
        for i in range(3):
            map_forest1.occupy(23+i, 10, wall)
        for i in range(3):
            map_forest1.occupy(26+i, 10-i, wall)
        for i in range(4):
            map_forest1.occupy(28-i, 7, wall)
        map_forest1.occupy(25, 6, wall)
        map_forest1.occupy(25, 5, wall)
        map_forest1.occupy(26, 5, wall)
        for i in range(7):
            map_forest1.occupy(26+i, 4, wall)
        for i in range(3):
            map_forest1.occupy(32+i, 5, wall)
        map_forest1.occupy(35, 6, wall)
        map_forest1.occupy(36, 6, wall)
        for i in range(4):
            map_forest1.occupy(32+i, 13, wall)
        for i in range(4):
            map_forest1.occupy(29+i, 12, wall)
        for i in range(3):
            map_forest1.occupy(29+i, 11-i, wall)
        for i in range(3):
            map_forest1.occupy(31+i, 8, wall)
        for i in range(4):
            map_forest1.occupy(33+i, 9, wall)

        map_forest1.occupy(36, 7, exit)
        map_forest1.occupy(36, 8, exit)

        if mon1_wild.alive:
            map_forest1.occupy(28, 9, mon1_wild)

        current_map.occupy(char_x, char_y, current_char)   # 人物一开始显示在地图的哪个位置

        # if denizen.x > 8 and denizen.x < self.grid_y - 8:
        #     self.center_x = denizen.x   # 地图跟着一起移动
        #
        # if denizen.y > 3 and denizen.y < self.grid_x - 6:
        #     self.center_y = denizen.y

        current_map.center_x = min(max(char_x, 8), 30)   # 地图中心点跟人物位置相同，让人物一开始在地图中心
        current_map.center_y = min(max(char_y, 3), 20)






#   cake_sprite = MapDenizen(5,5, "walking/cupcake.png", 35, 26, disappear)
#   aMap.occupy(5, 5, cake_sprite)
