# -*- coding:utf-8 -*-

# 作者：兄弟难当
# 版本：1.9.2
# 最早出品/开源时间：2022/7/22 14:22:00


import requests, time, random, \
    os  # 引入requests库，用于网页数据爬取和文件读写；引入time库，用于调用sleep()函数；引入random库，用于调用randint()函数；引入os库，用于创建文件夹
from drawing import drawing
from card import card
from portrait import portrait
from talent import talent

print(
    "欢迎使用原神图像资源脚本！\n\n作者：兄弟难当。\n软件版本：1.9.2(64-bit)。\n共51个角色，采用分析官方wiki图片源的方式进行爬取。\n获取期间，请勿在窗口内点击，否则会使进程暂停。如发生误触或画面卡住，请尝试轻按Enter键。如仍无法解决，请重启程序。\n\n您想获取什么？\n如果想获取角色立绘，请输入数字“1”后按下Enter(回车)键；如果想获取角色头像，请输入数字“2”后按下Enter(回车)键；如果想获取角色卡片，请输入数字“3”后按下Enter(回车)键；如果想获取角色天赋图标，请输入数字“4”后按下Enter(回车)键；直接退出请输入数字“5”后按下Enter(回车)键。")
get_input = input("请输入：")

while True:
    if get_input == "1":
        drawing()
        print(
            "\n全部保存成功！\n\n您还想获取什么？\n如果想获取角色立绘，请输入数字“1”后按下Enter(回车)键；如果想获取角色头像，请输入数字“2”后按下Enter(回车)键；如果想获取角色卡片，请输入数字“3”后按下Enter(回车)键；如果想获取角色天赋图标，请输入数字“4”后按下Enter(回车)键；直接退出请输入数字“5”后按下Enter(回车)键。")  # 给用户查看进程日志的机会，让用户主动关闭窗口，而不是自动关闭
        get_input = input("请输入：")
    if get_input == "2":
        portrait()
        print(
            "\n全部保存成功！\n\n您还想获取什么？\n如果想获取角色立绘，请输入数字“1”后按下Enter(回车)键；如果想获取角色头像，请输入数字“2”后按下Enter(回车)键；如果想获取角色卡片，请输入数字“3”后按下Enter(回车)键；如果想获取角色天赋图标，请输入数字“4”后按下Enter(回车)键；直接退出请输入数字“5”后按下Enter(回车)键。")  # 给用户查看进程日志的机会，让用户主动关闭窗口，而不是自动关闭
        get_input = input("请输入：")
    if get_input == "3":
        card()
        print(
            "\n全部保存成功！\n\n您还想获取什么？\n如果想获取角色立绘，请输入数字“1”后按下Enter(回车)键；如果想获取角色头像，请输入数字“2”后按下Enter(回车)键；如果想获取角色卡片，请输入数字“3”后按下Enter(回车)键；如果想获取角色天赋图标，请输入数字“4”后按下Enter(回车)键；直接退出请输入数字“5”后按下Enter(回车)键。")  # 给用户查看进程日志的机会，让用户主动关闭窗口，而不是自动关闭
        get_input = input("请输入：")
    if get_input == "4":
        talent()
        print(
            "\n全部保存成功！\n\n您还想获取什么？\n如果想获取角色立绘，请输入“1”；如果想获取角色头像，请输入“2”；如果想获取角色卡片，请输入“3”；直接退出请输入“4”。")  # 给用户查看进程日志的机会，让用户主动关闭窗口，而不是自动关闭
    if get_input == "5":
        break
    else:
        print("\n输入有误。")
        get_input = input("请重新输入：")
