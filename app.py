import os
import asyncio
from openai import AsyncOpenAI
import dotenv
dotenv.load_dotenv()
from chatbot import get_openai_response, init_chat_history
import gradio as gr
from transcriber import Transcriber


def transcribe_audio(audio_path: str) -> str:
    return transcriber(audio_path)


def answer_message(message: str, chat_history: list[str], transformed_chat_history: list):
    system_message, history, end_chat_flag = asyncio.run(get_openai_response(client=client, conversation_history=transformed_chat_history, user_message=message, ai_model=ai_model))
    chat_history.append((message, system_message))
    if end_chat_flag == 'Yes':
        return chat_history, history, gr.update(interactive=False), gr.update(interactive=False)
    return chat_history, history, gr.update(), gr.update()


def answer_voice(voice_filepath: str, chat_history: list[str], transformed_chat_history: list):
    if not voice_filepath:
        return chat_history, transformed_chat_history
    message = transcribe_audio(voice_filepath)
    return answer_message(message, chat_history, transformed_chat_history)


if __name__ == "__main__":    
    transcriber = Transcriber()
    ai_model = 'gpt'
    client = AsyncOpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    initial_history = init_chat_history()
    initial_message = initial_history[1]['content']


    with gr.Blocks() as demo:
        gr.Markdown("# Audio Transcriber")
        gr.Markdown("Upload an audio file to transcribe its content")
        voice_input = gr.Audio(label='Record a voice', type='filepath', sources=['microphone'], format='mp3')
        text_input = gr.Text(label='Type in your message')
        chat_history = gr.Chatbot([(None, initial_message)])
        transformed_chat_history = gr.State(initial_history)
        voice_input.change(
            answer_voice,
            inputs=[voice_input, chat_history, transformed_chat_history],
            outputs=[chat_history, transformed_chat_history, text_input, voice_input]
        )
        text_input.submit(
            answer_message,
            inputs=[text_input, chat_history, transformed_chat_history],
            outputs=[chat_history, transformed_chat_history, text_input, voice_input]
        )

    demo.launch()
