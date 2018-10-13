import os, sys, json, time
from acrcloud.recognizer import ACRCloudRecognizer
from acrcloud.recognizer import ACRCloudRecognizeType


class SongRecognizer:
    
    def __init__(self):
        self.config = {
            'host':'identify-eu-west-1.acrcloud.com',
            'access_key':'68656320837e6d5930619a6e7eb28005',
            'access_secret':'mca8noI3mO1Sl7t39umBEVy8B32rWLil5dzeev7F',
            'recognize_type': ACRCloudRecognizeType.ACR_OPT_REC_AUDIO, # you can replace it with [ACR_OPT_REC_AUDIO,ACR_OPT_REC_HUMMING,ACR_OPT_REC_BOTH], The     SDK decide which type fingerprint to create accordings to "recognize_type".
            'debug':False,
            'timeout':10 # seconds
        }
    
    def recognize_song(self, file):
        re = ACRCloudRecognizer(self.config)
        print('Recognizing song')
        result = re.recognize_by_file(file, 0, 10)
        result = json.loads(result)
        success = result.get('status').get('msg')
        if success == 'Success':
            #print(result.get('metadata').get('music')[0])
            artist = result.get('metadata').get('music')[0].get('artists')[0].get('name')
            title = result.get('metadata').get('music')[0].get('title')
            offset = result.get('metadata').get('music')[0].get('play_offset_ms')
            duration = result.get('metadata').get('music')[0].get('duration_ms')
            print("duration_ms=" + str(ACRCloudRecognizer.get_duration_ms_by_file(file)))
            value = (artist, title, float(offset)/duration)
        else:
            value = None
        print(value)
        return value
        
