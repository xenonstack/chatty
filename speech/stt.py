'''
Created on 13-Jul-2015

@author: abhay
'''

class STT():
    '''
    Speech audio to text conversion.
    '''

    def __init__(self):
        pass
    
    def load(self, audio_file= '/tmp/chatty-shout.wav'):
        fd = open(audio_file, 'rb')
        audio_binary = ''
        try:
            byte = fd.read(1)
            while byte != '':
                audio_binary += byte
                