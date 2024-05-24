from openai import OpenAI 
from .tokens import OPENAI_API_KEY 

client = OpenAI(
    api_key = OPENAI_API_KEY
)

assistant = client.beta.assistants.create(
    name="Virtial assistant for analyst",
    model="gpt-3.5-turbo",
)

vector_store = client.beta.vector_stores.create(name="Product descriptions")

file_paths = ["config/products_parameters.md"]
file_streams = [open(path, "rb") for path in file_paths]

file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
    vector_store_id=vector_store.id, files=file_streams
)

assistant = client.beta.assistants.update(
    assistant_id=assistant.id,
    tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
)

def generate_response(text):
    thread = client.beta.threads.create()
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=text
    )
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant.id,
        )
    messages = ''
    if run.status == 'completed': 
        messages = client.beta.threads.messages.list(
            thread_id=thread.id)
        print(messages)
    else:
        print(run.status)


    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1024,
        temperature=0.5,
    )
    print(response.choices[0].message.content.strip())
    return response.choices[0].message.content.strip()

def generate_transcription(audio_bytes):
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=("audio.oga", audio_bytes, "audio/ogg")
    )
    return transcription.text.strip()
