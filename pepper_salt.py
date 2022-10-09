import cv2
import numpy as np
#read the image and store it in the image 
image = cv2.imread("car2.png", cv2.IMREAD_UNCHANGED)

#create a kernel to sharpen the image 
text = [1, 1, 1, 1, 1, 1, 1, 1, 1]
kernel = np.array(text)
kernel = np.reshape(kernel,(3, 3))
print(kernel)

#this is the way how to padding the image
image = cv2.copyMakeBorder(image, int(kernel.shape[0]/2), int(kernel.shape[0]/2), int(kernel.shape[1]/2), int(kernel.shape[1]/2), borderType=cv2.BORDER_REPLICATE)
image2 = image


for y in range (0,image.shape[0]-2):
    for x in range (0,image.shape[1]-2):
            patch = image[y:y+kernel.shape[0],x:x+kernel.shape[1]]
            outPut_median = np.median(np.multiply(patch,kernel))
            image2[y,x] = outPut_median
        
cv2.imshow('window_name',image2)
cv2.waitKey(0)