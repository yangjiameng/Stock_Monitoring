import configparser as cf

config = cf.ConfigParser()
config["DEFAULT"] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9',
                     'ForwardX11': 'yes'
                     }
config['bitbucket.org'] = {'User': 'Atlan'}
config['topsecret.server.com'] = {'Host Port': '50022', 'ForwardX11': 'no'}
with open('message.ini', 'w') as f:
    config.write(f)
