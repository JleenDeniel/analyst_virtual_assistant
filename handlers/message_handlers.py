from telegram import Update
from config.openai_client import client, generate_response


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
    
    
    # text_1 = "Тебе дана структура данных компании:" + s + "ответь на вопрос:" + text + '\n'+ helper


    # assistant = client.beta.assistants.create(
    #       name="Bank Analyst Assistant",
    #       instructions="Ты помощник аналитика в банке" + helper,
    #       model="gpt-3.5-turbo",
    #       tools=[{"type": "file_search"}],
    # )

    # vector_store = client.beta.vector_stores.create(name="Bank Statements")

    # file_paths = ["utils/prompt_final.txt"]
    # file_streams = [open(path, "rb") for path in file_paths]
    
    # file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
    #   vector_store_id=vector_store.id, files=file_streams
    # )
    # print(file_batch.status)
    # print(file_batch.file_counts)

    # assistant = client.beta.assistants.update(
    #     assistant_id=assistant.id,
    #     tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
    # )

    # thread = client.beta.threads.create()
    # message = client.beta.threads.messages.create(
    #     thread_id=thread.id,
    #     role="user",
    #     content=text
    # )

    # run = client.beta.threads.runs.create_and_poll(
    #   thread_id=thread.id,
    #   assistant_id=assistant.id,
    # )

    # if run.status == 'completed':
    #     messages = list(client.beta.threads.messages.list(thread_id=thread.id, run_id=run.id))
    #     message_content = messages[0].content[0].text
    #     ai_reply = message_content.value
    #     reply = ai_reply[:-13]
    # else:
    #     reply = run.status

    reply = generate_response(text, helper)
    
    # запрос
    # response = client.chat.completions.create(
    #     model="gpt-3.5-turbo",
    #     messages=[{"role": "user", "content": text_1}],
    #     max_tokens=1024,
    #     temperature=0.5,
    # )

    # # ответ
    # reply = response.choices[0].message.content.strip()

    # перенаправление ответа в Telegram
    await update.message.reply_text(reply)   
    
    print("user:", text)
    print("assistant:", reply)
