# -*- coding: utf-8 -*-
'''
@Time : 2023/7/4 10:49
@Email : Lvan826199@163.com
@公众号 : 梦无矶的测试开发之路
@File : control_settings.py
'''
__author__: "梦无矶小仔"

## key是账号,value里面的第一位是pwd,后面的是对应的游戏

user_pwd = {
    "xli65512@gmail.com": ["Tll654321", "Whispers", "GrandCash", "BingoIsland", "NorthTower", "LuckyHit", "DoubleRich", "HarvestTown",
                           "PlagueInvader", "MatchScapes", "DoubleWin", "MatchTileDecor", "WhiteChord", "WeedMania", "MergeMaster"],
    "jinlimei86@gmail.com": ["Tll123456", "BingoJourney", "GoldenFish", "HugeWin", "CashHoard"],
    "wtavidly@gmail.com": ["Tll12345", "WeedInc420"],
    "treetll94@gmail.com": ["Tll654321", "BingoParty"],
}

is_tf_install_app_flag = 0  # 0表示不进行TF下载，1表示需要在TF下载，并且是卸载安装模式

devices_dict = {
    # "4438650ca0ef0073a711ae68b7c5fdc629db9772": 1,  # ;046 ->>
    # "e455517036f9aabe3ceb7111a8eaf1c01d7de3f0": 1,  # ;049 ->>
    # "49687f67a4c70fbd027e19b4a5e40218acdc06e4": 1,  # ; 067 ->>
    # "00008027-001968942140402E": 1,  # ;--100 ->>
    "00008101-001859DE1E38001E": 1,  # ; 123 ->>
    # "00008110-000275943EEB801E": 1,  # ; 182 ->>
    "00008030-001E19021A42802E": 1,  # ; 186 ->>
    # "27d62264ebf40fb3a9e4868590b62ff3b4de90ff": 1,  # ;192 ->>
}

game_project = {
    # "BingoParty": 1,
    # "BingoJourney": 1,
    # "DoubleWin": 1,
    # "Whispers": 1,
    # "GrandCash": 1,
    # "Demo": 1,
    # "BingoIsland": 1,
    # "NorthTower": 1,
    "MatchScapes": 1,
    # "LuckyHit": 1,
    # "GoldenFish": 1,
    # "DoubleRich": 1,
    # "CashHoard": 1,
    # "HugeWin": 1,
    # "HarvestTown": 1,
    # "PlagueInvader": 1,
    # "MatchTileDecor": 1,
    # "WhiteChord": 1,  # 纯白大作战
    # "WeedMania": 1, # 像素风商店类
    # "WeedInc420": 1, #
    # "MergeMaster": 1, #
}


def user_pwd_game():
    # 游戏名对应表
    game_name_dict = {
        "BingoParty": "Bingo Party！Live Classic Bingo",
        "BingoJourney": "Bingo Journey！Live Bingo Games",
        "DoubleWin": "Double Win Slots Casino Game",
        "Whispers": "Whispers - Interactive Stories",
        "GrandCash": "Grand Cash Casino Slots Games",
        "Demo": "PASS",
        "BingoIsland": "Bingo Island-Fun Family Bingo",
        "NorthTower": "North Tower! Merge TD Defense",
        "MatchScapes": "Match Tile Scenery",
        "LuckyHit": "Lucky Hit Classic Casino Slots",
        "GoldenFish": "黃金捕魚場Online -經典休閒捕魚遊戲街機",
        "DoubleRich": "Double Rich！Vegas Casino Slots",
        "CashHoard": "Cash Hoard Casino Slots Games",
        "HugeWin": "Huge Win Slots！Casino Games",
        "HarvestTown": "Harvest Town - Pixel Sim RPG",
        "PlagueInvader": "瘟疫入侵者: 生存之战",
        "MatchTileDecor": "Match Tile Decor",
        "WhiteChord": "Adventure of white chord",
        "WeedMania": "Weed Mania: Chill 420 Club",
        "MergeMaster": "Merge Master - Home Design",
        "WeedInc420": "Weed Inc 420: Blaze & Trade",
    }
    game_package = {
        "BingoParty": "com.bingo.tour.party.crazy.free.ios.avidly",
        "BingoJourney": "com.bingo.scape.ios.free",
        "DoubleWin": "com.huge.slots.casino.vegas.ios.avidly",
        "Whispers": "com.twincat.stories",
        "GrandCash": "com.grandcashslots.free.ios",
        "Demo": "PASS",
        "BingoIsland": "com.bingo.island.ios",
        "NorthTower": "com.strategy.north.tower.ios",
        "MatchScapes": "com.puzzle.matchscapes.apple",
        "LuckyHit": "com.bravo.slots.casino.ios",
        "GoldenFish": "com.golden.fishing.ios.avidly",
        "DoubleRich": "com.newclassic.doublerich",
        "CashHoard": "com.jackpot.fever.slots.ios",
        "HugeWin": "Hcom.cjfafafa.trojan.ios",
        "HarvestTown": "com.harvest.ios.grq",
        "PlagueInvader": "com.anotherworld.ios",
        "MatchTileDecor": "com.zymobile.match.tile.decor.ios",
        "WhiteChord": "com.yulong.sgame.ios",
        "WeedMania": "com.sfgh.weedmania.ios",
        "MergeMaster": "com.zymobile.merge.master.home.design.ios",
        "WeedInc420": "com.zhgh.cannabis.weed.please.gp",
    }
    isSelectProjectList = []
    user_pwd_game_dict = {"user": None,
                          "pwd": None,
                          "game": None,
                          "package_name": None,
                          "is_tf_install_app_flag": is_tf_install_app_flag
                          }

    for project, select in game_project.items():
        if select == 1:
            isSelectProjectList.append(project)

    if len(isSelectProjectList) != 1:
        print("----------选择的项目不是唯一,请检查是否多选项目或未选项目!----------")
        return None

    user_pwd_game_dict["game"] = game_name_dict[isSelectProjectList[0]]

    for userName, game_list in user_pwd.items():
        if isSelectProjectList[0] in game_list:
            user_pwd_game_dict["user"] = userName
            user_pwd_game_dict["pwd"] = game_list[0]
            user_pwd_game_dict["package_name"] = game_package[isSelectProjectList[0]]

    print(user_pwd_game_dict)
    return user_pwd_game_dict

# if __name__ == '__main__':
#     user_pwd_game()
