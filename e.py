# import threading

# def speak(message):
#     # Simulate speaking the message
#     print("Speaking:", message)

# def index(request):
#     # Call the asynchronous function to get the data
#     data = get_data()
#     # Return JSON response
#     response = 'response'

#     # Start a separate thread to speak the message
#     threading.Thread(target=speak, args=("Hello, World!",)).start()

#     print(response)

# a = ['a', 'b', 'c', 'd']

# print(a[-2:])



# import elevenlabs
# elevenlabs.set_api_key("e0c96d185e2e75e056f2b3d21e4f2652")


# voice = elevenlabs.Voice(
#     voice_id="EXAVITQu4vr4xnSDxMaL",
#     settings = elevenlabs.VoiceSettings(
#         stability=0,
#         similarity_boost=0.75
#     )
# )

# audio = elevenlabs.generate(
#         text="Hello this is blindally, and currently you are in home page.",
#         voice = voice
#     )
# elevenlabs.play(audio)

# import pyttsx3

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')

# from googletrans import Translator
# details = ['Hello', 'Whats up']
# print(len(details))
# if len([details]) >= 2: 
#     print('Here 1')
#     result = Translator().translate(details, dest='tl')
# else:
#     print('Here 2')
#     result = Translator().translate(' '.join(details), dest='tl')

# print('This is inside tagalog.', result.text)

# print(str(['Hello']))

# for voice in voices:
#     print(voice, voice.id)
#     engine.setProperty('voice', voice.id)
#     engine.say("Hello World!")
#     engine.runAndWait()

from googletrans import Translator

translator = Translator()


result = Translator().translate('Our team then decided to make a sample website that contains the technologies that will help website become accessible and help blind people in interacting with the website easily by removing technological barrier.', dest='tl')
print(result.text)


def translate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

# Example usage
text_to_translate = "Hello, how are you?"
translated_text = translate_text(text_to_translate, target_language='es')
print(f"Original text: {text_to_translate}")
print(f"Translated text: {translated_text}")

# class Hello:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def func_name(self):
#         print('It went here')
#         print('This is the none', self.name)

#     def func_age(self):
#         print('This is the self.age', self.age)


# Hello('marvelous', 19).func_age()




# import os
# from dotenv import load_dotenv

# import elevenlabs
# load_dotenv()
# elevenlabs_api = elevenlabs.set_api_key(os.getenv('ELEVENLABS_API_KEY'))

# from elevenlabs import generate, play, voices, Voice, VoiceSettings
# # [print(voice) for voice in voices()]


# audio = generate(
#     text='Hello, What are you doing today?',
#     voice=Voice(
#         voice_id='EXAVITQu4vr4xnSDxMaL',
#         settings=VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0)
#     )
# )
# play(audio)

# import os

# import gtts
# from gtts import gTTS
# from playsound import playsound
# text = 'Kamusta kayo lahat? Ako nga pala si blind ally ang inyong tagapaglingkod.'
# audio = gTTS(text, lang='tl') # 1. com.mx, 2. pt
# audio.save('audio/ex.mp3')
# playsound('audio/ex.mp3')

# import multiprocessing
# import pyttsx3
# import keyboard

# def sayFunc(phrase):
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 160)
#     engine.say(phrase)
#     engine.runAndWait()

# def say(phrase):
# 	# if __name__ == "__main__":
# 		p = multiprocessing.Process(target=sayFunc, args=(phrase,))
# 		p.start()
# 		while p.is_alive():
# 			if keyboard.is_pressed('q'):
# 				p.terminate()
# 			else:
# 				continue
# 		p.join()

# say("this process is running right now")

# import datetime

# # Get current date and time
# current_datetime = datetime.datetime.now()

# # Format the time in 12-hour format
# time_12_format = current_datetime.strftime("%I:%M %p")

# # Format the date in a more readable format
# date_readable_format = current_datetime.strftime("%B %d, %Y")

# # Print the formatted date and time
# print("Current time (12-hour format):", time_12_format)
# print("Formatted date:", date_readable_format)


# import os
# from dotenv import load_dotenv
# import requests
# from requests import post
# import base64
# import json

# load_dotenv()
# class AudioBook:
#     def __init__(self) -> None:  
#         self.client_id = os.getenv('CLIENT_ID')
#         self.client_secret = os.getenv('CLIENT_SECRET')
#         print(self.client_id, self.client_secret)

#     def get_token(self):
#         auth_string = self.client_id + ":" + self.client_secret
#         auth_bytes = auth_string.encode("utf-8")
#         auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

#         url = "https://accounts.spotify.com/api/token"

#         headers = {
#             "Authorization": "Basic " + auth_base64,
#             "Content-Type": "application/x-www-form-urlencoded"
#         }

#         data = {"grant_type": "client_credentials"}
#         result = post(url, headers=headers, data=data)
#         json_result = json.loads(result.content)
#         token = json_result["access_token"]
#         print('This is the Token', str(token))
#         return token
        
# print(AudioBook().get_token())
# from playsound import playsound
"""
import gtts
from gtts import gTTS
from playsound import playsound
text = 'Kamusta kayo lahat? Ako nga pala si blind ally ang inyong tagapaglingkod.'
audio = gTTS(text, lang='tl') # 1. com.mx, 2. pt
audio.save('audio/ex.mp3')
playsound('audio/ex.mp3')
"""
# import os
# from dotenv import load_dotenv

# load_dotenv()
# print(os.getenv('SECRET_KEY'))

# print(help(gtts.lang))

"""from gtts.lang import tts_langs
# print(tts_langs())

for k, v in tts_langs().items():
    print(k, v)"""

'''
    >>> from gtts import gTTS
>>> from io import BytesIO
>>>
>>> mp3_fp = BytesIO()
>>> tts = gTTS('hello', lang='en')
>>> tts.write_to_fp(mp3_fp)
>>>
>>> # Load `mp3_fp` as an mp3 file in
>>> # the audio library of your choice
'''




