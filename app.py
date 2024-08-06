import gradio as gr
from transcriber import Transcriber

def transcribe_audio(audio_path: str) -> str:
    return transcriber(audio_path)

transcriber = Transcriber()

with gr.Blocks() as demo:
    gr.Markdown("# Audio Transcriber")
    gr.Markdown("Upload an audio file to transcribe its content")
    audio_input = gr.Audio(label="Upload audio file", type='filepath')
    voice_input = gr.Audio(label='Record a voice', type='filepath', sources=['microphone'])
    text_output = gr.Textbox(label="Transcribed text")
    gr.Button("Transcribe").click(
        transcribe_audio,
        inputs=audio_input,
        outputs=text_output
    )
    voice_input.change(
        transcribe_audio,
        inputs=voice_input,
        outputs=text_output
    )

if __name__ == "__main__":
    demo.launch()