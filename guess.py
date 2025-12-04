import random
import sys
import time
print(sys.argv)

#sys.argv  是一个包含命令行参数的列表。 查询命令行传参
# PS E:\work2> python.exe .\guess.py 3
# ['.\\guess.py', '3']

# 元组与列表类似，元组元素不能修改，元组使用小括号，括号里添加元素，使用逗号隔开 tup1=(cycle,is_right,used_time)

scores = []#战绩
cycle = 0#第几轮
chance1 = int(sys.argv[1])
while(True):
    cycle+=1
    is_right = False
    chance = chance1
    answer = random.randint(1,10)
    #while版本
    begin_time = time.time()
    while(chance>0):
        chance -= 1#第几轮
        guess = int(input('你猜猜是数字几？\n'))
        
        if(answer>guess):
            print(f'猜小了，机会还有{chance}次')
        elif(answer<guess):
            print(f'猜大了，机会还有{chance}次')
        else:
            print('你猜对了√！')
            is_right = True
            break

    end_tinme = time.time()
    used_time = round((end_tinme - begin_time),2)# round() 方法返回浮点数x的四舍五入值。
    print(f'用时{used_time}秒')
    print('游戏结束！！')

    """ if(is_right):
            label = '✌️'
    else:
            label = '👎' """
            
    scores.append((cycle,is_right,used_time)) # append() 方法用于在列表末尾添加新的对象。
    # print(scores)
    
    bast_scores = min(scores,key=lambda x:x[2]if x[1]==True else 9999)
    #python使用lambda来创建匿名函数例： lambda 参数列表:表达式  ;  lambda a:a+1
    # print(f'bastscores:{bast_scores}')

    
    """ if(used_time==bast_scores[2]):
         bast='💕'
    else:
         bast=''
     """     
    # print(bast)    
    print('============战绩===========')
    for i,j,k in scores:
        bast_label='💕'if(i==bast_scores[0] and bast_scores[1])else''#三元运算符赋值 m=a if a>b else b
        label='✌️'if j else '❌'
        print(f'{i}轮，输赢{label}，用时{k} {bast_label}')
    print('===========================')
    con = input('继续输入y，其他退出\n')
    if(con != 'y'):
        print('886')
        break


#ValueError: invalid literal for int() with base 10: '& C:/Users/wang/AppData/Local/Microsoft/WindowsApps/python3.11.exe e:/work2/guess.py'
# ValueError: invalid literal for int() with base 10: ''
# #3中格式化方法
# name = "Alice"
# age = 25
# #  %操作符格式化
# print("My name is %s and I'm %s years old." % (name, age))
# #  .format()方法格式化
# print("My name is {} and I'm {} years old." .format(name, age))
# #f-string字面值
# print(f"My name is {name} and I'm {age} years old.")


#for版本
""" answer = random.randint(1,10)
for chance in range(3,0,-1):
    guess = int(input('输入数字：\n'))
    # chance-=1
    if(answer>guess):
        print(f'太小了,机会还有{chance}次')
    elif(answer<guess):
        print(f'太大了，机会还有{chance}次')
    else:
        print('猜对了！')
        break
print('游戏结束')
 """
# TypeError: 'int' object is not iterable

559