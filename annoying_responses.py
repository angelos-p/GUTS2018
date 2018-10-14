import speech_recognition as sr
import random
import subprocess
import webbrowser

from music.recorder import AudioRecorder
from os import path
from polly_talk import make_polly_talk
from difflib import SequenceMatcher

class Annoying_response:

    def __init__(self):
        self.AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "output.wav")
        self.r = sr.Recognizer()
    
    def make_response(self, annoy_output):
        with sr.AudioFile(self.AUDIO_FILE) as source:
            audio = self.r.record(source)

        user_input = self.convertUserVoiceToText(audio)
        outcome = self.getResponse(user_input)
        annoy_output.put(outcome)        

    def checkIfExists(self, word_list, target):
        """
        Checks whether any of the words in the list exists in the string
        """
        for word in word_list:
            if word in target:
                return True
        return False


    def getResponse(self, user_input):
        """
        User input is a string converted from the audio file saved.
        """

        creator = ["I was created by the Chad Developers", "I was created by the winners of this Hackathon.", "Some guys whom I never got to know"]
        jokes = ['Can a kangaroo jump higher than a house? Of course, a house doesnt jump at all.', 
                'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.', 
                'Doctor: Im sorry but you suffer from a terminal illness and have only 10 to live.Patient: What do you mean, 10? 10 what? Months? Weeks?!"Doctor: Nine.',
                'Why does the keyboard work 24 hours. Because, it has two shifts.']
        
        cmd1 = ['joke', 'funny']
        cmd2 = ['youtube', 'video']
        cmd3 = ['made', 'created']

        if(self.checkIfExists(cmd1, user_input)): 
            return random.choice(jokes)
        elif(self.checkIfExists(cmd3, user_input)):
            return random.choice(creator)
        elif(self.checkIfExists(cmd2, user_input)):
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            return "Haha"
        else:
            return "Speak clearly for once."

    def convertUserVoiceToText(self, audio_file):
        try:
            return("Google Speech Recognition thinks you said " + self.r.recognize_google(audio_file))
        except sr.UnknownValueError:
            return("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            return("Could not request results from Google Speech Recognition service; {0}".format(e))
