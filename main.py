import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
recognizer = sr.Recognizer()

def record_text():
     # Loop in case of error
    while(1):
        try:
             # use microphone as source of input
            with sr.Microphone() as source:
                # Prepare reconizer to recieve input
                recognizer.adjust_for_ambient_noise(source, duration=0.2)

                print("I'm listening")

                # Listen's for user input
                audio_data = recognizer.listen(source)

                # Using google to recognize audio
                MyText = recognizer.recognize_google(audio_data)

                return MyText

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        
        except sr.UnknownValueError:
            print("Unknown Error Occured")
    return

def output_text():
    f = open("output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()
    return

while(1):
    text = record_text()
    output_text()

    print("Wrote text")
