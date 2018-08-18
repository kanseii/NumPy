#-*- coding:utf-8 -*-
#@Time     :2018/8/18 14:42 
#@Author   :Kanseii
#@Emai     :kanseii@yahoo.com
#@File     :create1.py
#@Software :PyCharm

import numpy as np

#自动生成数组
#arange()类似于内置闲数range()，通过指定开始值、终值和步长来创建表示等差数列的一维数组，注意所得到的结果中不包含终值。
print(np.arange(0,1,0.1)) #[0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]

#linspace()通过指定幵始值、终值和元素个数来创建表示等差数列的一维数组，可以通过 endpoint参数指定是否包含终值，默认值为Tme,即包含终值。
print(np.linspace(0,1,10))
#[0.         0.11111111 0.22222222 0.33333333 0.44444444 0.55555556 0.66666667 0.77777778 0.88888889 1.        ]

print(np.linspace(0,1,10,endpoint=False))#[0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]


#logspace()和linspace()类似，不过它所创建的数组是等比数列。
#从10^0到10^2、 有5个元素的等比数列，注意起始值0表示10^0,而终值2表示10^2:
print(np.logspace(0,2,5))
#基数可以通过base参数指定，其默认值为10。下而通过将base参数设置为2,并设置endpoint 参数为False
print(np.logspace(0,1,5,base=2,endpoint=False)) #[1.         1.14869835 1.31950791 1.51571657 1.74110113]


'''
    zeros()、ones()、empty()可以创建指定形状和类型的数组。
    empty()只分配数组所使用的内存，不对数组元素进行初始化操作，因此它的运行速度是最快的。
    zeros()将数组元素初始化为0
    ones()将数组元素初始化为1。
'''
print(np.empty((2,3),dtype=int))
print()
print(np.zeros(5,dtype=int)) #[0 0 0 0 0]

#full()将数组元素初始化为指定的值
print(np.full(4,np.pi)) #[3.14159265 3.14159265 3.14159265 3.14159265]


