from pygame import mixer


class Player:
    def __init__(self, file):
        mixer.init()
        mixer.music.load('{}'.format(file))

    def play_audio(self):
        mixer.music.play()
