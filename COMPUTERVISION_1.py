import cv2
img=cv2.imread("image1.jpg")
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray Image",imgGray)
cv2.waitKey(0)
cv2.imwrite("C:\\Users\\CC-Lab42\\Desktop\\sivaMCA\\grayimg1.jpg",img)






























"""import cv2


img = cv2.imread("images.jfif")


if img is None:
    print("Error: Could not read the image.")
else:
    
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    
    cv2.imshow("Gray Image", imgGray)

   
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    cv2.imwrite("gray_images.jfif", imgGray) """ 
