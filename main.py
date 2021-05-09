import pyttsx3
import speech_recognition as sr

recipe_name = "recipe_" + input("What would you like to cook today?") + ".txt"
recipe = open(recipe_name, "r+")
recipe1 = open(recipe_name, "r+")

NumOfLines = len(recipe1.readlines())


def SpeechOut(sentence):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 25)
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    engine.say(sentence)
    engine.runAndWait()


def DoneForNextStep():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        audio = r.listen(source)
    done = r.recognize_google(audio)
    return done


print("\nLet\'s start \n")

def AskTillDone():
    try:
        done1 = DoneForNextStep()
        if done1 != "done":
            SpeechOut("You said something I didn't recognize. Please say \"done\" clearly if you have completed the step")
            AskTillDone()
    except sr.UnknownValueError:
        AskTillDone()

def ReadRecipe(i):
    line = recipe.readline()
    print(line)
    SpeechOut(line)
    i += 1

    AskTillDone()

    if i < NumOfLines:
        ReadRecipe(i)
    else:
        SpeechOut("Well Done. Now enjoy your food.")


ReadRecipe(0)
