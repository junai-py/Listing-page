import configparser
config = configparser.ConfigParser()
config['xpath'] = {'title': '//article/a/div[3]/div[1]/div[1]/h2/text()',
                     'img_url': '//article/a/div[2]/div[2]/img/@data-original',
                     'prd_url': '''detailUrl: "/en/ip/.*"'''}

with open('config.ini', 'w') as configfile:
    config.write(configfile)
