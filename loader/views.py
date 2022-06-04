# Импорт функций и классов фласк для работы с вьюшками
from flask import Blueprint, send_from_directory, render_template, request

# Импорт из пользовательского модуля функций для валидации и работы с файлами
from utils import save_post_into_json, is_file_allowed
# Импорт логгера
from logger import logger


# Конструкция блюпринта
loader_blueprint = Blueprint(
    'loader_blueprint',
    __name__,
    template_folder='templates'
)

# Путь для сохранения файлов
UPLOAD_FOLDER = "uploads/images"


@loader_blueprint.route("/", methods=["GET"])
def page_post_form():
    """
    Вьюшка для представления страницы для добавления постов
    :return форма для добавления постов:
    """
    # форма для добавления постов
    return render_template('post_form.html')


@loader_blueprint.route("/", methods=["POST"])
def page_post_upload():
    """
    Вьюшка для обработки данных поста, текст, картинка
    :return Статус завершения процесса добавления поста:
    """
    # Объект файла
    picture = request.files.get('picture')
    # Содержимое текстового поля
    content = request.form.get('content')

    # Если файл был передан
    if picture:
        # Выделения имени файла с расширением
        filename = picture.filename

        # Если расширение файла картинка
        if is_file_allowed(filename):
            # Путь куда сохранить картинку
            path_save = f"{UPLOAD_FOLDER}/{filename}"

            # Сохранение картинки
            picture.save(path_save)

            try:
                # Сохранить данные о посте в json файл, путь к картинке и содержимое текстового поля
                save_post_into_json(path_save, content)

                # Возвращает обработанный шаблон с информацией о добавленном посте
                return render_template(
                    'post_uploaded.html',
                    path_save=path_save,
                    content=content
                )
            # Если не получилось сохранить данные поста в json
            except AttributeError as att:
                # Запись в лог об ошибке
                logger.error(f"{att}")
                return "<h1>Что то пошло не так</h1>"
        else:
            # Расширение файла
            ext = filename.split('.')[-1]
            # Текст для заголовка
            text = f'Выбранный формат {ext} не поддерживается'
            # Текст для сообщения
            message = 'Выберите файл с расширением jpeg, png, jpg'

            # Если файл не картинка, запись в лог и вывод пользователю
            logger.info(f"the extension {ext} is not supported")
            return render_template(
                'repeat.html',
                text=text,
                message=message
            )
    else:
        # Если файл не выбран, запись в лог и вывод пользователю
        text = 'Выберите картинку'
        message = 'Поле не должно быть пустым'
        return render_template(
            'repeat.html',
            text=text,
            message=message
        )


@loader_blueprint.route("/uploads/<path:path>/")
def static_dir(path):
    """
    Эта вьюшка дает доступ к директории uploads
    :param path:
    :return send_from_directory("uploads", path):
    """
    return send_from_directory("uploads", path)
