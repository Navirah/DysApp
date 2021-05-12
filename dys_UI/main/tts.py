from gtts import gTTS 
import os
def speechConversion():
    module_dir = os.path.dirname(__file__)  
    file_path=os.path.join(module_dir,'gector','Output','result.txt')
    #file_path = os.path.join(module_dir, 'draft.txt')
    file = open(file_path, "r").read().replace("\n", " ")
    path=os.path.join(module_dir,'media','global.mp3')
    '''if os.path.exists(path):
        os.remove(path)
    f=open(path,'x')
    f.close()'''
    speech = gTTS(text = str(file), slow = False)
    #audio_path=os.path.join(module_dir,'media','global.mp3')
    #f=open(audio_path,'w')
    '''if not os.path.exists(audio_path):
        os.mkdir(audio_path)'''
    speech.save(path)
    #os.system('start'+audio_path)