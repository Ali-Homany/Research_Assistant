# Speech Feature
This branch aims to provide an easy way to recognize text from a given audio

It includes 3 modules:
- **transcriber:**
This is the main module that provides the Transcriber class, which can be created, and called with the audio file path to return it as text

- **app:** This is a simple gradio interface to use the transcriber

- **main:** This is just for testing and using the Transcriber directly

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

4. Run app.py, insert the audio file you want
