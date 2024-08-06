# Speech Feature
This branch aims to provide an easy way to recognize text from a given audio, and integrate it with the chatbot in a gradio interface.

It includes 4 modules:
- **transcriber:**
This is the main module that provides the Transcriber class, which can be created, and called with the audio file path to return it as text

- **chatbot:** This module mainly offers a way to chat and interact with a medical assistant using OpenAI's gpt4o-mini

- **app:** This is a simple gradio interface for chatting with the chatbot.

## Usage:
1. Clone the repository


2. Install requirements:
```
pip install -r requirements.txt
```

3. Install ffmpeg:
    - Download the zip file from [here](https://ffmpeg.org/download.html). (for direct download link for windows click [here](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip))
    - Unzip the downloaded file, and put it under C:/ffmpeg
    - Add `C:\ffmpeg\ffmpeg-7.0.2-essentials_build\bin` to Path variable in your System Enviroment Variables

4. Run app.py, you can chat with the bot through text or voice messages
