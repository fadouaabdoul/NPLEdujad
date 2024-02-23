import sys
import string
import speech_recognition as sr
import gramformer

def speech_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)  # Record the audio file

    try:
        text = recognizer.recognize_google(audio_data)  # Use the Google Web Speech API for recognition
        return text
    except sr.UnknownValueError:
        return "Speech recognition could not understand the audio"
    except sr.RequestError:
        return "Speech recognition service is unavailable"

#%%

try:
    result = speech_to_text("data/Test3.wav")
    print("Transcribed Text:", result)
except ValueError:
    print('Error importing your file. Try uploading a file with the extension ".wav", or press on record to record a '
          'new tape')
    sys.exit()
# Initialize Gramformer (adjust models parameter if needed)
gf = gramformer.Gramformer(models=1)

while True:
    # Get user input
    user_input = result
    print("Do you want to:")
    print("      1. Correct this text")
    print("      2. Exit the program")

    choice = input("Enter your choice: ")
    if choice == '1':

        corrected_sentences = gf.correct(user_input)

        # Compare original and corrected versions to highlight potential mistakes


        for original, corrected in zip(user_input, corrected_sentences):
            if corrected is None:  # Check if Gramformer returned None
                print(f"No corrections suggested for: '{original}'")
            else:
                if original != corrected:
                    translator = str.maketrans('', '', string.punctuation)
                    original_words = result.translate(translator).split()
                    corrected_words = corrected.translate(translator).split()

                    mistakes = [word for word, corrected_words in zip(original_words, corrected_words) if word != corrected_words]

                    print(f"Your transcribed text: '{result}'")
                    if mistakes:
                        print(f'Your mistakes are: ')
                        for mistakes in mistakes:
                            print(f'- {mistakes}')
                    else:
                        print('There is no mistakes in your text')
                    print(f"Suggested Correction: '{corrected}'")
                    print("-" * 30)  # Separator between different corrections
                else:
                    print(f"Cannot process this text: '{original}'")
    if choice == '2':
            break

    # Process the input with Gramformer

print("Exiting the program.")