import cv2
import numpy as np
img=cv2.imread("image9.jpg")
resized_img=cv2.resize(img,(600,300))
rotation_matrix=cv2.getRotationMatrix2D((img.shape[1]/2,img.shape[0]/2),30,1)
rotated_img=cv2.warpAffine(img,rotation_matrix,(img.shape[1],img.shape[0]))
cv2.imshow("Resized Image:",resized_img)
cv2.imshow("Rotated Image:",rotated_img)




cv2.waitKey(0)
