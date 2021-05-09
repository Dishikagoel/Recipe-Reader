# RecipeReader

This is a simple Recipe Reader which reads out the recipe line by line from a text file and only reads next line after the user have said "done". This project used 2 python libraries : pyttsx3 and speech_recognition.

## Setting Up

To install pyttsx3:
```
$ pip install pyttsx3
```

To install SpeechRecognition:
```
$ pip install SpeechRecognition
```
#### Note: Internet Connection will be required as Google Web Speech API is used with SpeechRecognition.

To Install PyAudio (for microphone access):

On Debian Linux:
```
$ sudo apt-get install python-pyaudio python3-pyaudio
```
On Windows:
```
$ pip install pyaudio
```
On macOS:
```
$ brew install portaudio
$ pip install pyaudio
```

## Testing the code:

A plaintext file (.txt) is included for example. To setup a plaintext file, use the name `recipe_NameOfTheItem.txt` (replace `NameOfTheItem` with the name of the food item). In the plaintext file separate the lines using `ENTER`. Do not give empty line breaks. When prompted to enter the recipe name (while running the code) enter the `NameOfTheItem`. After a line has been read out, wait for some time and say "done" to get the next line.

## References 

1. pyttsx3 documentation: https://pypi.org/project/pyttsx3/

2. SpeechRecognition documentation: https://pypi.org/project/SpeechRecognition/

3. PyAudio documentation: https://pypi.org/project/PyAudio/

4. Pancake recipe: https://www.bbc.co.uk/food/recipes/fluffyamericanpancak_74828
