```bash
API: http://127.0.0.1:8000/cinemas/
GET /cinemas/?full_name=Абдулгужин
GET /cinemas/?city=Уфа
GET /cinemas/?fo=ПФО
POST-запросы

Загрузка xlsx данных в PostgerSQL: add_data_to_db.py

Установка библиотек: requirements.txt

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',                            # Name of your PostgreSQL database
        'USER': 'postgres',                            # PostgreSQL username
        'PASSWORD': 'postgres',                        # PostgreSQL user password
        'HOST': 'localhost',                           # Database host (usually 'localhost')
        'PORT': '5432',                                # Port where PostgreSQL runs (usually 5432)
    }
}
