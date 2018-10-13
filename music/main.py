from recorder import AudioRecorder
from music_api import SongRecognizer
from lyric_finder import LyricFinder
import time 
import lyricwikia

FILE = 'output.wav'
LYRIC_LENGTH = 40
RECORDING_TIME = 5


def do_music(music_output):
    recognizer = SongRecognizer()
    recorder = AudioRecorder(FILE)
    lyric_finder = LyricFinder(LYRIC_LENGTH)

    recorder.record(RECORDING_TIME)
    recorder.destroy()
    result = recognizer.recognize_song(FILE)
    if result:
        lyrics = lyric_finder.find_lyrics(result[0], result[1], result[2])
        rate = ((float(len(lyrics.split()))/(result[3]/1000))/0.4) * 100
        music_output.put((lyrics, rate))
    else:
        music_output.put(None)


if __name__ == "__main__":
    main()
    
