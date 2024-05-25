from openai import OpenAI 
from .tokens import OPENAI_API_KEY 

client = OpenAI(
    api_key = OPENAI_API_KEY,
)

def generate_response(text, helper):
    assistant = client.beta.assistants.create(
          name="Bank Analyst Assistant",
          instructions="Ты помощник аналитика в банке" + helper,
          model="gpt-3.5-turbo",
          tools=[{"type": "file_search"}],
    )

    vector_store = client.beta.vector_stores.create(name="Bank Statements")

    file_paths = ["utils/prompt_final.txt"]
    file_streams = [open(path, "rb") for path in file_paths]
    
    file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
      vector_store_id=vector_store.id, files=file_streams
    )
    print(file_batch.status)
    print(file_batch.file_counts)

    assistant = client.beta.assistants.update(
        assistant_id=assistant.id,
        tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
    )

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

    if run.status == 'completed':
        messages = list(client.beta.threads.messages.list(thread_id=thread.id, run_id=run.id))
        message_content = messages[0].content[0].text
        ai_reply = message_content.value
        reply = ai_reply[:-13]
    else:
        reply = run.status
        
    return reply

def generate_transcription(audio_bytes):
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=("audio.oga", audio_bytes, "audio/ogg")
    )
    return transcription.text.strip()
