# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 09:58:34 2018

@author: lenovo
"""

import urllib.request as r
city=input("请输入城市拼音:")
url='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996'
info=r.urlopen(url.format(city)).read().decode('utf-8','ignore')   
print(info)
print("欢迎进入天气查询APP")
import json
tianqi=json.loads(info)

for i in range(38): 
    dt_txt=tianqi['list'][i]['dt_txt']
    print("当前时期时刻为："+str(dt_txt))
    temp=tianqi['list'][i]['main']['temp']
    print("当前温度是："+str(temp)+"开氏度")
    temp_min=tianqi['list'][i]['main']['temp_min']
    print("当前最低温度："+str(temp_min)+"开氏度")
    temp_max=tianqi['list'][i]['main']['temp_max']
    print("当前最高温度："+str(temp_max)+"开氏度")
    description=tianqi['list'][i]['weather'][0]['description']
    print("天气描述："+str(description))
    pressure=tianqi['list'][i]['main']['pressure']
    print("气压为："+str(pressure)+"pa")
    if str(tianqi['list'][i]['dt_txt'])[9:10]!=str(tianqi['list'][i+1]['dt_txt'])[9:10]:
        print("..................................")    
    print("**********************************")
        
    
    
    
    
    

