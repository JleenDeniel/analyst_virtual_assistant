# Чат-бот "Ассистент Аналитика"

Чат-бот "Ассистент Аналитика" помогает новым сотрудникам аналитических отделов, сотрудникам data science и их бадди получать необходимую информацию о бизнесе банка, особенностях его процессов, информацию по базам данных.

## Репо

```
analyst_virtual_assistant/
│
├── config/
│   ├─── openai_client.py
│   ├─── telegram_bot.py
│   └─── tokens.py
│
├── handlers/
│   ├── __init__.py
│   ├── command_handlers.py
│   └── message_handlers.py
│
├── utils/
│   ├── __init__.py
│   └── helpers.py
│
├── app.py
├── Dockerfile
├── Makefile
└── requirements.txt
```

- `config/` - конфигурационные файлы
- `handlers/` - обработчики сообщений и команд
- `utils/` - вспомогательные функции
- `app.py` - главный файл приложения
- `Dockerfile` - скрипт для создания Docker образа
- `Makefile` - автоматизация процесса сборки
- `requirements.txt` - зависимости проекта

---
## Как поднять сервис
Для работы с этим репозиторием нужно:
1. Форкнуть код
2. Добавить секреты:
   TELEGRAM_BOT_TOKEN 
   OPENAI_API_KEY 
   DOCKER_USERNAME
   DOCKER_REPO
   SERVER_HOST
   SERVER_LOGIN
   SERVER_PASSWORD
3. Сделать пуш коммита в main и запустится action, который начнет пайплайн сборки и оживления сервиса

Или, можно просто на сервере сделать
git clone
docker build
docker push
docker pull <image>
docker run

*сори за такую инструкцию, просто до дедлайна считанные минуты*

## Использование бота

Найти бота можно по ссылке: https://t.me/raif_virtual_assistant_bot

Команды, которые есть в боте: 
    1) /start - начать работу с ботом
    2) /explain - вывести все команды
    3) /mode - выбрать стиль общения бота
    4) /joke - бот напишет шутку или частушку чтобы расслабиться и отвлечься от работы

Бот поддерживает несколько видов промптов: 

  /intern - режим стажера: все ответы на вопросы достаточно подробные, чтобы сотрудник без опыта смог разобраться в процессах
  
  /DA - режим дата-аналитика: ответы достаточно подробные, бот хорошо отвечает на вопросы по базам данных
  
  /DS - режим data science специалиста: подходит для сотрудников, которые очень хорошо понимают в данных, но плавают в бизнес процессах
  
  /Buddy - режим наставника, в этом случае бот рассказывает, как лучше объяснить тот или иной бизнес-процесс стажеру или новому сотруднику

Также бот поддерживает 2 формата ввода: 

  1) тектстовой
  2) голосовой
     
## Что спрашивать у бота? 
Бот обучен на контенте, связанном напрямую с компанией. В нашем случае мы создали новый банк Global Financial Solutions (GFS)

Этот банк находится на территории Германии, поэтому все средства представлены в евро. 

Контекст, который сейчас вложен в модель: 
  
  Продукты, описание продуктов
  
  Описание типов счетов
  
  Описание структуры банка
  
  Список сотрудников банка и их должности
  
  Описание программ кредитования
  
  Сегментация розничных клиентов, используемая кредитным департаментом
  
  Описание метрик при оценке кредитных рисков
  
  Принципов формирования параметров
  
  Описание используемой модели оценки вероятности дефолта (фичи, показатели модели)
  
  Добавлена структура баз данных с описанием ключей (возможность запрашивать sql код)
  
  Описание процесса обработки кредитных заявок и принятия решения по ним

На данный момент бот поддерживает работу по нескольким сценариям: 

