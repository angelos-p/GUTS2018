from recorder import AudioRecorder
from music_api import SongRecognizer
from lyric_finder import LyricFinder
import time 
import lyricwikia

FILE = 'output.wav'
LYRIC_LENGTH = 20
RECORDING_TIME = 10


def main():
    while True:
        recognizer = SongRecognizer()
        recorder = AudioRecorder(FILE)
        lyric_finder = LyricFinder(LYRIC_LENGTH)
        recorder.record(RECORDING_TIME)
        recorder.destroy()
        result = recognizer.recognize_song(FILE)
        if result:
            lyrics = lyric_finder.find_lyrics(result[0], result[1], result[2])
            print(lyrics)


if __name__ == "__main__":
    main()
    
