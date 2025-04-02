import whisper
from pydub import AudioSegment



for path in range(2):
    mp3_path = f"Test {path+1}.mp3" # your audio file
    wav_path = f"output{path+1}.wav" # This doesn't change


    audio = AudioSegment.from_mp3(mp3_path)
    audio.export(wav_path, format="wav")


    model = whisper.load_model("base")


    result = model.transcribe(wav_path)


    print(result["text"]+"\n\n\n\n")
