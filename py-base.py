print('##################################### 一、输入输出 ############################################')

# 一、输入输出

# input() 默认所有输入的数据都是 str 类型，int(input()) 将输入的 str 转成 int 类型
# a = int(input())
# print('a\'s value is: %d' % a)



# 以f开头的字符串，称之为f-string
b = 10
print(f'b\'s value is: {b}')

print('#################################### 二、基本数据类型 #############################################')

# 二、基本数据类型
# int
# str
# boolean
# list
# tuple
# dict
# set

## str
str1 = "aaaaa"
str2 = 'bbbbb'
print(str1, str2)

# 使用 len() 求 str 的长
# len() 是 builtins 模块内的方法。builtins 是 python 的内建模块
# 所谓内建模块就是你在使用时不需要 import
# 在python 启动后，在没有执行程序员编写的任何代码前，python 会加载内建模块中的函数到内存中

str1_len = len(str1)
print(str1_len)

# replace('old', 'new')，将old替换成new
# replace('old', 'new', n)，若 old 字符串出现多次，仅替换匹配到的前 n 次
str3 = str1.replace('aa', 'bb', 1)
print(str3)


print()
## list，类似 Java 中 ArrayList 和数组的结合
list_empty = [] # 空 list

list1 = ['apple', 'lemon', 'zzzz', 'banana']
print(list1[0])

list_len = len(list1) # 使用 len() 求 list 的长
print(list_len)

# 可以使用负值逆序取数据
print(list1[-1], list1[-2])

# 取数下标大于等于 list 的 len 就会报错 IndexError: list index out of range，即 list 下标越界
# print(list1[3])

list1.insert(0, 'peach') # insert 指定位置插入

list1.append('strawberry') # append, 在 list 的末尾追加数据

print(list1)

list1.pop(2) # 删除指定下标的数据

print(list1)

# list 中可以存在多种不同类型的数据
mul_list = [True, 100, 'gnl', ['aaa', 200], False]
print(mul_list)

# range(n)，生成一个 0-n 范围内的整数序列，再通过 list() 函数可以转换为 list
list_5 = list(range(5))
print(list_5)

# 使用 sort() 对 list 进行排序
list1.sort()
print(list1)

print()
## tuple
# 元组，又称不可变数组，数据一旦初始化就不可修改
# 当你定义一个 tuple 时，在定义的时候，tuple 的元素就必须被确定下来
tuple_empty = () # 空元组

tuple_one = (1, ) # 单数据元组，必须在末尾跟上一个逗号，避免歧义

tuple = ('aa', 'bb', True, 100)
print(tuple)

print(tuple[0], tuple[1], tuple[-1])

print(len(tuple))

# 元组数据无法修改，报错 TypeError: 'tuple' object does not support item assignment
# tuple[0] = 'cc' 


## dict
# 类似 map，使用键-值（key-value）存储，具有极快的查找速度
# dict内部存放的顺序和key放入的顺序是没有关系的
d = {
    'k1': 100,
    'k2': 'aaa',
    'k3': True,
    'k4': [1,2,3,],
}

print(d)
print(d['k1'], d['k2'], d['k3'], d['k4'])

d['k2'] = 'apple'
print(d['k1'], d['k2'], d['k3'], d['k4'])

# 使用 get 方法获取对应key的value
v1 = d.get('k1')
print(v1)

# 若是key不存在，可以指定默认返回值
v10 = d.get('k10', 0)
print(v10)

# 判断 dict 中是否存在某个key
has_key = 'k1' in d
print(has_key)

# 删除某个key
d.pop('k2')
print(d)

## dict 特点
# 1、查找和插入的速度极快，不会随着key的增加而变慢；
# 2、需要占用大量的内存，内存浪费多。

## dict 与 list 比较
# 1、查找和插入的时间随着元素的增加而增加；
# 2、占用空间小，浪费内存很少。


## set
# set 和 dict 类似，无序，也是一组 key 的集合，但不存储 value。由于 key 不能重复，所以，在 set 中，没有重复的 key
# 要创建一个 set，需要提供一个 list 作为输入集合
set1 = set([1, 2, 3])
print(set1)

# 重复元素在 set 中自动被过滤
set2 = set([1, 2, 3, 3, 2, 5, 4, 4])
print(set2)

set2.add(6)
set2.add(6)
set2.add(6) # 可以重复添加，但不会有效果
print(set2)

# 删除指定的 key
set2.remove(3)
print(set2)

# 删除最左边的 key
set2.pop()
print(set2)

## 两个set可以做数学意义上的交集、并集等操作
set_un = set1.union(set2) # 并集
print(set_un)

set_inter = set1.intersection(set2) # 交集
print(set_inter)


print('#################################### 三、条件与循环 #############################################')


# 三、条件与循环

## 1、if-else
a = 0
if a == 0:
    print('equal')
elif a > 0:
    print('big')
else:
    print('small')

## 2、for

names = ['tony', 'jack', 'rose', 'brown', 'catty']

for name in names:
    print(name)

sum = 0
for num in [1,2,3,4,5,6,7,8,9,10]:
    sum += num

print(sum)

## 3、while

sum_wh = 0
n_wh = 101
while n_wh > 0:
    sum_wh += n_wh
    n_wh -= 2
print(sum_wh)

