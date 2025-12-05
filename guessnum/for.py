#561 for语法结构基于range循环
""" for i in 5:
    print('hi') """
# TypeError: 'int' object is not iterable

""" for i in range(5):
    print(i) """

#562基于list列表与tuple元组的循环
""" num = [2,3,4,5,6]
num2 = (7,1,2,5,9,)
name = 'zhagnsan' """
#列表，元组，字典，集合，字符串（iterable可迭代）
""" for i in name:
    print(i) """

#563跳过循环 continue #跳过本次循环语句，马上进入下一轮循环
""" for i in [1,2,3,4,5,6,7,8,9]:
    if(i%3==0):
        continue
    print(i*5) """

#564马上退出循环
""" for i in [1,2,3,4,5,6,7,8,9]:
    if(i==5):
        break
    print(i)
print('程序结束') """

#565 嵌套循环
""" name = ['zhangsan','lisi','wangwu']
for i in name:
    print(i)
    for j in i:
        print(j) """

#566一次性跳出嵌套循环
name = ['zhangsan','lisi','wangwu']
is_found = False
for i in name:
    if (is_found):
        break
    print(i)
    for j in i:
        print(j)
        if(j=="s"):
            is_found=True
            break

