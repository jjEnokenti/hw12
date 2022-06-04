import os
import dotenv

# Импорт приложения фласк
from flask import Flask

# Импорт блюпринтов
from main.views import main_blueprint
from loader.views import loader_blueprint


# Конструкция приложения
app = Flask(__name__)

# Регистрация блюпринтов
app.register_blueprint(main_blueprint, url_prefix="/")
app.register_blueprint(loader_blueprint, url_prefix="/post")

dotenv.load_dotenv(override=True)
user = os.environ.get("USER")

if os.environ.get("APP_CONFIG") == "development":
    app.config.from_pyfile('config/development.py')
else:
    app.config.from_pyfile('config/production.py')

print(app.config.get("MY_VALUE"))

if __name__ == "__main__":
    app.run()

