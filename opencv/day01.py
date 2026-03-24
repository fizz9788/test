import cv2
import numpy as np
from matplotlib import pyplot as plt

def cv_show(img,name):
    cv2.imshow(name,img)
    cv2.waitKey()

img_cat=cv2.imread(r"C:\Users\Windows\Desktop\opencv\cat.jpg")
# gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# cv2.imshow("cat",gray_img)
# cv2.waitKey()
# print(gray_img.shape)

# hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# cv2.imshow("cat_hsv",hsv_img)
# cv2.waitKey()
'''
ret,thresh1=cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY)
cv2.THRESH_BINARY:灰度值大于127的为255，小于等于127的为0
cv2.THRESH_BINARY_INV：上面的情况反转
cv2.THRESH_TRUNC：灰度值大于127的为127，小于等于127的保持原值
THRESH_TOZERO：大于127的保持原值，小于等于的为0
cv2.THRESH_TOZERO_INV：上面的情况反转
'''
# ret,thresh1=cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY)
# ret,thresh2=cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY_INV)
# ret,thresh3=cv2.threshold(gray_img,127,255,cv2.THRESH_TRUNC)
# ret,thresh4=cv2.threshold(gray_img,127,255,cv2.THRESH_TOZERO)
# ret,thresh5=cv2.threshold(gray_img,127,255,cv2.THRESH_TOZERO_INV)
#
# images=[img,thresh1,thresh2,thresh3,thresh4,thresh5]
# tags=['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
#
# for i in range(6):
#     plt.subplot(2,3,i+1)
#     plt.imshow(images[i],'gray')
#     plt.title(tags[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()






# img=cv2.imread(r"C:\Users\Windows\Desktop\opencv\lenaNoise.png")
# cv2.imshow('img',img)

#blur是均值滤波
# bule=cv2.blur(img,(3,3))
# cv2.imshow('bule',bule)
# cv2.waitKey(0)


#boxFilter(方形滤波) : 参数1 图像 参数2 -1:输入图像深度和输出图像深度保持一致， 参数3 滤波内核大小
# 参数4 normalize:默认为True,如果内核大小为3，3 则为3*3大小内的灰度值相加平均，如果为False为不平均只相加，会过曝
# box=cv2.boxFilter(img,-1,(5,5),normalize=False)
# cv2.imshow('box',box)
# cv2.waitKey(0)


#高斯滤波，第三个参数为：X 方向（水平方向）的高斯核标准差（σ）,值越大约模糊
# gas=cv2.GaussianBlur(img,(5,5),0)
# cv2.imshow('gas',gas)
# cv2.waitKey(0)


#中值滤波
# med=cv2.medianBlur(img,3)
# cv2.imshow('med',med)
# cv2.waitKey(0)


#形态学---腐蚀
img=cv2.imread(r"C:\Users\Windows\Desktop\opencv\dige.png")
# kernal=np.ones((3,3),np.uint8)
# erosion=cv2.erode(img,kernal,iterations=1)
# cv2.imshow("erosion",erosion)
# cv2.waitKey(0)

img_pie=cv2.imread(r"C:\Users\Windows\Desktop\opencv\pie.png")
# kernal=np.ones((30,30),np.uint8)
# erosion1=cv2.erode(img_pie,kernal,iterations=1)
# erosion2=cv2.erode(img_pie,kernal,iterations=2)
# erosion3=cv2.erode(img_pie,kernal,iterations=3)
# cv2.imshow("ero1",erosion1)
# cv2.imshow("ero2",erosion2)
# cv2.imshow("ero3",erosion3)
# cv2.waitKey(0)

#形态学----膨胀
# shape=np.ones((4,4),np.uint8)
# dela=cv2.dilate(img,shape,iterations=1)
# cv2.imshow("img",img)
# cv2.imshow("dilate",dela)
# cv2.waitKey(0)


#开运算和闭运算
#开运算=先腐蚀再捧着，闭运算=先膨胀再腐蚀  作用: 开运算=去毛刺   闭运算=填空洞
# kernal=np.ones((3,3),np.uint8)
# opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernal)
# closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernal)
# cv2.imshow("opening",opening)
# cv2.imshow("closing",closing)
# cv2.waitKey(0)


