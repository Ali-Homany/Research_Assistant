import os
import asyncio
from openai import AsyncOpenAI
import dotenv
dotenv.load_dotenv()


MODELS = {
    'gpt': 'gpt-4o-mini'
}
async def get_openai_response(client, user_message, conversation_history, ai_model):
    conversation_history.append({"role": "user", "content": user_message})
    response = await client.chat.completions.create(
        model= MODELS[ai_model],
        messages=conversation_history
    )
    system_message = response.choices[0].message.content
    # Append user and system messages to conversation history
    conversation_history.append({"role": "assistant", "content": system_message})
    # now check for end of chat
    chat_message = [{"role" : "system",
                    "content": "Is this message stating the end of the chat? Answer by Yes or No.}"},
                    {"role" : "assistant", "content" : f" MESSAGE: {system_message}"}]
    response = await client.chat.completions.create(
        model=MODELS[ai_model],
        messages=chat_message
    )
    end_chat_flag = response.choices[0].message.content
    # return system_message
    return system_message, conversation_history, end_chat_flag


with open('./prompt_template_v2.txt', 'r') as file:
    PROMPT_TEMPLATE_V2 = file.read()
GREETING_MESSAGE = 'Hello, welcome! I am your medical assistant, please describe your issue'


def init_chat_history(version=2):
    # prompt_template = init_prompt_template()
    prompt_template = init_prompt_template(2)
    chat_history = [{"role" : "system", "content" : prompt_template}]
    chat_history.append({"role" : "assistant" , "content" : GREETING_MESSAGE})
    # return [{"role" : "system", "content" : prompt_template}]
    return chat_history


def init_prompt_template(version):
    # prompt_template = main_prompt_template.replace("<QUESTIONS>" , str(questions))
    if version == 1 :
        with open("rare_medical_questions.txt", "rb") as f :
            questions = f.read()
        return PROMPT_TEMPLATE_V1.replace("<QUESTIONS>" , str(questions))
    if version == 2:
        return PROMPT_TEMPLATE_V2


if __name__ == '__main__':
    ai_model = 'gpt'
    history = init_chat_history()
    print(history)
    input('continue?')
    user_message = 'I have a headache'
    client = AsyncOpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    system_message, history, end_chat_flag = asyncio.run(get_openai_response(client=client, conversation_history=history, user_message=user_message, ai_model=ai_model))
    print(history)
