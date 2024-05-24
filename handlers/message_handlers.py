from telegram import Update
from config.openai_client import client, assistant, generate_response
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

MODE = range(1)

async def chatgpt_reply(update: Update, context):
    # текст входящего сообщения
    text = update.message.text

    # # запрос
    # response = generate_response(text)

    # # ответ
    # reply = response.choices[0].message.content.strip()
    reply = generate_response(text=text)

    # перенаправление ответа в Telegram
    await update.message.reply_text(reply)   
    
    print("user:", text)
    print("assistant:", reply)
