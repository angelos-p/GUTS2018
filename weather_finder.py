# Program to get the weather at Glasgow and print some results
# Downloaded the Yahoo Weather API using: pip install weather-api
# Downloaded the Python Text to Speech using: sudo pip install pyttsx
# Downloaded the AWS Polly API using: pip install boto3

from weather import Weather, Unit
from difflib import SequenceMatcher

import random
import boto3
import pyttsx

class Weather_find:

    def __init__(self):
        
        # Define the sarcasm lists categorised by weather
        sun = ["I hope you remembered the sunscreen this time or else you will look like a lobster again.",
        "Looks like it is your lucky day. It's sunny in Glasgow.",
        "Don't forget to wear your hat or else your nose will look like a tomato again.",
        "Don't wear a jacket or you will get pit stains and everyone will be staring at you."]

        cloud = ["Just another day in Glasgow.",
        "It may rain or it may not. Guess you will have to find out by going outside.",
        "Cloudy again. One more excuse to stay in."
        "Those clouds mean it might rain if it was not obvious already."]

        rain = ["Don't forget to get an umbrella.",
        "Looks like you will ruin your hair if you go out now, or make it worse for that matter",
        "Someone will be soaking wet again, haha.",
        "Better stay inside today. It's not like you have any friends waiting for you."]
        
        condition = self.get_weather()

        outcome = self.similarity_checker(condition, sun, cloud, rain)

        self.make_polly_talk(outcome)

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

    def make_polly_talk(self, outcome):
        """
        Gets the AWS Polly API to read out the outcome.
        """
        polly_client = boto3.Session(
                aws_access_key_id="AKIAJLSAW3L7HUIICDXA",                     
                aws_secret_access_key="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",
                region_name='us-west-2').client('polly')

        response = polly_client.synthesize_speech(VoiceId='Matthew',
                        OutputFormat='mp3', 
                        Text = outcome)
            
        file = open('speech.mp3', 'w')
        file.write(response['AudioStream'].read())
        file.close()
 
    def make_python_talk(self, outcome):
        """
        Gets the Python Text to Speech API to read out the outcome.
        """
        engine = pyttsx.init()
        engine.say(outcome)
        engine.runAndWait()

    def similarity_checker(self, condition, sun, cloud, rain):
        """
        Check which list name better matched the weather in Glasgow
        """
        if self.similar(condition, "sun") > 0.5:
            return(sun[random.randrange(0, len(sun))])
        elif self.similar(condition, "cloud") > 0.5:
            return(cloud[random.randrange(0, len(cloud))])
        elif self.similar(condition, "rain") > 0.5:
            return(rain[random.randrange(0, len(rain))])

weather = Weather_find()