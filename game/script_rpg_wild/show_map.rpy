label show_wild_map:
    window hide
    stop music
    scene black with fade
    with Pause(1.0)
    play music "sound/bgm/吴欣睿 - 神州大地.mp3"
    $ eventrunning = False
    $ config.allow_skipping = False
    $ config.rollback_enabled = False
    $ renpy.block_rollback()
    $ renpy.choice_for_skipping()
    $ preferences.afm_enable = False
    call screen map_screen(current_map)
