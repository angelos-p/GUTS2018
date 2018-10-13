from music.main import do_music
from polly_talk import make_polly_talk
import multiprocessing as mp
import time
import subprocess

def printHello(print_output):
    for x in range(5):
        time.sleep(2)
    print_output.put("hello")

def main():
    while True:
        print_output = mp.Queue()
        music_output = mp.Queue()
        processes = [mp.Process(target=printHello, args=[print_output]), 
                     mp.Process(target=do_music, args=[music_output])
                    ]
        for p in processes:
            p.start()
        for p in processes:
            p.join()
        results = [music_output.get()]
        if results[0]:
            polly = mp.Process(target=make_polly_talk, args=[results[0][0], results[0][1]])
            polly.start()
            polly.join()

main()
