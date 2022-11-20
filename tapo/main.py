import Levenshtein

from sound import SpeechRecognizer
from tapo4 import turn_on, turn_off, bright, dark, close
from Levenshtein import distance
from mq import Publisher

commands = {
    "свет": turn_on,
    "тьма": turn_off,
    "спать": turn_off,
    "больше": bright,
    "меньше": dark, "темнее": dark,
    "светлее": bright,
    "ярче": bright,
    "включить": turn_on,
    "выключить": turn_off,
    "стоп": None
}


def find_command(w: str, tolerance: int = 1):
    if w is None:
        return None

    min_d = None
    cmd = None
    for k in commands.keys():
        d = Levenshtein.distance(w, k)
        if d <= tolerance:
            if min_d is None:
                min_d = d
                cmd = k
            else:
                if d < min_d:
                    min_d = d
                    cmd = k

    return cmd


def main():
    sr = SpeechRecognizer()
    it = iter(sr)

    #    p = Publisher()

    #    with p:
    while True:
        w = next(it)
        print(f"{w}")
        #           p.publish(w)

        cmd = find_command(w)
        if cmd is not None:
            func = commands[cmd]

            if func is not None:
                func()
                pass

        if cmd == "стоп":
            break


    #close()

if __name__ == "__main__":
    main()
