#import argparse
import json

from cv2 import cv2
import editdistance
from path import Path

from .DataLoaderIAM import DataLoaderIAM, Batch
from .Model import Model, DecoderType
from .SamplePreprocessor import preprocess

#from .infer import segment
import os

from .WordSegmentation import wordSegmentation
from .WordSegmentation import prepareImg

from .Spelling import spelling

from .gector.predict import grammar_correct

from .segmentationNN.process import Segment



class FilePaths:
	#"filenames and paths to data"
	#module_dir = os.path.dirname(__file__)  # get current directory
	#file_path = os.path.join(module_dir, 'baz.txt')
	fnCharList = ''
	fnSummary = ''
	def __init__(self):
		module_dir = os.path.dirname(__file__) 
		self.fnCharList = os.path.join(module_dir, 'model', 'charList.txt')
		self.fnSummary = os.path.join(module_dir, 'model', 'summary.json')
		self.fnInfer= os.path.join(module_dir, 'pictures', 'trail.png')

    #fnInfer = '../data/pragatitest.JPG'
    #fnCorpus = '../data/corpus.txt'

def fetchforinfer(pathimg):
    return Segment(pathimg)
    '''
    img = prepareImg(cv2.imread(pathimg), 50)
    res = wordSegmentation(img, kernelSize=25, sigma=11, theta=7, minArea=100)

    print('Segmented into %d words'%len(res))

    words=[]
    for (j, w) in enumerate(res):
        (wordBox, wordImg) = w
        (x, y, w, h) = wordBox
        words.append(wordImg)
        #cv2.imwrite('../out/pg.jpg/%d.png'%(j), wordImg) # save word
        #cv2.rectangle(img,(x,y),(x+w,y+h),0,1) 
    return [words]'''
    

def infer(model, fnImg):
    "recognize text in image provided by file path"
    module_dir = os.path.dirname(__file__) 
    pathoutF= os.path.join(module_dir, 'gector','Output', 'HTR.txt')
    outF = open(pathoutF, "w")

    #img = preprocess(cv2.imread(fnImg, cv2.IMREAD_GRAYSCALE), Model.imgSize)
    #img2= preprocess(cv2.imread("../data/2.png", cv2.IMREAD_GRAYSCALE), Model.imgSize)

    pagewiselist=fetchforinfer(fnImg)
    #print(len(pagewiselist))
    #print(type(pagewiselist[0]))
    for pagesin in range(len(pagewiselist)):
        for (i,j) in enumerate(pagewiselist[pagesin]):
            pagewiselist[pagesin][i]=preprocess(j,Model.imgSize)
        batch = Batch(None, pagewiselist[pagesin])
        (recognized, probability) = model.inferBatch(batch, True)

        for i in range(len(recognized)):
            outF.write(recognized[i])
            outF.write(" ")
            print("Recognized:",recognized[i]," ; Probability:",probability[i])
        outF.write('\n')
    
    outF.close()
    
    

    s=spelling() 
    pathspello=s.correct() #s will contain pathoutF
    outpath=grammar_correct(pathspello) #path to final result
    f=open(outpath,'r')
    corrected=f.readlines()
    #corrected=s.punct()
    print(corrected[0])
    return corrected[0]
    #outF1 = open("../data/corrected.txt", "w+")
    #outF1.write(corrected[0])
    #outF1.close()

    #print(f'Recognized: "{recognized[0]}","{recognized[1]}"')
    #print(f'Probability: {probability[0]},{probability[1]}')


def runmodel(fpath):
	#args = tools.argparser.parse_args()
	'''if args.decoder == 'bestpath':
		decoderType = DecoderType.BestPath
	elif args.decoder == 'beamsearch':
		decoderType = DecoderType.BeamSearch
	elif args.decoder == 'wordbeamsearch':
		decoderType = DecoderType.WordBeamSearch'''

	decoderType = DecoderType.BestPath

	F=FilePaths()
	model = Model(open(F.fnCharList).read(), decoderType, mustRestore=True)
	result = infer(model, fpath)
	return result