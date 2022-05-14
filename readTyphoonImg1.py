import cv2
# from PIL import Image
import numpy as np
'''
在提取图像中的像素值时，首先需要将图像转化为数组，对数组进行提取，因此需要用到numpy库。
'''
# Step 1：读取图像，并显示和储存
img = cv2.imread("Typhoon Chanthu image09182021_500m.jpeg")
cv2.imshow("Color 2", img)


# cv2.imshow("img",img)
# b, g, r = cv2.split(img)
# cv2.imshow("Blue 1", b)
# cv2.imshow("Green 1", g)
# cv2.imshow("Red 1", r)
# cv2.waitKey()
# cv2.destroyAllWindows()
# 此处没有用openCV中的split函数进行RGB图的拆分，而是定义了三个拆分函数，其效果与split函数一致。
# 第一函数get_red(),输入参数为三波段RGB图像，其中2，1，0分别对应蓝，绿，红三个波段
def get_red(img):
    redImg = img[:, :, 2]
    return redImg


def get_green(img):
    greenImg = img[:, :, 1]
    return greenImg


def get_blue(img):
    blueImg = img[:, :, 0]
    return blueImg


# 应用上述定义函数进行波段赋值
b = get_blue(img)
g = get_green(img)
r = get_red(img)
# 再将三个波段用窗口展示
cv2.imshow("Blue 2", b)
cv2.imshow("Green 2", g)
cv2.imshow("Red 2", r)
# 分别将图像的三个波段写出
cv2.imwrite("typtoon2_r.jpg", r)
cv2.imwrite("typtoon2_g.jpg", g)
cv2.imwrite("typtoon2_b.jpg", b)
# 定义弛豫时间，按任意键结束
cv2.waitKey()
# 关闭窗口
cv2.destroyAllWindows()

# Step 2：获取图像的像素值
# 首先打印图像的信息
print("图像形状大小：")
print(img.shape)
print("图像像素数目：")
print(img.size)
print("图像数据类型：")
print(img.dtype)

# 此为第二种获取图像像素值的方法，需要将图像先转化为三维数组np.array(),然后输出数组对应的值来获取图像的像素值
# 将图像转化为数组
img_array = np.array(img)
# 利用数组的位置（三维坐标）来获取所需的像素值

# 打印像素点（左上角）(0,0)的各个通道值
print("像素点(0,0)的R通道值为：")
print(img_array[0, 0, 2])
print("像素点(0,0)的G通道值为：")
print(img_array[0, 0, 1])
print("像素点(0,0)的B通道值为：")
print(img_array[0, 0, 0])

# 打印像素点(838, 757)的各个通道值
print("像素点(838,757)的R通道值为：")
print(img_array[838, 757, 2])
print("像素点(838,757)的G通道值为：")
print(img_array[838, 757, 1])
print("像素点(838,757)的B通道值为：")
print(img_array[838, 757, 0])

# 打印像素点(726, 1287)的各个通道值
print("像素点(726,1287)的R通道值为：")
print(img_array[726, 1287, 2])
print("像素点(726,1287)的G通道值为：")
print(img_array[726, 1287, 1])
print("像素点(726,1287)的B通道值为：")
print(img_array[726, 1287, 0])

# 打印像素点(2096, 1870)的各个通道值
print("像素点(2096,1870)的R通道值为：")
print(img_array[2096, 1870, 2])
print("像素点(2096,1870)的G通道值为：")
print(img_array[2096, 1870, 1])
print("像素点(2096,1870)的B通道值为：")
print(img_array[2096, 1870, 0])

# 打印像素点(2168, 2014)的各个通道值
print("像素点(2168,2014)的R通道值为：")
print(img_array[2168, 2014, 2])
print("像素点(2168,2014)的G通道值为：")
print(img_array[2168, 2014, 1])
print("像素点(2168,2014)的B通道值为：")
print(img_array[2168, 2014, 0])