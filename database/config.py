from configparser import ConfigParser

config_filename = './database/config.ini'

parser = ConfigParser()




"""
Модуль для проверки конфигурационных файлов

"""


def get_db_params(filename=config_filename, section='postgresql'):
    parser.read(filename, "utf-8")

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Ошибка подключения к БД! Секция {0} не найдена в файле {1}'.format(section, filename))

    
    return db