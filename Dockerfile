FROM python:3.11
WORKDIR /app

# копируем файл зависимостей и устанавливаем их
COPY req.txt .
RUN pip install --no-cache-dir -r req.txt

# Копируем остальные файлы проекта в контейнер
COPY config/ ./config/
COPY handlers/ ./handlers/
COPY utils/ ./utils/
COPY app.py .

# команда запуска приложения
CMD ["python", "app.py"]