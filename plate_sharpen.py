import cv2
import numpy as np

image = cv2.imread("car1.jpg", cv2.IMREAD_UNCHANGED)
text = [0, -1, 0, -1, 5, -1, 0, -1, 0]
kernel = np.array(text)
kernel.reshape((3, 3))
print(kernel)
image = cv2.copyMakeBorder(image, int(kernel.shape[0]/2), int(kernel.shape[0]/2), int(kernel.shape[1]/2), int(kernel.shape[1]/2), borderType=cv2.BORDER_REPLICATE)
image2 = image
for y in range (0,image.shape[0]-2):
    for x in range (0,image.shape[1]-2):
            patch = image[y:y+kernel.shape[0],x:x+kernel.shape[1]]
            outPut_sum = ((np.multiply(patch,kernel)).sum())/9
            image2[y,x] = outPut_sum 
        
cv2.imshow('window_name',image2)
cv2.waitKey(0)