Сценарий 1: 
Текущий сотрудник data science команды хочет добавить фичу “остатки на счетах клиента” в модель рекомендации инвестиционных продуктов банка. Знания, которых не хватает сотруднику для решения вопроса: 
  
  Откуда можно взять данные по счетам (в какой таблице они хранятся)
  
  Как таблица по счетам связывается с другими
  
  Какие типы счетов есть, и какая между ними разница
  
  Какие конкретно типы счетов нужны для создания фичи
  
  К кому из сотрудников банка можно обратиться с дополнительным вопросом по таблице с счетами

Сценарий 2: 
Новый сотрудник кредитного департамента не имел ранее опыта работы в банке и  не понимает, как оперирует система принятия решений по выдаче кредитов. Вопросы, которые он может уточнить у бота:
  
  Какие типы клиентов приходят за кредитами в банк?
  
  Какие есть этапы выдачи кредита?
  
  Где можно посмотреть результаты прохождения каждого этапа обработки заявки?
  
  Как все таблицы, в которых хранятся эти данные связаны друг с другом?

Более узкие вопросы, которые могут возникнуть:
  
  Какие есть метрики по оценке клиентов на этапе обработки заявки?
  
  Какие значения вероятности дефолта считаются экстремальными (банк скорее откажет)?
  
  Сколько в среднем поступает заявок на кредит в месяц?
  
  Как определяется размер лимита для клиента? 
  
  Как определяется ставка кредитования?

Сценарий 3:
Сотрудник data science хочет использовать внутреннюю оценку кредитного рейтинга, для разработки модели вероятности одобрения заявок на кредитование (возможность для автоматической обработки поступающих заявок). Для этого он обращается к боту по следующим вопросам: 
  
  На основе какой модели формируется оценка кредитного рейтинга клиента?
  
  Какие фичи входят в модель?
  
  Какие коэффициенты у текущей модели?
  
  Как в модели обработаны категориальные значения?
  
  Какой Джини и текущий PSI модели?
  
  К кому можно обратиться с вопросом по коду сборки модели?

# Предисловие

Туториал поможет развернуть чат-бота Telegram, использующего API OpenAI, как локально, так и в Docker контейнере на облачном сервере.

Библиотеки:

