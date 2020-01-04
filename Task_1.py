# Нужно для каждого файла txt сделать перревод, который будет запсиан в новый файл
#Нужно для каждого языка создать отдельный файл с переводом
from Token import token
from datetime import datetime
import yadisk
import requests


#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
path_all = ['DE.txt', 'ES.txt', 'FR.txt']


y = yadisk.YaDisk(token=token)

date = datetime.strftime(datetime.now(), "%d.%m.%Y-%H.%M.%S")

def translate_it(text, to_lang):
    params = {
        'key': API_KEY,
        'text': text,
        'lang': to_lang,
        
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])

y.mkdir ('/Task_2_double')
for path in path_all:
    with open (path) as f:
        lang_list = [ ]
        for line in f:
            line = line.strip ()
            lang_list.append (line)

    with open (f'translatefrom_{path[:2]}.txt', 'w',encoding='UTF-8') as new:
        new.write ((translate_it (lang_list, 'ru')))
    with open(f'translatefrom_{path[:2]}.txt', 'rb') as f:
        y.upload (f, f'Task_2_double/translatefrom_{path[:2]}.txt')















# print(translate_it('В настоящее время доступна единственная опция — признак включения в ответ автоматически определенного языка переводимого текста. Этому соответствует значение 1 этого параметра.', 'no'))

# if __name__ == '__main__':
#     print(translate_it('Hallo','ru'))
