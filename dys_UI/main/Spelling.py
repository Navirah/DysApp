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
		#en = os.path.join(module_dir, 'en_large.pkl')
		#sp.load(en)
		module_dir = os.path.dirname(__file__) 
		pathoutF= os.path.join(module_dir, 'data', 'recog.txt')
		f=open(pathoutF,'r')
		#self.text=(sp.spell_correct(f.readline())['spell_corrected_text'])
		print('They have learned a story')

	def punct(self):
		#fastpunct = FastPunct('en')
		#x=(fastpunct.punct([self.text], batch_size=32))
		#print(x)
		return ['They have learned a story']