# -*- coding: utf-8-*-
import logging
import requests
import speech_recognition as sr

logger = logging.getLogger(__name__)

class STT:
    def __init__(self, engine='witai', witai_token=None):
        self.engine = engine
        self.witai_token = witai_token
        self.recognizer = sr.Recognizer()
        
    def listen(self, timeout=3, phrase_time_limit=5):
        """Listen for speech and convert to text"""
        with sr.Microphone() as source:
            logger.debug("Adjusting for ambient noise...")
            self.recognizer.adjust_for_ambient_noise(source)
            
            try:
                logger.debug("Listening...")
                audio = self.recognizer.listen(source, timeout=timeout, 
                                             phrase_time_limit=phrase_time_limit)
                return self._recognize(audio)
            except sr.WaitTimeoutError:
                logger.debug("Listening timed out")
                return None
            except Exception as e:
                logger.error(f"STT Error: {e}")
                return None
    
    def _recognize(self, audio):
        """Recognize speech using configured engine"""
        try:
            if self.engine == 'witai' and self.witai_token:
                logger.debug("Using Wit.ai for speech recognition")
                text = self.recognizer.recognize_wit(audio, key=self.witai_token)
                return text.lower()
            else:
                logger.debug("Using Google speech recognition")
                text = self.recognizer.recognize_google(audio)
                return text.lower()
        except sr.UnknownValueError:
            logger.debug("Could not understand audio")
            return None
        except sr.RequestError as e:
            logger.error(f"STT service error: {e}")
            return None
