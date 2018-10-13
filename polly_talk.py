# Program that makes use of the Polly API
import boto3

def make_polly_talk(outcome):
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