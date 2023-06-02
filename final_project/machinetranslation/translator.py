"""Simple Translation Tool"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """Translates English text input to French Text ouput"""
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

def french_to_english(french_text):
    """Translates French text input to English text output"""
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
