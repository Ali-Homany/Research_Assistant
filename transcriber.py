import whisper
from typing import Literal


class Transcriber:
    def __init__(self):
        self.model = whisper.load_model("base")
    def __call__(self, audio: str, language: Literal['en', 'fr'] | None = None) -> str:
        if isinstance(audio, str):
            # audio is given as filepath
            if language:
                return self.model.transcribe(audio=audio, language=language)['text']
            return self.model.transcribe(audio=audio)['text']