- [openai](https://pypi.org/project/openai/)
- [python-telegram-bot](https://pypi.org/project/python-telegram-bot/)
- [Jupyter Notebook](https://pypi.org/project/notebook/)

## Структура проекта

```
telegram_chatbot_boilerplate/
│
├── config/
│   ├─── openai_client.py
│   ├─── telegram_bot.py
│   └─── tokens.py
│
├── handlers/
│   ├── __init__.py
│   ├── command_handlers.py
│   └── message_handlers.py
│
├── utils/
│   ├── __init__.py
│   └── helpers.py
│
├── app.py
├── Dockerfile
├── Makefile
└── requirements.txt
```

- `config/` - конфигурационные файлы
- `handlers/` - обработчики сообщений и команд
- `utils/` - вспомогательные функции
- `app.py` - главный файл приложения
- `Dockerfile` - скрипт для создания Docker образа
- `Makefile` - автоматизация процесса сборки
- `requirements.txt` - зависимости проекта

---
# Часть 0: Создание репозитория

- нажми кнопку справа сверху **USE THIS TEMPLATE**
- назови проект
- контент в репозитории будет использоваться для хакатона

---
  
# Часть 1: Локальная установка

Для локальной установки проекта потребуется:

- подключение к VPN серверу для доступа к API OpenAI
- токен Telegram бота
- токен API OpenAI
- операционная система Linux или MacOS

## Токен Телеграм бота

Для начала нужно получить токен для доступа к HTTP API вашего бота:

1. Найдите в Telegram бота `@BotFather`
2. Отправьте ему команду `/newbot`
3. Введите имя проекта и имя бота
4. Скопируйте полученный токен

## Установка проекта
0. Склонировать репозиторий
   ```
   git clone github.com/yourreponame
   ```
2. В `Makefile` введите токены Telegram и OpenAI:
   ```
   TELEGRAM_BOT_TOKEN=1235
   OPENAI_API_KEY=1234
   ```
3. Установка зависимостей, генерация файла `.env`:
   ```
   make setup
   ```

## Запуск проекта

1. Запускаем бота локально
   ```
   make run
   ```
2. Открываем Telegram бота и отправляем сообщение

   > Сообщения в Telegram боте и в терминале дублируются.

3. Для удаления .venv, .env, cache и других временных файлов:
   ```
   make clean
   ```

---

# Часть 2: Разработка на облачном сервере

Для удаленной разработки потребуется:

- Доступ к Серверу (ssh user@ip & password)
- Jupyter Notebook
- Visual Studio Code

#### Предустановленный софт на сервере:
- vim
- build-essential
- python3
- python3-venv
- docker-ce
- docker-ce-cli
- docker-buildx-plugin
- docker-compose-plugin

# Удаленная разработка
0. Заходим на сервер
  ```
  ssh -i PATH_TO_YOUR_KEY.pem admin@SERVER_IP_ADDRESS
  ```

1. Клонируем (по https) свой репозиторий в отдельную папку на сервер
   ```
   git clone <repositorylink>
   ```

3. В `Makefile` введите токены Telegram и OpenAI:
   ```
   TELEGRAM_BOT_TOKEN=1235
   OPENAI_API_KEY=1234
   ```
4. Установка зависимостей, генерация файла `.env`:
   ```
   make setup
   ```
5. Запускаем Jupyter Notebook
   ```
   make notebook
   ```
6. Копируем после **token=** в заметки:
   ```
   http://127.0.0.1:8888/tree?token=YOUR_PERSONAL_TOKEN
   ```
7. На своем **персональном устройстве** создаем туннель:
   ```
   ssh -NL 8888:localhost:8888 root@SERVER_IP_ADDRESS
   ```

   или (в зависимости от того, как вы залогинены на сервере)

   ```
   ssh -NL 8888:localhost:8888 admin@SERVER_IP_ADDRESS
   ```
  также если вы залогинены на сервере с использованием ключа (-i PATH_TO_YOUR_KEY.pem), его нужно указать при создании тунеля
   
9. Открываем в браузере;
   ```
   http://localhost:8888
   ```
10. Вставляем токен, который скопировали на шаге **5**, в поле "Password or token" и нажимаем Login.
11. Пользуемся

---

# Запуск Docker контейнера

Для деплоя контейнера на облачный сервер потребуется:

- Скаченная программа [Docker](https://www.docker.com/products/docker-desktop/)
- Аккаунт в [DockerHub](https://hub.docker.com/)
- [Создать репозиторий](https://docs.docker.com/docker-hub/repos/create/)
- токен Telegram бота
- токен API OpenAI
- операционная система Linux или MacOS

1. В `Makefile` добавим к уже имеющимся токенам, **username** и **repositoryname**:

   ```
   # данные пользователя на Docker Hub
   USERNAME=UserNameDockerHub
   REPO=RepositoryNameDockerHub
   TAG=v1
   TELEGRAM_BOT_TOKEN=1235
   OPENAI_API_KEY=1234
   ```
#### Для публикации образа в [DockerHub](https://hub.docker.com/) нужно залогиниться через CLI командой `docker login`


2. Собираем образ под Linux Debian:

   ```
   make build
   ```

3. Запускаем контейнер с приложением

  ```
   make dockerrun
  ```

4. Также, можно опубликовать образ в DockerHub:

   ```
   make push
   ```

---

## Скачивание и запуск опубоикованного образа

1. Находим опубликованный образ в DockerHub:

   ```
   docker search username/projectname
   ```

2. Скачиваем образ:

   ```
   docker pull username/projectname:v1
   ```

3. Запускаем контейнер с токенами Telegram бота и OpenAI API:

   ```
   sudo docker run -i -t -e TELEGRAM_BOT_TOKEN=YOURTOKEN -e OPENAI_API_KEY=YOURTOKEN username/projectname:v1
   ```

4. Открываем Telegram бота и отправляем сообщение
   > Сообщения в Telegram боте и в терминале дублируются.
