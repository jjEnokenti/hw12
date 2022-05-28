import json


# Путь к файлу json с постами
POST_PATH = "posts.json"
# Поддерживаемые расширения
ALLOWED_EXTENSIONS = {'png', 'jpeg', 'jpg'}


def _load_data(path=POST_PATH):
    """
    Функция форматировании данных json для работы
    :param path:
    :return format data:
    """
    try:
        # Чтение данных и форматирование
        with open(path, encoding='utf-8') as file:
            data = json.load(file)
        # Возврат форматированных данных
        return data
    except FileNotFoundError:
        # Если проблемы с файлом json False для обработки исключений
        return False


def search_by_keyword(keyword):
    """
    Функция поиска постов по ключевому слову
    :param keyword:
    :return posts:
    """
    # Загрузка данных о постах
    data = _load_data()

    # Ключевое слово в нижний регистр
    keyword = keyword.lower()
    # Для коллекции найденных постов
    posts = []

    # Цикл по постам
    for post in data:
        if keyword in post['content'].lower():
            # Если ключевое слово есть в посте, добавить к найденным постам
            posts.append(post)

    # Найденные посты
    return posts


def save_post_into_json(path_save, content, path=POST_PATH):
    """
    Функция для добавления нового поста в json
    :param path_save:
    :param content:
    :param path:
    :return:
    """
    # Загрузка данных для добавления к ним нового поста
    data = _load_data()

    # Новый пост
    post = {
        'pic': path_save,
        'content': content
    }

    # Добавление поста к постам
    data.append(post)

    # Запись готовых данных с новым постом в файл json
    with open(path, 'w', encoding='utf-8') as file:

        json.dump(data, file, ensure_ascii=False, indent=3)


def is_file_allowed(filename):
    """
    Функция валидации расширений файлов
    :param filename:
    :return:
    """

    # Если файл поддерживается то вернется True
    if filename.split('.')[-1] in ALLOWED_EXTENSIONS:
        return True

    return False
