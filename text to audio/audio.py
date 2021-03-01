import os
from gtts import gTTS
text = 'Hallo! ich bien Ariel und whone in Argentinien und habe Fünfundvierzig jahre alt, bye!'
#text = 'Leandro, dejá de hacer sentadillas con tu novia en las redes sociales.'

#lenguaje en el cual queremos convertir
lang = 'de'

obj = gTTS(text = text, lang = lang, slow = False)
obj.save("audio.mp3")

#Play al audio convertido
os.system("audio.mp3")