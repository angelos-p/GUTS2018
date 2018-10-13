from music.main import do_music
from annoying_responses import Annoying_response
from polly_talk import make_polly_talk
import multiprocessing as mp
import time
import subprocess
import webbrowser, os

def printHello(print_output):
    for x in range(5):
        time.sleep(2)
    print_output.put("hello")

def main():
    webbrowser.open('file://' + os.path.realpath("welcome.html"))
    annoy = Annoying_response()
    while True:
        print_output = mp.Queue()
        music_output = mp.Queue()
        annoy_output = mp.Queue()

        processes = [mp.Process(target=printHello, args=[print_output]), 
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
        else:
            arguements = [annoy_results[0]] 
        polly = mp.Process(target=make_polly_talk, args=arguements)
        polly.start()
        polly.join()

main()
