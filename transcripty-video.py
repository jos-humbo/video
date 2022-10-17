import pytube
import whisper

"""Agregar url de video de youtube dentro de los parentesis"""
youtubeUrl = "https://youtu.be/YQHsXMglC9A"
youtubeVideo = pytube.YouTube(youtubeUrl)

audio = youtubeVideo.streams.get_audio_only()
audio.download(filename='tmp.mp4')

model = whisper.load_model("small")

result = model.transcribe('tmp.mp4')

print(result["text"])
