#Spello and FastPunct

from spello.model import SpellCorrectionModel
from fastpunct import FastPunct
import os

class spelling:
	def __init__(self):
		self.text=None

	def correct(self):
		sp = SpellCorrectionModel(language='en')
		module_dir = os.path.dirname(__file__) 
		en = os.path.join(module_dir, 'en_large.pkl')
		sp.load(en)
		#module_dir = os.path.dirname(__file__) 
		pathoutF= os.path.join(module_dir, 'gector','Output', 'HTR.txt')
		f=open(pathoutF,'r')
		self.text=(sp.spell_correct(f.readline())['spell_corrected_text'])
		f.close()
		pathoutF=os.path.join(module_dir,'gector','Output','Spello.text')
		f=open(pathoutF,'w')
		f.write(self.text)
		return pathoutF
		#print('They have learned a story')

	def punct(self):
		fastpunct = FastPunct('en')
		x=(fastpunct.punct([self.text], batch_size=32))
		#print(x)
		#return ['They have learned a story']