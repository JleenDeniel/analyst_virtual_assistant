from telegram import Update
from config.openai_client import client


async def chatgpt_reply(update: Update, context):
    # текст входящего сообщения
    text = update.message.text

    f = open("utils/prompt.txt", "r")
    s = f.read()

    with open('utils/logs.txt') as f_1:
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
    
    
    text_1 = "Тебе дана структура данных компании:" + s + "ответь на вопрос:" + text + '\n'+ helper
    
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
