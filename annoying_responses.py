import speech_recognition as sr
import random
import webbrowser

from music.recorder import AudioRecorder
from os import path
from polly_talk import make_polly_talk



class Annoying_response:

    def __init__(self):
        AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "output.wav")

        self.r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = self.r.record(source)

        user_input = self.convertUserVoiceToText(audio)

        outcome = self.getResponse(user_input)

        make_polly_talk(outcome)

    def getResponse(self, user_input):
        """
        User input is a string converted from the audio file saved.
        """

        greetings = ["hey there", "hello", "hi", "Hai", "hey"]
        creator = ["I was created by the Chad Developers", "Chad Developers", "Some guys whom I never got to know"]
        jokes = ['Can a kangaroo jump higher than a house? Of course, a house doesnt jump at all.', 
                'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.', 
                'Doctor: Im sorry but you suffer from a terminal illness and have only 10 to live.Patient: What do you mean, 10? 10 what? Months? Weeks?!"Doctor: Nine.']

        
        cmd1 = ['tell a joke', 'tell me a joke', 'say something funny', 'tell something funny']
        cmd2 = ['open youtube', 'i want to watch a video', 'play a video']
        cmd3 = ['who made you', 'who created you']

        if(user_input in greetings): 
            return random.choice(greetings)
        elif(user_input in cmd3):
            return random.choice(creator)
        elif(user_input in cmd1):
            return random.choice(jokes)
        elif(user_input in cmd2):
            webbrowser.open("www.youtube.com/watch?v=dQw4w9WgXcQ")
            return "Haha"
        else:
            return "I didn't understand you once again."

    def convertUserVoiceToText(self, audio_file):
        try:
            return("Google Speech Recognition thinks you said " + self.r.recognize_google(audio_file))
        except sr.UnknownValueError:
            return("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            return("Could not request results from Google Speech Recognition service; {0}".format(e))

annoy = Annoying_response()
