import requests
import json
import openpyxl as pl
import datetime


def write_csv(now_time_url, now_time_excel):
    url_zt = 'http://push2ex.eastmoney.com/getTopicZTPool?cb=callbackdata7254380&ut=' \
             '7eea3edcaed734bea9cbfc24409ed989&dpt=wz.ztzt&Pageindex=0&pagesize=170&sort=' \
             'fund%3Aasc&date=' + now_time_url + '&_=1632288573835'
    url_dt = 'http://push2ex.eastmoney.com/getTopicDTPool?cb=callbackdata8517117&ut=' \
             '7eea3edcaed734bea9cbfc24409ed989&dpt=wz.ztzt' \
             '&Pageindex=0&pagesize=170&sort=fund%3Aasc&date=' + now_time_url + '&_=1632724948658 '
    zt = requests.get(url_zt)
    dt = requests.get(url_dt)
    j = json.loads(zt.text[20:len(zt.text) - 2])
    j_dt = json.loads(dt.text[20:len(dt.text) - 2])
    lenth_zt = len(j['data']['pool'])
    lenth_dt = len(j_dt['data']['pool'])
    wbr = pl.Workbook()
    sheet_0 = wbr.active
    sheet_0.title = '每日涨停股'
    info_zt = ['代码', '名称', '价格/(元)', '涨跌幅/(%)', '成交额/(亿)', '流通市值/(亿)', '总市值/(亿)', '换手率/(%)', '连板数',
               '首次封板/(h,m)', '最后封板/(h,m)', '封板资金/(亿)', '炸板数', '涨停统计', '所属行业']
    sheet_0.append(info_zt)
    for i in range(0, lenth_zt):
        list_data_zt = [j['data']['pool'][i]['c'], j['data']['pool'][i]['n'], j['data']['pool'][i]['p'] / 1000,
                        round(j['data']['pool'][i]['zdp'], 2), round(j['data']['pool'][i]['amount'] / pow(10, 8), 2),
                        round(j['data']['pool'][i]['ltsz'] / pow(10, 8), 2),
                        round(j['data']['pool'][i]['tshare'] / pow(10, 8), 2), round(j['data']['pool'][i]['hs'], 2),
                        j['data']['pool'][i]['lbc'],
                        round(j['data']['pool'][i]['fbt'] / 10000, 2), round(j['data']['pool'][i]['lbt'] / 10000, 2),
                        round(j['data']['pool'][i]['fund'] / pow(10, 8), 2),
                        j['data']['pool'][i]['zbc'],
                        str(j['data']['pool'][i]['zttj']['ct']) + '/' + str(j['data']['pool'][i]['zttj']['days']),
                        j['data']['pool'][i]['hybk']]
        sheet_0.append(list_data_zt)
    print('涨停股已写入完毕！')
    wbr.create_sheet('每日跌停股')
    wbr._active_sheet_index = 1
    sheet_1 = wbr.active
    info_dt = ['代码', '名称', '价格/(元)', '涨跌幅/(%)', '成交额/(亿)', '流通市值/(亿)', '总市值/(亿)', '换手率/(%)', '连续跌停',
               '动态市盈率', '最后封板/(h,m)', '封板资金/(亿)', '翘板板数', '板上成交额', '所属行业']
    sheet_1.append(info_dt)
    for j in range(0, lenth_dt):
        list_data_dt = [j_dt['data']['pool'][j]['c'], j_dt['data']['pool'][j]['n'], j_dt['data']['pool'][j]['p'] / 1000,
                        round(j_dt['data']['pool'][j]['zdp'], 2),
                        round(j_dt['data']['pool'][j]['amount'] / pow(10, 8), 2),
                        round(j_dt['data']['pool'][j]['ltsz'] / pow(10, 8), 2),
                        round(j_dt['data']['pool'][j]['tshare'] / pow(10, 8), 2),
                        round(j_dt['data']['pool'][j]['hs'], 2),
                        j_dt['data']['pool'][j]['days'],
                        round(j_dt['data']['pool'][j]['pe'], 2), round(j_dt['data']['pool'][j]['lbt'] / 10000, 2),
                        round(j_dt['data']['pool'][j]['fund'] / pow(10, 8), 2),
                        j_dt['data']['pool'][j]['oc'],
                        round(j_dt['data']['pool'][j]['fba'] / pow(10, 8), 2),
                        j_dt['data']['pool'][j]['hybk']]
        sheet_1.append(list_data_dt)
    print('跌停股已写入完毕！')
    wbr.save('zd/涨跌停股明细' + now_time_excel + '.xlsx')


def get_date():
    now_time_url = datetime.datetime.now().strftime('%Y%m%d')
    now_time_excel = datetime.datetime.now().strftime('%Y-%m-%d')
    write_csv(now_time_url, now_time_excel)


if __name__ == '__main__':
    # write_csv()
    get_date()
