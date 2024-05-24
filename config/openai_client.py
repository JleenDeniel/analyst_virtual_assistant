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

    messages = list(client.beta.threads.messages.list(thread_id=thread.id, run_id=run.id))

    message_content = messages[0].content[0].text
    annotations = message_content.annotations
    citations = []
    for index, annotation in enumerate(annotations):
        message_content.value = message_content.value.replace(annotation.text, f"[{index}]")
        if file_citation := getattr(annotation, "file_citation", None):
            cited_file = client.files.retrieve(file_citation.file_id)
            citations.append(f"[{index}] {cited_file.filename}")
    print(message_content.value)
    return message_content.value
    # response = client.chat.completions.create(
    #     model="gpt-3.5-turbo",
    #     messages=messages,
    #     max_tokens=1024,
    #     temperature=0.5,
    # )
    # print(response.choices[0].message.content.strip())
    # return response.choices[0].message.content.strip()

def generate_transcription(audio_bytes):
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=("audio.oga", audio_bytes, "audio/ogg")
    )
    return transcription.text.strip()
