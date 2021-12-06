# 一、输入输出
# 将输入的str转成int类型
a = int(input())
print('a\'s value is: %d' % a)

# 二、条件循环
# 1、if-else
if a == 0:
    print('equal')
elif a > 0:
    print('big')
else:
    print('small')

# for

# 三、基本数据类型
list = ['aaa', 'bbb', 'ccc']
list_len = list.__len__
print(list_len)