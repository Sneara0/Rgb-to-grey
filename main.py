import cv2

orig_img=cv2.imread("C:\\Users\sneara\Downloads\\sneara.jpeg")
grey_img=cv2.cvtColor(orig_img,cv2.COLOR_BGR2RGB)
cv2.imshow('color',orig_img)
cv2.imshow('SNEARA',grey_img)

cv2.waitKey(0)
cv2.destroyWindow()

