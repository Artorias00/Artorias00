#programma per un  semplice assistente vocale
#program for a simple voice assisent
#made by Nicolò Francescon
#github: Artorias00

import speech_recognition as sr
from datetime import datetime
import time
from pyaudio import *
from playsound import playsound

#questa funzione converte un numero da stringa ad intero
def stringanumero(text):
    d = {"uno": 1,
         "due": 2,
         "tre": 3,
         "quattro": 4,
         "cinque": 5,
         "sei": 6,
         "sette": 7,
         "otto": 8,
         "nove": 9,
         "dieci": 10,
         "undici": 11,
         "dodici": 12,
         "tredici": 13,
         "quattordici": 14,
         "quindici": 15,
         "sedici": 16,
         "diciassette": 17,
         "diciotto": 18,
         "diciannove": 19,
         "vent": 20,
         "trent": 30,
         "quarant": 40,
         "cinquant": 50,
         "sessant": 60,
         "settant": 70,
         "ottant": 80,
         "novant": 90,
         "cento": 100}
    
    n = 0
    for e in d.keys():
        if e in text:
            n += d[e]
    return n 

#qui creiamo l'istanza per poter utilizzare il riconoscitore vocale di google
r = sr.Recognizer()

#qui possiamo dare al nostro assistente uno o più nomi
#consiglio di insesire una parola facile da scandire e con una consonante dura
#nel mio caso ho messo jarvis, sia maiuscolo che minuscolo perchè dipende da com'è inserita la parola del discorso
keyWord = "Jarvis"
keyWord2 = "jarvis"

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    while True:
        audio = r.listen(source)
#in questo momento ha appena filtrato il rumore ambientale e ha registrato l'audio
        try:
            text = r.recognize_google(audio, language="it-IT")
#qui il programma converte l'audio in testo
            print (text)
            if keyWord.lower() in text.lower() or keyWord2.lower() in text.lower():
#qui cerca se nel testo è presente la keyword per attivare l'assistente
                with sr.Microphone() as source:
                    print('dimmi')
                    audio = r.listen(source)
                    text = r.recognize_google(audio, language="it-IT")
                    print (text)
#da qui in poi ci sono le funioni, il programa uò esser velocizzato dicendo subito tutte le frasi
#ma è terribilmente dispendioso di tempo se lo si vuole utilizzare in un dispositivo raspberry
                    if text =='Che ore sono' or text =='che ore sono' or text =='che ora è' or text =='Che ora è':
                        now = datetime.now()
                        time = now.strftime("%H:%M:%S")
                        print("sono le", time)
                    if text == 'Che giorno è' or text == 'quanti ne abbiamo oggi' or text == 'quanti ne abbiamo'or text == 'quanti ne abbiamo oggi'or text == 'che giorno è':
                        now = datetime.now()
                        data = now.strftime("%m/%d/%Y")
                        print("oggi è il", data)
                    if text =='Imposta un timer' or text =='metti un timer' or text =='Metti un timer':
                        print ("quanti minuti?")
                        with sr.Microphone() as source:
                            r.adjust_for_ambient_noise(source)
                            audio = r.listen(source)
                            text = r.recognize_google(audio, language="it-IT")
                            num = int(text)
                            for i in range(num*60):
                                print(num*60-i)
                                time.sleep(1)
                            print("driiiiin")
                            quit()
                   # if text == "":
                #da qui in poi possiamo sbizzarrirsci con el nostre funzioni








        except Exception:
            pass
