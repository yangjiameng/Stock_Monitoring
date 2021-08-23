import configparser as cf

config = cf.ConfigParser()


def config_write():
    config["DEFAULT"] = {'first_code': '600733',
                         'second_code': '600111',
                         'start_date': '20210801',
                         'end_date': '20210818'
                         }
    config['personal_message'] = {'money': '100000'}
    config['profit_message'] = {'今日盈亏': '10127.40',
                                '资产剩余': '120325.48',
                                '总收益率': '9.44%%',
                                '持有公司': '北方稀土',
                                '持仓占比': '70%%',
                                '投资风格': '激进型'}
    with open('message.ini', 'w') as f:
        config.write(f)


def config_read():
    config.read('message.ini')
    # print(type(config['profit_message']['今日盈亏']))
    return float(config['personal_message']['money'])


if __name__ == '__main__':
    config_write()
    # config_read()
