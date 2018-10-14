# Program to get the weather at Glasgow and print some results
# Downloaded the Yahoo Weather API using: pip install weather-api
# Downloaded the Python Text to Speech using: sudo pip install pyttsx
# Downloaded the AWS Polly API using: pip install boto3

from weather import Weather, Unit
from difflib import SequenceMatcher

import random
import boto3
import pyttsx
from polly_talk import make_polly_talk

class Weather_find:

    def __init__(self):
        
        # Define the sarcasm lists categorised by weather
  
        sun = ["I hope you remembered the sunscreen this time or else you will look like a lobster again.",
        "Looks like it is your lucky day. It's a rare occurence in Glasgow."]

        cloud = ["It may rain or it may not. Guess you will have to find out by going outside.",
        "One more excuse for you to stay inside and play videogames by yourself."
        "Those clouds mean it might rain if it was not obvious already."]

        rain = ["Don't forget to get an umbrella.",
        "Looks like you will ruin your hair if you go out now, or make it worse for that matter.",
        "Someone will be soaking wet again, haha.",
        "Better stay inside today. It's not like you have any friends waiting for you."]

        back_up = ["Better stay inside today. It's not like you have any friends waiting for you.", 
        "It may rain or it may not. Guess you will have to find out by going outside."]
        
        condition = self.get_weather()

        outcome = self.similarity_checker(condition, sun, cloud, rain, back_up)

        make_polly_talk(outcome)

        #self.make_python_talk(outcome)

    def similar(self, a, b):
        """
        Calculates the similarity percentage for two strings. 
        """
        return SequenceMatcher(None, a, b).ratio()

    def get_weather(self):
        """
        Gets the weather in Glasgow
        """
        weather = Weather(unit=Unit.CELSIUS)
        location = weather.lookup_by_location('glasgow')
        condition = location.condition
        condition = condition.text
        return condition

    def make_python_talk(self, outcome):
        """
        Gets the Python Text to Speech API to read out the outcome.
        """
        engine = pyttsx.init()
        engine.say(outcome)
        engine.runAndWait()

    def similarity_checker(self, condition, sun, cloud, rain, back_up):
        """
        Check which list name better matched the weather in Glasgow
        """
        if self.similar(condition, "sun") > 0.5:
            return("It's sunny right now. {}".format(random.choice(sun)))
        elif self.similar(condition, "cloud") > 0.5:
            return("It's cloudy right now. {}".format(random.choice(cloud)))
        elif self.similar(condition, "rain") > 0.5:
            return("It's raining right now. {}".format(random.choice(rain)))
        else:
            return(random.choice(back_up))

weather = Weather_find()