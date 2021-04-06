#Word Segmentation NN

#import argparse

import torch
from path import Path
import os

from .dataloader import DataLoaderImgFile
from .eval import evaluate
from .net import WordDetectorNet
from .visualization import FetchImages
import cv2



def segment(filepath=None):
    #parser = argparse.ArgumentParser()
    #parser.add_argument('--device', choices=['cpu', 'cuda'], default='cpu')
    #args = parser.parse_args()

    net = WordDetectorNet()
    module_dir = os.path.dirname(__file__) 
    wts = os.path.join(module_dir, 'modelSegment', 'weights')
    net.load_state_dict(torch.load(wts, map_location='cpu'))
    net.eval()
    net.to('cpu')

    loader = DataLoaderImgFile(Path(filepath), net.input_size, 'cpu')
    res = evaluate(net, loader, max_aabbs=1000)

    pagewise=[]

    for i, (img, aabbs) in enumerate(zip(res.batch_imgs, res.batch_aabbs)):
        f = loader.get_scale_factor(i)
        aabbs = [aabb.scale(1 / f, 1 / f) for aabb in aabbs]
        img = loader.get_original_img(i)
        pagewise.append(FetchImages(img, aabbs))

    return pagewise


