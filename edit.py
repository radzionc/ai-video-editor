import whisper
from utils.trim_video import trim_video

input_path = "input.mp4"
output_path = "output.mp4"

model = whisper.load_model("base")
transcription = model.transcribe(input_path)

segments = [(d['start'], d['end']) for d in transcription['segments']]
trim_video(input_path, output_path, segments)

