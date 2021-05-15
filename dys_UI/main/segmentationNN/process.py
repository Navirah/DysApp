import torch
from path import Path
import cv2
import os

from .dataloader import DataLoaderImgFile
from .eval import evaluate
from .net import WordDetectorNet
from .visualization import visualize_and_plot
from .sort import sortit



def Segment(FilePath):
    net = WordDetectorNet()
    module_dir = os.path.dirname(__file__) 
    modelpath=os.path.join(module_dir,'model','weights')
    net.load_state_dict(torch.load(modelpath, map_location='cpu'))
    net.eval()
    net.to('cpu')

    loader = DataLoaderImgFile(Path(FilePath), net.input_size, 'cpu')
    res = evaluate(net, loader, max_aabbs=1000)

    pageset=[]
    for i, (img, aabbs) in enumerate(zip(res.batch_imgs, res.batch_aabbs)):
        f = loader.get_scale_factor(i)
        aabbs = [aabb.scale(1 / f, 1 / f) for aabb in aabbs]
        img = loader.get_original_img(i)
        #visualize_and_plot(img, aabbs)
        listpictures=sortit(img,aabbs,11)
        pageset.append(listpictures)

    return pageset

    '''name=1
    if not os.path.exists('../data/out'):
            os.mkdir('../data/out')
    for i in listpictures:
        pathh=os.path.join('..','data','out','img%d.jpg'%(name))
        cv2.imwrite(pathh, i)
        print(i)
        #print("yellow")
        name=name+1'''


