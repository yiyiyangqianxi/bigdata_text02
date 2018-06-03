# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 14:51:26 2018

@author: lenovo
"""

msg={"地址":"乐山市市中区乐山师范学院",
 "手机号码":"15884330122",
 "寄件方":"yiyiyangyang"}
print(msg["地址"])
print(msg["手机号码"])
print(msg["寄件方"])
#写一个字典类型，表示一个人的基本信息：姓名，身高，性别，年龄
information={"姓名":"易羊羊",
             "性别":"男",
             "年龄":"18",
             "身高":"180"}
print(information["姓名"])
print(information["性别"])
print(information["年龄"])
print(information["身高"])
    
jacson={'name':'易烊千玺',
        'songs':['你说','萤火虫','拥抱你'],
        '昵称':'大佬',
        '兄弟':['王俊凯','王源']}    
songs=jacson['songs']
print(songs)
print("歌曲总数："+str(len(songs)))
print(max(jacson['兄弟']))
#天气：未来5天的，未来的5天的情况，今天星期几。
#用字典写出天气信息，并且查询最高温度是

weather={'日期':['6.3','6.4','6.5','6.6','6.7'],
         '温度':['25','28','32','33','32'],
         '情况':['多云','晴','晴','多云','晴']}
wendu=weather['温度']
print(wendu)
print(max(weather['温度']))
today=['星期六','6.2','27','小雨']
print(today)








