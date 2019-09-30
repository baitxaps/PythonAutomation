#! /usr/bin/env python3
# coding: utf-8

import json,requests,sys
import csv


def cvc():
    exampleFile = open('./automate_online-materials/example.csv')
    exampleReader = csv.reader(exampleFile)
    exampleData = list(exampleReader)
    print(exampleData)


def jsonData():
    stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
    jsonDataAsPythonValue = json.loads(stringOfJsonData)
    print(jsonDataAsPythonValue)

    pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
    stringOfJsonData = json.dumps(pythonValue)
    print(jsonDataAsPythonValue)


#jsonData() 


def argsFunction():
    if len(sys.argv) < 2:
        print('Usage: quickWeather.py location')
        sys.exit()
    location = ' '.join(sys.argv[1:])
    url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
    response = requests.get(url)
    response.raise_for_status()
    weatherData = json.loads(response.text)
    w = weatherData['list']
    print('Current weather in %s:' % (location))
    print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
    print()
    print('Tomorrow:')
    print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description']) 
    print()
    print('Day after tomorrow:')
    print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])


argsFunction()

