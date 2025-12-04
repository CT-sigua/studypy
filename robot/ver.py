""" name1 = '张三'
print(f'{name1}')
age = 11
print(f'111{age}')
print('111' ,name1)
print(age) """

#变量在用一作用于不能重名
#变量有作域
#invalid syntax. Perhaps you forgot a comma?语法无效。也许你忘记了逗号


#!/usr/bin/python
 
""" str = "this is string example....wow!!! this is really string"
print (str.replace("is", "was"))
print (str.replace("is", "was", 3)) """


def ai_talk(question):
    return question.replace('你','我').replace('不','').replace('吗',' ').replace('?','!')

