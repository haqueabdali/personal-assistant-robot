# -*- coding: utf-8-*-
import os
import logging
import subprocess
from gtts import gTTS

logger = logging.getLogger(__name__)

class TTS:
    def __init__(self, engine='espeak'):
        self.engine = engine
        
    def say(self, text, lang='en'):
        """Convert text to speech and play it"""
        logger.debug(f"TTS: {text}")
        
        if self.engine == 'espeak':
            self._espeak(text)
        elif self.engine == 'google':
            self._gtts(text, lang)
        else:
            logger.warning(f"Unknown TTS engine: {self.engine}")
            self._espeak(text)
    
    def _espeak(self, text):
        """Use eSpeak for TTS"""
        try:
            subprocess.call(['espeak', '-ven+f3', '-k5', '-s150', text])
        except OSError:
            logger.error("eSpeak not found. Please install it.")
            raise
    
    def _gtts(self, text, lang):
        """Use Google TTS"""
        try:
            tts = gTTS(text=text, lang=lang, slow=False)
            tts.save('/tmp/response.mp3')
            subprocess.call(['mpg123', '/tmp/response.mp3'])
            os.remove('/tmp/response.mp3')
        except Exception as e:
            logger.error(f"Google TTS failed: {e}")
            self._espeak(text)
