# -*- coding: utf-8-*-
import logging
import time

logger = logging.getLogger(__name__)

class Conversation:
    def __init__(self, wake_word, mic, brain, config):
        self.wake_word = wake_word.lower()
        self.mic = mic
        self.brain = brain
        self.config = config
        
    def handle_forever(self):
        """Main conversation loop"""
        logger.info("Starting conversation handler")
        
        while True:
            try:
                # Wait for wake word
                if self.mic.passive_listen():
                    # Listen for command
                    command = self.mic.active_listen()
                    if command:
                        self.brain.query(command)
                    else:
                        self.mic.say("I didn't catch that")
                        
                time.sleep(0.1)
                
            except KeyboardInterrupt:
                logger.info("Conversation interrupted")
                break
            except Exception as e:
                logger.error(f"Conversation error: {e}")
                time.sleep(1)
