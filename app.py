# Импорт приложения фласк
from flask import Flask

# Импорт блюпринтов
from main.views import main_blueprint
from loader.views import loader_blueprint

# Конструкция приложения
app = Flask(__name__)

# Регистрация блюпринтов
app.register_blueprint(main_blueprint, url_prefix='/')
app.register_blueprint(loader_blueprint, url_prefix='/post')


if __name__ == "__main__":
    app.run()