#梯度运算
#梯度=先膨胀再腐蚀
#梯度值 = 相邻像素的差值 → 差值越大，梯度值越大（边缘越明显）；
# 梯度运算的最终目的：把图像的「边缘」从背景中凸显出来（边缘检测的核心逻辑）。
# kernel=np.ones((5,5),np.uint8)
# ero=cv2.erode(img_pie,kernel,iterations=1)
# dil=cv2.dilate(img_pie,kernel,iterations=1)
# res=np.hstack((ero,dil))
# cv2.imshow('res',res)

#参数2：梯度类型,
# cv2.MORPH_GRADIENT(基本梯度：膨胀-腐蚀)/
# cv2.MORPH_ERODE（内部梯度：原图-腐蚀）/
# cv2.MORPH_DILATE（外部梯度：膨胀-原图）
#参数3:卷积核，决定边缘提取的粒度
# gradient=cv2.morphologyEx(img_pie,cv2.MORPH_GRADIENT,kernel)
# cv2.imshow('gradient', gradient)
# cv2.waitKey(0)


#Sobel\Scharr\Laplacian
# - ddepth:图像的深度
# - dx和dy分别表示水平和竖直方向
# - ksize是Sobel算子的大小
#白到黑是正数，黑到白就是负数了，所有的负数会被截断成0，所以要取绝对值
#先计算X
# sobelx=cv2.Sobel(img_pie,cv2.CV_64F,1,0,ksize=3)
# sobelx=cv2.convertScaleAbs(sobelx)
#再计算Y
# sobely=cv2.Sobel(img_pie,cv2.CV_64F,0,1,ksize=3)
# sobely=cv2.convertScaleAbs(sobely)
#
# sobelxy=cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
# cv_show(sobelxy,'sobelxy')

#不要一起计算xy
# img_lina=cv2.imread(r"C:\Users\Windows\Desktop\opencv\lena.jpg",cv2.IMREAD_GRAYSCALE)
# sobelx = cv2.Sobel(img_lina,cv2.CV_64F,1,0,ksize=3)
# sobelx = cv2.convertScaleAbs(sobelx)
# sobely = cv2.Sobel(img_lina,cv2.CV_64F,0,1,ksize=3)
# sobely = cv2.convertScaleAbs(sobely)
'''addWeighted参数：图片1，权重1，图片2，权重2，亮度补偿'''
# sobelxy = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
# cv_show(sobelxy,'sobelxy')
#
# sobelxy=cv2.Sobel(img_lina,cv2.CV_64F,1,1,ksize=3)
# sobelxy = cv2.convertScaleAbs(sobelxy)
# cv_show(sobelxy,'sobelxy')



'''Canny边缘检测
   使用高斯滤波器，以平滑图像，滤除噪声。
   计算图像中每个像素点的梯度强度和方向。
   应用非极大值（Non-Maximum Suppression）抑制，以消除边缘检测带来的杂散响应。
   应用双阈值（Double-Threshold）检测来确定真实的和潜在的边缘。
   通过抑制孤立的弱边缘最终完成边缘检测。
   
    双阈值筛选：用两个阈值（低阈值 / 高阈值）筛选边缘：
    像素梯度值 > 高阈值 → 确定为 “强边缘”（保留）；
    低阈值 <像素梯度值 < 高阈值 → 仅当该像素与强边缘相连时，才保留为 “弱边缘”；
    像素梯度值 < 低阈值 → 剔除（视为噪声）；
   '''

# img_lina=cv2.imread(r"C:\Users\Windows\Desktop\opencv\lena.jpg",cv2.IMREAD_GRAYSCALE)
# v1=cv2.Canny(img_lina,80,150)
# v2=cv2.Canny(img_lina,50,100)
# res=np.hstack((v1,v2))
# cv_show(res,"canny")


# v1=cv2.Canny(img_cat,120,250)
# v2=cv2.Canny(img_cat,50,100)
# res=np.hstack((v1,v2))
# cv_show(res,"cat")


'''
高斯金字塔：向下采样，缩小图片，会变模糊

拉普拉斯金字塔：用来存储 “差值”，方便以后上采样恢复图像（重建）
pyrUp 不是 pyrDown 的逆操作！缩小再放大，图像会变模糊，细节回不来
'''
# img_AM=cv2.imread(r"C:\Users\Windows\Desktop\opencv\AM.png")
# cv_show(img_AM,"AM")
# up=cv2.pyrUp(img_AM)
# cv_show(up,'up')
# down=cv2.pyrDown(img_AM)
# cv_show(down,'down')
# up=cv2.pyrUp(img_AM)
# up_down=cv2.pyrDown(up)
# cv_show(img_AM-up_down,'img-up_down')

