# -*- coding: utf-8-*-
import requests
import logging

logger = logging.getLogger(__name__)

# Module metadata
PRIORITY = 3
WORDS = ["WEATHER", "TEMPERATURE", "FORECAST"]

def is_valid(text):
    """Check if text is valid for this module"""
    return any(word in text.upper() for word in WORDS)

def handle(text, mic, config):
    """Handle the weather request"""
    logger.debug("Handling weather request")
    
    location = config.get('location', {}).get('city', 'your area')
    api_key = config.get('weather', {}).get('api_key')
    
    if not api_key:
        mic.say("I don't have a weather API key configured")
        return
        
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            mic.say(f"The weather in {location} is {desc} with a temperature of {temp} degrees Celsius")
        else:
            mic.say("Sorry, I couldn't get the weather information")
            
    except Exception as e:
        logger.error(f"Weather API error: {e}")
        mic.say("I had trouble getting the weather information")
