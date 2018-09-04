#coding:utf-8
import requests

#GET无参
# url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getRegionProvince'
# reponse = requests.get(url=url)
# print(reponse.status_code)
# print(reponse.text)

#GET有参
# url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString'
# params_dic = {'theRegionCode': '3117'}
# response = requests.get(url=url, params=params_dic)
# print(type(response.text))  #unicode编码，字符串
# print(response.text)

#POST
#x-www-form-urlencoded形式
# url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString'
# headers_dic = {'Content-Type': 'application/x-www-form-urlencoded'}
# data_dic = {'theRegionCode': '3117'}
# response = requests.post(url = url, headers = headers_dic, data = data_dic)
# print(response.text)

#POST
#form表单
#这种形式不要指定headers，如果指定反而会报错
# url='http://139.199.132.220:9000/event/index/submit_info/'
# data_dic = {'username': '19430904', 'email':'1943@163.com', 'password': '123456'}
# response = requests.post(url = url, data = data_dic)
# print(response.text)

#POST
#form表单，可以上传二进制文件。而urlencoded不能上传二进制文件,同时可以上传多个文件
#上传二进制文件
# url='http://139.199.132.220:9000/event/index/uploadFile/'
# data_dic = {'myfile': open('F:\\discuz.jmx', 'rb')}
# response = requests.post(url = url, files = data_dic)
# print(response.text)

#POST
#raw:xml---webservice或soap
#普通字符串
# url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx'
# headers_dic = {'Content-Type': 'text/xml'}
# data_str = '''<?xml version="1.0" encoding="utf-8"?>
# <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
#   <soap:Body>
#     <getSupportCityString xmlns="http://WebXml.com.cn/">
#       <theRegionCode>3117</theRegionCode>
#     </getSupportCityString>
#   </soap:Body>
# </soap:Envelope>
# '''
# response = requests.post(url=url, headers = headers_dic, data = data_str)
# print(response.text)

#POST
#raw:json
url = 'http://139.199.132.220:9000/event/weather/getWeather/'
headers_dic = {'Content-Type': 'application/json'}
params_dic = {'theCityCode': 1}
reponse = requests.post(url=url, headers = headers_dic, json=params_dic)
# print('type(reponse.text) =%s' %type(reponse.text))  #unicode
# print('reponse.text = %s' %reponse.text)
# print reponse.status_code
# print reponse.headers
# print reponse.cookies
print('type(reponse.json) =%s' %type(reponse.json()))  #dict
print('response.json = %s' %reponse.json())
# print reponse.json()['name']
#下面的，如果找不到，返回None，而不会报错
print(reponse.json().get('name'))
#print reponse.json().get('cid')
#print reponse.json().get('error_code')








