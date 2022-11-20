import json, queue

from vosk import Model, KaldiRecognizer
import pyaudio


class SpeechRecognizer:
    def __init__(self):
        self.model = Model(lang="ru")
        self.rec = KaldiRecognizer(self.model, 48000)
        self.p = pyaudio.PyAudio()
        self.q = queue.Queue()

    def __iter__(self):
        self.stream = self.p.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=48000,
            input=True,
            frames_per_buffer=8000
        )
        self.stream.start_stream()

        return self

    def __next__(self):
        dt = self.stream.read(4000, exception_on_overflow=False)
        if len(dt) == 0 and self.q.empty():
            raise StopIteration

        res = self.rec.AcceptWaveform(dt)
        txt:str = ""
        s:dict = None
        if res:
            s = json.loads(self.rec.Result())
            txt: str = s["text"]
        else:
            pass
            #s = json.loads(self.rec.PartialResult())

        for w in txt.split (" "):
            if len(w) > 0:
                self.q.put(w)

        if self.q.empty():
            return None
        else:
            return self.q.get()


def main ():
    sr = SpeechRecognizer()

    it = iter(sr)

    while True:
        w = next(it)
        print (f"{w=}")


if __name__ == "__main__":
    main()