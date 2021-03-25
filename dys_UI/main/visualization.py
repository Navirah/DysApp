#Word Segmentation NN

import cv2
import matplotlib.pyplot as plt
import numpy as np

def prepareImg(img, height):
    """convert given image to grayscale image (if needed) and resize to desired height"""
    assert img.ndim in (2, 3)
    if img.ndim == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h = img.shape[0]
    factor = height / h
    return cv2.resize(img, dsize=None, fx=factor, fy=factor)


def visualize(img, aabbs):
    img = ((img + 0.5) * 255).astype(np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    for aabb in aabbs:
        aabb = aabb.enlarge_to_int_grid().as_type(int)
        #cv2.rectangle(img, (aabb.xmin, aabb.ymin), (aabb.xmax, aabb.ymax), (0, 0, 0), 2)

    return img


def FetchImages(img, aabbs):

    img = ((img + 0.5) * 255).astype(np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    listofimages=[]

    for aabb in aabbs:
        aabb = aabb.enlarge_to_int_grid().as_type(int)
        #cv2.rectangle(img, (aabb.xmin, aabb.ymin), (aabb.xmax, aabb.ymax), (255, 0, 255), 2)
        imgCropped=img[aabb.ymin:aabb.ymax,aabb.xmin:aabb.xmax]
        listofimages.append(prepareImg(imgCropped,50))

    return listofimages
    #for aabb in aabbs:
        #plt.plot([aabb.xmin, aabb.xmin, aabb.xmax, aabb.xmax, aabb.xmin],
                 #[aabb.ymin, aabb.ymax, aabb.ymax, aabb.ymin, aabb.ymin])

    #plt.show()
