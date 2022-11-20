import pyaudio
from tapo4 import turn_on, turn_off, bright,dark, init



model = Model(lang="ru")
rec = KaldiRecognizer(model, 48000)
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=48000,
    input=True,
    frames_per_buffer=8000
)
stream.start_stream()


commands = {"свет": turn_on, "тьма": turn_off, "спать": turn_off,
            "больше": bright, "меньше": dark, "темнее": dark, "светлее": bright}




while True:
    data = stream.read(4000, exception_on_overflow=False)
    if len(data) == 0:
        break

    result = rec.AcceptWaveform(data)
    s = None
    if result:
        s = json.loads(rec.Result())
        t:str = s["text"]
        print(t)

        cmd = commands.get(t)
        if cmd:
            print(f"{cmd}")
            cmd()

    else:
        s = json.loads(rec.PartialResult())


print(rec.FinalResult())