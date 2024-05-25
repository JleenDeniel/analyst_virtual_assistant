from telegram import Update
from config.openai_client import client, generate_response, generate_transcription
from io import BytesIO

async def audio_reply(update: Update, context):
    if update.message.voice is None:
        return
    
    # входящее аудио сообщение
    audio_file = await context.bot.get_file(update.message.voice.file_id)

    # конвертация аудио в формат .ogg
    audio_bytes = BytesIO(await audio_file.download_as_bytearray())
    
    # запрос транскрипции аудио
    transcription = generate_transcription(audio_bytes)

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
    
    # openai ответ
    reply = generate_response(transcription, helper)
    
    # перенаправление ответа в Telegram
    await update.message.reply_text(reply)
    
    print("user:", audio_file.file_path)
    print("transcription:", transcription)
    print("assistant:", reply)
