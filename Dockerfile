FROM python:3.11
WORKDIR /app

# копируем файл зависимостей и устанавливаем их
RUN apt-get update && apt-get install -y curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && export PATH="$HOME/.local/bin:$PATH"
COPY pyproject.toml poetry.lock ./

RUN curl -sSL https://install.python-poetry.org | python3 - \
    && export PATH="/root/.local/bin:$PATH" \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev

# Копируем остальные файлы проекта в контейнер
COPY config/ ./config/
COPY handlers/ ./handlers/
COPY utils/ ./utils/
COPY app.py .

# команда запуска приложения
CMD ["poetry", "run", "python", "app.py"]