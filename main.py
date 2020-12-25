import smtplib  #simple mail transfer protocol library
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
talker = pyttsx3.init()

email_list = {"thisara": "madushantjg@gmail.com"}

def talk(text):
    talker.say(text)
    talker.runAndWait()

def speech_to_text():
        try:
            with sr.Microphone() as source:
                print('Listening..')
                voice = listener.listen(source)
                message = listener.recognize_google(voice)
                print(message)
                return message.lower()
        except:
            pass


def get_mail_info():
    talk("give me the receiver's email address")
    name = speech_to_text()
    address = email_list["name"]

    talk("give me the subject of email")
    subject = speech_to_text()

    talk("give me the message")
    content = speech_to_text()

    sendEmail(address, subject, content)


def sendEmail(address, subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('jgtmadushan@gmail.com', 'Jg8612036@')
    email = EmailMessage()
    email['From'] = 'jgtmadushan@gmail.com'
    email['To'] = address
    email['Subject'] = subject
    email.set_content(content)

    server.send_message(email)

get_mail_info()