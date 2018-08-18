#-*- coding:utf-8 -*-
#@Time     :2018/8/18 14:09 
#@Author   :Kanseii
#@Emai     :kanseii@yahoo.com
#@File     :create.py
#@Software :PyCharm
'''
    标准的Python中用列表(list)保存一组值，可以用来当作数组使用。但由于列表的元素可以 是任何对象，因此列表中保存的是对象的指针。
    这样的话，为了保存一个简单的列表，比如[1，2,3J, 需要三个指针和三个整数对象。
    对于数值运算来说，这种结构显然比较浪费内存和CPU计算时间。
    此外，Python还提供了 array模块，它所提供的array对象和列表不同，能直接保存数值，
    和 C 语言的一维数组类似。但是由于它不支持多维数组，也没有各利I运算函数，因此也不适合做数值运算。

    NumPy的诞生弥补了这些不足，NumPy提供了两种基本的对象:
    • ndarray:英文全称为n-dimensional array object，它是存储单一数掘类型的多维数组，后统一称之为数组。
    • ufunc: 英文全称为universal function object，它是一种能够对数组进行处理的特殊函数。
'''
import numpy as np

a = np.array([[1,2,3],[4,5,6,],[7,8,9]])
print(a.shape) #(3,3)

#当设置某个轴的元素个数为-1时，将自动计兑此轴的长度。
a.shape=(3,-1)
print(a.shape) #(3, 3)

#使用reshape方法可以创建指定形状的新数组 ，而原数组的形状不变

b = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]])

c = b.reshape(4,3)
print(c.shape) #(4,3)
print(b.shape) #(3,4)

#数组b 和 c 其实共享数椐存储空间，因此修改其中任意一个数组的元素都会同时修改另一个数组的内容。
b[2][3] = 0
print(c[3][2]) # 0

print('----------------------------------------')

'''
    元素类型
    数组的元素类型可以通过dtype属性获得。在前而的例子中，创建数组所用的序列的元素都是整数，因此所创建的数组的元素类型是整型，并且是32位的长整型。
    这是因为笔者所使用的Python是64位的，如果使用32位的操作系统和Python, 那么默认整数类型的长度为32位。

'''
print(c.dtype) #int64

#可以通过dtype参数在创建数组吋指定元素类型，注意float类型是64位的双精度浮点类型， 而complex是128位的双精度复数类型

ai32 = np.array([1,2,3],dtype=np.int32)
af = np.array([1,2,3],dtype=np.float)
ac = np.array([1,2,3],dtype=np.complex)

#通过NumPy的数值类型也可以创建数值对象.
#下面创建一个16位的符号整数对象，它与 Python的整数对象不同的是，它的収值范围有限.
#因此计算200*200会溢出，得到一个负数，这一点与C语言的16位整数的结果相同
aa = np.int16(200)
print(aa*aa) #-25536

#注意！！NumPy的数值对象的运兑速度比Python的内置类型的运算速度慢很多，如果程序中耑要大量地对单个数值运算，应当尽量避免使用NumPy的数值对象

# 使用astype方法可以对数组的元素类型进行转换
t = af.astype(np.int32)
print(t.dtype) #int32
