import pytesseract
from pytesseract import Output
import cv2
import pyautogui
import speech_recognition as sr
import pyttsx3
from difflib import SequenceMatcher as SM


#- Speech recognition
recognizer = sr.Recognizer()
microphone = sr.Microphone(device_index=0)

#- Text to speech
eng = pyttsx3.init()
eng.setProperty('rate', 140)
eng.setProperty('volume', 1.0)
list_voice = eng.getProperty('voices')
eng.setProperty('voice',list_voice[2].id)


#- Reconocer audio
def recognizeMicAudio():
    palabra = ''
    print('Escuchando...')

    with microphone as source:
        audio = recognizer.listen(source, phrase_time_limit=3)
        palabra = recognizer.recognize_google(audio, language='es-ES')
        print(palabra)
    return palabra

eng.say('Reconocimiento de pantalla activado')
eng.runAndWait()
palabra = recognizeMicAudio()


#- Reconocimiento de pantalla
img = pyautogui.screenshot()

d = pytesseract.image_to_data(img, lang='spa+eng', output_type=Output.DICT)
n_boxes = len(d['level'])

for i in range(n_boxes):
    x, y, text = (d['left'][i], d['top'][i], d['text'][i])

    if text != '' or text != ' ' or text != '   ' or text != '    ':
        print((i+1), 'X: ', x, 'Y: ', y, 'Text: ', text)
        print("Se van a comparar ",text," y ",palabra)

    similitud = SM(None, text, palabra).ratio()

    if similitud > 0.7:
        cadena = 'Palabra ' + palabra + ' encontrada, posicionando el cursos'
        eng.say(cadena)
        eng.runAndWait()

        pyautogui.moveTo(x,y,2)


