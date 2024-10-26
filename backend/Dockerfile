# 1. Используем Python как базовый образ
FROM python:3.10

# 2. Устанавливаем рабочую директорию
WORKDIR /backend

# 3. Копируем файлы проекта
COPY . .

# 4. Устанавливаем зависимости
RUN pip install -r requirements.txt

RUN python3 manage.py collectstatic --noinput

# 5. Expose порт для вебсокетов (например, 8000) и HTTP (например, 8001)
EXPOSE 8000

# 6. Команда для запуска сервера Django с daphne
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
