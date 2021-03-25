#Word Segmentation NN

import argparse

import torch
from path import Path

from .dataloader import DataLoaderImgFile
from .eval import evaluate
from .net import WordDetectorNet
from .visualization import FetchImages
import cv2



def segment(filepath=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--device', choices=['cpu', 'cuda'], default='cpu')
    args = parser.parse_args()

    net = WordDetectorNet()
    net.load_state_dict(torch.load('../model/weights', map_location=args.device))
    net.eval()
    net.to(args.device)

    loader = DataLoaderImgFile(Path(filepath), net.input_size, args.device)
    res = evaluate(net, loader, max_aabbs=1000)

    pagewise=[]

    for i, (img, aabbs) in enumerate(zip(res.batch_imgs, res.batch_aabbs)):
        f = loader.get_scale_factor(i)
        aabbs = [aabb.scale(1 / f, 1 / f) for aabb in aabbs]
        img = loader.get_original_img(i)
        pagewise.append(FetchImages(img, aabbs))

    return pagewise


