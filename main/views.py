# Импорт функций и классов фласк для работы с вьюшками
from flask import Blueprint, render_template, request

# Импорт из пользовательского модуля функций для валидации и работы с файлами
from utils import search_by_keyword
# Импорт логгера
from logger import logger


# Конструкция блюпринта
main_blueprint = Blueprint(
    'main_blueprint',
    __name__,
    template_folder='templates'
)


@main_blueprint.route('/')
def page_index():
    """
    Вьюшка главной страницы сайта
    :return:
    """
    return render_template('index.html')


@main_blueprint.route('/search/')
def page_tag():
    """
    Вьюшка по поиску постов по ключевым словам
    :return:
    """
    # Ключевое слово
    keyword = request.args.get('s')
    try:
        # Пост по ключевому слову
        posts = search_by_keyword(keyword)
        # Запись в лог
        logger.info(f"Поисковой запрос по ключу {keyword}")
        # Старница с постами по ключевому слову
        return render_template('post_list.html',
                               posts=posts,
                               keyword=keyword
                               )
    except TypeError as t:
        # Если json файла нет
        logger.error(f"TypeError: {t}")
        return """<link rel="stylesheet" type="text/css" href="/static/styles/style.css">
        <h1>Что то на стороне сервера...</h1>
        <a href="/" class="button">Вернуться</a>"""
