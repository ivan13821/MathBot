from configparser import ConfigParser


config_filename = 'config.ini'
parser = ConfigParser()




"""
Модуль для проверки и получения конфигурационных файлов

"""






def get_tg_api_token(filename=config_filename, section='telegram'):
    parser.read(filename, "utf-8")


    if parser.has_section(section):
        token = parser.get(section, 'api_token')
    else:
        raise Exception('Ошибка получения API токена бота. Секция {0} не найдена в файле {1}'.format(section, filename))


    return token




