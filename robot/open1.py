

def hello():
    #字符串转换（在结合字符串和数字打印时，需要将数字类型转换为字符串类型再进行拼接）
    #name = '王sir'
    #age = 16
    #2、提问 输入姓名
    name = input('你叫什么名字，输入名字:\n')
    age = input('输入年龄:\n')#age是字符串

    print('you name is'  + name + '!，年龄' + str(age) + '!')#这是拼接加转换（拼接会省略前后空格）
    print('you name is' ,name, '!，年龄' ,age, '!')#如果要同时打印多个字符串和数字的组合，可以使用逗号分隔它们

    #这是格式化
    print('you name is {} !，年龄 {} !'.format(name,age))#简洁！

    #使用格式化字符串字面值，我们可以在字符串前加上”f”前缀，并在字符串中插入变量。推荐！
    #name = '王sir'
    #age = 16
    print(f"you name is {name} !，年龄 {age} !")
    print(f"you name is {name} !，年龄 {age} !!")
    return age



def hi():
    print("hello")
    print("nice to meet you")
    print("吃了吗")
    print('''
    oooo                  oooo  oooo            
    `888                  `888  `888            
    888 .oo.    .ooooo.   888   888   .ooooo.  
    888P"Y88b  d88' `88b  888   888  d88' `88b 
    888   888  888ooo888  888   888  888   888 
    888   888  888    .o  888   888  888   888 
    o888o o888o `Y8bod8P' o888o o888o `Y8bod8P' 
                                                                                        
    ''')

    """
    这是   变量
    注释   及拼接
    """
def Determine_Age(age):
    age = int(age)

#判断
#如果age大于30：我喜欢成熟人的魅力
#如果age小于30：你真年轻如花似玉
#条件语句 顺序很重要
    if (age < 30):
        if (age < 10):
            print('你是个小屁孩哈哈')
        else:
            print(f'你才{age}啊')
            print('你真年轻如花似玉的年纪！！')
    elif (age > 30):
        print(f'你居然都{age}了！')
        print('我喜欢成熟人的魅力,假的！')
    else:
        print('你居然刚好30！')

def ai_talk(question):
    return question.replace('你','我').replace('不','').replace('吗',' ').replace('?','!')

def tianqi(city):
    print(f'{city}:晴天！')
