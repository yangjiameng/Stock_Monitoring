import requests
import json
import csv
from time import sleep


def get_realtime_quote(code):
    data_dict = {}
    id_flag = '0.'
    if code[0] == '6':
        id_flag = '1.'
    url = 'http://push2.eastmoney.com/api/qt/stock/get?ut=fa5fd1943c7b386f172d6893dbfba10b&invt=2&fltt=2&fields=f43,' \
          'f57,f58,f169,f170,f46,f44,f51,f168,f47,f164,f163,f116,f60,f45,f52,f50,f48,f167,f117,f71,f161,f49,f530,' \
          'f135,f136,f137,f138,f139,f141,f142,f144,f145,f147,f148,f140,f143,f146,f149,f55,f62,f162,f92,f173,f104,' \
          'f105,f84,f85,f183,f184,f185,f186,f187,f188,f189,f190,f191,f192,f107,f111,f86,f177,f78,f110,f262,f263,f264,' \
          'f267,f268,f250,f251,f252,f253,f254,f255,f256,f257,f258,f266,f269,f270,f271,f273,f274,f275,f127,f199,f128,' \
          'f193,f196,f194,f195,f197,f80,f280,f281,f282,f284,f285,f286,f287,' \
          'f292&secid=' + id_flag + code + '&_=1643078745300 '
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/93.0.4577.82 Safari/537.36 '
    }
    data = requests.get(url=url, headers=headers)
    data_json = json.loads(data.text)
    # value
    data_dict['a5_v'] = data_json['data']['f32']
    data_dict['a4_v'] = data_json['data']['f34']
    data_dict['a3_v'] = data_json['data']['f36']
    data_dict['a2_v'] = data_json['data']['f38']
    data_dict['a1_v'] = data_json['data']['f40']
    data_dict['b1_v'] = data_json['data']['f20']
    data_dict['b2_v'] = data_json['data']['f18']
    data_dict['b3_v'] = data_json['data']['f16']
    data_dict['b4_v'] = data_json['data']['f14']
    data_dict['b5_v'] = data_json['data']['f12']
    # price
    data_dict['a5_p'] = data_json['data']['f31']
    data_dict['a4_p'] = data_json['data']['f33']
    data_dict['a3_p'] = data_json['data']['f35']
    data_dict['a2_p'] = data_json['data']['f37']
    data_dict['a1_p'] = data_json['data']['f39']
    data_dict['b1_p'] = data_json['data']['f19']
    data_dict['b2_p'] = data_json['data']['f17']
    data_dict['b3_p'] = data_json['data']['f15']
    data_dict['b4_p'] = data_json['data']['f13']
    data_dict['b5_p'] = data_json['data']['f11']
    # name
    data_dict['name'] = data_json['data']['f58']
    data_dict['price'] = data_json['data']['f43']
    data_dict['zd_value'] = data_json['data']['f170']
    data_dict['zd_price'] = data_json['data']['f169']
    data_dict['pre_close'] = data_json['data']['f60']

    for i in data_dict:
        if data_dict[i] == '-':
            data_dict[i] = '0'
    return data_dict


def csv_read_code_list():
    csv_file = csv.reader(open('Listed_company_msg/tushare_stock_basic.csv', 'r'))
    code_list = []
    for i in csv_file:
        if 'ST' not in i[2]:
            code_list.append(i[0][0:6])
    code_list.pop(0)
    print(code_list)
    print('正在获取数据...')
    num = 1
    for j in code_list:
        sleep(0.1)
        try:
            a = get_realtime_quote(j)
            print(num, a)
        except Exception as e:
            print(e)
            a = get_realtime_quote(j)
            print(num, a)
        num += 1
    return code_list


if __name__ == '__main__':
    get_realtime_quote('002717')
    # csv_read_code_list()
