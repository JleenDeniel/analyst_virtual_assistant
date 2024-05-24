from telegram import Update
from config.openai_client import client, assistant, generate_response

async def chatgpt_reply(update: Update, context):
    # текст входящего сообщения
    text = update.message.text
    assistant_ = assistant

    
    # запрос
    response = generate_response(text)

    # ответ
    reply = response.choices[0].message.content.strip()

    # перенаправление ответа в Telegram
    await update.message.reply_text(reply)   
    
    print("user:", text)
    print("assistant:", reply)
