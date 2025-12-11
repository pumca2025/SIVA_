import cv2
image_one=cv2.imread("image4.jpg")
image_two=cv2.imread("image1.jpg")
rm1=cv2.resize(image_one,(500,500))
rm2=cv2.resize(image_two,(500,500))
result_image=cv2.addWeighted(rm2,0.5,rm1,0.9,0)
cv2.imshow('Addition operation of two Image',result_image)
cv2.waitKey(0)
