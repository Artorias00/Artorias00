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
    stringa = ["Uno", "Due", "Tre", "Quattro", "Cinque", "Sei", "Sette", "Otto", "Nove", "Dieci", "Undici", "Dodici",
               "Tredici", "Quattordici"
        , "Quindici", "Sedici", "Diciassette", "Diciotto", "Diciannove", "Venti", "Venticinque", "Trenta",
               "Trentacinque", "Quaranta", "Quarantacinque"
        , "Cinquanta", "Cinquantacinque", "Sessanta"]
    numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 30, 35, 40, 45, 50, 55, 60]
    for i in range(28):
        if text == stringa[i]:
            num = numero[i]
            return num
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