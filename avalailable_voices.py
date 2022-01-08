import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty("voices")

vozes = []

def getVoz():
    """ Function to list all available languages in the system.
    :rtype: list
    """
    for voice in voices:
        pvoz = str(voice.id) + str(voice.name) + str(voice.languages)
        vozes.append(pvoz)
    return vozes

if __name__ == "__main__":
    getVoz()