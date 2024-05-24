from telegram import Update
from config.openai_client import client


async def chatgpt_reply(update: Update, context):
    # текст входящего сообщения
    text = update.message.text

    # f = open("/root/cib_enjoyers/prompt.txt", "r")
    # s = f.read()

    # with open('/root/cib_enjoyers/logfile.log') as f_1:
    #     for line in f_1:
    #         pass
    #     last_line = line

    with open('logfile.log') as f_1:
        for line in f_1:
            pass
        last_line = line

    last_line = last_line.replace('\n', '')

    helper = ''
    
    if 'DA' in last_line:
        helper = 'Отвечай максимально просто, не нужно объяснять каждую деталь'
    elif 'DS' in last_line:
        helper = 'После ответа на вопрос ниже объясни каждый финансовый термин и бизнес значимость'
    if 'Intern' in last_line:
        helper = 'Отвечай максимально подробно, чтобы понял даже ребенок'
    if 'Buddy' in last_line:
        helper = 'Подскажи, как объяснить этот ответ новичку'
    
    # f = open('/root/cib_enjoyers/database.md', 'r')
    # htmlmarkdown=markdown.markdown( f.read() )

    # htmlmarkdown = htmlmarkdown.replace('\*', '')
    # htmlmarkdown = htmlmarkdown.replace('\#', '')
    # htmlmarkdown = htmlmarkdown.replace('\-', '')
    
    # text_1 = "Тебе дана структура данных компании:" + s + "ответь на вопрос:" + text + '\n'+ helper
    text_1 = "Тебе дана структура данных компании:" + "ответь на вопрос:" + text + '\n'+ helper
    
    # запрос
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text_1}],
        max_tokens=1024,
        temperature=0.5,
    )

    # ответ
    reply = response.choices[0].message.content.strip()

    # перенаправление ответа в Telegram
    await update.message.reply_text(reply)   
    
    print("user:", text)
    print("assistant:", reply)import json

import logging

from telegram import Update,KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup
from telegram.ext import ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

MODE = range(1)

async def start_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # объект обновления
    update_obj = json.dumps(update.to_dict(), indent=4)


    name = str(update['message']['from']['first_name'])
    # ответ
    reply = "*Привет " + name + "!*" + "\n\n Для описания и возможных команд набери /explain"

    # перенаправление ответа в Telegram
    await update.message.reply_text(reply, parse_mode="Markdown")

    print("assistant:", reply)

async def explain_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # ответ
    reply = """
    Это бот CIB_Enjoyers, который помогает разобраться со структурой данных в твоей компании
    
    Команды, которые есть в боте: 
    /start - начать работу с ботом
    /explain - вывести все команды
    /mode - выбрать стиль общения бота
    /joke - бот напишет шутку или частушку чтобы расслабиться и отвлечься от работы 

    """

    # перенаправление ответа в Telegram
    await update.message.reply_text(reply)

    print("assistant:", reply)


async def mode_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # ответ
    reply = """
    Выбери свой уровень  взаимодействия: 
    
    * /Intern (начинающий специалист, ничего не понимаю)
    
    * /DA (аналитик данных, есть понимание и в данных, и в бизнес процессах)
    
    * /DS (дата-сайентист, очень хорошо понимаю в данных, но плаваю в бизнес процессах)
    
    * /Buddy (наставник начинающего специалиста)

    """

    reply_keyboard = [["/Intern", "/DA", "/DS", "/Buddy"]]

    # перенаправление ответа в Telegram
    await update.message.reply_text(reply, reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Какой твой уровень?"
        ))

    print("assistant:", reply)

    return MODE

async def mode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Stores the selected mode and asks for a question."""
    user = update.message.from_user
    logger.info("Mode of %s: %s", user.first_name, update.message.text)
    await update.message.reply_text(
        "Отлично, задавай свой вопрос!",
        # reply_markup=ReplyKeyboardRemove(),
    )

    print(update.message.text)


async def joke_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):

    
    # ответ
    reply = """
    А там армяне в нарды играют    

    """

    # перенаправление ответа в Telegram
    await update.message.reply_text(reply)

    print("assistant:", reply)


