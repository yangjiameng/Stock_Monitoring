import requests
import json
import openpyxl as pl

url = 'http://push2ex.eastmoney.com/getTopicZTPool?cb=callbackdata7254380&ut=' \
      '7eea3edcaed734bea9cbfc24409ed989&dpt=wz.ztzt&Pageindex=0&pagesize=170&sort=' \
      'fbt%3Aasc&date=20210922&_=1632288573835'
a = requests.get(url)
j = json.loads(a.text[20:len(a.text) - 2])
lenth = len(j['data']['pool'])


def write_csv():
    wbr = pl.Workbook()
    sheet_0 = wbr.active
    sheet_0.title = '每日涨停股'
    info = ['代码', '名称', '价格', '涨跌幅', '成交额', '流通市值', '总市值', '换手率', '连板数', '首次封板', '最后封板', '封板资金', '炸板数', '涨停统计', '所属行业']
    sheet_0.append(info)
    for i in range(0, lenth):
        list_data = [j['data']['pool'][i]['c'], j['data']['pool'][i]['n'], j['data']['pool'][i]['p'],
                     j['data']['pool'][i]['zdp'], j['data']['pool'][i]['amount'], j['data']['pool'][i]['ltsz'],
                     j['data']['pool'][i]['tshare'], j['data']['pool'][i]['hs'], j['data']['pool'][i]['lbc'],
                     j['data']['pool'][i]['fbt'], j['data']['pool'][i]['lbt'], j['data']['pool'][i]['fund'],
                     j['data']['pool'][i]['zbc'], str(j['data']['pool'][i]['zttj']['ct']) + '/' + str(j['data']['pool'][i]['zttj']['days']),
                     j['data']['pool'][i]['hybk']]
        sheet_0.append(list_data)
    wbr.save('E:/pypro/涨停股明细.xlsx')


if __name__ == '__main__':
    write_csv()

