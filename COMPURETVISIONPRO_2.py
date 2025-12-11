import cv2
img=cv2.imread("image2.jpg",cv2.IMREAD_COLOR)
value=img[10,10,:]
print("ACCESSING PIXEL VALUES:",value)
img[10,10,0]=0
value=img[10,10,:]
print("MODIFYING PIXEL VALUES:",value)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
