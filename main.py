from music.main import do_music
from music.recorder import AudioRecorder
from annoying_responses import Annoying_response
from polly_talk import make_polly_talk
from timecheck.timelightcheck import TimeLightCheck
import multiprocessing as mp
import time
import datetime
import subprocess
import webbrowser, os

FILE = 'output.wav'
RECORDING_TIME = 5

def printHello(print_output):
    for x in range(5):
        time.sleep(2)
    print_output.put("hello")

def record_voice():
    recorder = AudioRecorder(FILE)
    recorder.record(RECORDING_TIME)
    recorder.destroy()

def main():
    webbrowser.open('file://' + os.path.realpath("welcome.html"))
    annoy = Annoying_response()
    light_checker = TimeLightCheck()
    last_light = 0
    while True:
        recorder = mp.Process(target=record_voice, args=[])
        recorder.start()
        recorder.join()

        light_output = mp.Queue()
        music_output = mp.Queue()
        annoy_output = mp.Queue()
        light_results = None

        is_light = time.time() - last_light > 60

        if is_light:
            light = mp.Process(target=light_checker.bedtime, args=[light_output])
            light.start()
            light.join()
            light_results = [light_output.get()]

        processes = [ 
                     mp.Process(target=do_music, args=[music_output]),
                     mp.Process(target=annoy.make_response, args=[annoy_output])
                    ]
        for p in processes:
            p.start()
        for p in processes:
            p.join()
        music_results = [music_output.get()]
        annoy_results = [annoy_output.get()]

        if music_results[0]:
            arguements = [music_results[0][0], music_results[0][1]]
        elif is_light and light_results[0]:
            arguements = [light_results[0]] 
            last_light = time.time()
        elif annoy_results[0]:
            arguements = [annoy_results[0]]
        polly = mp.Process(target=make_polly_talk, args=arguements)
        polly.start()
        polly.join()

main()
