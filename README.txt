һ��GET���޲�
    response = requests.get(url=url)
    response.text

����GET���в���
    requests.get(url=url, params=�����ֵ�)
    response.text

����POST��x-www-form-urlencoded
    requests.post(url = url, headers = {'Content-Type': 'application/x-www-form-urlencoded'}, data = �����ֵ�)
    response.text

�ġ�POST��form-data����Ҫ������ͷ��ָ��Content-Type�����ָ������������
    requests.post(url = url, data = �����ֵ�)
    response.text

�塢POST��form-data���ϴ��������ļ���
    data_dic = {'myfile': open('F:\\discuz.jmx', 'rb')}  #��һ�������ǣ�ͨ��webҳ���У�input���name���ԡ��ڶ��������ǣ���ȡ�����ļ�Ϊ���������ļ�
    response = requests.post(url = url, files = data_dic)
    response.text

����POST��raw��text/xml��
    reponse = requests.post(url=url, headers = {'Content-Type': 'text/xml'}, data = �ַ���)
    response.text

�ߡ�POST��raw��application/json��������������ͷ��ָ��Content-TypeΪapplication/json
    reponse = requests.post(url=url, headers = {'Content-Type': 'application/json'}, json=�����ֵ�)
    response.json  #�ֵ�
    response.json.get('')  #ͨ���ֵ��keyȡvalueֵ
    