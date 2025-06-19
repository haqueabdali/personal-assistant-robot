#!/usr/bin/env python2
# -*- coding: utf-8-*-

import os
import sys
import logging
import yaml
import argparse

from src.tts import TTS
from src.stt import STT
from src.brain import Brain
from src.mic import Mic
from src.conversation import Conversation

# Set up logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class PersonalAssistant:
    def __init__(self, config_path):
        self.config = self._load_config(config_path)
        self._init_components()
        
    def _load_config(self, config_path):
        try:
            with open(config_path, "r") as f:
                return yaml.safe_load(f)
        except Exception as e:
            logger.error(f"Failed to load config: {e}")
            sys.exit(1)
    
    def _init_components(self):
        # Initialize speech components
        self.tts = TTS(self.config.get('tts_engine', 'espeak'))
        self.stt = STT(self.config.get('stt_engine', 'witai'), 
                      self.config.get('witai', {}).get('access_token'))
        
        # Initialize microphone
        self.mic = Mic(self.tts, self.stt)
        
        # Initialize brain (command processor)
        self.brain = Brain(self.mic, self.config)
        
        # Initialize conversation handler
        self.conversation = Conversation("JOHN", self.mic, self.brain, self.config)
    
    def run(self):
        try:
            greeting = f"Hello {self.config.get('first_name', '')}, how can I help you today?"
            self.mic.say(greeting)
            self.conversation.handle_forever()
        except KeyboardInterrupt:
            logger.info("Shutting down...")
            self.mic.say("Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Personal Assistant Robot')
    parser.add_argument('--config', default='config.yaml', help='Path to config file')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    args = parser.parse_args()
    
    if args.debug:
        logger.setLevel(logging.DEBUG)
    
    assistant = PersonalAssistant(args.config)
    assistant.run()
