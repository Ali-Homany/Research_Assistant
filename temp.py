async def get_openai_response(client, user_message, conversation_history, ai_model):
    system_message = 'hello there i am alive!'
    if not conversation_history: conversation_history = []
    history = conversation_history + [{'wow':system_message}]
    return system_message, history, True