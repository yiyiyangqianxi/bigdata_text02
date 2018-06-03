# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 16:30:28 2018
#应用其他包
import 包名/类名
@author: lenovo
"""

city_pinyin=input("请输入城市拼音:")
address='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
print(address.format(city_pinyin))

#1.查看当前城市天气 2.查看其他城市天气 3.保存当前城市天气

print("欢迎使用全球天气app")
print("1.查看当前城市天气 2.查看其他城市天气 3.保存当前城市天气")
menno=input("请输入菜单：")

if menno=='1':
    print("1.查看当前城市天气")
if menno=='2':
    print("2.查看其他城市天气")
if menno=='3':
    print("3.保存当前城市天气")
    
import urllib.request as r
city_pinyin=input("请输入城市拼音:")
address='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
infor=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')   
print(infor)
#json(dict)格式工具包
import json
data=json.loads(infor)
tep=data["main"]["temp"]
print("温度:"+str(tep))
maxwep=data["main"]["temp_max"]
print("最高温度:"+str(maxwep))
pes=data["main"]["pressure"]
print("气压:"+str(pes))
hum=data["main"]["humidity"]
print("湿度:"+str(hum))
des=data["weather"][0]["description"]
print("天气情况:"+str(des))

















