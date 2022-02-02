# Reconocimiento Palabras en Pantalla

Aplicacion que reconoce palabras en la pantalla. Utiliza reconocimiento de voz y reconocimiento optico de caracteres (OCR).

## Funcionamiento
Al iniciar la apliacion se abre el microfono para introducir una palabra por voz. Una vez reconocida la palabra se busca en la pantalla, al encontrarse la palabra el cursor del mouse se posiciona en dicha palabra.


------------

**Se programo en python 3 y se utilizaron las siguientes librerias:**

**pytesseract:** Reconocimiento optico de caracteres (OCR).
**pyautogui:** Para posicionar el cursor del mouse en las coordenadas de la palabra encontrada.
**speech_recognition:** Reconocimiento de voz (speech to text)
**pyttsx3:** Text to speech
