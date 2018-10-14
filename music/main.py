from recorder import AudioRecorder
from music_api import SongRecognizer
from lyric_finder import LyricFinder
import time 
import lyricwikia
import os

filepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE = os.path.join(filepath, 'output.wav')
LYRIC_LENGTH = 40


def do_music(music_output):
    recognizer = SongRecognizer()
    lyric_finder = LyricFinder(LYRIC_LENGTH)
    result = recognizer.recognize_song(FILE)
    if result:
        lyrics = lyric_finder.find_lyrics(result[0], result[1], result[2])
        rate = ((float(len(lyrics.split()))/(result[3]/1000))/0.4) * 110
        music_output.put((lyrics, rate))
    else:
        music_output.put(None)


if __name__ == "__main__":
    main()
    
