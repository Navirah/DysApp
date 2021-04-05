# DysApp

Models:

1. Handwritten Text Recognition:
Location- dys_UI/main/model/ (Trained on IAM + Dyagraphia dataset)

2. Gector:
Download- https://grammarly-nlp-data-public.s3.amazonaws.com/gector/roberta_1_gector.th
Location- dys_UI/main/gector/models/

3. Spello:
Download- https://haptik-website-images.haptik.ai/spello_models/en_large.pkl.zip
Location- dys_UI/main/

________________________________________________

Dependencies:

-tensorflow (version 2.4.0)
-torch (version 1.8.0)
-editdistance
-matplotlib
-cv2
-lmdb
-spello
-Fastpunct
-numpy
-allennlp (version 0.8.4)
-python-Levenshtein (version 0.12.0)
-transformers (version 2.2.2)
-scikit-learn (version 0.20.0)
-sentencepiece (version 0.1.91)
