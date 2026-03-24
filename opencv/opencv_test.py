import cv2
import numpy as np
img_path=r"C:\Users\Windows\Desktop\opencv_tutorial-main\poker.jpg"
image=cv2.imread(img_path)
# print(image.shape)
# cv2.imshow('1',image)
# cv2.waitKey()
# print(cv2.getVersionString())

# #image三原色
# cv2.imshow("blue",image[:,:,0])
# cv2.imshow("green",image[:,:,1])
# cv2.imshow("red",image[:,:,2])
#
# gray_iamge=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#RGB转灰度图
# cv2.imshow('gray',gray_iamge)
# cv2.waitKey()

# crop = image[10:170,40:200] #先y方向10到170 下、方向40到200裁剪
# cv2.imshow('crop',crop)
# cv2.waitKey()

# image=np.zeros([300,300,3],dtype=np.uint8)
# cv2.line(image,(100,200),(250,250),(250,0,0),2)
# cv2.rectangle(image,(30,100),(60,150),(0,0,255),2)
# cv2.circle(image,(150,150),100,(0,255,0),2)
# cv2.putText(image,"hello",(100,100),0,1,(255,255,255),2)
# cv2.imshow('image',image)
# cv2.waitKey()

#高斯滤波和中值滤波
# image=cv2.GaussianBlur(image,(7,7),0)
# cv2.imshow("gaus",image)
# cv2.waitKey()
# image=cv2.medianBlur(image,5)
# cv2.imshow('median',image)
# cv2.waitKey()

#特征提取
# gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# corners=cv2.goodFeaturesToTrack(gray_image,500,0.1,10)
# for i in corners:
#     x,y=i.ravel()
#     cv2.circle(gray_image,(int(x),int(y)),3,(0,0,255),-1)
# cv2.imshow('gray',gray_image)
# cv2.waitKey()

#模板匹配
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
template=gray_image[75:105,235:265]
match=cv2.matchTemplate(gray_image,template,cv2.TM_CCOEFF_NORMED)
locations=np.where(match>=0.8)
w,h=template.shape[0:2]
for i in zip(*locations[::-1]):
    x1, y1 = i[0] , i[1]
    x2, y2 = x1 + w, y1 + h
    cv2.rectangle(image,(x1,y1),(x2,y2),(0,0,255),1)

cv2.imshow('image',image)
cv2.waitKey()