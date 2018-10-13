# Program that makes use of the Polly API
import boto3
import subprocess

def make_polly_talk(outcome, speed=85):
        """
        Gets the AWS Polly API to read out the outcome.
        """
        polly_client = boto3.Session(
                aws_access_key_id="",                     
                aws_secret_access_key="",
                region_name='us-west-2').client('polly')
        text = '<speak><prosody rate="{}%">{}</prosody></speak>'.format(speed, outcome)
        response = polly_client.synthesize_speech(VoiceId='Matthew',
                        OutputFormat='mp3',
                        TextType='ssml', 
                        Text = text)
        file = open('speech.mp3', 'w')
        file.write(response['AudioStream'].read())
        file.close()
        subprocess.call(['afplay', 'speech.mp3'])