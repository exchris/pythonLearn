"""
Created on 七月 28 2017
@author: dev.erxuan@gmail.com
"""
# -*- coding: utf-8 -*-
# 查询天气

from urllib import request, parse
from xml.parsers.expat import ParserCreate

class weatherSaxHandler(object):
    def __init__(self):
        self.location = {}
        self.forcast = []
    def start_element(self, name, attrs):
        if name == 'yweather:location':
            self.location = attrs
            attrs.pop('xmlns:yweather')
        if name == 'yweather:forecast':
            self.forcast.append(attrs)
    def end_element(self, name):
        pass
    def char_data(self,text):
        pass

def parse_weather(xml): # 输入xml字符串，输出天气信息dict
    parser = ParserCreate()
    handler = weatherSaxHandler()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)
    today = {
        'text': handler.forcast[0]['text'],
        'low': int(handler.forcast[0]['low']),
        'high': int(handler.forcast[0]['high'])
    }
    tomorrow = {
        'text': handler.forcast[1]['text'],
        'low': int(handler.forcast[1]['low']),
        'high': int(handler.forcast[1]['high'])
    }
    d = {
        'today': today,
        'tomorrow': tomorrow
    }
    weather = handler.location
    weather.update(d)
    return weather

def get_weather(city): # 输入城市名（拼音）字符串，输出天气dict
    baseurl = "https://query.yahooapis.com/v1/public/yql?"
    yql_query = 'select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="%s")' % city
    yql_url = baseurl + parse.urlencode({'q':yql_query})
    with request.urlopen(yql_url) as f:
        city_xml = f.read().decode('utf-8')
    city_weather = parse_weather(city_xml)
    return city_weather

def main():
    city = input('Weather Forecast in City: ')
    print(get_weather(city))

main()
