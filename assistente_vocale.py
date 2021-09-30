# programma per un semplice assistente vocale
# program for a simple voice assisent
# made by Nicolò Francescon
# github: Artorias00

import re
import time
from datetime import datetime

import speech_recognition as sr
from playsound import playsound
from pyaudio import *

# qui creiamo l'istanza per poter utilizzare il riconoscitore vocale di google
r = sr.Recognizer()

# qui possiamo dare al nostro assistente uno o più nomi
# consiglio di insesire una parola facile da scandire e con una consonante dura
# nel mio caso ho messo jarvis, sia maiuscolo che minuscolo perchè dipende da com'è inserita la parola del discorso
keyWord = "goldrake"
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    while True:
        audio = r.listen(source)
        # in questo momento ha appena filtrato il rumore ambientale e ha registrato l'audio
        try:
            text = r.recognize_google(audio, language="it-IT")
        except sr.RequestError:
            print("nessuna connessione")
            continue
        except sr.UnknownValueError:
            continue
        # qui il programma converte l'audio in testo
        print(text)
        if keyWord.lower() in text.lower():
            # da qui in poi ci sono le funioni, il programa uò esser velocizzato dicendo subito tutte le frasi
            # ma è terribilmente dispendioso di tempo se lo si vuole utilizzare in un dispositivo raspberry
            if (
                "che ore sono" in text.lower()
                or "che ora è" in text.lower()
            ):
                now = datetime.now()
                time = now.strftime("%H:%M:%S")
                print("sono le", time)

            elif (
                "quanti ne abbiamo" in text.lower()
                or "che giorno è" in text.lower()
            ):
                now = datetime.now()
                data = now.strftime("%m/%d/%Y")
                print("oggi è il", data)

            elif (
                "imposta un timer" in text.lower()
                or "metti un timer" in text.lower()
            ):
                minuti = 0
                secondi = 0
                matches = re.findall(r"(\d+)\s+(\w+)", text)
                for match in matches:
                    num, unit = match
                    if "un" in num.lower():
                        num = 1
                    if unit == "minuti":
                        minuti = int(num)
                    elif unit == "secondi":
                        secondi = int(num)
                for i in range(minuti * 60 + secondi):
                    print(f"minuti: {minuti}")
                    print(f"secondi: {secondi}")
                    secondi -= 1
                    if secondi == 0:
                        minuti -= 1
                        secondi = 60
                    time.sleep(1)
                print("driiiiin")
            elif (
                    "attiva citazioni" in text.lower()
                    or "metti citazioni" in text.lower()
            ):
                #qui facciamo partire il programma delle cit
                pass
            elif (
                    "quanti gradi ci sono" in text.lower()
                    or "qual è  la temperatura" in text.lower()
            ):
                pass
            elif (
                    "dimmene una" in text.lower()
                    or "dimmi una battuta" in text.lower()
                    or "" in text.lower()
            ):
                pass
