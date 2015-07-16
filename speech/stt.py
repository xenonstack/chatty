'''
Created on 13-Jul-2015

@author: abhay
'''

import speech_recognition as sr

class STT():
    '''
    Speech audio to text conversion.
    '''

    audio_file = '/tmp/chatty-shout.wav'

    def __init__(self):
        pass
    
    def load(self, audio_file= '/tmp/chatty-shout.wav'):
        self.audio_file = audio_file
    
    def transcript(self):
        r = sr.Recognizer()
        with sr.WavFile(self.audio_file) as source:
            audio = r.record(source)
        try:
            list = r.recognize(audio,True)
            print("Possible transcriptions:")
            for prediction in list:
                print(" " + prediction["text"] + " (" + str(prediction["confidence"]*100) + "%)")
        except LookupError:
            print("Could not understand audio")

''' eof '''