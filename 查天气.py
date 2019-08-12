# -*- coding: 'utf-8' -*-

import requests

print('Hello!^_^')

while True:
    city = input('\n请输入你所查的城市，回车键退出：\n')
    if not city:
        break

    try:
        req = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s' % city)
    except:
        print('对不起，查询失败！')
        break

    # print(req.text)
    dic_city = req.json()                                   # 转换为字典
    # print(dic_city)

    city_data = dic_city.get('data')                        # 没有‘data’的话返回 None

    if city_data:
        city_forecast = city_data['forecast'][0]            # 下面的都可以换成‘get’方法
        print(city_forecast.get('date'))
        print(city_forecast.get('high'))
        print(city_forecast.get('low'))
        print(city_forecast.get('type'))
    else:
        print('Sorry,未获得"%s"相关的天气数据。#_#' % city)
