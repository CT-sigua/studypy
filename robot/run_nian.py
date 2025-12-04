def determine_a_leap_year (year):
    # year = input('input year:')
    year = int(year)
    if(year%100 == 0):
        if(year%400 == 0):
            print('闰年！')
            return True
        else:
             print('不是闰年')
             return False
    elif(year%4 == 0):
            print('闰年！')
            return True
    else:
        print('不是闰年')
        return False

def determine_a_leap_lear2(year):
     if(year%4 == 0 and year%100 !=0 or year%400 == 0):
          return True
     else:
          return False
     
def determine_a_leap_lear3(year):
     return(year%4 == 0 and year%100 !=0 or year%400 == 0)

          
#shift+alt+上键 复制上一行
#shift+alt 竖着选中一列

#assert 断言 测试用
# assert determine_a_leap_year(2004)==True
# assert determine_a_leap_year(2005)==False
# assert determine_a_leap_year(2000)==True
# assert determine_a_leap_year(2100)==False

assert determine_a_leap_lear3(2004)== True
assert determine_a_leap_lear3(2005)== False
assert determine_a_leap_lear3(2000)== True
assert determine_a_leap_lear3(2100)== False
#TypeError: determine_a_leap_year() takes 0 positional arguments but 1 was given

# determine_a_leap_year()
