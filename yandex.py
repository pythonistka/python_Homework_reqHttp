import os.path
import requests

from token_ya import token_yandex


class YaUploader:

    def __init__(self, token: str):
        self.token = token
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {token}'
        }

    def upload(self, file_path: str, save_file: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        host = 'https://cloud-api.yandex.net/v1/disk/resources'
        if not os.path.exists(file_path):
            print("Ошибка, файла нет")
            return
        # Тут ваша логика
        # Функция может ничего не возвращать
        res = requests.get(f'{host}/upload?path={save_file}&overwrite=true', headers=self.headers).json()
        url_where_to_upload_file = res['href']
        with open(file_path, 'rb') as f:
            try:
                requests.put(url_where_to_upload_file, files={'file': f})
            except KeyError:
                print(res)



if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = r"C:\Users\lopatinadi\PycharmProjects\python_Homework_reqHttp\hw_yandex.txt"
    save_file_name = 'hw_yandex.txt'
    token = token_yandex
    uploader = YaUploader(token)
    uploader.upload(file_path=path_to_file, save_file=save_file_name)
