# DysApp

UPDATE: Model has been updated to take a page of handwritten text as an input (instead of sentences). Find updated code for the same in the SegmentationNN folder.

________________________________________

Pre-trained Models:

1. Handwritten Text Recognition:
Location- dys_UI/main/model/ (Trained on IAM + Dyagraphia dataset)

2. Gector:
Download- https://grammarly-nlp-data-public.s3.amazonaws.com/gector/roberta_1_gector.th
Location- dys_UI/main/gector/models/

3. Spello:
Download- https://haptik-website-images.haptik.ai/spello_models/en_large.pkl.zip
Location- dys_UI/main/

________________________________________________

DEPENDENCIES: Python 3.7.9

- tensorflow (version 2.4.0)
- torch (version 1.8.0)
- editdistance
- matplotlib
- cv2
- lmdb
- spello
- Fastpunct
- numpy
- allennlp (version 0.8.4)
- python-Levenshtein (version 0.12.0)
- transformers (version 2.2.2)
- scikit-learn (version 0.20.0)
- sentencepiece (version 0.1.91)

________________________________________________

Notes:

1. Download the gector model and put in the specified location. (If folder doesn't exist, create folder)
2. Download the spello model and put in the specidied location.
3. Delete any .DS_Store file (If found)
4. Delete any pycache file (If found)

________________________________________

REFERENCES:

1. https://github.com/githubharald/SimpleHTR
2. https://github.com/hellohaptik/spello
3. https://github.com/grammarly/gector
