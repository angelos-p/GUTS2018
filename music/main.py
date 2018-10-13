from recorder import AudioRecorder
from music_api import SongRecognizer
import time

FILE = 'output.wav'


def main():
    while True:
        recognizer = SongRecognizer()
        recorder = AudioRecorder(FILE)
        recorder.record(10)
        recorder.destroy()
        result = recognizer.recognize_song(FILE)

if __name__ == "__main__":
    main()
    
