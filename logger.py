import logging

# Создание логгера
logger = logging.getLogger('my_log')
# Установка левела логгеру
logger.setLevel(logging.INFO)

# Обработчик для записи логгов в файл
file_handler = logging.FileHandler('main.log', encoding='utf-8')

# Формат записей
formatter_log = logging.Formatter("%(asctime)s : %(levelname)s : %(message)s")

# Установка формата записей
file_handler.setFormatter(formatter_log)

# Добавление обработчика
logger.addHandler(file_handler)

