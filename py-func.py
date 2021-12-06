print('#################################### 四、函数 #############################################')

# python 提供的内置函数几乎都是定义在 builtins.pyi 模块中的
print(bool(1))
print(bool(''))
print(float('12.34'))

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
my_abs = abs
print(my_abs(-2))

# 定义一个空函数，没有任何实现，需要使用pass关键字来作为占位符，避免报错。
# pass 还可以用在条件循环中作为占位
def empty_func(): 
    pass

## 1、单个返回值
def custom_abs(num):
    flag = 0
    if not isinstance(num, (int, float)):
        raise TypeError('operation type not support')
    
    if num >= flag:
        return num
    else:
        return -num

print(custom_abs(-99))

## 2、多个返回值

import math

# @param x 向x轴方向前进的距离
# @param y 向y轴方向前进的距离
# @param step 前进的步数
# @param angle 前进的角度
def move(x, y, step, angle=0):
    final_x = x + step * math.cos(angle)
    final_y = y + step * math.sin(angle)
    return final_x, final_y

x, y = move(100, 50, 30, math.pi / 6)
print(x, y)

# 实际上，多返回值返回的是一个tuple
move_res = move(100, 50, 30, math.pi / 6)
print(move_res)

## 3、默认参数

# 注意
# 1、必选参数在前，默认参数在后，否则Python的解释器会报错
# 2、如何设置默认参数
# 3、定义默认参数要牢记一点：默认参数必须指向不变对象

# 求n的m次方，默认求2次方
def power(n, m=2):
    if not isinstance(n, (int, float)) or not isinstance(m, (int, float)):
        raise TypeError('operation type not support')
    return n ** m

print(power(5))

## 4、可变参数
# 在参数前面加了一个 * 号，在函数内部，可变参数接收到的是一个 tuple
# 可以输入0或任意个参数

def calc(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

print(calc(1, 2, 3, 4, 5, 6))

# 把 list 或 tuple 的元素变成可变参数传入
list1 = [11, 22, 33, 44]
tuple1 = (12, 23, 34, 45)
print(calc(*list1))
print(calc(*tuple1))

## 5、关键字参数
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **keyword):
    print('name: ', name, 'age: ', age, 'others: ', keyword)

person('rose', 20)
person('jack', 20, male='M', city='hangzhou')

extra = {'male': 'M', 'adult': True, 'city': 'beijing'}
person('hins', 38, **extra)

## 6、命名关键字参数
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person1(name, age, *, city, job):
    print('name: ', name, 'age: ', age, 'city: ', city, 'job: ', job)

person1('aaa', 10, city='nanning', job='engineer')

# TypeError: person1() missing 2 required keyword-only arguments: 'city' and 'job'
# person1('bbb', 12, )

## 7、参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。


## 递归
def fab(n):
    if n <= 2:
        return n
    else:
        return n * fab(n - 1)

print(fab(10))