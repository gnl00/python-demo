#################################### 六、函数式编程 #############################################

## 1、高阶函数
# 在python中，函数本身也可以赋值给变量，即：变量可以指向函数
# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

f_test = abs

print(f_test(-20))

def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))


## 1.1 map/reduce

## map()
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

def f1(x):
    return x ** 2

res = map(f1, range(11))
print(list(res))

print('######################################### reduce #################################################')
# reduce()
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

from functools import reduce, wraps
import functools
from typing import Counter

def add2(x, y):
    return x + y

res2 = reduce(add2, [1,2,3,4,5,6,7,8,9,])

# lambda 函数写法
res3 = reduce(lambda x, y: x+y, [1,2,3,4,5,6,7,8,9,])
print(res2)

# list to int 把序列[1, 3, 5, 7, 9]变换成整数13579
res4 = reduce(lambda x, y: x*10 + y, [1,3,5,7,9])
print(res4)

# python 内部提供的sum方法
print(sum([1,2,3,4,5]))

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']

def normalize(name):
    if isinstance(name, (str)):
        tail = name[1:].lower()
        head = name[0].upper()
        return head + tail
        
print(normalize('ABC'))

names = ['adam', 'LISA', 'barT']
res_name = map(normalize, names)
print(list(res_name))


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(L):
    return reduce(lambda x, y: x * y, L)

print(prod([1,2,3,4,5]))

# str2int

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

print(str2int('123456'), type(str2int('123456')))


print('######################################### filter #################################################')
# 1.2 filter
# 和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

def is_odd(num):
    return num % 2 == 1

res_filter = filter(is_odd, [1,2,3,4,5,6,7,8,9])
print(list(res_filter))

def remove_empty(s):
    return s and s.strip()

res_filter2 = filter(remove_empty, ['A', ' ', 'B', None, 'C'])
print(list(res_filter2))


# 计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
# 首先，列出从2开始的所有自然数，构造一个序列：
# 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
# 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
# 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
# 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 不断筛下去，就可以得到所有的素数。

# 构建一个从3开始的奇数无限序列
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n

def odd_filter(n):
    return lambda x: x % n > 0

def primes():
    # 先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列
    yield 2
    L = _odd_iter()
    while True:
        n = next(L)
        yield n
        L = filter(odd_filter(n), L)

for i in primes():
    if i < 1000:
        print(i)
    else:
        break

# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

res_palindrome = filter(is_palindrome, range(1, 1000))
print(list(res_palindrome))



print('######################################### sorted #################################################')
# 1.3 sorted
# Python内置的sorted()函数就可以对list进行排序

sort_list1 = [3,45,2,13,4,56,43,1]
print(sorted(sort_list1))

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
res_sort = sorted([-1,-2,-40,-32,-10], key=abs)
print(res_sort)


# 给sorted传入key函数，实现忽略大小写的排序
res_sort2 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(res_sort2)

# 行反向排序，不必改动key函数，可以传入第三个参数reverse=True
res_sort3 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(res_sort3)

# 用一组tuple表示学生名字和成绩
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# 用sorted()对上述列表分别按名字排序
def by_name(t):
    return t[0]

def by_score(t):
    return t[1]

res_sort4 = sorted(L, key=by_name)
print(res_sort4)

res_sort5 = sorted(L, key=by_score)
print(res_sort5)




print('######################################### 返回函数 #################################################')
## 2、返回函数

# 2.1 函数作为返回值
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回

# 实现一个可变参数的求和。通常情况下，求和的函数是这样定义的
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

# 但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数
res_sum = lazy_sum(1,2,3,4,5)
print(res_sum)
print(res_sum())

# 2.2 闭包
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3()) # 9 9 9 原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9


# 如果一定要引用循环变量怎么办？
# 方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count2():
    fs = []
    def f(n):
        def g():
            return n*n
        return g
    for i in range(1, 4):
        fs.append(f(i)) #  f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f12, f22, f32 = count2()
print(f12(), f22(), f32())


