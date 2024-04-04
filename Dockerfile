# Используем базовый образ Python
FROM python:3.8

# Установка переменной среды PYTHONUNBUFFERED, чтобы вывод был направлен прямо в терминал без буферизации
ENV PYTHONUNBUFFERED 1

# Установка рабочей директории внутри контейнера
WORKDIR /app

# Копирование файлов в рабочую директорию
COPY . .

# Установка зависимостей
RUN pip install --no-cache-dir -r myproject/requirements.txt

# Команда для запуска скрипта добавления данных в БД
CMD ["python", "add_data_to_db.py"]
