from gtts import gTTS 
import os
def speechConversion():
    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'draft.txt')
    file = open(file_path, "r").read().replace("\n", " ")
    speech = gTTS(text = str(file), slow = False)
    audio_path=os.path.join(module_dir,'media','global.mp3')
    if not os.path.exists(audio_path):
        os.mkdir(audio_path)
    speech.save(audio_path)
    os.system('start'+audio_path)