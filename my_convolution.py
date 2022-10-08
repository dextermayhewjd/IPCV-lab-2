import cv2
import numpy as np

image = cv2.imread("mandrill.jpg", cv2.IMREAD_UNCHANGED)

#for y in range(0, image.shape[0]):  # go through all rows (or scanlines)
#	for x in range(0, image.shape[1]):  # go through all columns
#		pixelBlue = image[y, x, 0]
#		pixelGreen = image[y, x, 1]
#		pixelRed = image[y, x, 2]
#		if (pixelBlue>200):
#			image[y, x, 0] = 255
#			image[y, x, 1] = 255
#			image[y, x, 2] = 255
#		else:
#			image[y, x, 0] = 0
#			image[y, x, 1] = 0
#			image[y, x, 2] = 0
kernel1 = np.ones([3,3])
print(kernel1)

image = cv2.copyMakeBorder(image, int(kernel1.shape[0]/2), int(kernel1.shape[0]/2), int(kernel1.shape[1]/2), int(kernel1.shape[1]/2), borderType=cv2.BORDER_REPLICATE)
image2 = image


#cv2.imshow('window_name',image)
#cv2.waitKey(0)
for y in range (0,image.shape[0]-2):
    for x in range (0,image.shape[1]-2):
            patch = image[y:y+kernel1.shape[0],x:x+kernel1.shape[1]]
            #print(image2.shape)
            outPut_sum = ((np.multiply(patch,kernel1)).sum())/9
            image2[y,x] = outPut_sum 
        
cv2.imshow('window_name',image2)
cv2.waitKey(0)
            