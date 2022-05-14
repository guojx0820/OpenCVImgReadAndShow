import cv2
# import numpy as np

'''
在读取真彩色RGB三波段图像时，需要用到openCV开源库中的函数，较为方便，但也可以自己写函数处理，openCV是专门用于图像处理的开源库，
应用较为方便简单所以本程序应用到了其split函数，就是为了分出图像的三个通道。
'''
# Step 1：读取图像并显示保存
# 读取图像，应用openCV的imread函数
img = cv2.imread("Typhoon Chanthu image09182021_500m.jpeg")
# 显示图像，应用openCV的imshow函数
cv2.imshow("Color", img)
# 利用openCV的split函数将彩色图像的R、G、B三个波段的灰度图分开，并将其值赋给b,g,r
# 在此需要注意的是，第n波段是图像的第3维信息，在python中顺序是从0开始的，所以波段对应为0对应b（蓝波段），
# 1对应g（绿波段），2对应r（红波段）
b, g, r = cv2.split(img)
# 分别显示三个波段的图像，显示框标题分别设为："Blue 1"，"Green 1"，"Red 1"
cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)

# 分别将图像的三个波段写出
cv2.imwrite("typtoon_r.jpg", r)
cv2.imwrite("typtoon_g.jpg", g)
cv2.imwrite("typtoon_b.jpg", b)
# 这里出现了error，如果需要显示图像窗口时，如imshow图像的时候，需要加上cv2.waitKay()函数，控制着imshow的持续时间
# 其中waitKay()函数中的参数值代表弛豫时间，0和不填代表无限制时间，也就是说，图像显示窗口无限制时间显示。若是其他数字，
# 则是以毫秒为计数单位，写多少就代表图像显示多少毫秒。需要注意的是，窗口显示图像时，按任意键会结束显示。
cv2.waitKey(1)
# cv2.destroyAllWindows() 用来删除窗口的，（）里不指定任何参数，则删除所有窗口，删除特定的窗口，往（）输入特定的窗口值。
cv2.destroyAllWindows()

# Step 2 读取各个波段的像素值
# 首先打印图像的信息
print("图像形状大小：")
print(img.shape)
print("图像像素数目：")
print(img.size)
print("图像数据类型：")
print(img.dtype)

# 打印像素点（左上角）(0,0)的各个通道值，在此item()函数则是字典函数，遍历图像找到图像中的像素值
print("像素点(0,0)的R通道值为：")
print(img.item(0, 0, 2))
print("像素点(0,0)的G通道值为：")
print(img.item(0, 0, 1))
print("像素点(0,0)的B通道值为：")
print(img.item(0, 0, 0))

# 打印像素点(838, 757)的各个通道值
print("像素点(838,757)的R通道值为：")
print(img.item(838, 757, 2))
print("像素点(838,757)的G通道值为：")
print(img.item(838, 757, 1))
print("像素点(838,757)的B通道值为：")
print(img.item(838, 757, 0))

# 打印像素点(726, 1287)的各个通道值
print("像素点(726,1287)的R通道值为：")
print(img.item(726, 1287, 2))
print("像素点(726,1287)的G通道值为：")
print(img.item(726, 1287, 1))
print("像素点(726,1287)的B通道值为：")
print(img.item(726, 1287, 0))

# 打印像素点(2096, 1870)的各个通道值
print("像素点(2096,1870)的R通道值为：")
print(img.item(2096, 1870, 2))
print("像素点(2096,1870)的G通道值为：")
print(img.item(2096, 1870, 1))
print("像素点(2096,1870)的B通道值为：")
print(img.item(2096, 1870, 0))

# 打印像素点(2168, 2014)的各个通道值
print("像素点(2168,2014)的R通道值为：")
print(img.item(2168, 2014, 2))
print("像素点(2168,2014)的G通道值为：")
print(img.item(2168, 2014, 1))
print("像素点(2168,2014)的B通道值为：")
print(img.item(2168, 2014, 0))
