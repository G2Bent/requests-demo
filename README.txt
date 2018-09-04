一、GET：无参
    response = requests.get(url=url)
    response.text

二、GET：有参数
    requests.get(url=url, params=参数字典)
    response.text

三、POST：x-www-form-urlencoded
    requests.post(url = url, headers = {'Content-Type': 'application/x-www-form-urlencoded'}, data = 参数字典)
    response.text

四、POST：form-data（不要在请求头中指定Content-Type，如果指定，反而报错）
    requests.post(url = url, data = 参数字典)
    response.text

五、POST：form-data（上传二进制文件）
    data_dic = {'myfile': open('F:\\discuz.jmx', 'rb')}  #第一个参数是：通过web页面中，input框的name属性。第二个参数是：读取本地文件为二进制流文件
    response = requests.post(url = url, files = data_dic)
    response.text

六、POST：raw（text/xml）
    reponse = requests.post(url=url, headers = {'Content-Type': 'text/xml'}, data = 字符串)
    response.text

七、POST：raw（application/json），必须在请求头中指定Content-Type为application/json
    reponse = requests.post(url=url, headers = {'Content-Type': 'application/json'}, json=参数字典)
    response.json  #字典
    response.json.get('')  #通过字典的key取value值
    