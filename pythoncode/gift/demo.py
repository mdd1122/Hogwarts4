# a = 1.0
# # python 允许任何地方定义变量
# # 变量可以重新赋值
# # 变量会被就近调用
# # 调用全局变量global x
# # 打印变量的内存地址 x.id
#
#
# def demo1():
#     # 告诉解释器要调用外边的a
#     global a
#     a=2
#     print(a)
#     print(type(a))
#     print(id(a))
#
# print(id(a))
# print(demo1())
#
# # python 支持嵌套函数,闭包函数
# def  outer():
#     def inner():
#         print('inner')
#     return inner()
#
# #模块 不要起名为系统模块名、第三方包名

nums = [1,2,3]
# 深拷贝
nums1 = nums
# 浅拷贝
nums2 = nums.copy()