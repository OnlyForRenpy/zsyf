define audio.block = "sound/battle_system/battle/skills/block.ogg"
define audio.fanfare = "sound/battle_system/game/林坤信 - 战斗胜利 2.mp3"
define audio.failure = "sound/battle_system/game/林坤信 - 战斗失败 1.mp3"
define sfx_whoosh = RandomBag(["sound/battle_system/battle/whoosh1.ogg", "sound/battle_system/battle/whoosh2.ogg", "sound/battle_system/battle/whoosh3.ogg", "sound/battle_system/battle/whoosh4.ogg", "sound/battle_system/battle/whoosh5.ogg", "sound/battle_system/battle/whoosh6.ogg", "sound/battle_system/battle/whoosh7.ogg"])
define sfx_monsterdead = RandomBag(["sound/battle_system/battle/monsterdead1.ogg", "sound/battle_system/battle/monsterdead2.ogg", "sound/battle_system/battle/monsterdead3.ogg"])

label battle_music:
    random:
        play music "sound/battle_system/林坤信 - 势如破竹 1.mp3"
        play music "sound/battle_system/林坤信 - 御剑伏魔 1.mp3"
        play music "sound/battle_system/林坤信 - 逆天而行1.mp3"
    return
