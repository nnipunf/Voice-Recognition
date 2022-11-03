import speech_recognition as sr
listener = sr.Recognizer()

import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pyaudio

init_commands = ['hello', 'boss', 'hello boss']

def talk(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    print(rate)
    engine.setProperty('rate', 125)
    volume = engine.getProperty('volume')
    print(volume)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'boss' in command:
                command = command.replace('boss', '')
                print(command)
    except Exception as e:
        print(e)
        print('sorry')
        command=''
    return command

def hello_boss():
    try:
        with sr.Microphone() as source:
            print('Boss is Listening...')
            vo = listener.listen(source)
            com = listener.recognize_google(vo)
            com = com.lower()
            print(com)
            if com in init_commands:
                talk('Yes, I am here. Whats your command sir')
                return True
            # elif 'boss' in com:
            #     talk('Yes, I am here. Whats your command sir')
            #     return True
            else:
                return False
    except Exception as e:
        print(e)
        pass
    return False

def otherqueries():
    try:
        with sr.Microphone() as source:
            print('Do you have any other queries ')
            talk('Do you have any other queries ?')
            print('other command listening...')
            voOther = listener.listen(source)
            comOther = listener.recognize_google(voOther)
            comOther = comOther.lower()
            print('command to me is '+comOther)
            if 'yes' in comOther:
                return True
            elif 'ok' in comOther:
                return True
            elif 'okay' in comOther:
                return True
            elif 'i have' in comOther:
                return True
            else:
                return False
    except Exception as e:
        print(e)
        pass
    return False
def run_boss_again():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        try:
            print(command)
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        except Exception as e:
            print(e)
            talk('Sorry i miss the name.Please tell anyother porson name for details')
            pass
    elif 'what is' in command:
        try:
            print(command)
            person = command.replace('what is', '')
            info = wikipedia.page(person, 1)
            print(info.content)
            talk(info.content)
        except Exception as e:
            print(e)
            talk('Sorry i miss the Command.Please tell anyting else for details')
            pass
    elif 'today' in command:
        dateT = datetime.datetime.now().strftime('%m/%d/%Y, %I:%M %p')
        talk(dateT)
    elif 'love me' in command:
        talk('Yes, I love you dear! Will you marry me?')
    elif 'love you' in command:
        talk('I love you too! Are you free to night?')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Sorry sir, please say the command again')

    if(otherqueries()):
        talk('Okay tell me againg')
        run_boss_again()
    else:
        talk('Thank you sir. Bye for now. have a good time.')


def run_boss():
    if(hello_boss()):
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print('Current time is ' + time)
            talk('Current time is ' + time)
        elif 'who is' in command:
            try:
                print(command)
                person = command.replace('who is', '')
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)
            except Exception as e:
                print(e)
                talk('Sorry i miss the name.Please tell anyother porson name for details')
                pass
        elif 'what is' in command:
            try:
                print(command)
                person = command.replace('what is', '')
                info = wikipedia.page(person, 1)
                print(info.content)
                talk(info.content)
            except Exception as e:
                print(e)
                talk('Sorry i miss the Command.Please tell anyting else for details')
                pass
        elif 'today' in command:
            dateT = datetime.datetime.now().strftime('%m/%d/%Y, %I:%M %p')
            talk(dateT)
        elif 'love me' in command:
            talk('Yes, I love you dear! Will you marry me?')
        elif 'love you' in command:
            talk('I love you too! Are you free to night?')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        else:
            talk('Sorry sir, please say the command again')

        if(otherqueries()):
            talk('Okay tell me againg')
            run_boss_again()
        else:
            talk('Thank you sir. Bye for now. have a good time.')



run_boss()

while True:
    run_boss()