print('##################################### nonlocal #######################################')
# 2.3 nonlocal
# 使用闭包，就是内层函数引用了外层函数的局部变量。如果只是读外层变量的值，我们会发现返回的闭包函数调用一切正常
# 使用闭包时，对外层变量赋值前，需要先使用nonlocal声明该变量不是当前函数的局部变量
def inc():
    x = 0
    def fn():
        # 仅读取x的值
        return x + 1
    return fn

res_inc = inc()
print(res_inc()) # 1
print(res_inc()) # 1

def inc2():
    x = 0
    def fn():
        # 仅读取x的值
        # x = x + 1 报错 "x" is not defined 原因是 x 作为局部变量并没有初始化，直接计算x+1是不行的
        # 想引用inc()函数内部的x，需要在fn()函数内部使用 nonlocal 来修饰 x 变量
        # 加上 nonlocal 声明后，解释器把 fn() 的 x 看作外层函数的局部变量，它已经被初始化了，可以正确计算 x+1。
        nonlocal x
        x += 1
        return x
    return fn

print('with nonlocal')
res_inc2 = inc2()
print(res_inc2()) # 1
print(res_inc2()) # 2



# 利用闭包返回一个计数器函数，每次调用它返回递增整数
def calculator():
    num = 0
    def inc():
        nonlocal num
        num += 1
        return num
    return inc

my_counter = calculator()
print(my_counter(), my_counter(), my_counter(), my_counter())


print('######################################### 匿名函数 #################################################')
## 3、匿名函数
# 当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便

list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
# 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
# 此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
annoy_f = lambda x: x * x
print(annoy_f) # <function <lambda> at 0x0000020C5ECA8AF0>

# 也可以把匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y


print('######################################### 装饰器 #################################################')
## 4、装饰器
# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
# 函数对象有一个__name__属性，可以拿到函数的名字
def now():
    return '20xx-xx-xx'

f_now = now
print(now.__name__, f_now.__name__)

# 假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# 本质上，decorator就是一个返回函数的高阶函数
def log(func):
    def wrapper(*args, **kw):
        print('execute before call %s(): ' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 把@log放到now()函数的定义处，相当于执行了语句 now = log(now)
@log
def now2():
    return '20xx-xx-xx'

print(now2())


# 由于log()是一个decorator，返回一个函数，
# 所以原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，
# 于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。
# 比如，要自定义log的文本

def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s function: %s' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
        
@log2('execute')
def now3():
    return '20xx-xx-xx'

print(now3())


# 和两层嵌套的decorator相比，3层嵌套的效果是这样的 now = log('execute')(now)

# 可以看到，添加了装饰器之后，修饰的方法名都变成了 wrapper
print(now2.__name__) # wrapper
print(now3.__name__) # wrapper

# 因为返回的那个wrapper()函数名字就是'wrapper'，
# 所以需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，
# 一个完整的decorator的写法如下

def my_log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('my_log call %s' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 带参数的decorator
def my_log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s call function: %s' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@my_log
def now4():
    return '20xx-xx-xx'

@my_log2('execute')
def now5():
    return '20xx-xx-xx'

print(now4())
print(now4.__name__) # now4

print(now5())
print(now5.__name__) # now5

# 只需记住在定义wrapper()的前面加上@functools.wraps(func)即可


# 设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
import time

def exe_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('%s start in %s' % (func.__name__, time.asctime()))
        res = func(*args, **kw)
        time.sleep(3)
        print('%s end in %s' % (func.__name__, time.asctime()))
        return res
    return wrapper

@exe_time
def my_print():
    print('112233')

my_print()


print('######################################### 偏函数 #################################################')
## 5、偏函数
# python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）

# 例子
# int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换
# int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换

# 8进制字符串转10进制
int('12345', base=8)

# 16转10
int('12345', 16)

# 自定义2进制转10进制
def my_int2(x, base=2):
    return int(x, base)

# 简单总结functools.partial的作用就是，
# 把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2
int2 = functools.partial(int, base=2)