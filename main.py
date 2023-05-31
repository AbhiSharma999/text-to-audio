from PyPDF2 import PdfReader
import pyttsx3

reader = PdfReader("sample.pdf")
page = reader.pages[1]
text = page.extract_text()
# print(page.extract_text())

engine = pyttsx3.init()

voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say(text)

# saving audio to file named as audio_file.mp3
engine.save_to_file(text, 'audio_file.mp3')
engine.runAndWait()