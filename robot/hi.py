
#引入文件
import open1 as op
import time1 as tm
import weather as wt
import time 
'''python解释器一行行的执行代码，会遇到两种：以def开头的和不是def开头的
1、非def就是做具体的，马上执行
2、def是准本后面可用
3、还有类似class也是准备后面可用 
注释快捷键
shift+alt+a
ctrl+/
'''
#1、问好
op.hi()
time.sleep(1)

#2、提问 输入姓名
age = op.hello() 

#3、打招呼
op.Determine_Age(age)

#内存转换和内存模型
#print(id(age))


      
#0，空字符串，空数组，None，为Fales

while(True):
    print('----------------------')
    print('你有什么吩咐？')
    order = input()
    if(order == 'time'):
        tm.time1()
    elif(order == 'hi'):
       op.hi()
    elif(order == '88'):
        print('再见了')
        break
    elif(order == 'tianqi'):
        ct = input('请输入城市：')
        wt.tianqi(ct)
    else:
         print(op.ai_talk(order))


548
