from decouple import config
import openai
from openai import OpenAI

# Import custom functions
from functions.database import get_recent_messages

client = OpenAI(api_key=config("OPEN_AI_KEY"))


# Retrieve Environment Variables
# TODO: The 'openai.organization' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(organization=config("OPEN_AI_ORG"))'
# openai.organization = config("OPEN_AI_ORG")


# Open AI - Whisper
# Convert Audio to Text
def convert_audio_to_text(audio_file):
    try:
        # Assuming client.audio.transcriptions.create returns a string
        transcription_response = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file,
            response_format="text"
        )

        # Return the transcribed text directly
        return transcription_response
    except Exception as e:
        print(e)
        return None  # Handle the error or return a default value

# Open AI - Chat GPT
# Convert audio to text
def get_chat_response(message_input):

    messages = get_recent_messages()
    user_message = {"role": "user", "content": message_input}
    messages.append(user_message)
    print(messages)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    message_text = response.choices[0].message.content.strip()
    return message_text

    