#提取轮廓
# img=cv2.imread(r"C:\Users\Windows\Desktop\opencv\contours.png")
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
#返回值为contours：轮廓，hierarchy：层级
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# draw_img=img.copy()
'''
drawContours参数:图像，轮廓，轮廓索引（-1为所有），颜色模式，线条厚度
'''
# res=cv2.drawContours(draw_img,contours,-1,(0,0,255),2)
# cv_show(res,'res')
#
# res=cv2.drawContours(draw_img,contours,0,(0,0,255),2)
# cv_show(res,'res')

# #轮廓特征
# cnt=contours[0]
# #轮廓面积
# print(cv2.contourArea(cnt))
# #轮廓周长 True表示闭合的
# print(cv2.arcLength(cnt,True))


#轮廓近似
# img=cv2.imread(r"C:\Users\Windows\Desktop\opencv\contours2.png")
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# cnt=contours[0]
# draw_img=img.copy()
# res=cv2.drawContours(draw_img,[cnt],-1,(0,0,255),2)
# cv_show(res,'res')
#
# epsilon=0.1*cv2.arcLength(cnt,True)#0.15为误差值，越小与原先轮廓越接近
# approx=cv2.approxPolyDP(cnt,epsilon,True)#执行轮廓逼近
#
# draw_img_1=img.copy()
# res=cv2.drawContours(draw_img_1,[approx],-1,(0,0,255),2)
# cv_show(res,'res')

#边界矩形
# img=cv2.imread(r"C:\Users\Windows\Desktop\opencv\contours.png")
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
# contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# cnt=contours[0]
# print(cnt)
# x,y,w,h=cv2.boundingRect(cnt)
# img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
# cv_show(img,'img')

# area=cv2.contourArea(cnt)
# x,y,w,h=cv2.boundingRect(cnt)#xy为外接矩形左上角的左边
# react_area=w*h
# extent=float(area)/react_area
# # print('轮廓面积与边界矩形比',extent)
# (x,y),radius=cv2.minEnclosingCircle(cnt)
# center=(int(x),int(y))
# radius=int(radius)
# img=cv2.circle(img,center,radius,(0,255,0),2)
# cv_show(img,'img')



#傅里叶变换
''''
高频：变化剧烈的灰度分量，比如边界
低频：变化缓慢的灰度分量

滤波
低通滤波器：保留低频，图像变糊
高通滤波器：只保留高频，图像细节增强

cv2.dft()和cv2.idft()的输入图像要先转换成float32格式
得到的结果中频率为0的部分会在左上角，通过shift转换到中心位置
cv2.dft()返回
'''
img=cv2.imread(r"C:\Users\Windows\Desktop\opencv\lena.jpg",0)

img_float32=np.float32(img)

# dft=cv2.dft(img_float32,flags=cv2.DFT_COMPLEX_OUTPUT)
# dft_shift=np.fft.fftshift(dft)
# # 得到灰度图能表示的形式
# magnitude_spectrum=20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
# plt.subplot(121),plt.imshow(img,cmap='gray')
# plt.title('Input Image'),plt.xticks([]),plt.yticks([])
# plt.subplot(122),plt.imshow(magnitude_spectrum,cmap='gray')
# plt.title('Magnitude Spectrum'),plt.xticks([]),plt.yticks([])
# plt.show()



dft=cv2.dft(img_float32,flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift=np.fft.fftshift(dft)

rows,cols=img.shape
crow,ccol=int(rows/2),int(cols/2)#图像的中心位置

#低通滤波
mask=np.zeros((rows,cols,2),np.uint8)
mask[crow-30:crow+30,ccol-30:ccol+30]=1

#IDFT
fshift=dft_shift*mask
f_ishift=np.fft.ifftshift(fshift)
img_back=cv2.idft(f_ishift)
img_back=cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title('Input Image'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(img_back,cmap='gray')
plt.title('Result'),plt.xticks([]),plt.yticks([])
plt.show()

#自适应直方图均衡化
# img=cv2.imread(r"C:\Users\Windows\Desktop\opencv\cat.jpg")
# img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# equ=cv2.equalizeHist(img)
# clahe=cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
# res_clahe=clahe.apply(img)
# res=np.hstack((img,equ,res_clahe))
# cv_show(res,'res')




















