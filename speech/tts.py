'''
Created on 13-Jul-2015

@author: abhay
'''

from gtts import gTTS
from pydub import AudioSegment

class TTS():
    '''
    Text to speech conversion.
    '''
    
    text = ''
    lang = 'en'

    def __init__(self):
        pass
    
    def set_language(self, lang):
        self.lang = lang
        return self
    
    def load(self, text):
        self.text = text
        return self
    
    def mp3(self, path='/tmp/chatty-shout.mp3'):
        tts = gTTS(text= self.text, lang= self.lang)
        tts.save(path)

    def wav(self, path='/tmp/chatty-shout.wav'):
        self.mp3(path + '.mp3')
        audio_file = AudioSegment.from_mp3(path + '.mp3')
        audio_file.export(path, format='wav')
        

''' eof '''