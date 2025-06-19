# -*- coding: utf-8-*-
import logging
import time

logger = logging.getLogger(__name__)

class Mic:
    def __init__(self, tts, stt):
        self.tts = tts
        self.stt = stt
        self.hotword = "john"
        
    def say(self, text):
        """Speak the given text"""
        self.tts.say(text)
        
    def passive_listen(self, timeout=5):
        """Listen for hotword"""
        logger.debug(f"Listening for hotword '{self.hotword}'...")
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            text = self.stt.listen(timeout=1)
            if text and self.hotword in text:
                logger.debug(f"Hotword detected: {text}")
                return True
                
        return False
        
    def active_listen(self, timeout=10):
        """Listen for commands after hotword"""
        self.say("How can I help you?")
        return self.stt.listen(timeout=timeout)
