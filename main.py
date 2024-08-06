from transcriber import Transcriber


transcriber = Transcriber()
audio_path = './french.m4a'
text = transcriber(audio_path)
print(text)
