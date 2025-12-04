from datetime import datetime

def time1():
     #4、显示时间
     dt = datetime.now()
     #print(f'今天是{dt.year}年{dt.month}月{dt.day}日') 
     print(dt.strftime('今天是:%Y年%m月%d日 %H:%M:%S'))