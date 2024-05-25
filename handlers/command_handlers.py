import json

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
            reply_keyboard, one_time_keyboard=False, input_field_placeholder="Выбери свой уровень и задай вопрос"
        ))

    print("assistant:", reply)

    return MODE

async def mode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Stores the selected mode and asks for a question."""
    user = update.message.from_user
    logger.info(update.message.text)

    f = open("utils/logs.txt", "a")
    f.write(update.message.text+'\n')
    f.close()

    
    await update.message.reply_text(
        "Отлично, задавай свой вопрос!",
        # reply_markup=ReplyKeyboardRemove(),
    )

    print(update.message.text)

    # return update.message.text


async def joke_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):

    
    # ответ
    reply = """
    А там армяне в нарды играют    

    """

    # перенаправление ответа в Telegram
    await update.message.reply_text(reply)

    print("assistant:", reply)


