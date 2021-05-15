import cv2
import numpy as np


def prepareImg(img, height):
    """convert given image to grayscale image (if needed) and resize to desired height"""
    assert img.ndim in (2, 3)
    if img.ndim == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h = img.shape[0]
    factor = height / h
    return cv2.resize(img, dsize=None, fx=factor, fy=factor)

def bubbleSort(arr):
	n = len(arr)
  
    # Traverse through all array elements
	for i in range(n-1):
    # range(n) also work but outer loop will repeat one time more than needed.
  
        # Last i elements are already in place
		for j in range(0, n-i-1):
  
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
			if arr[j].xmin > arr[j+1].xmin :
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr

def sortit(img, aabbs,segments):
    img = ((img + 0.5) * 255).astype(np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    rangepage=img.shape[1]/segments
    d={}

    for segs in range(1,segments+1):
    	start=rangepage*segs
    	d[start]=[]

    buffer=rangepage/20
    for i in aabbs:
    	for j in d:
       		if (i.ymin<j+buffer and i.ymin>(j-rangepage-buffer)) and (i.ymax<j+buffer and i.ymax>(j-rangepage-buffer)): #both in range
       			d[j].append(i)

    for i in d:
    	d[i]=bubbleSort(d[i])

    listofimages=[]
    for i in d:
	    for aabb in d[i]:
	    	aabb = aabb.enlarge_to_int_grid().as_type(int)
	    	imgCropped=img[aabb.ymin:aabb.ymax,aabb.xmin:aabb.xmax]
	    	listofimages.append(prepareImg(imgCropped,50))
	        #cv2.rectangle(img, (aabb.xmin, aabb.ymin), (aabb.xmax, aabb.ymax), (255, 0, 255), 2)
    return listofimages




