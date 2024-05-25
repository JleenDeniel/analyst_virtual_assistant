# Чат-бот "Ассистент Аналитика"

Чат-бот "Ассистент Аналитика" помогает новым сотрудникам аналитических отделов, сотрудникам data science и их бадди получать необходимую информацию о бизнесе банка, особенностях его процессов, информацию по базам данных.

## Логика построения проекта

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

