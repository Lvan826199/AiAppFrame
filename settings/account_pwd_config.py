# -*- coding: utf-8 -*-
'''
@Time : 2023/7/5 11:05
@Email : Lvan826199@163.com
@公众号 : 梦无矶的测试开发之路
@File : account_pwd_config.py
'''
__author__ = "梦无矶小仔"

account_pwd_config = {
    "xli65512@gmail.com": ["Tll654321", "Whispers", "GrandCash", "BingoIsland", "NorthTower", "LuckyHit", "DoubleRich", "HarvestTown",
                           "PlagueInvader", "MatchScapes", "DoubleWin", "MatchTileDecor", "WhiteChord", "WeedMania"],
    "jinlimei86@gmail.com": ["Tll123456", "BingoJourney", "GoldenFish", "HugeWin", "CashHoard"],
    "wtavidly@gmail.com": ["Tll12345", "WeedInc420"],
    "treetll94@gmail.com": ["Tll654321", "BingoParty"],
}
game_name_dict = {
    "BingoParty": "Bingo Party！Live Classic Bingo",
    "BingoJourney": "Bingo Journey！Live Bingo Games",
    "DoubleWin": "Double Win Slots Casino Game",
    "Whispers": "Whispers - Interactive Stories",
    "GrandCash": "Grand Cash Casino Slots Games",
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


def get_pwd(project_name):
    password = "Tll123456"
    for account, project in account_pwd_config.items():
        if project_name in project:
            password = project[0]

    return password


def get_account(project_name):
    for account, project in account_pwd_config.items():
        if project_name in project:
            return account


def get_game_package(project_name):
    return game_package[project_name]