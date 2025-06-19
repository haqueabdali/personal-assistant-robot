# -*- coding: utf-8-*-
import logging
import importlib
import pkgutil
import os

logger = logging.getLogger(__name__)

class Brain:
    def __init__(self, mic, config):
        self.mic = mic
        self.config = config
        self.modules = self._load_modules()
        
    def _load_modules(self):
        """Dynamically load all modules from the modules directory"""
        modules = []
        module_path = os.path.join(os.path.dirname(__file__), 'modules')
        
        for loader, name, is_pkg in pkgutil.iter_modules([module_path]):
            try:
                module = importlib.import_module(f'src.modules.{name}')
                if hasattr(module, 'WORDS'):
                    logger.debug(f"Loaded module: {name}")
                    modules.append(module)
            except Exception as e:
                logger.warning(f"Failed to load module {name}: {e}")
                
        # Sort by priority (higher first)
        modules.sort(key=lambda m: getattr(m, 'PRIORITY', 0), reverse=True)
        return modules
        
    def query(self, text):
        """Process the user input through all modules"""
        logger.debug(f"Processing query: {text}")
        
        for module in self.modules:
            if module.is_valid(text):
                logger.debug(f"Module {module.__name__} can handle this query")
                try:
                    module.handle(text, self.mic, self.config)
                    return
                except Exception as e:
                    logger.error(f"Module {module.__name__} failed: {e}")
                    self.mic.say("I encountered an error processing that request")
                    return
                    
        logger.debug("No module could handle the query")
        self.mic.say("I'm not sure how to help with that")
