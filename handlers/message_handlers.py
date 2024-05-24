from telegram import Update
from config.openai_client import client 

async def chatgpt_reply(update: Update, context):
    # текст входящего сообщения
    text = update.message.text

    f = open("analyst_virtual_assistant/prompt.txt", "r")
    s = f.read()

    # f = open('/root/cib_enjoyers/database.md', 'r')
    # htmlmarkdown=markdown.markdown( f.read() )

    # htmlmarkdown = htmlmarkdown.replace('\*', '')
    # htmlmarkdown = htmlmarkdown.replace('\#', '')
    # htmlmarkdown = htmlmarkdown.replace('\-', '')
    
    text_1 = "Тебе дана структура данных компании:" + s + "ответь на вопрос:" + text
    
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
    print("assistant:", reply)
