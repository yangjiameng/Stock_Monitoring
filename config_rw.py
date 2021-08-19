import configparser as cf

config = cf.ConfigParser()


def config_write():
    config["DEFAULT"] = {'first_code': '600733',
                         'second_code': '600111',
                         'start_date': '20210801',
                         'end_date': '20210818'
                         }
    config['personal_message'] = {'money': '100000'}
    config['profit_message'] = {'Host Port': '50022', 'ForwardX11': 'no'}
    with open('message.ini', 'w') as f:
        config.write(f)


def config_read():
    config.read('message.ini')
    return float(config['personal_message']['money'])
    # config.set('personal_message', 'money', '2222')
    # with open('message.ini', 'w') as f:
    #     config.write(f)


if __name__ == '__main__':
    config_write()
    # config_read()
